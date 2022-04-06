from datetime import datetime
from typing import Any

import pandas as pd


def prices_or_qte_cleaning(x: Any) -> float:
    if pd.isnull(x):
        return 0
    return float(x.replace(",", ".").replace("\u202f", ""))


transformations = {
    "details": {
        "cols": ["actif", "valorisation", "qte", "pu", "pru", "devise", "type"],
        "rows": (0, 100),
        "cleaning": [
            ("qte", prices_or_qte_cleaning),
            (
                "valorisation",
                lambda x: float(x.replace(" ", "").replace(",", ".")),
            ),
            (
                "pu",
                prices_or_qte_cleaning,
            ),
            ("pru", prices_or_qte_cleaning),
        ],
        "new_cols": [
            ("date", datetime.now()),
            ("day", datetime.now().strftime("%y-%m-%d")),
        ],
    },
    "rente": {
        "cols": [
            "action",
            "dividende",
        ],
        "rows": (0, 100),
        "new_cols": [
            ("date", datetime.now()),
            ("day", datetime.now().strftime("%y-%m-%d")),
        ],
    },
}
