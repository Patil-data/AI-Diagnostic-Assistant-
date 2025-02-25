from app import db

class Symptom(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

class Disease(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

class UserInput(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    symptoms = db.Column(db.String(200), nullable=False)
    predicted_disease = db.Column(db.String(100), nullable=False)

class LabTest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    disease_id = db.Column(db.Integer, db.ForeignKey('disease.id'), nullable=False)
    disease = db.relationship('Disease', backref=db.backref('lab_tests', lazy=True))

class MedicalRecord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_input_id = db.Column(db.Integer, db.ForeignKey('user_input.id'), nullable=False)
    diagnosis = db.Column(db.String(100), nullable=False)
    prescriptions = db.Column(db.String(200), nullable=False)
    user_input = db.relationship('UserInput', backref=db.backref('medical_records', lazy=True))

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sender = db.Column(db.String(100), nullable=False)
    receiver = db.Column(db.String(100), nullable=False)
    content = db.Column(db.String(500), nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())

class ChronicDiseaseRisk(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user_input.id'), nullable=False)
    disease = db.Column(db.String(100), nullable=False)
    risk_score = db.Column(db.Float, nullable=False)
    suggestions = db.Column(db.String(500), nullable=False)
    user_input = db.relationship('UserInput', backref=db.backref('chronic_disease_risks', lazy=True))

class Hospital(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)

class Pharmacy(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)

class SymptomTracking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user_input.id'), nullable=False)
    symptoms = db.Column(db.String(200), nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())
    user_input = db.relationship('UserInput', backref=db.backref('symptom_trackings', lazy=True))

class MedicationReminder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user_input.id'), nullable=False)
    medication = db.Column(db.String(100), nullable=False)
    reminder_time = db.Column(db.Time, nullable=False)
    user_input = db.relationship('UserInput', backref=db.backref('medication_reminders', lazy=True))