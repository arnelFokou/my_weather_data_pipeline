import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
import pandas as pd

load_dotenv()

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
        # capture toute  erreur (Python, Pandas, sqlalchemy, etc.)
        print(f" Erreur inattendue : {e}")
    finally:
        name_file = data_cleaned['extract_date'].replace(" ","_").split(":")[0] 
        df.to_csv(f"extraction_{name_file+"h"}.csv")
