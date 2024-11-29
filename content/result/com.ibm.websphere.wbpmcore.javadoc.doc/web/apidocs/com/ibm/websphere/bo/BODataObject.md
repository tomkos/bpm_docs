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

## Interface BODataObject

- public interface BODataObject
The BODataObject interface represents the client programming model interface
 for the BODataObject service.  The BODataObject service provides a set of
 helper methods that are extensions to the operations that are currently
 provided as part of the commonj.sdo.DataObject interface.

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT
    - Method Summary

Methods 

Modifier and Type
Method and Description

commonj.sdo.DataObject
getBusinessGraph(commonj.sdo.DataObject businessObject)
Returns the Business Graph associated with the provided Business
 Object, if one exists.

commonj.sdo.ChangeSummary
getChangeSummary(commonj.sdo.DataObject businessObject)
Returns the Change Summary associated with the provided Business
 Object, if one exists.

BOEventSummary
getEventSummary(commonj.sdo.DataObject businessObject)
Returns the Event Summary associated with the provided Business
 Object, if one exists.

commonj.sdo.DataObject
getRootBusinessObject(commonj.sdo.DataObject businessObject)
If the provided Business Object is contained in a Business Graph,
 the root Business Object of the Business Graph is returned
 (the value of the data property of the Business Graph).

- ============ FIELD DETAIL =========== ============ METHOD DETAIL ==========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
See Also:Constant Field Values

- Method Detail

### Method Detail

    - getBusinessGraph
commonj.sdo.DataObject getBusinessGraph(commonj.sdo.DataObject businessObject)
Returns the Business Graph associated with the provided Business
 Object, if one exists.
Parameters:businessObject - The Business Object contained in a Business
 Graph
Returns:The Business Graph associated with the Business Object
    - getChangeSummary
commonj.sdo.ChangeSummary getChangeSummary(commonj.sdo.DataObject businessObject)
Returns the Change Summary associated with the provided Business
 Object, if one exists.
Parameters:businessObject - The Business Object contained in a Business
 Graph that contains the Change Summary
Returns:The Change Summary associated with the Business Object
    - getEventSummary
BOEventSummary getEventSummary(commonj.sdo.DataObject businessObject)
Returns the Event Summary associated with the provided Business
 Object, if one exists.
Parameters:businessObject - The Business Object contained in a Business
 Graph that contains the Event Summary
Returns:The Event Summary associated with the Business Object
    - getRootBusinessObject
commonj.sdo.DataObject getRootBusinessObject(commonj.sdo.DataObject businessObject)
If the provided Business Object is contained in a Business Graph,
 the root Business Object of the Business Graph is returned
 (the value of the data property of the Business Graph).  If the
 Business Object is not contained in a Business Graph then the root
 of the Business Object hierarchy is returned.
Parameters:businessObject - The Business Object for which the root
 Business Object can be found
Returns:The root Business Object in the object hierarchy