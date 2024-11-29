# Using the TWObjectFactory, TWObject and TWList classes

The following classes provide methods that are helpful to an external Java application working
with a Java integration step in a business process. To use these methods you
must include the psclnt.jar and svrcoreclnt.jar files in
your build classpath. You can find these JAR files in the following path:
install\_root/BPM/Lombardi/lib. You should use the
teamworks package for these classes.

- TWObjectFactory class
- TWObject class
- TWList class

## TWObjectFactory class

This class' methods create the business objects and lists (arrays) that your Java application can
use.

| Methods with input and output parameters           | Description                                                                                     |
|----------------------------------------------------|-------------------------------------------------------------------------------------------------|
| VersioningContext getThreadVersioningContext()     | Gets the current thread's versioning context. A context encompasses a set of versioned objects. |
| void setThreadVersioningContext(VersioningContext) | Sets the thread's versioning context.                                                           |
| TWObject createObject()                            | Creates a business object.                                                                      |
| TWObject createObject(String)                      | Creates a business object of the specified type in the argument.                                |
| TWObject createPrototype()                         | Creates a prototype of an object.                                                               |
| TWList createList()                                | Creates a list. A list is an array.                                                             |
| TWList createList(String)                          | Creates a List which will contain items of the type specified in the argument.                  |
| TWList createList(Collection)                      | Creates a List containing the items in the collection argument.                                 |
| TWObject createIndexedMapObject()                  | Creates an indexed map object.                                                                  |

## TWObject class

The methods in this class allow you to work with the properties of the business objects.

| Methods with input and output parameters   | Description                                                                                                                     |
|--------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|
| String getTWClassName()                    | Gets the class name of the business object.                                                                                     |
| Set getPropertyNames()                     | Gets the property names.                                                                                                        |
| Object getPropertyValue(String)            | Retrieves the property value named in the argument.                                                                             |
| void setPropertyValue(String, Object)      | Sets the property value named in the argument.                                                                                  |
| void setPropertyValue(Map)                 | Sets the property value using a map to take the property from. A map contains a property value object keyed by a property name. |
| void removeProperty(String)                | Removes the property named in the argument.                                                                                     |

## TWList class

The methods in
this class allow you to work with the values in a list (array).

| Methods with input and output parameters   | Description                                                               |
|--------------------------------------------|---------------------------------------------------------------------------|
| String getTWClassName()                    | Gets the class name of the business object.                               |
| int getArraySize()                         | Gets the size of the array; that is, the number of elements in the array. |
| void addArrayData(Object)                  | Adds an object to the array.                                              |
| void addArrayData(int, Object)             | Assigns an object to the array at the index named in the argument.        |
| Object getArrayData(int)                   | Gets the object from the array at the index named in the argument.        |
| void removeIndex(int)                      | Removes the index identified in the argument.                             |
| boolean isEmptyArray()                     | Specifies if the array has no elements.                                   |
| List getUnmodifiableArray()                | Gets a read-only list.                                                    |