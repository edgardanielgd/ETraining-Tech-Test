# This notebook is designed to load data from a set of raw files to a relational database

from pyspark.sql import SparkSession

from schemas import cases_schema, department_schema, municipality_schema, \
    gender_schema, type_contagion_schema, status_schema

from renames import cases_renames, municipality_renames, type_contagion_renames
from type_changes import cases_types
from additional_transform import rename_fields, change_fields_types

from config import PATH, MYSQL_USERNAME, MYSQL_PASSWORD, MYSQL_DATABASE, \
    MYSQL_HOST, MYSQL_PORT

spark = SparkSession.builder.appName("Database Sample") \
    .config('spark.jars', f'{PATH}/jars/mysql-connector-j-9.1.0.jar')\
    .config("spark.sql.legacy.charVarcharAsString","true")\
    .getOrCreate()

def load_data( csv_path, target_table, schema, additional_transformations = []):

    csv_path = f"{PATH}/{csv_path}"

    # Rewrite batched statements is necessary to prevent row by row insertions, which can lead to serious performance issues
    url = f"jdbc:mysql://{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}?rewriteBatchedStatements=true"

    df = None

    # Read CSV from local disk
    df = spark.read \
        .format("csv") \
        .option("delimiter", ";") \
        .option("header", True) \
        .schema(schema) \
        .load(csv_path)
    
    for transformation in additional_transformations:
        df = transformation( spark, df )

    # Write target to database
    df.write \
        .mode('append') \
        .format("jdbc") \
        .option('url', url ) \
        .option('driver', 'com.mysql.jdbc.Driver') \
        .option('dbtable', target_table) \
        .option("user", MYSQL_USERNAME) \
        .option("password", MYSQL_PASSWORD) \
        .option("batchsize", "10000") \
        .save()

load_data( 'Data/Department.csv', 'department', department_schema )
load_data( 'Data/gender.csv', 'gender', gender_schema )
load_data( 'Data/municipality.csv', 'municipality', municipality_schema, [
        rename_fields( municipality_renames )
    ]
)
load_data( 'Data/status.csv', 'status', status_schema )
load_data( 'Data/type_contagion.csv', 'type_contagion', type_contagion_schema, [
        rename_fields( type_contagion_renames )
    ] 
)
load_data( 'Data/cases.csv', 'cases', cases_schema, [
        change_fields_types( cases_types ),
        rename_fields( cases_renames )
    ]
)