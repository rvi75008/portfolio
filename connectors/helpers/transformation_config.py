from datetime import datetime

transformations = {
    "details": {
        "cols": ["actif", "valorisation", "qte", "pu", "pru", "devise"],
        "rows": (0, 100),
        "cleaning": [
            (
                "valorisation",
                lambda x: float(x.replace(" ", "").replace(",", ".")),
            )
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
