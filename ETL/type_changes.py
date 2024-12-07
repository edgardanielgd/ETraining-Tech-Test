from pyspark.sql.types import *

# Certain fields change their data types between source file and target database, they must be overwritten

cases_types = {
    "id_status": IntegerType()
}