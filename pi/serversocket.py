import os
import socketio
from dotenv import load_dotenv
load_dotenv()

class PiSocket(socketio.ClientNamespace):
    serverSocket = None

    def __init__(self, namespace, serverSocket):
        super().__init__(namespace)
        self.serverSocket = serverSocket

    def on_connect(self):
        print('connected to server')
        
    def on_led_state(self, data):
        self.serverSocket.lightsUpdated(data['state'])

class ServerSocket:
    ADDRESS = os.getenv("SERVER_ADDRESS")
    sio = socketio.Client()
    lightsUpdated = lambda : None

    def __init__(self):
        self.sio.connect('http://172.20.10.3:3000', namespaces=['/pi'])
        self.sio.register_namespace(PiSocket('/pi', self))
        # self.sio.wait()

    def setLightsUpdated(self, f):
        self.lightsUpdated = f

    def sendFlameState(self, state):
        print('sending flame', state)
        self.sio.emit('flame_state', {'secret': os.getenv("PI_SECRET"), 'state': state}, namespace='/pi')