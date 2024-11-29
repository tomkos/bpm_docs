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

## Interface OperationSelectionRecordList

- All Superinterfaces:
BusinessRuleChangeDetector, BusinessRuleValidateable, java.lang.Iterable<OperationSelectionRecord>, java.io.Serializable

public interface OperationSelectionRecordList
extends BusinessRuleValidateable, BusinessRuleChangeDetector, java.io.Serializable, java.lang.Iterable<OperationSelectionRecord>
This interface represents a list of operation selection records.  Specific methods are provided for
 getting an iterator to iterate through the list and to add and remove elements from the list.
 In order to change an existing OperationSelectionRecord in the list, use
 an iterator obtained using the iterator method to get the object to be changed
 and then simply use set methods to change the object.

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT
    - Method Summary Methods Modifier and Type Method and Description void addOperationSelectionRecord (OperationSelectionRecord newSelectionRecord) Add the specified operation selection record to the list. OperationSelectionRecord get (int index) Get the OperationSelectionRecord at the specified index in the list. boolean isEmpty () Determine whether or not this list is empty. java.util.Iterator<OperationSelectionRecord > iterator () Get an iterator over this list. OperationSelectionRecord newOperationSelectionRecord () Create a new OperationSelectionRecord object that is associated with the operation containing this operation selection record list. OperationSelectionRecord newOperationSelectionRecord (java.util.Date startDate, java.util.Date endDate, BusinessRule businessRuleTarget) Create a new OperationSelectionRecord object that is associated with the operation containing this operation selection record list. boolean removeOperationSelectionRecord (OperationSelectionRecord selectionRecord) Remove the specified operation selection record from the list. int size () Get the number of operation selection records in this list.

### Method Summary

| Modifier and Type                            | Method and Description                                                                                                                                                                                                                                                                                    |
|----------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| void                                         | addOperationSelectionRecord(OperationSelectionRecord newSelectionRecord) Add the specified operation selection record to the list.                                                                                                                                                                        |
| OperationSelectionRecord                     | get(int index) Get the OperationSelectionRecord at the specified index in the list.                                                                                                                                                                                                                       |
| boolean                                      | isEmpty() Determine whether or not this list is empty.                                                                                                                                                                                                                                                    |
| java.util.Iterator<OperationSelectionRecord> | iterator() Get an iterator over this list.                                                                                                                                                                                                                                                                |
| OperationSelectionRecord                     | newOperationSelectionRecord() Create a new OperationSelectionRecord object that is associated with the  operation containing this operation selection record list.                                                                                                                                        |
| OperationSelectionRecord                     | newOperationSelectionRecord(java.util.Date startDate,                            java.util.Date endDate,                            BusinessRule businessRuleTarget) Create a new OperationSelectionRecord object that is associated with the  operation containing this operation selection record list. |
| boolean                                      | removeOperationSelectionRecord(OperationSelectionRecord selectionRecord) Remove the specified operation selection record from the list.                                                                                                                                                                   |
| int                                          | size() Get the number of operation selection records in this list.                                                                                                                                                                                                                                        |

- Methods inherited from interface com.ibm.wbiserver.brules.mgmt.BusinessRuleValidateable
validate

- Methods inherited from interface com.ibm.wbiserver.brules.mgmt.BusinessRuleChangeDetector
hasChanges