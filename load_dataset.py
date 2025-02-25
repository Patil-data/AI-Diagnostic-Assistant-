import pandas as pd
from app import db
from models import Symptom, Disease

# Load the dataset
df = pd.read_csv('data/processed_dataset.csv')

# Load data into the database
for index, row in df.iterrows():
    symptom = Symptom.query.filter_by(name=row['Symptom']).first()
    if not symptom:
        symptom = Symptom(name=row['Symptom'])
        db.session.add(symptom)
        db.session.commit()
    disease = Disease.query.filter_by(name=row['Disease']).first()
    if not disease:
        disease = Disease(name=row['Disease'])
        db.session.add(disease)
        db.session.commit()
    # Here you can associate symptoms and diseases if there's a many-to-many relationship