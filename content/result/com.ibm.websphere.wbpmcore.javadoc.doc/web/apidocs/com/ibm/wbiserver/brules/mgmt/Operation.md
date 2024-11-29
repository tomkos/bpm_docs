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

## Interface Operation

- All Superinterfaces:
BusinessRuleChangeDetector, BusinessRuleValidateable, java.io.Serializable

public interface Operation
extends BusinessRuleValidateable, BusinessRuleChangeDetector, java.io.Serializable
An object implementing this interface represents an operation of a business rule group.  
 An operation can have one or more potential targets.  Which target is invoked when the 
 operation is invoked is determined by a selection algorithm based on date.  Each target is 
 a business rule, which can be either a ruleset or a decision table.  There can be one 
 default business rule target that is invoked if no other targets are found.  There can also 
 be 0 or more business rule targets that are selected based on date/time.  Each of these 
 targets has a date range associated with it.  If the date in question falls within the 
 specified date range for the target, then that target business rule is invoked.  Each of 
 these targets is represented by an OperationSelectionRecord object associated 
 with the Operation.  Methods are provided to make changes to all of these 
 possible targets.
 
 An Operation also has an available targets list.  This is a list of all
 business rules that are valid targets for this operation.  The available targets list is a 
 superset of the set of targets that are specified as either the default or with an
 associated date range.  This means that there can be business rules in the available targets
 list that are not currently specified as a target.  The available targets list cannot be
 updated directly.  The only way to change the available targets list is to create a new
 business rule by copying an existing one.  The new business rule is implicitly adding to the
 appropriate available targets list.

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT
    - Method Summary Methods Modifier and Type Method and Description BusinessRuleGroup getAssociatedBusinessRuleGroup () Get the business rule group that this operation is associated with. java.util.List<BusinessRule > getAvailableTargets () Get the list of available target business rules for this operation. java.util.List<BusinessRule > getBusinessRulesByName (java.lang.String name, QueryOperator op, int numberToSkip, int maxToReturn) Get business rules associated with the operation using the name as a key. java.util.List<BusinessRule > getBusinessRulesByTNS (java.lang.String tns, QueryOperator op, int numberToSkip, int maxToReturn) Get business rules for this operation that have the specified target name space. java.util.List<BusinessRule > getBusinessRulesByTNSAndName (java.lang.String tns, QueryOperator tnsOp, java.lang.String name, QueryOperator nameOp, int numberToSkip, int maxToReturn) Get business rules associated with this operation using the target name space and name as a key. BusinessRule getDefaultBusinessRule () Get the default business rule for this operation. java.lang.String getDescription () Get the description of the operation. java.lang.String getName () Get the name of the operation. OperationSelectionRecordList getOperationSelectionRecordList () Get the selection records associated with this operation. void setDefaultBusinessRule (BusinessRule newDefaultBusinessRule) Set the default business rule for this operation.

### Method Summary

| Modifier and Type            | Method and Description                                                                                                                                                                                                                                                                                                                                                                                 |
|------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| BusinessRuleGroup            | getAssociatedBusinessRuleGroup() Get the business rule group that this operation is associated with.                                                                                                                                                                                                                                                                                                   |
| java.util.List<BusinessRule> | getAvailableTargets() Get the list of available target business rules for this operation.                                                                                                                                                                                                                                                                                                              |
| java.util.List<BusinessRule> | getBusinessRulesByName(java.lang.String name,                       QueryOperator op,                       int numberToSkip,                       int maxToReturn) Get business rules associated with the operation using the name as a key.                                                                                                                                                         |
| java.util.List<BusinessRule> | getBusinessRulesByTNS(java.lang.String tns,                      QueryOperator op,                      int numberToSkip,                      int maxToReturn) Get business rules for this operation that have the specified target name space.                                                                                                                                                       |
| java.util.List<BusinessRule> | getBusinessRulesByTNSAndName(java.lang.String tns,                             QueryOperator tnsOp,                             java.lang.String name,                             QueryOperator nameOp,                             int numberToSkip,                             int maxToReturn) Get business rules associated with this operation using the target name space and name as   a key. |
| BusinessRule                 | getDefaultBusinessRule() Get the default business rule for this operation.                                                                                                                                                                                                                                                                                                                             |
| java.lang.String             | getDescription() Get the description of the operation.                                                                                                                                                                                                                                                                                                                                                 |
| java.lang.String             | getName() Get the name of the operation.                                                                                                                                                                                                                                                                                                                                                               |
| OperationSelectionRecordList | getOperationSelectionRecordList() Get the selection records associated with this operation.                                                                                                                                                                                                                                                                                                            |
| void                         | setDefaultBusinessRule(BusinessRule newDefaultBusinessRule) Set the default business rule for this operation.                                                                                                                                                                                                                                                                                          |

- Methods inherited from interface com.ibm.wbiserver.brules.mgmt.BusinessRuleValidateable
validate

- Methods inherited from interface com.ibm.wbiserver.brules.mgmt.BusinessRuleChangeDetector
hasChanges