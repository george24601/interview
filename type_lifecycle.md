### What happens when JVM creates an instance?  
(TO review)
* loading - creating the type
  * class loader locates the ".class" file and parse it
  * create an instance of java.lang.Class
* linking
  * class loader verification
     * check in the constant pool if params are valid, check if the type has been loaded
     * basically all except symbolic references
  * allocate memory and init default value for class variables
  * translate symbolic reference to direct reference - optinal until first used by the program
* Initialization -  <clinit>() / () method. At this time, the CLASS is ready to use, including static fields/methods and creating an instance of it
* now starts working with the instance -  set object header - type, object's hash, object's gc gen info, 
* run init() method. This method is in the class file. One init() for each constrctor. The default init() just calls super class's default init()

### How is a reference to object implemented in JVM?
* handle: in heap has a handle pool, that has pointer to the object type data and pointer to object instance data.
*  direct pointer, to the object instance data already AND pointer to the object type data

### bootstrap loader
* part of VM implementation
* search the CLASSPATH in the order of its appearence for the ".class" file

### How many ways to create a new object?
* new operator
* newInstance() on Class or java.lang.reflect.Constructor object
* clone() exisiting object
* deserialize via getObject() from I/O stream?
