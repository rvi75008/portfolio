from airflow import DAG
from datetime import datetime
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from connectors.google_sheet_connector import run_extraction
from loader.loader import run_loading
import os
from datetime import timedelta

os.chdir(os.environ['DBT_PROFILES_DIR'])

with DAG(dag_id='ELT_DEV', start_date=datetime(2022, 1, 1, 12, 0, 0), schedule_interval="@daily", catchup=False) as dag:
    extraction = PythonOperator(
        task_id='extract_data',
        python_callable=run_extraction,
        retries=3,
        retry_delay=timedelta(seconds=10)
    )

    loading = PythonOperator(
        task_id='load_data',
        python_callable=run_loading,
        retries=3,
        retry_delay=timedelta(seconds=10)
    )

    transforming = BashOperator(
        task_id='transform_data',
        bash_command='dbt run --project-dir /dbt'
    )

    data_quality_checking = BashOperator(
        task_id='check_data_quality',
        bash_command='dbt test --project-dir /dbt'
    )


extraction >> loading >> transforming >> data_quality_checking


with DAG(dag_id='ELT_PROD', start_date=datetime(2022, 1, 1, 12, 0, 0), schedule_interval="@daily", catchup=False) as dag_prod:
    extraction = PythonOperator(
        task_id='extract_data',
        python_callable=run_extraction,
        retries=3,
        retry_delay=timedelta(seconds=10),
        op_kwargs={'target': None}
    )

    loading = PythonOperator(
        task_id='load_data',
        python_callable=run_loading,
        retries=3,
        retry_delay=timedelta(seconds=10),
        op_kwargs={'target': None}
    )

    transforming = BashOperator(
        task_id='transform_data',
        bash_command='dbt run --project-dir /dbt -t prod'
    )

    data_quality_checking = BashOperator(
        task_id='check_data_quality',
        bash_command='dbt test --project-dir /dbt -t prod'
    )
