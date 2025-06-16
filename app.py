from flask import Flask, render_template
from flask_socketio import SocketIO
import threading
import time

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

# Simulated threat data
def fetch_threat_data():
    while True:
        threat = {
            "type": "IP",
            "value": "8.8.8.8",
            "source": "Simulated Feed"
        }
        socketio.emit('new_threat', threat)
        time.sleep(10)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    threading.Thread(target=fetch_threat_data).start()
    socketio.run(app, debug=True)