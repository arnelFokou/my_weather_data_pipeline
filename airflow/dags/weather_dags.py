from pathlib import Path
import sys
# chemin du fichier DAG actuel
current_file = Path(__file__).resolve()

# remonter 2 niveaux (dags -> airflow -> my_weather_data_pipeline)
project_root = current_file.parent.parent.parent

# ajouter au path pour que Python trouve etl_functions
sys.path.append(str(project_root))


from airflow import DAG
from airflow.operators.python import PythonOperator
from etl_functons.extract import extract
from etl_functons.load import load
from etl_functons.transform import transform 
from etl_functons.load_to_postgres import load_to_postgres
from datetime import datetime







with DAG(
    'first_weather_dag',
    description='A simple ETL DAG',
    schedule = '30 * * * *',
    start_date = datetime(2025, 1, 5),
    catchup = False
) as weather_dag:
    
    extract_task = PythonOperator(
        task_id = "extract",
        python_callable = extract
        
    )

    transform_task = PythonOperator(
        task_id = "transform",
        python_callable = transform
    )

    load_task = PythonOperator(
        task_id = "load",
        python_callable = load
    )

    load_db = PythonOperator(
        task_id = 'db',
        python_callable = load_to_postgres

    )
   
    extract_task >> transform_task >> load_task >> load_db
