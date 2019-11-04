## How is class-related data stored on JVM? 

* Class loader reads the class file and loads the interpreted data into the JVM
* Static non-final variables are stored in the memory area, but static final variables are stored in runtime constant pool - still in the PermGen though. Also, final class variables are stored as part of the data that any type can use, whereas class variables is stores as part of the data for the type that declares them
* For each type: 
  * FQN of the type
  * FQN of super class
  * Is this type a class or interface?
  * Type modifier set - public, abstract, final?
  * FQN of direct superinterfaces it implements
  * Constant pool: an array holding literals and symbolic reference to types, fields, and methods
  * For each field:
    * name
    * type
    * modifier
  * For each method:
    * name
    * return type
    * parameter # and types
    * modifier set (public, private, abstract, final...)
    * If method is not abstract or native:
      * method byte codes 
      * size of the operand stack and local variables
      * Exception table
  * Class variables, i.e., static but not final
  * Reference to ClassLoader to support user-defined ClassLoader
  * Reference to class Class 
  * For non-abstract class, method table - array of direct references to array instance methods that maybe invoked from the instance


## How is the method area involved when we execute the main()

```java
class Volcano {

    public static void main(String[] args) {
        Lava lava = new Lava();
        lava.flow();
    }
}
```
 
* Class loader loads the class the main() method is in, populate method area with the type info listed above
* VM runs the byte codes of main() from method area, and maintain a pointer to the contant pool (in method area) of main()'s class
* `Lava` is a symbol in constant pool, so the class loader loads the `Lava` type and populate the corresponding method area  
* VM replace the symbol with reference to the `Lava` class's class data
* VM allocates memory for Lava, by look up Lava in method area to find out its heap space 
* VM inits all fields in lava to its default value
* Pushs the reference to the new Lava object into (operand) stack
* use the reference to init the private value of Lava
