import json

class DataLoader(object):
    def __init__(self):
        self.dailyReads = None
        with open('dailyReading.txt') as f:
            self.dailyReads = json.loads((f.read()))

    def getDailyReading(self, dayOfTheYear):
        return self.dailyReads[dayOfTheYear]