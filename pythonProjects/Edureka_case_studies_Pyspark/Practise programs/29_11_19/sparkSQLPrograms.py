#!/usr/bin/python3.6
#!/usr/bin/env python3.6
# coding: utf-8

import sys, time
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('First App').getOrCreate()
df = spark.read.json('people.json')
print(df)