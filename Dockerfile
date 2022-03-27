FROM python:3.8

ADD ./requirements.txt ./src/requirements.txt
ADD ./connectors ./src/connectors
ADD ./loader ./src/loader
ADD ./config ./src/config
ADD ./setup.py ./src/setup.py
ADD ./models ./dbt/models
ADD ./profiles.yml ./dbt/profiles.yml
ADD ./target ./dbt/target
ADD ./dbt_packages ./dbt/dbt_packages
ADD ./dbt_project.yml ./dbt/dbt_project.yml
ADD ./infra/airflow ./airflow
ENV LOADER_CONNECTION_URI ${LOADER_CONNECTION_URI}
ENV DBT_PASSWORD ${DBT_PASSWORD}
ENV DBT_DB ${DBT_DB}
ENV DBT_PROFILES_DIR /dbt

WORKDIR ./src
RUN python -m venv /app/venv
ENV PATH="/app/venv/bin:$PATH"
RUN python -m pip install -U pip==20.2
RUN python -m pip install -r requirements.txt
RUN python -m pip install .
RUN mkdir data
RUN mkdir inserted
RUN mkdir aborted
EXPOSE 8080
WORKDIR /airflow

CMD ["sh", "-c", "airflow db init"]
CMD ["sh", "-c", "airflow standalone"]