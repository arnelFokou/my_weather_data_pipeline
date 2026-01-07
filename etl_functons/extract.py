import requests
from airflow.models import Variable


def extract():
    API_KEY = Variable.get("API_KEY")
    url = f"https://api.openweathermap.org/data/2.5/weather?q=Paris&appid={API_KEY}"
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException as e:
        raise RuntimeError(f"Erreur lors de l'appel API : {e}")
    
    return response.json()