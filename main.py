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
    
    return response.json()

def transform(data):
    output_data ={}

    output_data["longitude"]    = data['coord'] ['lon']
    output_data["latitude"]     = data['coord'] [ 'lat']    
    output_data["description"]  = data['weather'] [0] ['description']

    output_data["temp"]         = data['main'] ['temp']
    output_data["feel_temp"]    = data['main'] ['feels_like']
    output_data["humidity"]     = data['main'] ['humidity']
    output_data["wind_speed"]   = int(data['wind'] ['speed']) * 3.6 # convert from m/s to km/h

    output_data["country"]      = data['sys'] ['country']
    output_data["city_name"]    = data['name']

    output_data["dt"]           = dt.fromtimestamp(data['dt']).strftime('%Y-%m-%d %H:%M:%S')
    output_data['extract_date'] = dt.now().strftime('%Y-%m-%d %H:%M:%S')

    df = pd.DataFrame([output_data],index=None) 
    name_file = output_data['extract_date'].replace(" ","_").split(":")[0] 
    df.to_csv(f"extraction_{name_file}.csv")

data = extract()

transform(data)