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

## Class WorkBasketDefinitionFactory

- java.lang.Object
    - com.ibm.task.api.WorkBasketDefinitionFactory

- public class WorkBasketDefinitionFactory
extends java.lang.Object
Factory to create a work basket definition object.
Since:
6.2.0.3

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT
    - Method Summary Methods Modifier and Type Method and Description WorkBasketDefinition createWorkBasketDefinition (java.lang.String name) Creates a work basket definition object with the specified work basket name. WorkBasketDefinition createWorkBasketDefinition (java.lang.String name, WorkBasketDefinition fromWorkBasketDefinition) Creates a work basket definition object based on the specified work basket definition. static WorkBasketDefinitionFactory newInstance () Returns the single instance of a WorkBasketDefinitionFactory.

### Method Summary

| Modifier and Type                  | Method and Description                                                                                                                                                                                            |
|------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| WorkBasketDefinition               | createWorkBasketDefinition(java.lang.String name) Creates a work basket definition object with the specified work basket name.                                                                                    |
| WorkBasketDefinition               | createWorkBasketDefinition(java.lang.String name,                           WorkBasketDefinition fromWorkBasketDefinition) Creates a work basket definition object based on the specified work basket definition. |
| static WorkBasketDefinitionFactory | newInstance() Returns the single instance of a WorkBasketDefinitionFactory.                                                                                                                                       |

- Methods inherited from class java.lang.Object
clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait