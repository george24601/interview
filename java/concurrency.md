* How is Reentrant lock implemented? compare that with synchronized, what is the difference?
* ConcurrentLinkedQueue
* CyclicBarrier
* How many ways to create a thread? 
  * inherit from Thread
  * implemnt RUnnable
  * finally use start()
  * start() means thread is ready statu, but not running, and then run() is the actual thing. run() will execute inside the main thread
* T1, T2, and T3, how to ensure that they execute in order, i.e., T2 executes after T1, when T3 throws execption after T2 finish, what will happen?
* Suppose you want multiple threads to execute at a point, reach it,a nd then execute again, how to implement (CDL and CyclicBarrir)
