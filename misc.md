* StringBuilder vs StringBuffer
  * StringBuffer is threadsafe
  * StringUtils.join uses StringBuilder too
* Why no isSuccess var name?
  * In Java Bean spec, the boolean type method must be isProperty. 
  * isSuccess var name may confuse different serialization/deserialization framework
  * As per alibaba recommendation, POJO member properteis must be packaged type, and local var uses basic type, so that you get NPE early instead unexpected null 
* Proper ex handling should have local context and stack race, or re-throw
```java
logger.error(param, object strings + "_" + e.getMessage(), e)
```
* Why need to override hashcode and equals?
* [Covariance and contravariance](http://george24601.github.io/2018/11/05/covariant-contravariance.html)
