import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'a_really_strong_secret_key'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'postgresql://postgres:password@localhost/medical_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False