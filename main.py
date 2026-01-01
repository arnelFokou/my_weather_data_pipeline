import os
from dotenv import load_dotenv
import pandas as pd
from datetime import datetime as dt
import requests
from sqlalchemy import create_engine

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

    output_data["temp"]         = int(data['main'] ['temp'] - 273.15) # convert from kelvin to celsius
    output_data["feel_temp"]    = int(data['main'] ['feels_like'] -273.15)
    output_data["humidity"]     = data['main'] ['humidity']
    output_data["wind_speed"]   = int(data['wind'] ['speed']) * 3.6 # convert from m/s to km/h

    output_data["country"]      = data['sys'] ['country']
    output_data["city_name"]    = data['name']

    output_data["dt"]           = dt.fromtimestamp(data['dt']).strftime('%Y-%m-%d %H:%M:%S')
    output_data['extract_date'] = dt.now().strftime('%Y-%m-%d %H:%M:%S')

    return output_data



def load(data_cleaned):
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_USER = os.getenv("DB_USER")
    DB_PORT = os.getenv("DB_PORT")
    DB_HOST = os.getenv("DB_HOST")
    DB_NAME = os.getenv("DB_NAME")
    engine = create_engine(f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")
    
    df = pd.DataFrame([data_cleaned])
    try:
        df.to_sql("weather_table",engine,if_exists='append',index=False)
        print("Data added Succesfully")

    except Exception as e:
        # Toute autre erreur (Python, Pandas, etc.)
        print(f"❌ Erreur inattendue : {e}")
    finally:
        name_file = data_cleaned['extract_date'].replace(" ","_").split(":")[0] 
        df.to_csv(f"extraction_{name_file}.csv")

data = extract()

data_cleaned = transform(data)

load(data_cleaned)