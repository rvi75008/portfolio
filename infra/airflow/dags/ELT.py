from airflow import DAG
from datetime import datetime
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from connectors.google_sheet_connector import run_extraction
from loader.loader import run_loading

with DAG(dag_id='ELT', start_date=datetime(2022, 1, 1, 12, 0, 0), schedule_interval="@daily", catchup=False) as dag:
    extraction = PythonOperator(
        task_id='extract_data',
        python_callable=run_extraction
    )

    loading = PythonOperator(
        task_id='load_data',
        python_callable=run_loading
    )

    transforming = BashOperator(
        task_id='transform_data',
        bash_command='dbt run'
    )

    data_quality_checking = BashOperator(
        task_id='check_data_quality',
        bash_command='dbt test'
    )


extraction >> loading >> transforming >> data_quality_checking
