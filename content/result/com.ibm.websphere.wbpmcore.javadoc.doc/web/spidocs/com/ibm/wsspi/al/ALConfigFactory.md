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

## Class ALConfigFactory

- java.lang.Object
    - com.ibm.wsspi.al.ALConfigFactory

- public class ALConfigFactory
extends java.lang.Object
ALConfigFactory is a factory class that can be used to create instance of ALConfig

- =========== FIELD SUMMARY =========== ======== CONSTRUCTOR SUMMARY ======== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT 

static java.lang.String
REMOTE\_LOCATOR
a constant for the name of RemoteLocator

static java.lang.String
REMOTE\_WEBSPHERE\_LOCATOR
a constant for the name of ClusterLocator
    - Constructor Summary

Constructors 

Constructor and Description

ALConfigFactory()
    - Method Summary Methods Modifier and Type Method and Description static ALConfiguration create (java.lang.String name, java.lang.String locatorName) create an instance of ALConfig static ALConfiguration createFromPreConfig (java.lang.String name) create an instance of ALConfig based on pre configured value.

### Method Summary

| Modifier and Type      | Method and Description                                                                                   |
|------------------------|----------------------------------------------------------------------------------------------------------|
| static ALConfiguration | create(java.lang.String name,       java.lang.String locatorName) create an instance of ALConfig         |
| static ALConfiguration | createFromPreConfig(java.lang.String name) create an instance of ALConfig based on pre configured value. |

- Methods inherited from class java.lang.Object
clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait