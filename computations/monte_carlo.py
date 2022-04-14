import logging
from abc import ABC
from typing import Any

import numpy as np
import pandas as pd
from psycopg2 import DatabaseError, OperationalError
from sqlalchemy import create_engine

from config.config import settings
from loader.loader import AsyncPostgresLoader


class PortfolioReadingError(Exception):
    pass


class PortfolioReader(ABC):
    def read(self, query: str) -> pd.DataFrame:
        ...  # pragma:no cover


class SqlPortfolioReader(PortfolioReader):
    def __init__(self, connection_uri: str):
        self.connection_uri = connection_uri
        self.logger = logging.getLogger(__name__)

    def read(self, query: str) -> pd.DataFrame:
        connection = create_engine(self.connection_uri)
        try:
            return pd.read_sql(sql=query, con=connection)
        except (OperationalError, DatabaseError) as e:
            self.logger.error(f"Error while reading portfolio: {e}")
            raise PortfolioReadingError(f"Error while inserting data into: {e}")


class MonteCarloSimulation:
    def __init__(
        self,
        portfolio: pd.DataFrame,
        returns_distribution: Any,
        cash_injection_over_period: float,
    ):
        self.portfolio = portfolio
        self.returns_distribution = returns_distribution
        self.cash_injection_over_period = cash_injection_over_period

    def simulate(self) -> pd.DataFrame:
        simulations = []
        starting_values = self.portfolio[self.portfolio.columns[0]].values
        for sim in self.returns_distribution:
            [sim[i].insert(0, value) for i, value in enumerate(starting_values)]
            assets_simulated_returns = [
                np.cumprod(sim[i]) for i in range(len(self.portfolio))
            ]
            simulations.append(
                np.add(*assets_simulated_returns)[-1] + self.cash_injection_over_period
                if len(assets_simulated_returns) > 1
                else assets_simulated_returns[0][-1] + self.cash_injection_over_period
            )
        return (
            pd.DataFrame([end_res if end_res >= 0 else 0 for end_res in simulations])
            .describe(percentiles=np.arange(0, 1, 0.1))
            .transpose()
        )


def run_simulation():
    reader = SqlPortfolioReader(settings.LOADER_CONNECTION_URI_PROD)
    portfolio = reader.read(
        query="select valeur_totale from portfolio_value order by day desc limit 1"
    )
    mcs = MonteCarloSimulation(
        portfolio=portfolio,
        returns_distribution=[
            [
                [1.0001 + np.random.standard_cauchy() / 2000 for _ in range(364)]
                for _ in range(len(portfolio))
            ]
            for _ in range(10000)
        ],
        cash_injection_over_period=10000,
    )
    output = mcs.simulate()
    output.columns = [
        "count",
        "mean",
        "std",
        "min",
        "bucket0",
        "bucket10",
        "bucket20",
        "bucket30",
        "bucket40",
        "bucket50",
        "bucket60",
        "bucket70",
        "bucket80",
        "bucket90",
        "max",
    ]
    loader = AsyncPostgresLoader(settings.LOADER_CONNECTION_URI_PROD)
    loader.load_from_dataframe(output)
