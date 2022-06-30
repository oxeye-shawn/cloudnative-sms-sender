from flask import Flask, Response
from SmsSender import SmsSender


app = Flask(__name__)

PHONE_NUMBER = "+972542472846"
MESSAGE = "Hello World!"


@app.route("/")
def notify_through_sms():
    sms_sender = SmsSender()
    sms_sender.publish_text_message(phone_number=PHONE_NUMBER, message=MESSAGE)
    return Response(mimetype="application/json", status=200)
