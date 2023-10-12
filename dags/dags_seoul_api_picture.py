from operators.seoul_api_to_csv_operator import SeoulApiToCsvOperator
from airflow import DAG
import pendulum

with DAG(
        dag_id='dags_seoul_api_picture',
        schedule='0 7 * * *',
        start_date=pendulum.datetime(2023, 4, 1, tz='Asia/Seoul'),
        catchup=False
) as dag:
    '''서울시립 미술 박물관 데이터 정보 '''

    tb_picture_info = SeoulApiToCsvOperator(
        task_id='tb_picture_info',
        dataset_nm='SemaPsgudInfoKorInfo',
        path='/opt/airflow/files/SemaPsgudInfoKorInfo/{{data_interval_end.in_timezone("Asia/Seoul") | ds_nodash}}',
        file_name='SemaPsgudInfoKorInfo.csv'
    )

    tb_picture_info
