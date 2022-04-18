import os
from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.utils.trigger_rule import TriggerRule

from computations.monte_carlo import run_simulation
from connectors.google_sheet_connector import run_extraction
from loader.loader import run_loading
from scrapper.scrapper import run_scrapping

os.chdir(os.environ["DBT_PROFILES_DIR"])


class DagFailed(Exception):
    """"""


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
    schedule_interval="*/15 * * * *",
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
        trigger_rule=TriggerRule.NONE_FAILED,
    )

    check_extraction_quality = BashOperator(
        task_id="check_extraction_quality",
        bash_command="dbt test --project-dir /dbt -t prod --select test_garbage_extracted",
        trigger_rule=TriggerRule.NONE_FAILED
    )

    scrapping = PythonOperator(
        task_id="scrap_data",
        python_callable=run_scrapping,
        retries=3,
        retry_delay=timedelta(seconds=10),
        trigger_rule=TriggerRule.NONE_FAILED,
    )

    transforming = BashOperator(
        task_id="transform_data",
        bash_command="dbt run --project-dir /dbt -t prod",
        trigger_rule=TriggerRule.NONE_FAILED,
    )

    data_quality_checking = BashOperator(
        task_id="check_data_quality",
        bash_command="dbt test --project-dir /dbt -t prod",
        trigger_rule=TriggerRule.NONE_FAILED,
    )

extraction >> loading >> check_extraction_quality >> scrapping >> transforming >> data_quality_checking

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
