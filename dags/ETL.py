
from datetime import datetime, timedelta
import psycopg2
from sqlalchemy import create_engine
from sqlalchemy import text

import pandas as pd
from sodapy import Socrata

import airflow
from airflow import DAG
from airflow.operators.python import PythonOperator



engine = create_engine("postgresql+psycopg2://airflow:airflow@postgres/airflow")
conn = engine.connect().execution_options(autocommit=True)


default_args = {
    "owner":"JaimeTavera",
    "start_date": airflow.utils.dates.days_ago(0),
    "retries": 1,   
    "retry_delay": timedelta(minutes=5),
    "schedule_interval": "15 8 * * *"
}   


def PostgreSQL():
    conn.execute(text("DROP TABLE IF EXISTS tasa_cambio"))

    sql_query = text(''' CREATE TABLE IF NOT EXISTS tasa_cambio (
                id SERIAL PRIMARY KEY,
                valor real,
                vigenciadesde date,
                vigenciahasta date);
            ''')
    conn.execute(sql_query)





def get_last_10_TRM():
    client = Socrata("www.datos.gov.co", None)
    results = client.get("ceyp-9c7c", limit=10, order = "vigenciadesde DESC")
    results_df = pd.DataFrame.from_records(results)

    results_df.to_sql("tasa_cambio", con=conn, if_exists="replace", index=False)
    



with DAG(
    default_args = default_args,
    dag_id="get_TRM",
    start_date=datetime(2023, 1, 1),
    schedule="15 8 * * *"
) as dag:

    get_TMR = PythonOperator(
        task_id = "get_last_10_days_TRM",
        python_callable = get_last_10_TRM
    )

    Postgre = PythonOperator(
        task_id = "Create_PostgreSQL_database",
        python_callable = PostgreSQL
    )




        
Postgre >> get_TMR




