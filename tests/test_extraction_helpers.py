import pandas as pd
from pandas._testing import assert_frame_equal

from connectors.helpers.extraction_helpers import prepare_df_for_insertion
from connectors.helpers.transformation_config import transformations


def test_clean_df() -> None:
    test_data = pd.read_csv("tests/data/details_stg.csv", nrows=6)
    cleaned_df = prepare_df_for_insertion(
        test_data, "details", transformations.get("details")
    )
    assert_frame_equal(
        cleaned_df[["actif", "valorisation", "qte", "pu", "pru", "devise", "type"]][:3],
        pd.DataFrame(
            [
                {
                    "actif": "OR - 10F",
                    "valorisation": 3500.0,
                    "qte": 20.0,
                    "pu": 0.0,
                    "pru": 121.00,
                    "devise": "Metal",
                    "type": "metal",
                },
                {
                    "actif": "AG - 5F",
                    "valorisation": 33.0,
                    "qte": 5.0,
                    "pu": 0.0,
                    "pru": 6,
                    "devise": "Metal",
                },
                {
                    "actif": "AG - Phil",
                    "valorisation": 167.3,
                    "qte": 7.0,
                    "pu": 0.0,
                    "pru": 15.2,
                    "devise": "Metal",
                },
            ]
        ),
    )
