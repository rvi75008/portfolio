1. Tester déploiement cloud "local"
2. Déployer sur un cloud (déploiement auto après build de l'image -> Mettre le token dockerhub dans la config?) -> Créer un repo à part pour la config kubernetes Azure
3. Rajouter Firewall/ratelimiter sur le login
4. Brancher sur une app de dataviz (Toucan)
5. Rajouter job airflow pour dump+compression de la base et stocker dans drive.


## Non Prio
"Data Mining" en C++: matrices de corélation entre les actifs.
Cacher les résultats de requêtes


# Archi
![image](https://user-images.githubusercontent.com/82377798/161422137-16dbaf16-9c8c-4489-b3c5-ec8ed6ee2d40.png)

# Démarrer les services localement
```
docker-compose run -d --name airflow-db -e AIRFLOW_DB_PASSWORD= airflow-db
docker-compose run -d --name portfolio-db -e AIRFLOW_DB_PASSWORD= db
docker-compose run --name portfolio-etl -d -e DBT_PASSWORD= -e DBT_DB=portfolio-db -e LOADER_CONNECTION_URI=postgresql+psycopg2://dbt:@portfolio-db:5432/dbt  -e AIRFLOW__CORE__SQL_ALCHEMY_CONN=postgresql+psycopg2://airflow:@airflow-db:5432/airflow etl

```
