from flask_jwt_extended import jwt_required
from flask_restful import Resource

import config
from flask import jsonify, request


class cadastro(Resource):

    conn = None

    def __init__(self):
        self.conn = config.config.connector()

    def get(self):
        cursor = self.conn.cursor()
        cursor.execute("""select * from otg_demo_users""")
        rows = cursor.fetchall()
        return jsonify(rows)

    @jwt_required()
    def post(self):
        cursor = self.conn.cursor()
        _name = request.json['name']
        _age = request.json['age']
        _city = request.json['city']
        insert_user_cmd = """INSERT INTO otg_demo_users(nome, idade, cidade)
                                VALUES(%s, %s, %s)"""
        cursor.execute(insert_user_cmd, (_name, _age, _city))
        self.conn.commit()
        response = jsonify(
            message='User added successfully.')
        cursor.close()
        self.conn.close()
        return (response)

    @jwt_required()
    def put(self, id):
        cursor = self.conn.cursor()
        _name = request.json['name']
        _age = request.json['age']
        _city = request.json['city']
        update_user_cmd = """update otg_demo_users
                                 set nome=%s, idade=%s, cidade=%s
                                 where id=%s"""
        cursor.execute(update_user_cmd, (_name, _age, _city, id))
        self.conn.commit()
        response = jsonify(
            message='User update successfully.')
        cursor.close()
        self.conn.close()
        return (response)

    @jwt_required()
    def delete(self, id):
        cursor = self.conn.cursor()
        sql = "delete from otg_demo_users where id = "+str(id)
        cursor.execute(sql)
        self.conn.commit()
        response = jsonify(
            message='User deletado successfully.')
        cursor.close()
        self.conn.close()
        return (response)
