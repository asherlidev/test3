import imp
from logging import NullHandler
from flask_socketio import SocketIO
from api import transaction
import asyncio
sock=None
def socket_wrapper(flask_app):
    global sock
    sock=SocketIO(flask_app,cors_allowed_origins='*')
    socket_event(sock)
def get_socket():
    return sock
def call_back_resp(resp):
    sock.emit('send_data',resp)

def socket_event(sock):
    @sock.on('message')
    def handle_message(data):
        print('received message: ' + data)
    @sock.on('new_data')
    def handle_new_data(data):
        print(data['page_index'])
        asyncio.run(transaction(data['page_index'],data['page_limit_count'],call_back_resp))
        print("request new data")