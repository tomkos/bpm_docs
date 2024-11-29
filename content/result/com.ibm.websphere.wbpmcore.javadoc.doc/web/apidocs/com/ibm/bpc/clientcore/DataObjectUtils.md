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

## Class DataObjectUtils

- java.lang.Object
    - com.ibm.bpc.clientcore.DataObjectUtils

- public class DataObjectUtils
extends java.lang.Object
Provides utilities that facilitate working with DataObjects.

- =========== FIELD SUMMARY =========== ======== CONSTRUCTOR SUMMARY ======== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT
    - Constructor Summary

Constructors 

Constructor and Description

DataObjectUtils()
    - Method Summary Methods Modifier and Type Method and Description static java.util.Map getValueMap (commonj.sdo.DataObject dataObject) Provides a modifiable map representation of the DataObject. static commonj.sdo.DataObject populateAll (commonj.sdo.DataObject dataObject, java.util.Map valueMap) Sets values in the value map on the DataObject. static commonj.sdo.DataObject populateAll (commonj.sdo.DataObject dataObject, java.util.Map valueMap, boolean setDefaultsForMandatoryFields) Sets values in the value map on the DataObject. static commonj.sdo.DataObject putAll (commonj.sdo.DataObject dataObject, java.util.Map valueMap) Sets values in the value map on the DataObject. static commonj.sdo.DataObject putAll (commonj.sdo.DataObject dataObject, java.util.Map valueMap, boolean setDefaultsForMandatoryFields) Sets values in the value map on the DataObject.

### Method Summary

| Modifier and Type             | Method and Description                                                                                                                                                              |
|-------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| static java.util.Map          | getValueMap(commonj.sdo.DataObject dataObject) Provides a modifiable map representation of the DataObject.                                                                          |
| static commonj.sdo.DataObject | populateAll(commonj.sdo.DataObject dataObject,            java.util.Map valueMap) Sets values in the value map on the DataObject.                                                   |
| static commonj.sdo.DataObject | populateAll(commonj.sdo.DataObject dataObject,            java.util.Map valueMap,            boolean setDefaultsForMandatoryFields) Sets values in the value map on the DataObject. |
| static commonj.sdo.DataObject | putAll(commonj.sdo.DataObject dataObject,       java.util.Map valueMap) Sets values in the value map on the DataObject.                                                             |
| static commonj.sdo.DataObject | putAll(commonj.sdo.DataObject dataObject,       java.util.Map valueMap,       boolean setDefaultsForMandatoryFields) Sets values in the value map on the DataObject.                |

- Methods inherited from class java.lang.Object
clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait