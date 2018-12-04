* Why we need reference to a type's method area when we allocate memory for the object?  
  * when casting an object reference, need run-time type checking
  * similar reason, instanceOf
  * when VM invokes instance method - need to do the dynamic binding - call the actual type
* Heap design: handle pool and object pool
  * Object reference points to a handle pool entry, which has a pointer to instance data in the object pool and a pointer to class data in method area  
  * Only need to update one pointer when the instance data is moved, e.g., during defragmentation
  * but any access requires dereferencing twice
* Heap design: native pointer to a data bundle that contains the instance data and a pointer to object's class data
  * when the object data is moved, need to update every single native pointer
* Each object is (logically) associated with a lock - most like re-entrant lock
* Each object is (logically) asoociated with a wait set - to support Object class's wait(), notify(), and notifyAll() 
* Each unreferenced object need to indicate whether or not the object's finalizer has been run
* One implementation to have method table at hand relative to the object: A pointer to special structure in the method area. The pointer itself is on heap just as we discussed above. The special structre has 2 parts:
  * pointer to the full class data for the object
  * method table: array of pointers to the data for each instance method (including ones from superclasses) which has
    * operand size and local varaible sizes
    * method's bytecode
    * Exception table
    * No param name and type here!
