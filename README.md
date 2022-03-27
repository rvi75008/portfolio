3/ Faire une image docker 'dev' + docker compose
4/ tester le flow
5/ Faire une image docker 'prod' avec une vrai db et un vrai executor + docker compose
6/ Voir pour déployer sur un cloud


# Démarrer les services
```
docker-compose run -d --name portfolio-db db
docker-compose run -d --name portfolio-etl -e DBT_PASSWORD= -e LOADER_CONNECTION_URI=postgresql+psycopg2://dbt:@portfolio-db:5432/dbt -e DBT_DB=portfolio-db etl
```
