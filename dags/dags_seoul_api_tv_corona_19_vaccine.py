from operators.seoul_api_to_csv_operator import SeoulApiToCsvOperator
from airflow import DAG
import pendulum

with DAG(
        dag_id='dags_seoul_api_tv_corona_19_vaccine',
        schedule='0 7 * * *',
        start_date=pendulum.datetime(2023, 4, 1, tz='Asia/Seoul'),
        catchup=False
) as dag:
    ''' 코로나 데이터 정보 '''

    tv_corona_19_vaccine_stat_new = SeoulApiToCsvOperator(
        task_id='tv_corona_19_vaccine_stat_new',
        dataset_nm='tvCorona19VaccinestatNew',
        path='/opt/airflow/files/tvCorona19VaccinestatNew/{{data_interval_end.in_timezone("Asia/Seoul") | ds_nodash}}',
        file_name='tvCorona19VaccinestatNew.csv'
    )

    tv_corona_19_vaccine_stat_new
