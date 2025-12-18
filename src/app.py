import datetime
import socket
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/v1/info')
def info():
    return jsonify({
        'date': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'hostname': socket.gethostname(),
        'message': 'Welcome',
        'deployed_on': 'kubernetes',
        'env': 'dev',
        'app_name': 'python-app-final',
    })

@app.route('/api/v1/healthz')
def healthz():
    return jsonify({'status': 'ok'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
