import datetime

from flask_jwt_extended import JWTManager
from flask_restful import Api

from flask import Flask
from models.cadastro import cadastro
from models.usuarios import usuarios

app = Flask(__name__)
api = Api(app)
app.config['JWT_EXPIRATION_DELTA'] = datetime.timedelta(seconds=30)
app.config["JWT_SECRET_KEY"] = "super-secret"  # Change this!
jwt = JWTManager(app)

api.add_resource(cadastro, '/')
api.add_resource(usuarios, '/login/')

if __name__ == '__main__':
    app.run(debug=True)
