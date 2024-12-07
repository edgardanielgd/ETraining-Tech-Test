from pyspark.sql.types import *

# Define sources structure

cases_schema = StructType(
   [
        StructField('id_case', IntegerType(), True),
        StructField('id_municipality', IntegerType(), True),
        StructField('age', IntegerType(), True),
        StructField('id_gender', IntegerType(), True),
        StructField('id_type', IntegerType(), True),
        StructField('id_status', DoubleType(), True),
        StructField('date_symptom', TimestampType(), True),
        StructField('date_death', TimestampType(), True),
        StructField('date_diagnosis', TimestampType(), True),
        StructField('date_recovery', TimestampType(), True)
   ]
)

department_schema = StructType(
   [
        StructField('id_department', IntegerType(), True),
        StructField('name', VarcharType(45), True)
   ]
)

municipality_schema = StructType(
   [
        StructField('id_municipality', IntegerType(), True),
        StructField('name_municipality', VarcharType(200), True),
        StructField('id_department', IntegerType(), True)
   ]
)

gender_schema = StructType(
   [
        StructField('id_gender', IntegerType(), True),
        StructField('name', VarcharType(45), True)
   ]
)

type_contagion_schema = StructType(
   [
        StructField('id_type', IntegerType(), True),
        StructField('name', VarcharType(45), True)
   ]
)

status_schema = StructType(
   [
        StructField('id_status', IntegerType(), True),
        StructField('name', VarcharType(45), True)
   ]
)