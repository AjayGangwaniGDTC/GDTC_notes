from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from pyspark.sql.functions import sum,avg,max,count
from pyspark.sql.functions import col, udf,lit
import pyspark.sql.functions as F
from pyspark.sql.types import StringType
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from earthquake_data_extractor.vault_config import update_vault
import h3

import os
from sqlalchemy import create_engine 

# Create a SparkSession
# spark = SparkSession.builder.appName("Testing PySpark Example").getOrCreate()
sc = SparkContext()
GlueContext = GlueContext(sc)
spark = GlueContext.spark_session


spark = SparkSession.builder \
    .appName("Spark with PostgreSQL") \
    .config("spark.jars.packages", "org.postgresql:postgresql:42.6.0") \
    .getOrCreate()
spark.conf.set("spark.sql.legacy.parquet.nanosAsLong", "true")

jdbc_url = "jdbc:postgresql://host.docker.internal:5432/postgres"
connection_props = {
    "user": "postgres",
    "password": "admin123",
    "driver": "org.postgresql.Driver"
}



def get_h3_index(lat,long):
    cell_val=h3.latlng_to_cell(lat,long,res=5)
    return cell_val
    
def check_for_seven_mag(col_name):
    if col_name>7:
        return 1
    else:
        return 0
    


def to_postgres(table_name,dataframe):
    dataframe.write.jdbc(url = jdbc_url,table =table_name,mode = 'overwrite', properties = connection_props)
    print("Data delivered to Postgres")

year = '1940'

def transform_data(table_name):
    for year in range(1939,2025):
        year = year+1
        parquet_file_path =  f"/home/glue_user/data/{str(year)}.parquet"
        print(f" working on file {str(year)}")
        # print(file_path)
        df = spark.read.parquet(parquet_file_path)
        # df.show(5)
        df_UDF = udf(lambda x,y: get_h3_index(x,y))
        df_new = df
        new_df =df_new.withColumn("h3_index",df_UDF(col('latitude'),col('longitude')))
        
        cond = lambda x: F.sum(F.when(x>7, 1).otherwise(0))
        # magnitude greater than seven count
        seven_mag = udf(lambda x: check_for_seven_mag(x))
        temp_df =new_df.select('h3_index','magnitude')
        seven_mag_df = temp_df.withColumn("seven_mag_flag",seven_mag(col('magnitude')))
        
        
        agg_df = new_df.groupBy('h3_index').agg(F.min('magnitude').alias('min_mag'),
                                            F.max('magnitude').alias('max_mag'),
                                           F.count('magnitude').alias('total_count'),                                       
                                            F.stddev('magnitude').alias('standard_deviation_mag'),
                                           F.variance('magnitude').alias('variance_mag'))
        agg_df =agg_df.withColumn("year",lit(year))
        
        to_postgres(table_name,agg_df)
        # print(f"Incremented to next year {start_year}")
        # return agg_df 

transform_data(table_name="earthquake_trial2")




