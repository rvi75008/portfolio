from typing import Any, Dict, Optional

import pandas as pd


def clean_df(
    df: pd.DataFrame, transformations: Optional[Dict[str, Any]] = None
) -> pd.DataFrame:
    if transformations is None:
        transformations = {}  # pragma: no cover
    cols = transformations.get("cols", df.columns)
    rows = transformations.get("rows", (0, -1))
    cleaning = transformations.get("cleaning", [])
    new_cols = transformations.get("new_cols", [])
    df = df[cols].iloc[rows[0] : rows[1]]
    for c in cleaning:
        df[c[0]] = df[c[0]].apply(c[1])
    for new_col in new_cols:
        df[new_col[0]] = new_col[1]
    return df
