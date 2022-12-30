import uuid
from datetime import date
from flask_sqlalchemy import SQLAlchemy

from app import db


class Wave(db.Model):
    __tablename__ = 'waves'
    wave_id = db.Column(db.String(60), primary_key=True)
    title = db.Column(db.String(360))
    description = db.Column(db.String(2000))
    date_created = db.Column(db.String(50))
    category = db.Column(db.String(300))
    user_id = db.Column(db.String(60), db.ForeignKey('users.user_id'), nullable=False)


    def __init__(self, title, description,category, user_id, date_created ):
        self.wave_id = uuid.uuid4()
        self.title = title
        self.description = description
        self.date_created = date_created
        self.category = category
        self.user_id = user_id


      

    def __repr__(self):
        return f"Wave('{self.wave_id}', '{self.title}', '{self.description}', '{self.date_created}', '{self.user_id}')"

    def create_wave(self):
        try:
            wave = Wave(title=self.title, description=self.description,category=self.category, user_id=self.user_id, date_created=self.date_created)
            db.session.add(wave)
            db.session.commit()
            serialized_wave = {
                "wave_id": wave.wave_id,
                "title": wave.title,
                "description": wave.description,
                "date_created": wave.date_created,
                "user_id": wave.user_id
            }
            return serialized_wave
        except Exception as e:
            print("exception", e)
            db.session.rollback()

    @classmethod
    def get_waves(cls):
        waves = cls.query.all()
        
        return waves

    @classmethod
    def get_wave(cls,wave_id):
        wave = cls.query.filter_by(wave_id=wave_id).first()
        return wave

