import os

import pytest
from airflow.models import DagBag

os.environ["DBT_PROFILES_DIR"] = "./"


@pytest.fixture()
def dagbag():
    return DagBag(dag_folder="infra/airflow/dags/ELT.py", include_examples=False)


def test_dag_loaded(dagbag: DagBag) -> None:
    dag = dagbag.get_dag(dag_id="ELT_DEV")
    assert dagbag.import_errors == {}
    assert dag is not None
    assert len(dag.tasks) == 4
    dag = dagbag.get_dag(dag_id="ELT_PROD")
    assert dagbag.import_errors == {}
    assert dag is not None
    assert len(dag.tasks) == 5
    dag = dagbag.get_dag(dag_id="Montecarlo")
    assert dagbag.import_errors == {}
    assert dag is not None
    assert len(dag.tasks) == 1
