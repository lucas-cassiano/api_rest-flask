from flask_jwt_extended import create_access_token
from flask_restful import Resource

import config
from flask import request


class usuarios(Resource):

    conn = None

    def __init__(self):
        self.conn = config.config.connector()

    def get(self):
        return self.login()

    def login(self):
        cursor = self.conn.cursor()
        login = request.json['login']
        senha = request.json['senha']
        insert_user_cmd = """select id from usuarios where login = %s and senha = %s"""
        cursor.execute(insert_user_cmd, (login, senha))
        rows = cursor.fetchall()
        cursor.close()
        self.conn.close()

        if rows:
            token = create_access_token(identity=rows[0][0])
            return {"access_token": token}
        return {"erro": "Login / senha nao encontrados"}
