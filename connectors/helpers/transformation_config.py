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
        "new_cols": [("date", datetime.now())],
    },
    "rente": {
        "cols": [
            "Nom",
            "Janvier",
            "Février",
            "Mars",
            "Avril",
            "Mai",
            "Juin",
            "Juillet",
            "Août",
            "Septembre",
            "Octobre",
            "Novembre",
            "Décembre",
            "Dvidende Estimé",
        ],
        "rows": (0, 100),
        "new_cols": [("date", datetime.now())],
    },
}
