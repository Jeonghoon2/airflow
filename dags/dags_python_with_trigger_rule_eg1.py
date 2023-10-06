from airflow import DAG
import pendulum
from airflow.decorators import task
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from airflow.exceptions import AirflowException

with DAG(
    dag_id="dags_python_with_trigger_rule_eg1",
    schedule=None,
    start_date=pendulum.datetime(2023, 1, 1, tz="Asia/Seoul"),
    catchup=False
) as dag:
    
    bash_upstream_1 = BashOperator(
        task_id = 'bash_upstream_1',
        bash_command='echo upstream1'
    )

    @task(task_id='python_upstream_1')
    def python_upstream_1():
        raise AirflowException('downstram_1 Exception!')
    
    @task(task_id='python_upstream_2')
    def python_upstream_2():
        print('정상 처리')

    @task(task_id='python_upstream_3')
    def python_upstream_3():
        print('정상 처리')

    @task(task_id='python_downstream_1', trriger_rule='all_done')
    def python_downstream_1():
        print('정상 처리')

    [bash_upstream_1, python_upstream_1(), python_upstream_2(), python_upstream_3()] >> python_downstream_1()