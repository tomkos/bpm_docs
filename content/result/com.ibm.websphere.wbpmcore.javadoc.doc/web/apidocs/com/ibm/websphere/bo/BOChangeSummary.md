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

## Interface BOChangeSummary

- public interface BOChangeSummary
The BOChangeSummary interface represents the client programming model interface
 for the BOChangeSummary service.  The BOChangeSummary service provides low
 level operations for reading and writing the Change Summary associated with
 a Business Graph.  The Change Summary is a data structure defined by the
 Service Data Object specification that records the changes to an associated
 graph of Business Objects.

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

void
addOldValue(commonj.sdo.DataObject businessObject,
           java.lang.String propertyPath,
           java.lang.Object lastValue,
           boolean lastIsSet)
Sets the old value and the isSet attributes of the property referenced
 by the combination of the Business Object and the property path in
 the Change Summary Setting for the property.

void
beginLogging(commonj.sdo.DataObject businessObject)
Initiate Change Summary logging while preserving the existing entries
 in the Change Summary.

void
clear(commonj.sdo.DataObject businessObject)
Clear all entries in the Change Summary associated with the object
 graph containing the Business Object.

java.util.List
getChangedProperties(commonj.sdo.DataObject businessObject)
Returns the list of all the changed properties of the Business
 Object.

commonj.sdo.DataObject
getOldContainer(commonj.sdo.DataObject businessObject)
Returns the Business Object that was the container of the Business
 Object before it was moved into the Change Summary.

commonj.sdo.Property
getOldContainmentProperty(commonj.sdo.DataObject businessObject)
Returns the Property of the Business Object that was the container
 of the Business Object before it was moved into the Change
 Summary.

commonj.sdo.ChangeSummary.Setting
getOldValue(commonj.sdo.DataObject businessObject,
           java.lang.String propertyPath)
Returns the first Change Summary Setting associated with the property
 referenced by the combination of the Business Object and the property
 path.

java.util.List
getOldValues(commonj.sdo.DataObject businessObject,
            java.lang.String propertyPath)
Returns the list of Change Summary Settings associated with the property
 referenced by the combination of the Business Object and the property
 path.

boolean
isUpdated(commonj.sdo.DataObject businessObject)
Determines whether the Change Summary associated with the Business
 Object has annotated the Business Object as Updated.

void
markCreated(commonj.sdo.DataObject businessObject)
Annotates the Business Object as Created in the Change Summary, such
 that ChangeSummary.isCreated() returns
 true.

void
markDeleted(commonj.sdo.DataObject businessObject)
Annotates the Business Object as Deleted in the Change Summary, such
 that ChangeSummary.isDeleted() returns
 true.

void
markListEntryMoved(java.lang.Object data,
                  commonj.sdo.DataObject businessObject,
                  java.lang.String propertyPath,
                  int newIndex)
Create a List Entry Moved annotation in the Change Summary for
 Object in the property represented by the combination of the
 Business Object and the property path.

void
markSimpleTypeCreated(java.lang.Object o,
                     commonj.sdo.DataObject businessObject,
                     java.lang.String propertyPath)
Marks a simple type object as Created.

void
markSimpleTypeDeleted(java.lang.Object o,
                     commonj.sdo.DataObject businessObject,
                     java.lang.String propertyPath)
Marks a simple type object as Deleted.

void
markUpdated(commonj.sdo.DataObject businessObject)
Annotates the Business Object as Updated in the Change Summary, such
 that BOChangeSummary.isUpdated() returns
 true.

void
removeAllOldValues(commonj.sdo.DataObject businessObject)
Remove all the Change Summary Settings associated with the Business
 Object.

void
removeChanges(commonj.sdo.DataObject businessObject)
Removes the Created, Updated, and Deleted annotations for this Business
 Object in its associated Change Summary.

void
removeOldValue(commonj.sdo.ChangeSummary.Setting oldValue)
Remove the Change Summary Setting from the Change Summary.

void
removeOldValues(commonj.sdo.DataObject businessObject,
               java.lang.String propertyPath)
Remove the Change Summary Settings associated with the property
 referenced by the combination of the Business Object and the property
 path.

- ============ FIELD DETAIL =========== ============ METHOD DETAIL ==========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
See Also:Constant Field Values

- Method Detail

### Method Detail

    - markCreated
void markCreated(commonj.sdo.DataObject businessObject)
Annotates the Business Object as Created in the Change Summary, such
 that ChangeSummary.isCreated() returns
 true.
 
 The Business Object must be contained in a Business Graph that
 contains a Change Summary.
Parameters:businessObject - The Business Object to annotate as Created
    - markUpdated
void markUpdated(commonj.sdo.DataObject businessObject)
Annotates the Business Object as Updated in the Change Summary, such
 that BOChangeSummary.isUpdated() returns
 true.
 
 The Business Object must be contained in a Business Graph that
 contains a Change Summary.
Parameters:businessObject - The Business Object to annotate as Updated
    - markDeleted
void markDeleted(commonj.sdo.DataObject businessObject)
Annotates the Business Object as Deleted in the Change Summary, such
 that ChangeSummary.isDeleted() returns
 true.
 
 The Business Object must be contained in a Business Graph that
 contains a Change Summary.
Parameters:businessObject - The Business Object to annotate as Deleted
    - isUpdated
boolean isUpdated(commonj.sdo.DataObject businessObject)
Determines whether the Change Summary associated with the Business
 Object has annotated the Business Object as Updated.

 The Business Object must be contained in a Business Graph that
 contains a Change Summary.
Parameters:businessObject - The Business Object whose Change Summary
 annotation will be checked against the Updated status
Returns:boolean true if the Business Object was annotated
 as Updated, false otherwise.
    - removeChanges
void removeChanges(commonj.sdo.DataObject businessObject)
Removes the Created, Updated, and Deleted annotations for this Business
 Object in its associated Change Summary.

 The Business Object must be contained in a Business Graph that
 contains a Change Summary.
Parameters:businessObject - The Business Object whose Change Summary
 annotations are to be removed
    - addOldValue
void addOldValue(commonj.sdo.DataObject businessObject,
               java.lang.String propertyPath,
               java.lang.Object lastValue,
               boolean lastIsSet)
Sets the old value and the isSet attributes of the property referenced
 by the combination of the Business Object and the property path in
 the Change Summary Setting for the property.
Parameters:businessObject - The Business Object used in combination with the
 property path to determine the property whose Change Summary value
 needs to be setpropertyPath - The property path used in combination with the
 Business Object to determine the property whose Change Summary value
 needs to be setlastValue - The property's value to add to the Change SummarylastIsSet - The property's isSet value to add to the Change Summary
    - getOldValue
commonj.sdo.ChangeSummary.Setting getOldValue(commonj.sdo.DataObject businessObject,
                                            java.lang.String propertyPath)
Returns the first Change Summary Setting associated with the property
 referenced by the combination of the Business Object and the property
 path.
Parameters:businessObject - The Business Object used in combination with
 the property path to reference the propertypropertyPath - The property path used in combination with the
 Business Object to reference the property
Returns:The first Change Summary Setting for the property
    - getOldValues
java.util.List getOldValues(commonj.sdo.DataObject businessObject,
                          java.lang.String propertyPath)
Returns the list of Change Summary Settings associated with the property
 referenced by the combination of the Business Object and the property
 path.

 Note: The current Change Summary will contain only one Change Summary
 setting so this method is functionally equivalent to
 getOldValue().
Parameters:businessObject - The Business Object used in combination with
 the property path to reference the propertypropertyPath - The property path used in combination with the
 Business Object to reference the property
Returns:The list of ChangeSummary.Settings for the property
    - getChangedProperties
java.util.List getChangedProperties(commonj.sdo.DataObject businessObject)
Returns the list of all the changed properties of the Business
 Object.
Parameters:businessObject - The Business Object whose changed properties
 are being queried
Returns:The list of Property objects that have changed
    - removeOldValue
void removeOldValue(commonj.sdo.ChangeSummary.Setting oldValue)
Remove the Change Summary Setting from the Change Summary.
Parameters:oldValue - Change Summary Setting to remove
    - removeOldValues
void removeOldValues(commonj.sdo.DataObject businessObject,
                   java.lang.String propertyPath)
Remove the Change Summary Settings associated with the property
 referenced by the combination of the Business Object and the property
 path.
Parameters:businessObject - The Business Object used in combination with
 the property path to reference the propertypropertyPath - The property path used in combination with the
 Business Object to reference the property
    - removeAllOldValues
void removeAllOldValues(commonj.sdo.DataObject businessObject)
Remove all the Change Summary Settings associated with the Business
 Object.
Parameters:businessObject - The Business Object used in combination with
 the property path to reference the propertypropertyPath - The property path used in combination with the
 Business Object to reference the property
    - clear
void clear(commonj.sdo.DataObject businessObject)
Clear all entries in the Change Summary associated with the object
 graph containing the Business Object.
Parameters:businessObject - The Business Object that is part of the
 Business Graph containing the Change Summary
    - beginLogging
void beginLogging(commonj.sdo.DataObject businessObject)
Initiate Change Summary logging while preserving the existing entries
 in the Change Summary.

 This operation is similar to ChangeSummary.beginLogging()
 except the ChangeSummary beginLogging() operation clears the Change
 Summary.
Parameters:businessObject - The Business Object that is part of the
 Business Graph containing the Change Summary
    - getOldContainer
commonj.sdo.DataObject getOldContainer(commonj.sdo.DataObject businessObject)
Returns the Business Object that was the container of the Business
 Object before it was moved into the Change Summary.
Parameters:businessObject - The Business Object in the Change Summary
Returns:The Business Object that was the container before it
 was added to the Change Summary
    - getOldContainmentProperty
commonj.sdo.Property getOldContainmentProperty(commonj.sdo.DataObject businessObject)
Returns the Property of the Business Object that was the container
 of the Business Object before it was moved into the Change
 Summary.
Parameters:businessObject - The Business Object in the Change Summary
Returns:The Property that contained the Business Object before it
 was moved into the Change Summary
    - markListEntryMoved
void markListEntryMoved(java.lang.Object data,
                      commonj.sdo.DataObject businessObject,
                      java.lang.String propertyPath,
                      int newIndex)
Create a List Entry Moved annotation in the Change Summary for
 Object in the property represented by the combination of the
 Business Object and the property path.
Parameters:data - The object in the listbusinessObject - The Business Object used in combination with
 the property path to reference the propertypropertyPath - The property path used in combination with the
 Business Object to reference the propertynewIndex - The new index of the item in the list
    - markSimpleTypeCreated
void markSimpleTypeCreated(java.lang.Object o,
                         commonj.sdo.DataObject businessObject,
                         java.lang.String propertyPath)
Marks a simple type object as Created.
Parameters:data - The object to mark as CreatedbusinessObject - The Business Object used in combination with
 the property path to reference the propertypropertyPath - The property path used in combination with the
 Business Object to reference the property
    - markSimpleTypeDeleted
void markSimpleTypeDeleted(java.lang.Object o,
                         commonj.sdo.DataObject businessObject,
                         java.lang.String propertyPath)
Marks a simple type object as Deleted.
Parameters:data - The object to mark as DeletedbusinessObject - The Business Object used in combination with
 the property path to reference the propertypropertyPath - The property path used in combination with the
 Business Object to reference the property