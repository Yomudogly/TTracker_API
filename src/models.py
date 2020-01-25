import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Boolean

db = SQLAlchemy()

class Fullfilment_center(db.Model):
    __tablename__ = 'fc'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    address = db.Column(db.String(120), nullable=False)
    city = db.Column(db.String(120), nullable=False)
    zip = db.Column(db.String(120), nullable=False)
    

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "address": self.address,
            "city": self.city,
            "zip": self.zip
        }



class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    fc_id = db.Column(db.Integer, db.ForeignKey('fc.id'))
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)

    def serialize(self):
        return {
            "username": self.username,
            "email": self.email,
            "id": self.id,
            "password": self.password,
            "fc_id": self.fc_id
        }

class Van(db.Model):
    __tablename__ = 'van'
    id = db.Column(db.Integer, primary_key=True)
    fc_id = db.Column(db.Integer, db.ForeignKey('fc.id'))
    vin = db.Column(db.String(17), unique=True, nullable=False)
    
    def serialize(self):
        return {
            "vin": self.vin,
            "fc_id": self.fc_id,
            "id": self.id,
        }

class Schedule_wave(db.Model):
    __tablename__ = 'wave'
    id = db.Column(db.Integer, primary_key=True)
    fc_id = db.Column(db.Integer, db.ForeignKey('fc.id'))
    start_time = db.Column(DateTime, default=datetime.datetime.utcnow)
    end_time = db.Column(DateTime, default=datetime.datetime.utcnow)
    status = db.Column(Boolean, default=True)
    

    def serialize(self):
        return {
            "start_time": self.start_time,
            "end_time": self.end_time,
            "status": self.vin,
            "fc_id": self.fc_id,
            "id": self.id,
        }


class Activity(db.Model):
    __tablename__ = 'activity'
    id = db.Column(db.Integer, primary_key=True)
    van_id = db.Column(db.Integer, db.ForeignKey('van.id'))
    wave_id = db.Column(db.Integer, db.ForeignKey('wave.id'))
    scan_time = db.Column(DateTime, default=datetime.datetime.utcnow)
    

    def serialize(self):
        return {
            "scan_time": self.scan_time,
            "wave_id": self.wave_id,
            "van_id": self.van_id,
            "id": self.id,
        }
