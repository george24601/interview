* Stack has 3 parts:
  * local variables, include method parameters. Instruction will use its index to refer to values
    * first parameter for local variable is refernce to 'this'
  * operands - accessed by pushing and poping
  * frame data - supports constant pool resolution, normal method return, and exception dispatch
* JVM is stack-based instead of register-based, instructions are taken from operand stack instead of registers
* Reference to types, fields, and methods are intially symbolic and resolved mostly on-demand
* when a method returns a normal value, JVM pushs it to the operand stack of the calling method
* 



