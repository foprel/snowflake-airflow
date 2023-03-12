from datetime import datetime
from airflow import DAG
from airflow.contrib.operators.snowflake_operator import SnowflakeOperator

# Create DAG default arguments
args = {
    "owner": "airflow",
    "start_date": datetime(2023, 3, 10, 12, 00)
}

#  Create DAG object
dag = DAG(
    dag_id="example",
    default_args=args,
    schedule_interval=None
)

#  Create Snowflake query
query = '''
    create or replace table examle_table (
        id          int,
        first_name  varchar(50),
        last_name   varchar(50)
    );
'''

#  Connect to Snowflake
with dag:
    execute_dag = SnowflakeOperator(
        task_id="snowflake_example",
        sql=query,
        snowflake_conn_id="snowflake_connector",
    )

#  Execute DAG
execute_dag
