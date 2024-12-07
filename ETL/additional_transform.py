import pyspark.sql.functions as F

# Add an extra record for each dimension table, since there could be null references in fact tables
def rename_fields( columns_mapper ):

    def _rename_fields( spark, dataset ):
        for v in columns_mapper:
            dataset = dataset.withColumnRenamed( v, columns_mapper[v] )
            
        return dataset
    
    return _rename_fields

def change_fields_types( type_changes ):

    def _update_type( _, dataset ):
        for v in type_changes:
            dataset = dataset.withColumn(  v, F.col(v).cast( type_changes[v] ) )

        return dataset
        
    return _update_type