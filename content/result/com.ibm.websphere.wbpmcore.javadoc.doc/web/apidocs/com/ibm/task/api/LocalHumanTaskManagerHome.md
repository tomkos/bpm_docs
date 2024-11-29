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

## Interface LocalHumanTaskManagerHome

- All Superinterfaces:
javax.ejb.EJBLocalHome

public interface LocalHumanTaskManagerHome
extends javax.ejb.EJBLocalHome
The local home interface of the HumanTaskManager session bean.

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
    - Method Summary Methods Modifier and Type Method and Description LocalHumanTaskManager create () Creates the local interface of the HumanTaskManager session bean.

### Method Summary

| Modifier and Type     | Method and Description                                                     |
|-----------------------|----------------------------------------------------------------------------|
| LocalHumanTaskManager | create() Creates the local interface of the HumanTaskManager session bean. |

- Methods inherited from interface javax.ejb.EJBLocalHome
remove