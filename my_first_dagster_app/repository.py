from dagster import repository

from my_first_dagster_app.jobs.say_hello import say_hello_job
from my_first_dagster_app.schedules.my_hourly_schedule import my_hourly_schedule
from my_first_dagster_app.sensors.my_sensor import my_sensor


@repository
def my_first_dagster_app():
    """
    The repository definition for this my_first_dagster_app Dagster repository.

    For hints on building your Dagster repository, see our documentation overview on Repositories:
    https://docs.dagster.io/overview/repositories-workspaces/repositories
    """
    jobs = [say_hello_job]
    schedules = [my_hourly_schedule]
    sensors = [my_sensor]

    return jobs + schedules + sensors
