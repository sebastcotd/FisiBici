'''Archivo que ejecuta la aplicacion'''
from flask import Flask, render_template
from flask_cors import CORS
from mongoengine import connect

from Backend.config.config import config_app
from Backend.routes.bicycles import create_routes_bicycles
from Backend.routes.login import create_routes_login

app = Flask(__name__, template_folder='../Frontend/templates', static_url_path='../Frontend/static')
DB_URI = "mongodb+srv://Mauricio:1234@fisibici"
DB_URI += ".cpmx7.mongodb.net/SistemaBicicletas?retryWrites=true&w=majority"
connect(host=DB_URI)

@app.route('/')
def index():
    return render_template('index.html')

CORS(app=app, supports_credentials=True)

config_app(app)
create_routes_bicycles(app)
create_routes_login(app)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
