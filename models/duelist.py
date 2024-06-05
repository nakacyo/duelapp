from duelapp import db
# from datetime import datetime

class Duelist(db.Model):
    __tablename__ = 'duelist'
    number = db.Column(db.Integer, primary_key=True)  # 識別番号
    name = db.Column(db.String(10))  # 名前
    deck1 = db.Column(db.String(10))
    deck2 = db.Column(db.String(10))
    deck3 = db.Column(db.String(10))
    deck4 = db.Column(db.String(10))
    deck5 = db.Column(db.String(10))
