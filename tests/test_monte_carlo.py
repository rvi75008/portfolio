import pandas as pd
import pytest
from psycopg2 import OperationalError
from pytest_mock import MockFixture

from computations.monte_carlo import PortfolioReadingError, run_simulation
from config import config


def test_montecarlo_simulation_one_asset(mocker: MockFixture) -> None:
    config.settings.LOADER_CONNECTION_URI_PROD = "postgresql+psycopg2://bla:bla@bla:12"
    mocked_load = mocker.patch(
        "computations.monte_carlo.AsyncPostgresLoader.load_from_dataframe"
    )
    mocker.patch(
        "computations.monte_carlo.pd.read_sql",
        return_value=pd.DataFrame({"val": [6000]}),
    )
    run_simulation()
    assert mocked_load.call_args_list[0][0][0]["0%"].values.tolist()[0] == 0.0
    assert mocked_load.call_args_list[0][0][0]["max"].values.tolist()[0] >= 30000.0
    assert mocked_load.call_args_list[0][0][0]["50%"].values.tolist()[0] >= 16000.0
    assert mocked_load.call_args_list[0][0][0]["50%"].values.tolist()[0] <= 25000.0


def test_montecarlo_simulation_multiple_assets(mocker: MockFixture) -> None:
    config.settings.LOADER_CONNECTION_URI_PROD = "postgresql+psycopg2://bla:bla@bla:12"
    mocked_load = mocker.patch(
        "computations.monte_carlo.AsyncPostgresLoader.load_from_dataframe"
    )
    mocker.patch(
        "computations.monte_carlo.pd.read_sql",
        return_value=pd.DataFrame({"val": [6000, 4000]}),
    )
    run_simulation()
    assert mocked_load.call_args_list[0][0][0]["0%"].values.tolist()[0] == 0.0
    assert mocked_load.call_args_list[0][0][0]["max"].values.tolist()[0] >= 30000.0
    assert mocked_load.call_args_list[0][0][0]["50%"].values.tolist()[0] >= 16000.0
    assert mocked_load.call_args_list[0][0][0]["50%"].values.tolist()[0] <= 25000.0


def test_montecarlo_simulation_error(mocker: MockFixture) -> None:
    config.settings.LOADER_CONNECTION_URI_PROD = "postgresql+psycopg2://bla:bla@bla:12"
    mocker.patch(
        "computations.monte_carlo.pd.read_sql", side_effect=OperationalError("foo")
    )
    with pytest.raises(PortfolioReadingError):
        run_simulation()
