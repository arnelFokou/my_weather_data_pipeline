import sys
from airflow.providers.postgres.hooks.postgres import PostgresHook
from pathlib import Path
import pandas as pd

path = Path(__file__).resolve()
archive_dir = path.parent.parent
sys.path.append(str(archive_dir))

def load(**args):
    #Step 1:Archivage
    # recuperation du retout de la tache transform en utilisant les xcom
    data_cleaned = args['ti'].xcom_pull(task_ids = "transform")
   
    df = pd.DataFrame([data_cleaned])
   
    name_file = data_cleaned['extract_date'].replace(" ","_").split(":")[0] 

    df.to_csv(f"files_extracted/extraction_{name_file+"h"}.csv")

    #Step 2: stockage dans la BD
    # Initialisation du Hook avec l'ID de la connexion cree en amont
    pg_hook = PostgresHook(postgres_conn_id='postgres_conn')
    
    # Transformation du DataFrame en liste de tuples (format attendu par le Hook)
    rows = [data_cleaned.values()]
    target_fields = list(data_cleaned.keys())
    # On insertion des données dans la BD
    pg_hook.insert_rows(
        table='weather_table', 
        rows=rows, 
        target_fields=target_fields
    )

    

