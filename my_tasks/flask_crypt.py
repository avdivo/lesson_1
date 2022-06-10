from flask import Flask
from flask import request
from cryptography.fernet import Fernet

app = Flask(__name__)
f = Fernet(b'ZgF2CwB-XLcBBUe0DGPqxRrzWe5GYFBRQvL_gRpE3kY=')


@app.route('/encrypt', methods=['GET'])
def encrypt():
    """
    Функция для кодрования сообщения переданного как параметр string методом GET
    в строке браузкра набрать 127.0.0.1:5000/encrypt?string=<string_to_encrypt>
    <string_to_encrypt> - заменить на сообщение
    """
    string = request.args.get('string')
    token = f.encrypt(string.encode())
    return f'<b><i>{token.decode()}</b></i>'


@app.route('/decrypt', methods=['GET'])
def decrypt():
    """
    Функция для кодрования сообщения переданного как параметр string методом GET
    в строке браузкра набрать 127.0.0.1:5000/decrypt?string=<string_to_decrypt>
    <string_to_decrypt> - заменить на сообщение
    """
    string = request.args.get('string')
    token = f.decrypt(string.encode())
    return f'<b><i>{token.decode()}</b></i>'


if __name__ == '__main__':
    app.run()
