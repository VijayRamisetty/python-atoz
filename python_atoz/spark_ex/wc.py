from pyspark.sql import SparkSession
import re

if __name__ == '__main__':
    print("Word Count Example")
    spark = SparkSession.builder.master('local[2]').appName('wc-app').getOrCreate()
    print(spark.version)

    pattern = re.compile("[^A-Za-z ]")

    textFile = spark.read.text("wc.py")
    baseRdd = textFile.rdd
    cleaned_rdd = baseRdd.map(lambda x: re.sub(pattern, ' ', x[0]))
    map_rdd = cleaned_rdd.flatMap(lambda x: x.split(" ")).map(lambda x: (x, 1))
    reduced_rdd = map_rdd.reduceByKey(lambda x, y: x + y)
    for k, v in reduced_rdd.coalesce(1).sortByKey().collect():
        print(k, v)

    spark.stop()
