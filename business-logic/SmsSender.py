# send sms through aws sns api

from flask import Response
import logging
import boto3
import sys

logging.basicConfig(stream=sys.stdout, level=logging.INFO)


class SmsSender:
    def __init__(self) -> None:
        self.sns = boto3.client(
            "sns",
            region_name="eu-west-2",
        )

    def publish_text_message(self, phone_number, message):
        self.sns.publish(PhoneNumber=phone_number, Message=message)
        # Validation if sms was sent successfully is only avilable through cloudwatch
