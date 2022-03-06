from email.message import Message
from decouple import config
import boto3

class SESService:
    def __init__(self):        
        self.key = config('AWS_ACCESS_KEY')
        self.secret = config('AWS_SECRET_ACCESS_KEY')
        self.region = config('AWS_SES_REGION')
        self.ses = boto3.client(
            'ses', 
            region_name = self.region,  
            aws_access_key_id=self.key, 
            aws_secret_access_key=self.secret
        )

    def send_mail(self, subject, to_addresses, text_data):
        """Send email

        Method to send email using SES of aws

        Args:
            subject (str): Title or subject of email
            to_addresses (str): Email Address where we will send the email
            text_data (str): Body of message
        """



        body = {"Text": {"Data": text_data, "Charset": "UTF-8"}}

        self.ses.send_email(
            Source=config('SOURCE_EMAIL_SES'),
            Destination={
                "ToAddresses": to_addresses,
                "CcAddresses": [],
                "BccAddresses": [],
            },
            Message = {
                "Subject": { "Data": subject, "Charset": "UTF-8" },
                "Body": body
            }
        )
