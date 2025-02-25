# Medical Diagnosis System

## Overview
This project is an AI-driven medical diagnosis system designed to assist in predicting diseases based on symptoms, patient history, and medical images. It also includes features such as lab test recommendations, hospital and pharmacy integration, and a virtual health assistant.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setup and Installation](#setup-and-installation)
- [Running the Application](#running-the-application)
- [API Endpoints](#api-endpoints)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features
- Symptom extraction using NLP (SciSpaCy & BioBERT)
- Disease prediction using machine learning models
- Medical image processing using CNN models (ResNet, EfficientNet, VGG16)
- Lab test recommendations
- Chronic disease risk assessment
- Hospital and pharmacy integration
- AI-powered virtual health assistant
- Telemedicine scheduling
- Real-time analytics dashboard for healthcare providers

## Technologies Used
- Python
- Flask
- SciSpaCy
- TensorFlow/PyTorch
- PostgreSQL
- Docker
- Chart.js

## Setup and Installation

### Prerequisites
- Python 3.9 or later
- Docker
- Docker Compose
- Kaggle account and API key
- PostgreSQL

### Cloning the Repository
```bash
git clone https://github.com/your-username/medical-diagnosis-system.git
cd medical-diagnosis-system
```

### Setting Up Kaggle API
1. Sign in to your Kaggle account.
2. Go to "My Account" and click on "Create New API Token" to download the `kaggle.json` file.
3. Place the `kaggle.json` file in the root directory of the project.

### Installing Dependencies
1. Create a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

### Setting Up Environment Variables
Create a `.env` file in the root directory and add the following environment variables:
```env
FLASK_APP=run.py
FLASK_ENV=development
DATABASE_URL=postgresql://postgres:password@db:5432/medical_db
KAGGLE_USERNAME=your_kaggle_username
KAGGLE_KEY=your_kaggle_api_key
```

### Setting Up Docker
1. Build and run the Docker containers:
   ```bash
   docker-compose up --build
   ```
2. Access the application at `http://localhost:5000`.

## Running the Application

### Running Flask Application
To run the Flask development server, use the following command:
```bash
flask run
```

### Running with Docker
To run the application using Docker, use the following command:
```bash
docker-compose up
```

## API Endpoints

### Symptom Prediction
- **Endpoint**: `/predict`
- **Method**: POST
- **Description**: Predict disease based on symptoms
- **Request Body**:
  ```json
  {
    "symptoms": "fever, cough, headache"
  }
  ```

### Upload Medical Image
- **Endpoint**: `/upload_image`
- **Method**: POST
- **Description**: Upload and process medical images (X-ray, MRI)
- **Request Body**: Multipart form data with file

### Chronic Disease Risk Assessment
- **Endpoint**: `/chronic_disease_risk`
- **Method**: POST
- **Description**: Assess risk for chronic diseases
- **Request Body**:
  ```json
  {
    "features": [value1, value2, ...]
  }
  ```

### Find Nearest Hospitals
- **Endpoint**: `/find_hospitals`
- **Method**: POST
- **Description**: Find nearest hospitals based on location
- **Request Body**:
  ```json
  {
    "location": "New York"
  }
  ```

### Virtual Health Assistant
- **Endpoint**: `/chat`
- **Method**: POST
- **Description**: Chat with AI-powered virtual health assistant
- **Request Body**:
  ```json
  {
    "message": "What are the symptoms of flu?"
  }
  ```

### Telemedicine Scheduling
- **Endpoint**: `/schedule_telemedicine`
- **Method**: POST
- **Description**: Schedule a telemedicine appointment
- **Request Body**:
  ```json
  {
    "provider_id": "123",
    "appointment_date": "2025-03-01"
  }
  ```

### Analytics Dashboard
- **Endpoint**: `/analytics`
- **Method**: GET
- **Description**: Get real-time analytics data for healthcare providers

## Usage
1. **Symptom Prediction**: Enter symptoms and get a probable disease prediction.
2. **Medical Image Upload**: Upload X-ray or MRI images for automated analysis.
3. **Chronic Disease Risk Assessment**: Assess your risk for chronic diseases.
4. **Find Hospitals**: Find the nearest hospitals based on your location.
5. **Virtual Health Assistant**: Chat with the AI-powered assistant for health-related queries.
6. **Telemedicine**: Schedule telemedicine appointments with healthcare providers.
7. **Analytics Dashboard**: View real-time analytics data for healthcare providers.

## Contributing
Contributions are welcome! Please read the [CONTRIBUTING.md](CONTRIBUTING.md) file for guidelines on how to contribute to this project.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.