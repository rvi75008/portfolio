import os
from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from scrapper.scrapper import run_scrapping
from computations.monte_carlo import run_simulation
from connectors.google_sheet_connector import run_extraction
from loader.loader import run_loading

os.chdir(os.environ["DBT_PROFILES_DIR"])


def on_failure_callback(context):
    import requests

    requests.post(
        os.environ.get("SLACK_URL"),
        json={
            "username": "airflow",
            "channel": "#portfolio-elt",
            "text": f"DAG Failed, context: {context}",
        },
    )


with DAG(
    dag_id="ELT_DEV",
    start_date=datetime(2022, 1, 1, 12, 0, 0),
    schedule_interval="@daily",
    catchup=False,
    default_args={"owner": "airflow", "on_failure_callback": on_failure_callback},
) as dag:
    extraction = PythonOperator(
        task_id="extract_data",
        python_callable=run_extraction,
        retries=3,
        retry_delay=timedelta(seconds=10),
    )

    loading = PythonOperator(
        task_id="load_data",
        python_callable=run_loading,
        retries=3,
        retry_delay=timedelta(seconds=10),
    )

    transforming = BashOperator(
        task_id="transform_data", bash_command="dbt run --project-dir /dbt"
    )

    data_quality_checking = BashOperator(
        task_id="check_data_quality", bash_command="dbt test --project-dir /dbt"
    )

extraction >> loading >> transforming >> data_quality_checking

with DAG(
    dag_id="ELT_PROD",
    start_date=datetime(2022, 1, 1, 12, 0, 0),
    schedule_interval="@hourly",
    catchup=False,
    default_args={"owner": "airflow", "on_failure_callback": on_failure_callback},
) as dag_prod:
    extraction = PythonOperator(
        task_id="extract_data",
        python_callable=run_extraction,
        retries=3,
        retry_delay=timedelta(seconds=10),
        op_kwargs={"target": None},
    )

    loading = PythonOperator(
        task_id="load_data",
        python_callable=run_loading,
        retries=3,
        retry_delay=timedelta(seconds=10),
        op_kwargs={"target": None},
    )

    scrapping = PythonOperator(
        task_id="scrap_data",
        python_callable=run_scrapping,
        retries=3,
        retry_delay=timedelta(seconds=10)
    )

    transforming = BashOperator(
        task_id="transform_data", bash_command="dbt run --project-dir /dbt -t prod"
    )

    data_quality_checking = BashOperator(
        task_id="check_data_quality", bash_command="dbt test --project-dir /dbt -t prod"
    )


with DAG(
    dag_id="Montecarlo",
    start_date=datetime(2022, 1, 1, 19, 0, 0),
    schedule_interval="@daily",
    catchup=False,
    default_args={"owner": "airflow", "on_failure_callback": on_failure_callback},
) as montecarlo:
    computations = PythonOperator(
        task_id="compute_montecarlo",
        python_callable=run_simulation,
        retries=3,
        retry_delay=timedelta(seconds=10),
    )
