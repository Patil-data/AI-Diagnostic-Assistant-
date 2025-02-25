import requests

def find_nearest_hospitals(location):
    api_url = f"https://api.example.com/hospitals?location={location}"
    response = requests.get(api_url)
    hospitals = response.json()
    return hospitals