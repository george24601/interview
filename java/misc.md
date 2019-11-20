* Why need to override hashcode and equals?
* T1, T2, and T3, how to ensure that they execute in order, i.e., T2 executes after T1, when T3 throws execption after T2 finish, what will happen?
* Suppose you want multiple threads to execute at a point, reach it,a nd then execute again, how to implement (CDL and CyclicBarrir)
* CopyOnWriteArrayList
   * Why no ConcurrentArrayList?
   * uses volatile to assign the copy back to the member variable
   * Add still has lock to defend against concurrent adds, for read-heavy scenario
* TreeMap, LinkedHashMap, WeakHashMap
* When will reflection not get the params? how to get overload/overwrite methods? private conflict problem?
* Why no return inside finally block? try catch fainally, return in try, will finally execute?
* 4 types of references strong/weak/soft/virtual, what are their use cases?
* Can a List<String> turned into List<Object>?
