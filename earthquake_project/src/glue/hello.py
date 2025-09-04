from pyspark.context import SparkContext
from awsglue.context import GlueContext
import pandas as pd
# from pyspark.sql import SparkSession
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

from pyspark.sql.types import StructType, StructField, IntegerType, StringType
 
 
# Define the schema for the DataFrame
schema = StructType([
    StructField("id", IntegerType(), True),
    StructField("name", StringType(), True),
    StructField("age", IntegerType(), True)
])
 
# Create sample data
data = [
    (1, "Alice", 25),
    (2, "Bob", 30),
    (3, "Charlie", 35),
    (4, "David", 40)
]
 
# Create DataFrame using the data and schema
df = spark.createDataFrame(data, schema)
 
# Show the DataFrame
df.show()