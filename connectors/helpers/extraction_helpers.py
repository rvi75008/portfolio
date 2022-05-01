from typing import Any, Dict, List, Optional

import pandas as pd

from connectors.helpers.checks import checks


class ScrapedValuesError(Exception):
    """"""


def check_values(df: pd.DataFrame, check_list: List[Dict[str, Any]]) -> None:
    for check in check_list:
        if len(
            df[
                (df[check["selector"]["col"]] == check["selector"]["value"])
                & (df[check["condition"]["col"]] == check["condition"]["value"])
            ]
        ):
            raise ScrapedValuesError


def prepare_df_for_insertion(
    df: pd.DataFrame,
    sheet_name: str,
    transformations: Optional[Dict[str, Any]] = None,
    check: Optional[bool] = True,
) -> pd.DataFrame:
    if transformations is None:
        transformations = {}  # pragma: no cover
    cols = transformations.get("cols", df.columns)
    rows = transformations.get("rows", (0, len(df)))
    cleaning = transformations.get("cleaning", [])
    new_cols = transformations.get("new_cols", [])
    df = df[cols].iloc[rows[0] : rows[1]]
    for c in cleaning:
        df[c[0]] = df[c[0]].apply(c[1])
    for new_col in new_cols:
        df[new_col[0]] = new_col[1]
    if check:
        check_values(df, checks.get(sheet_name))
    return df
