from flask import render_template, request, redirect, url_for, jsonify
from app import app, db
from models import Symptom, Disease, UserInput, LabTest, MedicalRecord, Message, ChronicDiseaseRisk, Hospital, Pharmacy, SymptomTracking, MedicationReminder
from nlp import extract_symptoms
from image_processing import process_image
from chronic_disease_risk import chronic_disease_risk
from hospital_integration import find_nearest_hospitals
from chatbot import generate_response
from telemedicine import schedule_telemedicine
from analytics_dashboard import get_analytics_data
import joblib
from werkzeug.utils import secure_filename
import os
import datetime

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'dcm'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    symptoms_text = request.form['symptoms']
    symptoms = extract_symptoms(symptoms_text)
    # Preprocess symptoms for model prediction
    
    # Make prediction
    prediction = model.predict([symptoms])
    confidence_scores = model.predict_proba([symptoms])
    
    user_input = UserInput(symptoms=symptoms_text, predicted_disease=prediction[0])
    db.session.add(user_input)
    db.session.commit()

    return render_template('index.html', prediction=prediction[0], confidence_scores=confidence_scores)

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
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            probabilities = process_image(filepath)
            return render_template('upload_image.html', probabilities=probabilities)
    return render_template('upload_image.html')

@app.route('/chronic_disease_risk', methods=['POST'])
def chronic_disease_risk():
    data = request.json
    model = joblib.load('models/chronic_disease_model.pkl')
    prediction = model.predict([data['features']])
    risk_score = model.predict_proba([data['features']])
    return jsonify({'prediction': prediction[0], 'risk_score': risk_score.tolist()})

@app.route('/find_hospitals', methods=['POST'])
def find_hospitals():
    location = request.form['location']
    hospitals = find_nearest_hospitals(location)
    return render_template('hospitals.html', hospitals=hospitals)

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

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_input = data['message']
    response = generate_response(user_input)
    return jsonify({"response": response})

@app.route('/schedule_telemedicine', methods=['POST'])
def schedule_telemedicine():
    data = request.json
    provider_id = data['provider_id']
    appointment_date = data['appointment_date']
    message = schedule_telemedicine(provider_id, appointment_date)
    return jsonify({"message": message})

@app.route('/analytics', methods=['GET'])
def analytics():
    data = get_analytics_data()
    return jsonify(data)