import os
import socketio
from dotenv import load_dotenv
load_dotenv()

class ServerSocket:
    ADDRESS = os.getenv("SERVER_ADDRESS")
    sio = socketio.Client()

    def __init__(self):
        self.sio.connect('http://192.168.0.29:3000')

        self.sio.wait()

    @sio.event
    def connect():
        for i in range(10):
            print('connected to server')