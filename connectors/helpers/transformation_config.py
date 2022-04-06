from datetime import datetime
from typing import Any

import pandas as pd


def sanitizer(x: Any) -> float:
    if pd.isnull(x):
        return 0
    return (
        float(x.replace(" ", "").replace(",", ".").replace("\u202f", ""))
        if not isinstance(x, float)
        else x
    )


transformations = {
    "details": {
        "cols": ["actif", "valorisation", "qte", "pu", "pru", "devise", "type"],
        "rows": (0, 100),
        "cleaning": [
            ("qte", sanitizer),
            (
                "valorisation",
                sanitizer,
            ),
            (
                "pu",
                sanitizer,
            ),
            ("pru", sanitizer),
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
