# Hadoop & MapReduce Notes

Classes: http://b-tierney.com/msc-prog-big-data/

1. If you still don't have, install Docker-desktop and activate Kubernetes ([Docker Desktop](https://www.docker.com/products/docker-desktop)).
    > You will also need [helm](https://helm.sh/docs/intro/install/) installed and running.

1. Add the lines bellow to your `/etc/hosts`
```
127.0.0.1 hadoop-hadoop-hdfs-dn-0.hadoop-hadoop-hdfs-dn.default.svc.cluster.local
127.0.0.1 hadoop-hadoop-hdfs-nn-0.hadoop-hadoop-hdfs-nn.default.svc.cluster.local
127.0.0.1 hadoop-hadoop-yarn-nm-0.hadoop-hadoop-yarn-nm.default.svc.cluster.local
127.0.0.1 hadoop-hadoop-yarn-nm-1.hadoop-hadoop-yarn-nm.default.svc.cluster.local
127.0.0.1 hadoop-hadoop-yarn-rm-0.hadoop-hadoop-yarn-rm.default.svc.cluster.local
```

1. [Hadoop Helm chart](https://github.com/helm/charts/tree/master/stable/hadoop)
```
cd /Users/bambrozi/workspace/github.com/bambrozio/helm

helm install --name hadoop \
--set persistence.nameNode.enabled=true \
--set persistence.nameNode.storageClass=hostpath \
--set persistence.dataNode.enabled=true \
--set persistence.dataNode.storageClass=hostpath \
--set persistence.nameNode.enabled=true \
stable/hadoop
```
> To delete it, use: `helm del hadoop --purge`.



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
$ kubectl exec -n default -it hadoop-hadoop-hdfs-nn-0 -- bash -c 'mkdir -p /root/bucket'
$ kubectl cp ~/Downloads/shakespeare.tar.gz hadoop-hadoop-hdfs-nn-0:/root/bucket
$ kubectl cp build/libs/labs-1.0-SNAPSHOT.jar hadoop-hadoop-hdfs-nn-0:/root/bucket/
$ kubectl exec -n default -it hadoop-hadoop-hdfs-nn-0 -- bash -c 'ls -lath /root/bucket'
```

1. Unzip and load it to the HDFS:
```
$ kubectl exec -n default -it hadoop-hadoop-hdfs-nn-0 -- bash -c 'tar -xzvf /root/bucket/shakespeare.tar.gz -C /root/bucket/'
$ kubectl exec -n default -it hadoop-hadoop-hdfs-nn-0 -- bash -c 'hdfs dfs -mkdir -p /user/root'
$ kubectl exec -n default -it hadoop-hadoop-hdfs-nn-0 -- bash -c 'hdfs dfs -put /root/bucket/shakespeare shakespeare'
$ kubectl exec -n default -it hadoop-hadoop-hdfs-nn-0 -- bash -c 'hdfs dfs -ls /user/root/shakespeare'
```

1. Execute the application:
```
$ kubectl exec -n default -it hadoop-hadoop-hdfs-nn-0 -- bash -c 'hadoop jar /root/bucket/labs-1.0-SNAPSHOT.jar sum shakespeare/poems output-wc-sum-1'
...
```

1. To monitory and see status of the execution, use hte YARN dashboard. To access it, you must create a port-forward of the service first, than access the URL http://localhost:8088/cluster/nodes.
```
$ kubectl port-forward svc/hadoop-hadoop-yarn-ui 8088:8088
```

1. Port-foward of the Hadoop dashboard to be able to download the resultset: 
> You will need 2 more different terminal sessions to keep the por-forward's connected.
```
$ kubectl port-forward svc/hadoop-hadoop-hdfs-nn 50070:50070
$ kubectl port-forward svc/hadoop-hadoop-hdfs-dn 50075:50075
$ kubectl port-forward hadoop-hadoop-yarn-nm-1 8042:8042
```

1. Access the URL and navigate to `Utilities > Browser File System`, then: `user > root` to see/download the output files.
```
http://localhost:50070/
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