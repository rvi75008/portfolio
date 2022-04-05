1. Rajouter job airflow pour dump+compression de la base et stocker dans drive (voir google drive api avec une key)


## Non Prio
"Data Mining" en C++: matrices de corélation entre les actifs.
Cacher les résultats de requêtes


# Archi
![image](https://user-images.githubusercontent.com/82377798/161844067-06dcb44d-e573-43cb-bba6-2350cabcc612.png)

# Démarrer les services localement
```
docker-compose run -d --name airflow-db -e AIRFLOW_DB_PASSWORD= airflow-db
docker-compose run -d --name portfolio-db -e AIRFLOW_DB_PASSWORD= db
docker-compose run --name portfolio-etl -d -e DBT_PASSWORD= -e DBT_DB=portfolio-db -e LOADER_CONNECTION_URI=postgresql+psycopg2://dbt:@portfolio-db:5432/dbt  -e AIRFLOW__CORE__SQL_ALCHEMY_CONN=postgresql+psycopg2://airflow:@airflow-db:5432/airflow etl

```
