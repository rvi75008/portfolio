FROM python:3.8

ADD ./requirements.txt ./src/requirements.txt
ADD ./connectors ./src/connectors
ADD ./loader ./src/loader
ADD ./config ./src/config
ADD ./setup.py ./src/setup.py
ADD ./models ./dbt/models
ADD ./profiles.yml ./dbt/profiles.yml
ADD ./dbt_packages ./dbt/dbt_packages
ADD ./dbt_project.yml /dbt/dbt_project.yml
ADD ./packages.yml /dbt/packages.yml
ADD ./tests/dbt /dbt/tests
ADD ./infra/airflow ./airflow
ENV LOADER_CONNECTION_URI ${LOADER_CONNECTION_URI}
ENV LOADER_CONNECTION_URI_PROD ${LOADER_CONNECTION_URI_PROD}
ENV DBT_DB dbt
ENV DBT_PROFILES_DIR /dbt
ENV AIRFLOW_HOME=/airflow
ENV DATA_DIR=data
ENV DEV_DIR=/development
ENV STAGING_DIRECTORY /${DATA_DIR}/staging/
ENV SUCCESSFUL_INGESTION_DIR /${DATA_DIR}/inserted/
ENV UNSUCCESSFUL_INGESTION_DIR /${DATA_DIR}/aborted/
ENV AIRFLOW_UID=1000

RUN mkdir $DATA_DIR
RUN mkdir $STAGING_DIRECTORY
RUN mkdir $SUCCESSFUL_INGESTION_DIR
RUN mkdir $UNSUCCESSFUL_INGESTION_DIR
RUN mkdir $DEV_DIR
RUN cp -R /$DATA_DIR $DEV_DIR

WORKDIR ./src
RUN python -m venv /app/venv
ENV PATH="/app/venv/bin:$PATH"
RUN python -m pip install -U pip==20.2
RUN python -m pip install -r requirements.txt
RUN python -m pip install .
RUN python -m pip install "apache-airflow[celery]==2.2.5" --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.2.5/constraints-3.6.txt"

WORKDIR ./dbt
CMD ["sh", "-c", "dbt deps"]
CMD ["sh", "-c", "dbt compile"]
EXPOSE 8080
WORKDIR /src
CMD ["sh", "-c", "airflow db init"]
CMD ["sh", "-c", "airflow standalone"]
