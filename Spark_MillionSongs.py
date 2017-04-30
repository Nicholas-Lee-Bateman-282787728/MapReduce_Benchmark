import os
import sys
import timeit
from pyspark import SparkContext
from pyspark import SparkConf
from pyspark.mllib.clustering import KMeans, KMeansModel
from pyspark.mllib.tree import RandomForest, RandomForestModel
from pyspark.mllib.util import MLUtils

sc = SparkContext("local", "test")
data = sc.textFile('YearPredictionMSD.txt')
parsedData = data.map(lambda line: array([float(x) for x in line.split(',')]))

#K-Means Code
#Sampling with replacement
data_sample = parsedData.sample(True, 100, 1234)

start_time = timeit.default_timer()

clusters = KMeans.train(data_sample, 2, maxIterations=10, initializationMode="random")

print(timeit.default_timer() - start_time)

#Random Forest Code
data = MLUtils.loadLibSVMFile(sc, 'YearPredictionMSD')

start_time = timeit.default_timer()

model = RandomForest.trainRegressor(data, categoricalFeaturesInfo={},
                                     numTrees=3, featureSubsetStrategy="auto",
                                     impurity='variance', maxDepth=4, maxBins=32)

print(timeit.default_timer() - start_time)
