from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.providers.http.operators.http import SimpleHttpOperator
from airflow.decorators import task
import pendulum

with DAG(
    dag_id='dags_simple_http_operator',
    start_date=pendulum.datetime(2023,4,1, tz='Asia/Seoul'),
    schedule=None,
    catchup=False
) as dag:
    
    picture_lst_info = SimpleHttpOperator(
        task_id='picture_lst_info',
        http_conn_id='openapi.seoul.go.kr',
        endpoint='{{var.value.api_key_openapi}}/json/SemaPsgudInfoKorInfo/1/10/',
        method='GET',
        headers={
            'Content-Type':'application/json',
            'charset':'utf-8',
            'Accept':'*/*'
        }
    )

    @task(task_id='python_2')
    def python_2(**kwargs):
        ti = kwargs['ti']
        rslt = ti.xcom_pull(task_ids='picture_lst_info')
        import json
        from pprint import pprint

        pprint(json.loads(rslt))

    picture_lst_info >> python_2()