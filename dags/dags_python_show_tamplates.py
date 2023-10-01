from airflow import DAG
import pendulum
import datetime
from airflow.decorators import task

with DAG(
    dag_id="dags_python_show_tamplates",
    schedule="30 9 * * *",
    start_date=pendulum.datetime(2023, 9, 20, tz="Asia/Seoul"),
    catchup=True
) as dag:
    
    @task(task_id='python_task')
    def show_templates(**kwars):
        from pprint import pprint
        pprint(kwars)
    
    show_templates()