import datetime
import pendulum
from airflow import DAG
from airflow.decorators import task
from airflow.operators.email import EmailOperator

with DAG(
    dag_id="dag_python_email_operator",
    schedule="30 6 * * *",
    start_date=pendulum.datetime(2021, 1, 1, tz="Asia/Seoul"),
    catchup=False
) as dag:
    @task(task_id='somethings_task')
    def some_logic(**kwargs):
        from random import choice
        return choice(['Success','Fail'])
    
    send_email = EmailOperator(
        task_id= 'send_email',
        to='ukidd12@naver.com',
        subject='{{data_interval_end.in_timezone("Asia/Seoul") | ds}} some_logic 처리결과',
        html_content='{{data_interval_end.in_timezone("Asia/Seoul") | ds}} 처리 결과는 <br> \
            {{ti.xcom_pull(task_ids="somethings_task")}} 했습니다. <br>'
    )

    some_logic() >> send_email