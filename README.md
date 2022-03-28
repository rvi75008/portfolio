1/ Tester le flow avec airflow "dev" dans le container 
2/ Faire une image docker 'prod' avec une vrai db et un vrai executor + docker compose
3/ Voir pour déployer sur un cloud


# Démarrer les services
```
docker-compose run --name portfolio-etl -d -e DBT_PASSWORD= -e DBT_DB=portfolio-db -e LOADER_CONNECTION_URI=postgresql+psycopg2://dbt:@portfolio-db:5432/dbt etl && docker-compose run -d --name portfolio-db db
```
