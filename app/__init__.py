from flask import Flask
from flask_restful import Api


app = Flask(__name__)
api = Api(app)

from app.controllers import DailyReading, BibleReading

api.add_resource(DailyReading, '/api/daily', endpoint='daily')
api.add_resource(BibleReading, '/api/bible', endpoint='bible')