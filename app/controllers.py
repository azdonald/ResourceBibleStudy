from flask_restful import Resource
from flask import jsonify, request
from app.data import DataLoader
import json
from datetime import datetime



class DailyReading(Resource):
    def get(self):
        dailyReading = None
        currentDate = datetime.now()
        bibleData = DataLoader()
        timeOfTheDay = currentDate.timetuple().tm_hour
        bibleReading = bibleData.getDailyReading(currentDate.timetuple().tm_yday)
        if (timeOfTheDay < 12 ):
            dailyReading = bibleReading['FirstReading']
        elif (timeOfTheDay >= 12 and timeOfTheDay < 17):
            dailyReading = bibleReading['SecondReading']
        else:
            dailyReading = bibleReading['ThirdReading']
        bibleVerse = dailyReading.split('.')
        chapters = None
        if '-' in bibleVerse[1]:
            chapters = bibleVerse[1].split('-')
        startChapter = chapters[0] if chapters else bibleVerse[1].strip()
        return jsonify(bibleData.getReading(bibleVerse[0], startChapter))

class BibleReading(Resource):
    def get(self):
        book = 'Genesis'
        bibleData = DataLoader()
        return jsonify(bibleData.getReading(book))

    def post(self):
        params = request.get_json()
        book = params['book']
        bibleData = DataLoader()
        return jsonify(bibleData.getReading(book))