import os
from dotenv import load_dotenv
import pandas as pd
from datetime import datetime as dt
import requests

load_dotenv(".env.secrets")


def extract():

    url = f"https://api.openweathermap.org/data/2.5/weather?q=Paris&appid={os.getenv('API_KEY')}"
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException as e:
        raise RuntimeError(f"Erreur lors de l'appel API : {e}")


    


print(extract())