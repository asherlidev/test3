from flask import Flask
from decouple import config
from mysock import socket_wrapper
from mysock import get_socket
from api import scheduler
from extern import get_web_socket
app=Flask(__name__)

@app.route('/')
def hello_word():
    return 'hello world'

if __name__ == '__main__':
        socket_wrapper(app)
        get_web_socket(get_socket())
        scheduler.start()
        app.run(port=config('PORT'))