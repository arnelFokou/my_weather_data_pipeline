import os
import requests
from dotenv import load_dotenv

load_dotenv('.env.secrets')
def extract():

    url = f"https://api.openweathermap.org/data/2.5/weather?q=Paris&appid={os.getenv('API_KEY')}"
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException as e:
        raise RuntimeError(f"Erreur lors de l'appel API : {e}")
    
    return response.json()