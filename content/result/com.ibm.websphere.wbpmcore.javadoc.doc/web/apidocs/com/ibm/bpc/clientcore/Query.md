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

## Interface Query

- All Known Implementing Classes: GenericBPCQuery public interface Query This interface encapsulates custom queries for application objects. The query should return a list of Java Beans. For example the queries for the HTM and BFM components in tbe BPC Explorer return ActivityInstanceBean or TaskInstanceBean objects. In addition to that, these object implement the following static methods which provide both the labels and the conversion logic for the UI: Using queries one can separate the UI code from the backend logic and thereby shield the application from configuration or access details for the backend modules.

```
public interface Query
```

    - static public String getLabel(String propertyName);
    - static public SimpleConverter getConverter(String propertyName);

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT
(C) Copyright IBM Corporation 2005, 2007.
    - Method Summary

Methods 

Modifier and Type
Method and Description

java.util.List
execute()
Retrieves a list of application objects.

java.lang.String
getType()
Returns a type that identifies the objects returned by the Query.execute method.

- ============ FIELD DETAIL =========== ============ METHOD DETAIL ==========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
(C) Copyright IBM Corporation 2005, 2007.
See Also:Constant Field Values

- Method Detail

### Method Detail

    - execute
java.util.List execute()
                       throws ClientException
Retrieves a list of application objects. Implement this method to access 
 backend modules and to filter the result list.
Returns:a list of objects that adhere to the Java Bean conventions.
Throws:
ClientException
    - getType
java.lang.String getType()
Returns a type that identifies the objects returned by the Query.execute method.
 Implement this type to establish type checking between the query and its caller.
Returns:The String representing the type of objects.