from flask_restful import Resource
from flask import jsonify
from app.data import DataLoader
import json
from datetime import datetime


class DailyReading(Resource):
    def get(self):
        dailyReading = None
        currentDate = datetime.now()
        bibleDate = DataLoader()
        timeOfTheDay = currentDate.timetuple().tm_hour
        bibleReading = bibleDate.getDailyReading(currentDate.timetuple().tm_yday)
        if (timeOfTheDay < 12 ):
            dailyReading = bibleReading['FirstReading']
        elif (timeOfTheDay >= 12 and timeOfTheDay < 17):
            dailyReading = bibleReading['SecondReading']
        else:
            dailyReading = bibleReading['ThirdReading']
        return jsonify(dailyReading)

class BibleReading(Resource):
    def get(self):
        pass