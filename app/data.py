import json

class DataLoader(object):
    def __init__(self):
        self.dailyReads = None
        with open('dailyReading.txt') as f:
            self.dailyReads = json.loads((f.read()))

    def getDailyReading(self, dayOfTheYear):
        return self.dailyReads[dayOfTheYear]

    def loadBible(self):
        bible = None
        with open('msg.txt') as f:
            bible = json.loads(f.read())
        return bible

    def getReading(self, book, startChapter=1, endChapter=None):
        bible = self.loadBible()
        chapters = self.getChapters(bible, book)
        verses = self.getVerses(chapters, startChapter, endChapter)
        return verses
        
        
    def getChapters(self, bible, book):
        chapters = None
        book = book.strip()
        for b in bible['Books']:
            if b['BookName'].startswith(book):
                chapters = b['BookChapter']
                break
        return chapters
    
    def getVerses(self, chapters, startChapter=1, endChapter=None):
        verses = None
        if endChapter:
            verses = chapters[int(startChapter) - 1: int(endChapter)]
        else:
            for c in chapters:
                if c['ChapterId'] == int(startChapter) :
                    verses = c['ChapterVerses']
                    break
        return verses

