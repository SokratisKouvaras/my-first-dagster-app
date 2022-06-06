FROM python:3.7-slim

RUN mkdir -p /opt/dagster/dagster_home /opt/dagster/app

RUN pip install dagit dagster-postgres

# Copy your code and workspace to /opt/dagster/app
COPY my_first_dagster_app/ /opt/dagster/app/my_first_dagster_app
COPY workspace.yaml /opt/dagster/app/

ENV DAGSTER_HOME=/opt/dagster/dagster_home/

# Copy dagster instance YAML to $DAGSTER_HOME

WORKDIR /opt/dagster/app

EXPOSE 3000

ENTRYPOINT ["python","dagit", "-h", "0.0.0.0", "-p", "3000"]