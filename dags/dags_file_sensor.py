from airflow import DAG
import pendulum
from airflow.sensors.filesystem import FileSensor

with DAG(
        dag_id="dags_file_sensor",
        start_date=pendulum.datetime(2023, 10, 12, tz='Asia/Seoul'),
        schedule='0 7 * * *',
        catchup=False
) as dag:
    tvCorona19VaccinestatNew_sensor = FileSensor(
        task_id='tvCorona19VaccinestatNew_sensor',
        fs_conn_id='conn_file_opt_airlfow_files',
        filepath='/SemaPsgudInfoKorInfo/{{data_interval_end.in_timezone("Asia/Seoul") | ds_nodash}}/SemaPsgudInfoKorInfo.csv',
        recursive=False,
        poke_interval=60,
        timeout=60*60*24,
        mode='reschedule'
    )
