from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#from flask_login import LoginManager
#from flask_apscheduler import APScheduler
#from argon2 import PasswordHasher
from dotenv import load_dotenv
import os

load_dotenv("./private/.env")

DATABASE_URI = f'{os.getenv("DB_NAME")}://' + \
               f'{os.getenv("DB_USER")}:' + \
               f'{os.getenv("DB_PASSWORD")}@' + \
               f'db:{os.getenv("DB_PORT")}/' + \
               f'{os.getenv("DB_DATABASE")}'

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = os.getenv("APP_SECRET_KEY")

db = SQLAlchemy(app)
#ph = PasswordHasher()
#login_manager = LoginManager(app)
#scheduler = APScheduler()
