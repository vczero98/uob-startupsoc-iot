import socketio

sio = socketio.Client()

@sio.event
def connect():
    print('connected to server')

def main():
    sio.connect('http://localhost:3000')
    sio.wait()

if __name__ == '__main__':
    main()