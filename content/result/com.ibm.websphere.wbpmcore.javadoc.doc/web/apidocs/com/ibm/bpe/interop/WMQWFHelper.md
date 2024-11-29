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

## Class WMQWFHelper

- java.lang.Object
    - com.ibm.bpe.interop.WMQWFHelper

- public class WMQWFHelper
extends java.lang.Object

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

WMQWFHelper()
    - Method Summary Methods Modifier and Type Method and Description static java.lang.String createCorrelationID () This method creates a WMQWF like unique correlation id for the UPES invocation. static commonj.sdo.DataObject initializeBO (commonj.sdo.DataObject obj, commonj.sdo.Type objType) This method creates a new BO using the given type just in case the given BO is null. static boolean isSet (commonj.sdo.DataObject obj, java.lang.String path) This function enhance the DataObject.isSet() method. static commonj.sdo.DataObject merge (commonj.sdo.DataObject source, java.lang.String sourcePath, commonj.sdo.DataObject target, java.lang.String targetPath, commonj.sdo.Type targetType) This method merges two BO's as it does WMQWF.

### Method Summary

| Modifier and Type             | Method and Description                                                                                                                                                                                                       |
|-------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| static java.lang.String       | createCorrelationID() This method creates a WMQWF like unique correlation id for the UPES  invocation.                                                                                                                       |
| static commonj.sdo.DataObject | initializeBO(commonj.sdo.DataObject obj,             commonj.sdo.Type objType) This method creates a new BO using the given type just in case the given  BO is null.                                                         |
| static boolean                | isSet(commonj.sdo.DataObject obj,      java.lang.String path) This function enhance the DataObject.isSet() method.                                                                                                           |
| static commonj.sdo.DataObject | merge(commonj.sdo.DataObject source,      java.lang.String sourcePath,      commonj.sdo.DataObject target,      java.lang.String targetPath,      commonj.sdo.Type targetType) This method merges two BO's as it does WMQWF. |

- Methods inherited from class java.lang.Object
clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait