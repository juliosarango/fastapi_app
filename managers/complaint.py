import uuid
import os

from models import complaint, RoleType, State
from config.db import database
from constants import TEMP_FILE_FOLDER
from services.s3 import S3Service
from services.ses import SESService
from utils.helpers import decode_photo

s3 = S3Service()
ses = SESService()


class ComplaintManager:
    """ Class to Manage the table complaint

    From this class manage the operations in the table complaint

    Methods:
    --------

    get_complaints(user): 
        Return registers from complaint table depends the role of the user

    create_complaint(complaint_data, user)
        This method create a register in the complaint table. 

    delete_complaint(complaint_id)
        This method delete a register from complaint table.

    approve_complaint(id)
        This method allow approve a complaint identified by id parameter

    reject_complaint(id)
        This method allow reject a complaint identified by id parameter
    """
    
    @staticmethod
    async def get_complaints(user):
        q = complaint.select()
        if user["role"] == RoleType.complainer:
            q = q.where(complaint.c.user_id == user["id"])
        elif user["role"] == RoleType.aprover:
            q = q.where(complaint.c.status == State.pending)

        return await database.fetch_all(q)


    @staticmethod
    async def create_complaint(complaint_data, user):

        complaint_data["user_id"] = user["id"]

        encoded_photo = complaint_data.pop("encoded_photo")
        extension = complaint_data.pop("extension")

        name = f"{uuid.uuid4()}.{extension}"
        path = os.path.join(TEMP_FILE_FOLDER, name)

        decode_photo(path, encoded_photo)
        #upload image to S3 and return the url
        complaint_data["photo_url"] =  s3.upload(path, name, extension)
        os.remove(path)
        
        id = await database.execute(complaint.insert().values(complaint_data))

        return await database.fetch_one(complaint.select().where(complaint.c.id == id))


    @staticmethod
    async def delete_complaint(complaint_id):
        await database.execute(complaint.delete().where(complaint.c.id == complaint_id))


    @staticmethod
    async def approve_complaint(id):
        await database.execute(complaint.update().where(complaint.c.id == id).values(status = State.approved))
        #send email notification
        ses.send_mail("Complaint approved", ["jsarangoq@gmail.com"], "Congrats, your claim is approved, check your account bank it two days")


    @staticmethod
    async def reject_complaint(id):
        await database.execute(complaint.update().where(complaint.c.id == id).values(status = State.rejected))   
        #send email notification     
        ses.send_mail("Complaint reject!!!", ["jsarangoq@gmail.com"], "Sorry!!!! Your claim was reject!!!")