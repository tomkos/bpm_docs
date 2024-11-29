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

## Class BusinessCategoryDefinitionFactory

- java.lang.Object
    - com.ibm.task.api.BusinessCategoryDefinitionFactory

- public class BusinessCategoryDefinitionFactory
extends java.lang.Object
Factory to create a business category definition object.
Since:
6.2.0.3

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT
    - Method Summary Methods Modifier and Type Method and Description BusinessCategoryDefinition createBusinessCategoryDefinition (java.lang.String name) Creates a business category definition object with the specified business category name. BusinessCategoryDefinition createBusinessCategoryDefinition (java.lang.String name, BusinessCategoryDefinition fromBusinessCategoryDefinition) Creates a business category definition object based on the specified business category definition. static BusinessCategoryDefinitionFactory newInstance () Returns the single instance of a BusinessCategoryDefinitionFactory.

### Method Summary

| Modifier and Type                        | Method and Description                                                                                                                                                                                                                                |
|------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| BusinessCategoryDefinition               | createBusinessCategoryDefinition(java.lang.String name) Creates a business category definition object with the specified business category name.                                                                                                      |
| BusinessCategoryDefinition               | createBusinessCategoryDefinition(java.lang.String name,                                 BusinessCategoryDefinition fromBusinessCategoryDefinition) Creates a business category definition object based on the specified business category definition. |
| static BusinessCategoryDefinitionFactory | newInstance() Returns the single instance of a BusinessCategoryDefinitionFactory.                                                                                                                                                                     |

- Methods inherited from class java.lang.Object
clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait