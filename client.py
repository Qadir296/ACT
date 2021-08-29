import socket
from pip._vendor import requests
import json
import time
from requests.auth import HTTPBasicAuth
import pygeohash as pgh
from datetime import datetime

HEADER= 64
port = 5050
FORMAT= 'utf-8'
DISCONNECT_MESSAGE= "Disconnected"
Server= "138.96.220.69"
address = (Server, port)
Time= datetime.now().isoformat()

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(address)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)

send("Data posted to ICON at" + Time )