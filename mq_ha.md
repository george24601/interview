* When multiple writes failed to write to MQ, stop to write backup traffic endpoint, provided by the traffic control cluster(TCC), and send it directly to the TCC, which uses rate limiting to discard excessive traffic. Probably can't be brute forced, i.e., more domain-specific discarding logic  
* When kv cluster is down, deploy Slave cluster by hand with additional factor of N, turn on the downgrade switch in the TCC, will will distribute it to each salve node. Slave node will save it in memmory. However, slave can't store all data, just store the latest hour
* If mysql is down, store part of data into cache cluster, with only limited capacities 
* For cold data, cache high frequency results
