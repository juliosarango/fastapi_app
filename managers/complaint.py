from models import complaint, RoleType, State
from config.db import database


class ComplaintManager:
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
        id = await database.execute(complaint.insert().values(complaint_data))

        return await database.fetch_one(complaint.select().where(complaint.c.id == id))


    @staticmethod
    async def delete_complaint(complaint_id):
        await database.execute(complaint.delete().where(complaint.c.id == complaint_id))


    @staticmethod
    async def approve_complaint(id):
        await database.execute(complaint.update().where(complaint.c.id == id).values(status = State.approved))

    @staticmethod
    async def reject_complaint(id):
        await database.execute(complaint.update().where(complaint.c.id == id).values(status = State.rejected))        