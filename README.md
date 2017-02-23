# MapReduce_Benchmark

Benchmarking MapReduce Implementations on the Amazon Web Services
Elastic Compute Cloud
Chris Patrick, Tim Schroeder, Aksheetha Sridhar, Megan Stiles

Goal
The primary goal of the project is to benchmark performance of several MapReduce algorithms across clusters of various sizes (e.g., 8, 64, and 128 nodes) on the Amazon Web Services (AWS) Elastic Compute Cloud (EC2) in order to determine the most efficient and cost-effective approaches for each implementation. Although selection of specific algorithms will be one of our first tasks, we are considering using MapReduce implementations for word count, k-means clustering, and random forest classification. The benefit of this project is to add to the growing body of literature analyzing performance of the popular and widely used EC2 web service.

Approach
For this project we will run three different algorithms using MapReduce on three distinct clusters of various sizes (9 runs total). We will record the amount of time it takes for the mappers and reducers to complete their tasks for the different algorithms for each cluster size. We will then use this metric to calculate a performance metric, cost per minute, in order to determine which cluster size is the most cost effective and whether the specific algorithm affects the cost effectiveness of a specific cluster.

Methodology
First we will finalize our algorithms and identify appropriate data sets for each algorithm we are testing. We will then learn how to implement each algorithm using MapReduce, set up the different AWS clusters, and run the algorithms on each of the three clusters. After running the algorithms, we can then calculate the cost effectiveness, analyze the results, and write up the report.

Metrics
Success will be measured by comparing the performance of specific algorithms using MapReduce on different cluster sizes (i.e., 8, 64, 128 nodes). The performance benchmarks that will be measured are the run time, expense, comparing predicted versus the measured duration of tasks, timing the duration of specific MapReduce phases and if different input data are used then the effect of size on the processing duration. These are the main benchmarks that will be measured which will then be segmented further into microbenchmarks during experimentation. 

Summary
In the course of completing this assignment, we will acquire practical experience in the components of cloud computing. This includes initial evaluation and design of our cluster setup and benchmarking algorithms with the guidance of current research literature in the field of cloud computing, setup and calibration of our cluster via Amazon Web Services, implementation of multiple machine learning algorithms and our benchmarking functions in a distributed computing context, and evaluation of our competing setups.
