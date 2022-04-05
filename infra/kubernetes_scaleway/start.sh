# minikube start
kubectl apply -f airflow-db-config.yml
kubectl apply -f airflow-db-secret.yml
kubectl apply -f airflow-db.yml
kubectl apply -f portfolio-db-config.yml
kubectl apply -f portfolio-db-secret.yml
kubectl apply -f portfolio-db-init-config.yml
kubectl apply -f portfolio-db.yml
kubectl apply -f portfolio-etl-config.yml
kubectl apply -f portfolio-etl-secret.yml
kubectl apply -f portfolio-etl.yml
echo "Remind to activate port forwarding to debug dags locally"