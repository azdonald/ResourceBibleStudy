from marshmallow import Schema, fields

class DailyReadingSchema(Schema):
    Id = fields.Int()
    FirstReading = fields.Str()
    SecondReading = fields.Str()
    ThirdReading = fields.Str()
    BookVersion = fields.Str()
    DayOfTheYear = fields.Int()