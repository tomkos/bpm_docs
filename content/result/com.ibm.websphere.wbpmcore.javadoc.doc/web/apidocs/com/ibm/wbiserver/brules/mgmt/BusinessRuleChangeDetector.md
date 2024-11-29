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

## Interface BusinessRuleChangeDetector

- All Known Subinterfaces:
ActionNode, BusinessRule, BusinessRuleGroup, CaseEdge, ConditionNode, DecisionTable, DecisionTableRule, DecisionTableTemplateInstanceRule, Operation, OperationSelectionRecord, OperationSelectionRecordList, ParameterValue, Property, PropertyList, Rule, RuleBlock, RuleSet, RuleSetRule, RuleSetTemplateInstanceRule, SystemDefinedProperty, TemplateInstanceExpression, TemplateInstanceRule, TreeAction, TreeBlock, TreeNode, UserDefinedProperty

public interface BusinessRuleChangeDetector
This interface defines methods related to detecting whether or not changes have been
 made to an object or to any object that can be reached from it.

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

boolean
hasChanges()
Determine whether or not any changes have been made to this object or any object
 reachable from it since the last publish.

- ============ FIELD DETAIL =========== ============ METHOD DETAIL ==========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
See Also:Constant Field Values

- Method Detail

### Method Detail

    - hasChanges
boolean hasChanges()
Determine whether or not any changes have been made to this object or any object
 reachable from it since the last publish.
Returns:true if a change has been made to this object or any object that can be 
 reached from it; otherwise false.