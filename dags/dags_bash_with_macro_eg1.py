from airflow import DAG
import pendulum
from airflow.operators.bash import BashOperator

with DAG(
    dag_id="dags_bash_with_macro_eg1",
    schedule="10 0 L * *",
    start_date=pendulum.datetime(2023, 3, 1, tz="Asia/Seoul"),
    catchup=False
) as dag:
    bash_task_1 = BashOperator(
        task_id="bash_task_1",
        env={'START_DATE':'{{ date_interval_start.in_timezone("Asia/Seoul") | ds }}',
             'END_DATE':'{{ (date_interval_end.in_timezone("Asia/seoul") - macros.dateutil.rerativedelta.relativedelta(day=1)) | ds }}'
            },
            bash_command='echo "START_DATE: $START_DATE" && echo "END_DATE: $END_DATE"'
    ) 