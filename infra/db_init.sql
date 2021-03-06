CREATE USER dbtdev with password 'password1234';
CREATE SCHEMA dev AUTHORIZATION dbtdev;
ALTER ROLE dbtdev set search_path = 'dev';
GRANT CONNECT ON DATABASE dbt to dbtdev;
GRANT ALL PRIVILEGES ON SCHEMA dev to dbtdev;
CREATE USER dbtprod with password 'password1234';
CREATE SCHEMA prod AUTHORIZATION dbtprod;
ALTER ROLE dbtprod set search_path = 'prod';
GRANT CONNECT ON DATABASE dbt to dbtprod;
GRANT ALL PRIVILEGES ON SCHEMA prod to dbtprod;
