import os
import sys
import timeit
import pyspark
from numpy import array
from pyspark import SparkContext
from pyspark import SparkConf
from pyspark import SparkFiles
from pyspark.mllib.clustering import KMeans, KMeansModel
from pyspark.mllib.tree import RandomForest, RandomForestModel
from pyspark.mllib.util import MLUtils

if __name__=="__main__":
	
	conf = SparkConf().setMaster("local[*]")
	conf = conf.setAppName("Spark_MillionSongs")
	sc = SparkContext(conf=conf)
	data = sc.textFile("s3://ccdatauvamsds2017/YearPredictionMSD.txt")
	#sc.addFile("YearPredictionMSD.txt")
	#sc.addFile("YearPredictionMSD")
	
	#data = SparkFiles.get('YearPredictionMSD.txt')
	parsedData = data.map(lambda line: array([float(x) for x in line.split(',')]))

	#K-Means Code
	#Sampling with replacement
	data_sample = parsedData.sample(True, 100, 1234)

	start_time = timeit.default_timer()

	clusters = KMeans.train(data_sample, 2, maxIterations=10, initializationMode="random")

	time_Kmeans =(timeit.default_timer() - start_time)
	print(timeit.default_timer() - start_time)
	time_Kmeans_string = str(time_Kmeans)
	time_Kmeans_string.saveAsTextFile("s3://ccdatauvamsds2017/output/")


	#Random Forest Code
	data = MLUtils.loadLibSVMFile(sc, sc.textFile("s3://ccdatauvamsds2017/YearPredictionMSD"))

	start_time = timeit.default_timer()

	model = RandomForest.trainRegressor(data, categoricalFeaturesInfo={},
	                                     numTrees=3, featureSubsetStrategy="auto",
	                                     impurity='variance', maxDepth=4, maxBins=32)

	print(timeit.default_timer() - start_time)
	time_RF =(timeit.default_timer() - start_time)
	time_RF_string = str(time_RF)
	time_RF_string.saveAsTextFile("s3://ccdatauvamsds2017/output/")
	sc.stop()
