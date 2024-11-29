- Overview
- Package
- Class
- Tree
- Deprecated
- Index
- Help

- Prev Class
- Next Class

- Frames
- No Frames

- All Classes

- Summary:
- Nested |
- Field |
- Constr |
- Method

- Detail:
- Field |
- Constr |
- Method

## Class CustomPropertyFactory

- java.lang.Object
    - com.ibm.task.api.CustomPropertyFactory

- public class CustomPropertyFactory
extends java.lang.Object
Factory to create a custom property or an inline custom property object.
Since:
6.2.0.2
 
Change History

Release
 Modification
 
7.5.1
 
 Allows for the creation of inline custom properties.

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT
    - Method Summary Methods Modifier and Type Method and Description CustomProperty createCustomProperty (java.lang.String propertyName, java.lang.String propertyValue) Creates a custom property object. InlineCustomProperty createInlineCustomProperty (java.lang.String propertyName, java.lang.String propertyValue) Creates an inline custom property object. static CustomPropertyFactory newInstance () Returns the single instance of a CustomPropertyFactory.

### Method Summary

| Modifier and Type            | Method and Description                                                                                                                                        |
|------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CustomProperty               | createCustomProperty(java.lang.String propertyName,                     java.lang.String propertyValue) Creates a custom property object.                     |
| InlineCustomProperty         | createInlineCustomProperty(java.lang.String propertyName,                           java.lang.String propertyValue) Creates an inline custom property object. |
| static CustomPropertyFactory | newInstance() Returns the single instance of a CustomPropertyFactory.                                                                                         |

- Methods inherited from class java.lang.Object
clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait