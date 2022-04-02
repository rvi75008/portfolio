1/ Préparer déploiement dans le cloud:
  a) Config "Naïve"
  b) Forwarder les secrets pour créer les utilisateur postgres. variables env + echo dans un fichier sql
2/ Voir pour déployer sur un cloud (déploiement auto après build de l'image ?)
3/ Brancher sur une app de dataviz (Toucan)

# Archi
![image](https://user-images.githubusercontent.com/82377798/161383439-889080a5-80eb-471d-967c-fa7ca56cc7a0.png)

# Démarrer les services
```
docker-compose run -d --name airflow-db -e AIRFLOW_DB_PASSWORD= airflow-db
docker-compose run -d --name portfolio-db -e AIRFLOW_DB_PASSWORD= db
docker-compose run --name portfolio-etl -d -e DBT_PASSWORD= -e DBT_DB=portfolio-db -e LOADER_CONNECTION_URI=postgresql+psycopg2://dbt:@portfolio-db:5432/dbt  -e AIRFLOW__CORE__SQL_ALCHEMY_CONN=postgresql+psycopg2://airflow:@airflow-db:5432/airflow etl

```
