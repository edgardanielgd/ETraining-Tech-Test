# This notebook is designed to load data from a set of raw files to a relational database

from pyspark.sql import SparkSession
import pyspark.sql.functions as F
import pyspark.sql.types as T

from schemas import cases_schema, department_schema, municipality_schema, \
    gender_schema, type_contagion_schema, status_schema

from renames import cases_renames

import os
from dotenv import load_dotenv

load_dotenv()

PATH = os.getcwd()

spark = SparkSession.builder.appName("Database Sample") \
    .config('spark.jars', f'{PATH}/jars/mysql-connector-j-9.1.0.jar')\
    .getOrCreate()

MYSQL_USERNAME = os.getenv("MYSQL_USERNAME")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
MYSQL_DATABASE = os.getenv("MYSQL_DATABASE")
MYSQL_HOST = os.getenv("MYSQL_HOST")
MYSQL_PORT = os.getenv("MYSQL_PORT")

def load_data( csv_path, target_table, schema, renames = {} ):

    csv_path = f"{PATH}/{csv_path}"
    print(csv_path)
    url = f"jdbc:mysql://{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}"

    df = spark.read \
        .format("csv") \
        .option("delimiter", ";") \
        .option("header", True) \
        .schema(schema) \
        .load(csv_path)
    
    for v in renames:
        df = df.withColumnRenamed( v, renames[v] )

    df.write \
        .format("jdbc") \
        .option('url', url ) \
        .option('driver', 'com.mysql.jdbc.Driver') \
        .option('dbtable', target_table) \
        .option("mode", "overwrite") \
        .option("user", MYSQL_USERNAME) \
        .option("password", MYSQL_PASSWORD) \
        .save()

load_data( 'Data/cases.csv', 'cases', cases_schema, cases_renames)
load_data( 'Data/Department.csv', 'Department', department_schema)
load_data( 'Data/gender.csv', 'gender', gender_schema)
load_data( 'Data/municipality.csv', 'municipality', municipality_schema)
load_data( 'Data/status.csv', 'status', status_schema)
load_data( 'Data/type_contagion.csv', 'type_contagion', type_contagion_schema)