.DEFAULT_GOAL := all
isort = isort connectors loader tests
black = black connectors loader tests
mypy = mypy connectors loader

.PHONY: format
format:
	$(isort)
	$(black)

.PHONY: lint
lint:
	flake8 connectors loader
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
