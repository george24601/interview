* CopyOnWriteArrayList
   * Why no ConcurrentArrayList?
   * uses volatile to assign the copy back to the member variable
   * Add still has lock to defend against concurrent adds, for read-heavy scenario
* BlockingQueue
  * LBQ, ABQ, DQ, SQ
* TreeMap and LinkedHashMap
* WeakHashMap
