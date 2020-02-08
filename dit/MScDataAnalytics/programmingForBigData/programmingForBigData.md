# Hadoop & MapReduce Notes

Classes: http://b-tierney.com/msc-prog-big-data/

1. Deploying on Kubernetes ([Docker Desktop](https://www.docker.com/products/docker-desktop)).
1. [Hadoop Helm chart](https://github.com/helm/charts/tree/master/stable/hadoop)
```
helm install --name hadoop \
--set persistence.nameNode.enabled=true \
--set persistence.nameNode.storageClass=hostpath \
--set per sistence.dataNode.enabled=true \
--set persistence.dataNode.storageClass=hostpath stable/hadoop
```

NOTES (From helm chart status):
```
1. You can check the status of HDFS by running this command:
   kubectl exec -n default -it hadoop-hadoop-hdfs-nn-0 -- /usr/local/hadoop/bin/hdfs dfsadmin -report

2. You can list the yarn nodes by running this command:
   kubectl exec -n default -it hadoop-hadoop-yarn-rm-0 -- /usr/local/hadoop/bin/yarn node -list

3. Create a port-forward to the yarn resource manager UI:
   kubectl port-forward -n default hadoop-hadoop-yarn-rm-0 8088:8088

   Then open the ui in your browser:

   open http://localhost:8088

4. You can run included hadoop tests like this:
   kubectl exec -n default -it hadoop-hadoop-yarn-nm-0 -- /usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/mapreduce/hadoop-mapreduce-client-jobclient-2.9.0-tests.jar TestDFSIO -write -nrFiles 5 -fileSize 128MB -resFile /tmp/TestDFSIOwrite.txt

5. You can list the mapreduce jobs like this:
   kubectl exec -n default -it hadoop-hadoop-yarn-rm-0 -- /usr/local/hadoop/bin/mapred job -list

6. This chart can also be used with the zeppelin chart
    helm install --namespace default --set hadoop.useConfigMap=true,hadoop.configMapName=hadoop-hadoop stable/zeppelin

7. You can scale the number of yarn nodes like this:
   helm upgrade hadoop --set yarn.nodeManager.replicas=4 stable/hadoop

   Make sure to update the values.yaml if you want to make this permanent.
```

## Labs

### WordCount & AVG Word length grouped by first character of the word
- [Instructions here (pdf)](https://secureservercdn.net/160.153.138.74/umw.129.myftpupload.com/wp-content/uploads/2020/02/Lab4-Creating_First_MR_Process.pdf)

#### Resolution steps
1. Build up the Java JAR as per instructions.

1. Download [shakespeare](https://www.dropbox.com/s/m84tzbn0489khb6/shakespeare.tar.gz?dl=0) or [shakespeare.tar.gz](https://github.com/swinton/Cloudera-Hadoop-for-Developers/blob/master/training_materials/developer/data/shakespeare.tar.gz)


1. Sent both the downloaded tar.gz and the generated .jar to a container
```
$ kubectl exec -n default -it hadoop-hadoop-hdfs-nn-0 -- bash
# mkdir -p /root/bucket
# exit

$ kubectl cp ~/Downloads/shakespeare.tar.gz hadoop-hadoop-hdfs-nn-0:/root/bucket
$ kubectl cp build/libs/labs-1.0-SNAPSHOT.jar hadoop-hadoop-hdfs-nn-0:/root/bucket/
```

1. Unzip and load it to the HDFS:
```
$ kubectl exec -n default -it hadoop-hadoop-hdfs-nn-0 -- bash
# cd ~/bucket/
# tar -xzvf shakespeare.tar.gz
# hdfs fs -mkdir -p /user/root
# hadoop fs -put shakespeare shakespeare
```

1. Execute the application:
```
# hadoop jar bucket/labs-1.0-SNAPSHOT.jar shakespeare/poems myOutput
 In Driver now!
20/02/08 13:29:17 INFO client.RMProxy: Connecting to ResourceManager at hadoop-hadoop-yarn-rm/10.1.0.107:8032
20/02/08 13:29:18 WARN mapreduce.JobResourceUploader: Hadoop command-line option parsing not performed. Implement the Tool interface and execute your app
lication with ToolRunner to remedy this.
20/02/08 13:29:19 INFO input.FileInputFormat: Total input files to process : 1
20/02/08 13:29:20 INFO mapreduce.JobSubmitter: number of splits:1
20/02/08 13:29:20 INFO Configuration.deprecation: yarn.resourcemanager.system-metrics-publisher.enabled is deprecated. Instead, use yarn.system-metrics-p
ublisher.enabled
20/02/08 13:29:20 INFO mapreduce.JobSubmitter: Submitting tokens for job: job_1581154485983_0002
20/02/08 13:29:21 INFO impl.YarnClientImpl: Submitted application application_1581154485983_0002
20/02/08 13:29:21 INFO mapreduce.Job: The url to track the job: http://hadoop-hadoop-yarn-rm-0.hadoop-hadoop-yarn-rm.default.svc.cluster.local:8088/proxy
/application_1581154485983_0002/
20/02/08 13:29:21 INFO mapreduce.Job: Running job: job_1581154485983_0002
20/02/08 13:29:38 INFO mapreduce.Job: Job job_1581154485983_0002 running in uber mode : false
20/02/08 13:29:38 INFO mapreduce.Job:  map 0% reduce 0%
20/02/08 13:29:53 INFO mapreduce.Job:  map 100% reduce 0%
20/02/08 13:30:05 INFO mapreduce.Job:  map 100% reduce 100%
20/02/08 13:30:07 INFO mapreduce.Job: Job job_1581154485983_0002 completed successfully
20/02/08 13:30:07 INFO mapreduce.Job: Counters: 49
        File System Counters
                FILE: Number of bytes read=558628
                FILE: Number of bytes written=1523147
                FILE: Number of read operations=0
                FILE: Number of large read operations=0
                FILE: Number of write operations=0
                HDFS: Number of bytes read=268266
                HDFS: Number of bytes written=67271
                HDFS: Number of read operations=6
                HDFS: Number of large read operations=0
                HDFS: Number of write operations=2
        Job Counters 
                Launched map tasks=1
                Launched reduce tasks=1
                Rack-local map tasks=1
                Total time spent by all maps in occupied slots (ms)=8831
                Total time spent by all reduces in occupied slots (ms)=9861
                Total time spent by all map tasks (ms)=8831
                Total time spent by all reduce tasks (ms)=9861
                Total vcore-milliseconds taken by all map tasks=8831
                Total vcore-milliseconds taken by all reduce tasks=9861
                Total megabyte-milliseconds taken by all map tasks=9042944
                Total megabyte-milliseconds taken by all reduce tasks=10097664
        Map-Reduce Framework
                Map input records=7308
                Map output records=50212
                Map output bytes=458198
                Map output materialized bytes=558628
                Input split bytes=126
                Combine input records=0
                Combine output records=0
                Reduce input groups=7193
                Reduce shuffle bytes=558628
                Reduce input records=50212
                Reduce output records=7193
                Spilled Records=100424
                Shuffled Maps =1
                Failed Shuffles=0
                Merged Map outputs=1
                GC time elapsed (ms)=263
                CPU time spent (ms)=2830
                Physical memory (bytes) snapshot=469868544
                Virtual memory (bytes) snapshot=3978256384
                Total committed heap usage (bytes)=314572800
        Shuffle Errors
                BAD_ID=0
                CONNECTION=0
                IO_ERROR=0
                WRONG_LENGTH=0
                WRONG_MAP=0
                WRONG_REDUCE=0
        File Input Format Counters 
                Bytes Read=268140
        File Output Format Counters 
                Bytes Written=67271
```

1. To monitory and see status of the execution, use hte YARN dashboard. To access it, you must create a port-forward of the service first, than access the URL http://localhost:8088/cluster/nodes.
```
$ kubectl port-forward svc/hadoop-hadoop-yarn-ui 8088:8088
```

1. Port-foward of the Hadoop dashboard to be able to download the resultset: 
> You need 2 different terminal sections
```
$ kubectl port-forward svc/hadoop-hadoop-hdfs-nn 50070:50070
$ kubectl port-forward svc/hadoop-hadoop-hdfs-dn 50075:50075
```

1. Access the URL and navigate to `Utilities > Browser File System`
```
http://localhost:50070/explorer.html#/user/root/myOutput
```

1. Resultset sample:
```
$ tail ~/Downloads/part-r-00000 
youngling       1
youngly 1
youngster       1
your    117
yours   9
yourself        10
yourselves      1
youth   33
youthful        4
zealous 1
```

1. AVG resolution, see WordCalc.java, AvgWordMapper.java and AvgReducer. Example of results:
```
A	3.1134538152610443
B	3.6926952141057936
C	6.320224719101123
D	5.245614035087719
E	4.8
F	3.831168831168831
...
w	4.540181691125087
y	3.927350427350427
z	7.0
```