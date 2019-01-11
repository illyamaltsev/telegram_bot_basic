import telebot
import constants
from telebot import types
from flask import Flask, request
import sqlalchemy as db
import os

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'photodb.sqlite?check_same_thread=False')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
engine = db.create_engine(SQLALCHEMY_DATABASE_URI)  # check_same_thread=False)  # Create test.sqlite automatically
connection = engine.connect()
metadata = db.MetaData()
# photos2 = db.Table('photos', metadata, autoload=True, autoload_with=engine)
# photos2.drop(engine)
photos = db.Table('photos', metadata,
                  db.Column('id', db.Integer(), primary_key=True),  # nullable=False, autoincrement=True),
                  db.Column('file_id', db.String(255), nullable=False)
                  )

metadata.create_all(engine)  # Creates the table

TOKEN = constants.token
adminId = constants.adminId
channelId = constants.channelId

# secret = "285ufh4uqgf94"
url = "https://kravchel17.pythonanywhere.com/"  # + secret

bot = telebot.TeleBot(TOKEN, threaded=False)
bot.remove_webhook()
bot.set_webhook(url=url)

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])  # + secret, methods=['POST', 'GET'])
def webhook():
    if request.method == 'POST':
        update = telebot.types.Update.de_json(request.stream.read().decode('utf-8'))
        bot.process_new_updates([update])
        return 'ok', 200

        query = db.insert(photos).values(file_id=call.message.photo[0].file_id)
        ResultProxy = connection.execute(query)

query_sql = db.select([photos])
ResultProxy = connection.execute(query_sql)
ResultSet = ResultProxy.fetchall()  # Result of query
