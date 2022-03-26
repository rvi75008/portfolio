.DEFAULT_GOAL := all
isort = isort connector loader tests
black = black connector loader tests
mypy = mypy connector tests

.PHONY: format
format:
	$(isort)
	$(black)

.PHONY: lint
lint:
	flake8 connector loader
	$(isort) --check-only
	$(black) --check
	$(mypy)


.PHONY: test
test:
	python -m pytest --junitxml=test-report.xml --cov=. --cov-report xml

.PHONY: install
install:
	pip install -U setuptools pip==20.2
	pip install -r requirements.txt --ignore-installed