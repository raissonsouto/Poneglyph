from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#from flask_login import LoginManager
#from flask_apscheduler import APScheduler
import logging
import os
import dotenv
import redis

dotenv.load_dotenv('../.env')

DATABASE_URI = f'postgresql://' + \
               f'{os.getenv("DB_USER")}:' + \
               f'{os.getenv("DB_PASSWORD")}@' + \
               f'127.0.0.1:{os.getenv("DB_PORT")}/' + \
               f'{os.getenv("DB_DATABASE")}'


logging.basicConfig(filename='../bifrost.log',
                    level=logging.INFO,
                    format='%(asctime)s %(levelname)s: %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

app = Flask(__name__)
logger = logging.getLogger(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = os.getenv("APP_SECRET_KEY")

db = SQLAlchemy(app)
rediss = redis.Redis(host='localhost', port=6379, db=0)
#login_manager = LoginManager(app)
#scheduler = APScheduler()
