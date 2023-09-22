from flask import Flask, render_template
import random
import time
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

@socketio.on('connect')
def handle_connect():
    print('A user connected')

@socketio.on('disconnect')
def handle_disconnect():
    print('A user disconnected')

def generate_coordinates():
    latitude = random.uniform(-90, 90)
    longitude = random.uniform(-180, 180)
    return latitude, longitude

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('request_coordinates')
def send_coordinates():
    while True:
        latitude, longitude = generate_coordinates()
        socketio.emit('update_coordinates', {'latitude': latitude, 'longitude': longitude})
        time.sleep(5)  # Update coordinates every 5 seconds

if __name__ == '__main__':
    socketio.run(app, debug=True)