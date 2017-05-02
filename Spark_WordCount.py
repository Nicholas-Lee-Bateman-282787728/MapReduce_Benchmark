import os
import sys
import timeit
import pyspark
from numpy import array
from pyspark import SparkContext
from pyspark import SparkConf
from pyspark import SparkFiles

if __name__=="__main__":

	conf = SparkConf().setMaster("local[*]")
	conf = conf.setAppName("Spark_MillionSongs")
	sc = SparkContext(conf=conf)


	start_time = timeit.default_timer()

	wordcounts = sc.textFile('s3://ccdatauvamsds2017/Wikidata').map( lambda x: x.replace(',',' ').replace('.',' ').replace('-',' ').lower()).flatMap(lambda x: x.split()).map(lambda x: (x, 1)).reduceByKey(lambda x,y:x+y).map(lambda x:(x[1],x[0])).sortByKey(False)

	print("$$$$$$$$$$$$$$$$$$TOOK THIS LONG:")
	print(timeit.default_timer() - start_time)
	print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
	sc.stop()
