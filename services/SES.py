from datetime import datetime

import boto3
from botocore.exceptions import ClientError
from decouple import config

from utils.logs import aws_logs


class SESservice:
    def __init__(self, recipient):
        self.region = config("REGION")
        self.recipient = recipient
        self.ses = boto3.client('ses',
                                region_name=self.region
                                )

    # Needed only for sandbox env, otherwise this can be deleted.
    def is_verified(self):
        response = self.ses.list_identities(
            IdentityType='EmailAddress',
            MaxItems=10
        )

        if self.recipient in response["Identities"]:
            return True
        return False

    # Needed only for sandbox env, otherwise this can be deleted.
    def verify_email(self):
        response = self.ses.verify_email_identity(
            EmailAddress=self.recipient
        )

        return response

    def send_email(self):
        SENDER = config("MAIL_USERNAME")

        SUBJECT = "Your order has been created"

        BODY_TEXT = (f"Your order has been created. The Order ID is: \r\n"
                     "This emails was sent as a confirmation, please do not reply to it. "
                     "Best regards shop_name."
                     )
        # Send via email the payment link

        BODY_HTML = """<html>
        <head></head>
        <body>
          <h1>Your order has been created</h1>
          <p>This emails was sent as a confirmation, please do not reply to it.
            <a href='#'>MyShop</a> using the
            <a href='#'>
              "Best regards shop_name."
        </body>
        </html>
        """

        CHARSET = "UTF-8"
        client = boto3.client('ses', region_name=self.region)

        try:
            # Provide the contents of the email.
            response = client.send_email(
                Destination={
                    'ToAddresses': [
                        self.recipient,
                    ],
                },
                Message={
                    'Body': {
                        'Html': {
                            'Charset': CHARSET,
                            'Data': BODY_HTML,
                        },
                        'Text': {
                            'Charset': CHARSET,
                            'Data': BODY_TEXT,
                        },
                    },
                    'Subject': {
                        'Charset': CHARSET,
                        'Data': SUBJECT,
                    },
                },
                Source=SENDER,
            )
        # Display an error if something goes wrong.
        except ClientError as e:
            print(e.response['Error']['Message'])

            with open(aws_logs, "a") as f:
                f.write(
                    f"[{datetime.utcnow()}] - Email sent! Message ID: {e.response['Error']['Message']}\n"
                )
        else:
            with open(aws_logs, "a") as f:
                f.write(
                    f"[{datetime.utcnow()}] - Email sent! Message ID: {response['MessageId']}\n"
                )
