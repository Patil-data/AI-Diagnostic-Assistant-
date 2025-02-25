import os
import kaggle

# Set up Kaggle API credentials
os.environ['KAGGLE_USERNAME'] = 'your_kaggle_username'
os.environ['KAGGLE_KEY'] = 'your_kaggle_api_key'

# Download the dataset
kaggle.api.dataset_download_files('username/dataset-name', path='data/', unzip=True)

# Preprocess the dataset
import pandas as pd

df = pd.read_csv('data/dataset.csv')
df = df[['Symptom', 'Disease']]  # Select relevant columns
df.to_csv('data/processed_dataset.csv', index=False)