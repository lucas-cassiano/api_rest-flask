import mysql.connector


class config():

    def connector():
        return mysql.connector.connect(
            user="root",
            password="",
            host="localhost",
            database="youtube")
