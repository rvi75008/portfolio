from datetime import datetime

transformations = {
    "details": {
        "cols": ["Actif", "Valorisation €"],
        "rows": (0, 100),
        "cleaning": [
            (
                "Valorisation €",
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
            "Dvidende Estimé",
        ],
        "rows": (0, 100),
        "new_cols": [
            ("date", datetime.now()),
            ("day", datetime.now().strftime("%y-%m-%d")),
        ],
    },
}
