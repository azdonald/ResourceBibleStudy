from flask_restful import Resource
from flask import jsonify
from app.schemas import DailyReadingSchema
import json


class DailyReading(Resource):
    def get(self):
        return 'hello to you'

class BibleReading(Resource):
    def get(self):
        dailyReading = ''
        with open('dailyReading.txt') as f:
            dailyReading = json.loads(json.dumps(f.read()))
        schema = DailyReadingSchema(many=True).loads(dailyReading)
        return jsonify(schema)