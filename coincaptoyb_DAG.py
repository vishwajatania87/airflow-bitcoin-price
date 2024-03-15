from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
import pytz
import requests
import pandas as pd
from sqlalchemy import create_engine
from airflow.models import Variable

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 2, 8),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(seconds=30),
}

def fetch_and_upload_bitcoin_price():
    api_url = 'https://api.coincap.io/v2/assets/bitcoin'
    response = requests.get(api_url)
    data = response.json()

    if 'data' in data and 'priceUsd' in data['data']:
        bitcoin_price = data['data']['priceUsd']
    # Get the current time in Eastern Standard Time (EST)
        est_tz = pytz.timezone('US/Eastern')
        timestamp = datetime.now(est_tz).strftime('%Y-%m-%d %H:%M:%S')
        result = [{'price': bitcoin_price, 'timestamp': timestamp}]

        # Convert the data to a DataFrame
        df = pd.DataFrame(result)

        # Securely fetch database connection details
        db_url = Variable.get("dbconn")  # Corrected Variable.get("dbconn")

        # Create SQLAlchemy engine
        engine = create_engine(db_url)

        # Insert DataFrame into PostgreSQL table
        df.to_sql('bitcoin_price', engine, schema='coincap_bitcoin', if_exists='append', index=False)
    else:
        raise Exception('Unable to fetch Bitcoin price from CoinCap API')

with DAG('coincaptoyb_dag',
         default_args=default_args,
         schedule_interval='*/1 * * * *',  # Run every minute
         catchup=False) as dag:

    fetch_and_upload_task = PythonOperator(
        task_id='fetch_and_upload_bitcoin_price',
        python_callable=fetch_and_upload_bitcoin_price
    )

    fetch_and_upload_task  # Corrected placement of task within the DAG context manager