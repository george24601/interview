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

Static code block will be compiled and put into clinit, when JVM executes clinit, it will lock this block, so DL may happen if they try to acquire each other's clinit via Class.forname.
