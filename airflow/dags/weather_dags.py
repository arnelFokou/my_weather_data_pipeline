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
from datetime import datetime







with DAG(
    'first_weather_dag',
    description='A simple ETL DAG',
    schedule = '30 * * * *',
    start_date = datetime(2025, 1, 7),
    catchup =   True # fait des rattrapages depuis le 5 janvier
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

     
    extract_task >> transform_task >> load_task 
