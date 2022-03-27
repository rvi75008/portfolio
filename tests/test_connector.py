from unittest.mock import AsyncMock, MagicMock

import pytest
from pytest_httpx import HTTPXMock
from pytest_mock import MockFixture

from config import config
from connectors.google_sheet_connector import Connector, DataSource, main


@pytest.fixture
def datasource() -> DataSource:
    return DataSource(
        "fooosheet",
        "sheet1",
        {
            "cols": ["bar", "foo"],
            "rows": (0, 1000),
            "cleaning": [
                (
                    "foo",
                    lambda x: float(x),
                )
            ],
            "new_cols": [("far", 5)],
        },
    )


@pytest.fixture
def connector(datasource: DataSource) -> Connector:
    return Connector(datasources=[datasource, datasource])


def test_datasource_build_url(datasource: DataSource) -> None:
    assert (
        datasource.build_url()
        == "https://docs.google.com/spreadsheets/d/fooosheet/gviz/tq?tqx=out:csv&sheet=sheet1"
    )


@pytest.mark.asyncio
async def test_connector_extraction(
    connector: Connector, mocker: MockFixture, httpx_mock: HTTPXMock
) -> None:
    fake_data = "foo,bar\n1,2\n3,4\n"
    httpx_mock.add_response(
        method="GET",
        url="https://docs.google.com/spreadsheets/d/fooosheet/gviz/tq?tqx=out:csv&sheet=sheet1",
        status_code=200,
        text=fake_data,
    )
    mocked_to_csv = mocker.patch("pandas.DataFrame.to_csv")
    spyed_async_extract_csvs = mocker.spy(connector, "async_extract_csvs")
    await connector.extract_data("path/", ",")
    assert mocked_to_csv.call_count == 2
    assert spyed_async_extract_csvs.spy_return[0].to_dict(orient="records") == [
        {"bar": 2, "foo": 1},
        {"bar": 4, "foo": 3},
    ]
    assert spyed_async_extract_csvs.spy_return[0].to_dict(orient="records") == [
        {"bar": 2, "foo": 1},
        {"bar": 4, "foo": 3},
    ]


@pytest.mark.asyncio
async def test_main(mocker: MockFixture, connector: Connector) -> None:
    mocker.patch("connectors.google_sheet_connector.open")
    mocker.patch(
        "connectors.google_sheet_connector.transformations",
        return_value={"retails": {}, "dente": {}},
    )
    config.settings.EXTRACTION_CONFIGURATION = {
        "spreadsheet_id": 12,
        "sheet_names": ["foo", "bar"],
    }
    mock = AsyncMock()
    mocker.patch("connectors.google_sheet_connector.Connector", return_value=mock)

    await main()
    assert mock.extract_data.call_count == 1
