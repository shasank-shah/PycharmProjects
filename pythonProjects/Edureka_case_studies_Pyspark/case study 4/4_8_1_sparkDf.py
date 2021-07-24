#!/usr/bin/python3.6
#!/usr/bin/env python3.6
# coding: utf-8

from pyspark.sql import SparkSession
from pyspark.sql.types import StructField, StringType, StructType, DoubleType, DateType
from pyspark.sql import functions as F

# spark declaration
spark = SparkSession \
        .builder \
        .appName("4_8_1 Spark App") \
        .getOrCreate()

# variable declarations
inputFileName = 'FINAL_FROM_DF.csv'

# processing part
dataFrameCSVDataSchema = [StructField('SYMBOL', StringType(), True), StructField('SERIES', StringType(), True), StructField('OPEN', DoubleType(), True), StructField('HIGH', DoubleType(), True), StructField('LOW', DoubleType(), True), StructField('CLOSE', DoubleType(), True), StructField('LAST', DoubleType(), True), StructField('PREVCLOSE', DoubleType(), True), StructField('TOTTRDQTY', DoubleType(), True), StructField('TOTTRDVAL', DoubleType(), True), StructField('TIMESTAMP', DateType(), True), StructField('TOTALTRADES', DoubleType(), True), StructField('ISIN', StringType(), True)]
dataFrameCSVFinalStruct = StructType(fields=dataFrameCSVDataSchema)
dataFrameCSV = spark.read.csv(inputFileName, schema=dataFrameCSVFinalStruct)
dataFrameCSV.createOrReplaceTempView('final_from_df')
queryResult = spark.sql('SELECT * FROM final_from_df WHERE totaltrades < 500')
updateResult = queryResult.withColumn("totaltrades", F.when(F.col("totaltrades")<500, 0))

# writing to csv file using spark df
updateResult.coalesce(1).write.option("header", "true").csv('TOTALTRADES')