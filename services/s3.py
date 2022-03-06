from asyncclick import ClickException
from decouple import config
import boto3

from fastapi import HTTPException
from botocore.exceptions import ClientError


class S3Service:
    def __init__(self):
        self.key = config('AWS_ACCESS_KEY')
        self.secret = config('AWS_SECRET_ACCESS_KEY')        
        self.s3 = boto3.client(
            's3',             
            aws_access_key_id = self.key, 
            aws_secret_access_key = self.secret
        )

        self.bucket = config('AWS_BUCKET_NAME')

    def upload(self, path, file_name, ext):
        """Upload files to S3

        Methos for upload images to bucket in s3 of AWS 

        Args:
            path (str): Directory where file is storage temporaly. Its in temp_files directory
            file_name (str): Name of image, this name is generate with uuid
            ext (str): Extension of file, e.g jpeg, jpg, png..

        Raises:
            HTTPException: _description_
            HTTPException: _description_

        Returns:
            str: Return de url of the file in s3 of aws
        """
        
        
        try:
            self.s3.upload_file(
                path, 
                self.bucket, 
                file_name,
                ExtraArgs={"ACL":"public-read", "ContentType": f"image/{ext}"}
            )

            return f"https://{config('AWS_BUCKET_NAME')}.s3.{config('AWS_REGION')}.amazonaws.com/{file_name}"

        except ClientError as ex:
            raise HTTPException(500, "S3 is not available ")
        except Exception as ex:            
            raise HTTPException(500, "S3 is not available ")
