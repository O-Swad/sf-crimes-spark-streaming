---
title: "SF Crime Statistics With Spark Streaming"
author: "Omar Álvarez Fres"
date: "16/5/2020"
output: html_document
---

  ## Step 3
### 1. How did changing values on the SparkSession property parameters affect the throughput and latency of the data?
Usually it is mandatory to find the right balance of throughput rate and latency, because many times a higher throughput rate implies higher latency value, and viceversa.
In this case, I will experiment with a subset of parameters related to the input rate, processing rate and batch duration. These paremeters are specified in the answer for question 2.

### 2. What were the 2-3 most efficient SparkSession property key/value pairs? Through testing multiple variations on values, how can you tell these were the most optimal?

First of all, to see RAM size and number of cores run the following commands:
```bash
cat /proc/meminfo
nproc --all
```

To avoid data processing bottlenecks, _backpressure_ feature has been enabled to allow Spark automatically adjusts records/sec, and not pre-fixing with *spark.streaming.receiver.maxRate* and *spark.streaming.kafka.maxRatePerPartition* options. The equivalent option is
__spark.streaming.backpressure.enabled = true__

Block intervals must be tunned according to cores and number of tasks per batch. The equivalent option is __spark.streaming.blockInterval__.

The __spark.default.parallelism__ it must be set to number of cores in local mode, in this case is 2.

Finally __spark.executor.memory__ has been tested from command line parameter to spark-submit wihout relevant performances differences seen in Spark UI. In this case the command was:
```r
spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.11:2.3.4 --executor-memory 6GB --executor-cores 2 --master local[*] data_stream.py
```


