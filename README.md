1/ Utiliser une DB postgres pour airflow change l'executor
2/ Différencier l'utilisation du dag dev vs prod & adapter connector (I/O dirs), loader (schema destination) et inserted/aborted, et DAG via https://airflow.apache.org/docs/apache-airflow/stable/best-practices.html#dynamic-dags-with-environment-variables
3/ Faire deux schéma dbt différent -> Dev/Prod
4/ Utiliser dbt dans la CI Github
5/ Voir pour déployer sur un cloud (déploiement auto après build de l'image ?)

# Démarrer les services
```
docker-compose run -d --name airflow-db -e AIRFLOW_DB_PASSWORD= airflow-db
docker-compose run -d --name portfolio-db -e AIRFLOW_DB_PASSWORD= db
docker-compose run --name portfolio-etl -d -e DBT_PASSWORD= -e DBT_DB=portfolio-db -e LOADER_CONNECTION_URI=postgresql+psycopg2://dbt:@portfolio-db:5432/dbt  -e AIRFLOW__CORE__SQL_ALCHEMY_CONN=postgresql+psycopg2://airflow:@airflow-db:5432/airflow etl

```
