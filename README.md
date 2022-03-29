1/ Utiliser une DB postgres pour airflow, change l'executor
2/ Différencer environnement de dev & de prod dans dbt (prévoir une db 'data/dev' et une db 'data/prod' différente) 
3/ Utiliser dbt dans la CI Github
4/ Voir pour déployer sur un cloud (déploiement auto après build de l'image ?)

# Démarrer les services
```
docker-compose run --name portfolio-etl -d -e DBT_PASSWORD= -e DBT_DB=portfolio-db -e LOADER_CONNECTION_URI=postgresql+psycopg2://dbt:@portfolio-db:5432/dbt etl && docker-compose run -d --name portfolio-db db
```
