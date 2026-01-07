
from airflow.providers.postgres.hooks.postgres import PostgresHook


def load_to_postgres(**args):
    df_cleaned = args['ti'].xcom_pull(task_ids = "transform")
    # 1. On initialise le Hook avec l'ID créé dans l'interface
    pg_hook = PostgresHook(postgres_conn_id='postgres_conn')
    
    # 2. On transforme le DataFrame en liste de tuples (format attendu par le Hook)
    rows = [df_cleaned.values()]
    target_fields = list(df_cleaned.keys())
    # 3. On insère les données
    pg_hook.insert_rows(
        table='weather_table', 
        rows=rows, 
        target_fields=target_fields
    )
