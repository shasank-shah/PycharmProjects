#!/usr/bin/python3.6
#!/usr/bin/env python3.6
# coding: utf-8

from pyspark.sql import SparkSession
from pyspark.sql.types import StructField, StringType, StructType, DoubleType, DateType, IntegerType
from pyspark.sql import functions as F

# spark declaration
spark = SparkSession \
        .builder \
        .appName("4_part2 Spark App") \
        .getOrCreate()

# variable declarations
inputFileName = 'aisles.csv'

# processing part
dataFrameCSVDataSchema = [StructField('AISLE_ID', IntegerType(), False), StructField('AISLE', StringType(), True)]
dataFrameCSVFinalStruct = StructType(fields=dataFrameCSVDataSchema)
dataFrameCSV = spark.read.csv(inputFileName, schema=dataFrameCSVFinalStruct)
dataFrameCSV.createOrReplaceTempView('final_from_df')
queryResult = spark.sql('SELECT * FROM final_from_df WHERE aisle = "specialty cheeses"')
updateResult = queryResult.withColumn("AISLE", F.when(F.col("AISLE") == "specialty cheeses", "specialty cheese"))

# writing to csv file using spark df
updateResult.coalesce(1).write.option("header", "true").csv('cheeses')