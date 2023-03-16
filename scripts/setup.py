from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#from flask_login import LoginManager
#from flask_apscheduler import APScheduler
from scripts.guardian import Guardian
from sqlalchemy.ext.declarative import declarative_base
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


app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = os.getenv("APP_SECRET_KEY")


guardian = Guardian(
    int(os.getenv("TIME_COST")),
    int(os.getenv("MEMORY_COST")),
    int(os.getenv("PARALLELISM")),
    int(os.getenv("HASH_LEN")),
    int(os.getenv("SALT_LEN")),
    os.getenv("ENCODING"),
    os.getenv("TYPE"),
    os.getenv("ALGORITHM"),
    os.getenv("CIPHER_MODE"),
    os.getenv("KEY"),
    os.getenv("NONCE")
)


rediss = redis.Redis(host='localhost', port=6379, db=0)
db = SQLAlchemy(app)
logger = logging.getLogger(__name__)
#login_manager = LoginManager(app)
#scheduler = APScheduler()

Base = declarative_base()