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

## Interface BusinessRuleValidateable

- All Known Subinterfaces:
ActionNode, BusinessRule, BusinessRuleGroup, CaseEdge, ConditionNode, DecisionTable, DecisionTableRule, DecisionTableTemplateInstanceRule, Operation, OperationSelectionRecord, OperationSelectionRecordList, ParameterValue, Rule, RuleBlock, RuleSet, RuleSetRule, RuleSetTemplateInstanceRule, TemplateInstanceExpression, TemplateInstanceRule, TreeAction, TreeBlock, TreeNode

public interface BusinessRuleValidateable
This interface defines methods related to validating an object and any objects that can
 be reached from it.

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

java.util.List<Problem>
validate()
Validate this object and all sub-objects that are reachable from it.

- ============ FIELD DETAIL =========== ============ METHOD DETAIL ==========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
See Also:Constant Field Values

- Method Detail

### Method Detail

    - validate
java.util.List<Problem> validate()
Validate this object and all sub-objects that are reachable from it.  A
 List of Problem objects is returned showing any errors found.
 If no errors are found, then a zero-length List is returned.
Returns:A List of validation errors for this object.  If no errors are
 found, a zero-length List is returned.