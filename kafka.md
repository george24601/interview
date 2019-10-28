### Kafka

* how is it stored on disk
* How to optimize producer/consumer
* How does Kafka controller handles failover
* How does leader and follower sync data
* [Flushing mechanism](http://george24601.github.io/2019/03/13/innodb-kafka-flushing.html)
* [What to do when MQ is down](mq_ha.md)
* How to design a system with 0-loss of data in the whole MQ
* How to handle the lagged consumer
* How to design a delayed task system
* How to design a Kafka to RocketMQ double write + double read problem, to ensure seamless migration

### MQ HA
* When multiple writes failed to write to MQ, stop to write backup traffic endpoint, provided by the traffic control cluster(TCC), and send it directly to the TCC, which uses rate limiting to discard excessive traffic. Probably can't be brute forced, i.e., more domain-specific discarding logic  
* When kv cluster is down, deploy Slave cluster by hand with additional factor of N, turn on the downgrade switch in the TCC, will will distribute it to each salve node. Slave node will save it in memmory. However, slave can't store all data, just store the latest hour
* If mysql is down, store part of data into cache cluster, with only limited capacities 
* For cold data, cache high frequency results
