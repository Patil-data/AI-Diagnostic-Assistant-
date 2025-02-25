from flask import render_template, request, redirect, url_for
from app import app, db
from models import Symptom, Disease, UserInput, LabTest, MedicalRecord, Message, ChronicDiseaseRisk, Hospital, Pharmacy, SymptomTracking, MedicationReminder
from werkzeug.utils import secure_filename
import os
import requests

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'dcm'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    symptoms = request.form['symptoms']
    # Placeholder for prediction logic
    predicted_disease = "Disease X"
    user_input = UserInput(symptoms=symptoms, predicted_disease=predicted_disease)
    db.session.add(user_input)
    db.session.commit()
    return render_template('index.html', prediction=predicted_disease)

@app.route('/recommend_tests', methods=['POST'])
def recommend_tests():
    predicted_disease = request.form['predicted_disease']
    disease = Disease.query.filter_by(name=predicted_disease).first()
    if disease:
        lab_tests = LabTest.query.filter_by(disease_id=disease.id).all()
    else:
        lab_tests = []
    return render_template('index.html', lab_tests=lab_tests)

@app.route('/medical_records', methods=['GET', 'POST'])
def medical_records():
    if request.method == 'POST':
        user_input_id = request.form['user_input_id']
        diagnosis = request.form['diagnosis']
        prescriptions = request.form['prescriptions']
        record = MedicalRecord(user_input_id=user_input_id, diagnosis=diagnosis, prescriptions=prescriptions)
        db.session.add(record)
        db.session.commit()
    records = MedicalRecord.query.all()
    return render_template('medical_records.html', records=records)

@app.route('/messages', methods=['GET', 'POST'])
def messages():
    if request.method == 'POST':
        sender = request.form['sender']
        receiver = request.form['receiver']
        content = request.form['content']
        message = Message(sender=sender, receiver=receiver, content=content)
        db.session.add(message)
        db.session.commit()
    messages = Message.query.order_by(Message.timestamp.desc()).all()
    return render_template('messages.html', messages=messages)

@app.route('/upload_image', methods=['GET', 'POST'])
def upload_image():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            # Placeholder for image processing logic
            return redirect(url_for('uploaded_file', filename=filename))
    return render_template('upload_image.html')

@app.route('/find_hospitals', methods=['POST'])
def find_hospitals():
    location = request.form['location']
    # Placeholder for API call to find nearest hospitals
    hospitals = [
        {'name': 'Hospital A', 'address': '123 Main St', 'latitude': 37.7749, 'longitude': -122.4194},
        {'name': 'Hospital B', 'address': '456 Elm St', 'latitude': 37.7849, 'longitude': -122.4094}
    ]
    return render_template('index.html', hospitals=hospitals)

@app.route('/schedule_appointment', methods=['POST'])
def schedule_appointment():
    hospital_id = request.form['hospital_id']
    appointment_date = request.form['appointment_date']
    # Placeholder for logic to schedule appointment
    return redirect(url_for('index'))

@app.route('/link_pharmacy', methods=['POST'])
def link_pharmacy():
    prescription_id = request.form['prescription_id']
    pharmacy_id = request.form['pharmacy_id']
    # Placeholder for logic to link pharmacy for prescription refills
    return redirect(url_for('index'))

@app.route('/track_symptoms', methods=['POST'])
def track_symptoms():
    user_id = request.form['user_id']
    symptoms = request.form['symptoms']
    symptom_tracking = SymptomTracking(user_id=user_id, symptoms=symptoms)
    db.session.add(symptom_tracking)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/set_medication_reminder', methods=['POST'])
def set_medication_reminder():
    user_id = request.form['user_id']
    medication = request.form['medication']
    reminder_time = request.form['reminder_time']
    medication_reminder = MedicationReminder(user_id=user_id, medication=medication, reminder_time=reminder_time)
    db.session.add(medication_reminder)
    db.session.commit()
    return redirect(url_for('index'))