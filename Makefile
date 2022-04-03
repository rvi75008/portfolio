.DEFAULT_GOAL := all
isort = isort connectors loader tests config infra/airflow/dags
black = black connectors loader tests config infra/airflow/dags
mypy = mypy connectors loader config

.PHONY: format
format:
	$(isort)
	$(black)

.PHONY: lint
lint:
	flake8 connectors loader config tests/
	$(isort) --check-only
	$(black) --check
	$(mypy) --explicit-package-bases --namespace-packages


.PHONY: test
test:
	python -m pytest --junitxml=test-report.xml --cov=. --cov-report xml

.PHONY: test_local
test_local:
	python -m pytest --junitxml=test-report.xml --cov=. --cov-report xml
	dbt test

.PHONY: install
install:
	pip install -U setuptools pip==20.2
	pip install -r requirements.txt --ignore-installed
	pip install .

.PHONY: doc
doc:
	dbt docs generate

.PHONY: build
build:
	docker build --tag raphaelvignes/portfolio:latest --file Dockerfile .

.PHONY: push-image
push-image:
	docker login && docker push raphaelvignes/portfolio:latest
