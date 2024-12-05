from flask import Flask
import socket

app = Flask(__name__)

# Retrieve hostname and IP address
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

@app.route('/')
def hello_api():
    return 'Welcome to venkataraghavan Final Test API Server'

@app.route('/host')
def host_name():
    return f'Hostname: {hostname}'

@app.route('/ip')
def host_ip():
    return f'IP Address: {ip_address}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
