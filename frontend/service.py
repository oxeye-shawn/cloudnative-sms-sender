from flask import Flask, Response
import requests
import logging
import sys
import os


logging.basicConfig(stream=sys.stdout, level=logging.INFO)

app = Flask(__name__)


def get_data(backendUrl):
    response = requests.get(backendUrl)
    logging.info(response)


@app.route("/")
def get_data():
    backendIp = os.environ["BACKEND_SERVICE_SERVICE_HOST"]
    backendPort = os.environ["BACKEND_SERVICE_SERVICE_PORT"]
    backendUrl = f"http://{backendIp}:{backendPort}"
    get_data(backendUrl)
    return Response(mimetype="application/json", status=200)
