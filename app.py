# Triggering redeploy after adding import os

import os  # Make sure this is at the top of the file!
import time
from flask import Flask, render_template
from flask_socketio import SocketIO

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
    port = int(os.environ.get("PORT", 5000))  # Use Render's assigned port or default to 5000
    socketio.start_background_task(fetch_threat_data)  # Start background task correctly
    socketio.run(app, host='0.0.0.0', port=port)