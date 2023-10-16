import pendulum
from airflow import DAG
from airflow.sensors.date_time import DateTimeSensorAsync

with DAG(
        dag_id='dags_time_sensor',
        start_date=pendulum.datetime(2023, 10, 15, 0, 0, 0),
        end_date=pendulum.datetime(2023, 10, 15, 1, 0, 0),
        schedule="*/10 * * * *",
        catchup=True
) as dag:
    async_sensor = DateTimeSensorAsync(
        task_id='async_sensor',
        target_time="""{{macros.datetime.utcnow() + macros.timedelta(minutes=5)}}"""
    )