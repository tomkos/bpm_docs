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

## Interface LocalBusinessFlowManagerHome

- All Superinterfaces:
javax.ejb.EJBLocalHome

public interface LocalBusinessFlowManagerHome
extends javax.ejb.EJBLocalHome
The local home interface of the BusinessFlowManager session bean.

 This interface is made available to the client through JNDI by the container
 where it is deployed.
Since:
6.0

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT
    - Method Summary Methods Modifier and Type Method and Description LocalBusinessFlowManager create () Creates the local interface of the BusinessFlowManager session bean.

### Method Summary

| Modifier and Type        | Method and Description                                                        |
|--------------------------|-------------------------------------------------------------------------------|
| LocalBusinessFlowManager | create() Creates the local interface of the BusinessFlowManager session bean. |

- Methods inherited from interface javax.ejb.EJBLocalHome
remove