import pandas as pd
from pandas._testing import assert_frame_equal

from connectors.helpers.extraction_helpers import clean_df
from connectors.helpers.transformation_config import transformations


def test_clean_df() -> None:
    test_data = pd.read_csv("tests/data/details_stg.csv", nrows=3)
    cleaned_df = clean_df(test_data, transformations.get("details"))
    assert_frame_equal(
        cleaned_df,
        pd.DataFrame(
            [
                {
                    "actif": "OR - 10F",
                    "valorisation": 3500.0,
                    "qte": 20.0,
                    "pu": 0,
                    "pru": 121.00,
                    "devise": "Metal",
                    "date": "2022-04-06 07:02:01.512803",
                    "day": "22-04-06",
                },
                {
                    "actif": "AG - 5F",
                    "valorisation": 33.0,
                    "qte": 5.0,
                    "pu": 0,
                    "pru": 6,
                    "devise": "Metal",
                    "date": "2022-04-06 07:02:01.512803",
                    "day": "22-04-06",
                },
                {
                    "actif": "AG - Phil",
                    "valorisation": 167.3,
                    "qte": 7.0,
                    "pu": 0,
                    "pru": 15.2,
                    "devise": "Metal",
                    "date": "2022-04-06 07:02:01.512803",
                    "day": "22-04-06",
                },
            ]
        ),
    )
