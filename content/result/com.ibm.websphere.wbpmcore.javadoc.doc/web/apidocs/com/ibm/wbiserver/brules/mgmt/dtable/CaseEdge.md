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

## Interface CaseEdge

- All Superinterfaces:
BusinessRuleChangeDetector, BusinessRuleValidateable, java.io.Serializable

public interface CaseEdge
extends BusinessRuleValidateable, BusinessRuleChangeDetector, java.io.Serializable
This interface represents a particular case (value) for a condition node.  For example, consider a 
 condition node that has a condition term of "mortgageValue".  This condition node could have
 the following three case edges "< 100000", ">= 100000 and < 500000", and ">= 500000", 
 representing the cases where the mortgage value falls within the specified range.  Each case
 edge must always be interpreted within the context of its containing condition node.  A case
 edge can be thought of as the lines connecting a parent tree node to it children in the 
 decision tree.
 
 A CaseEdge itself cannot be changed.  The value definition associated with
 the case edge may be changed if it is based on a template.  Use the 
 getValueDefinition method on this class to get the
 associated value definition.  If the returned TreeConditionValueDefinition
 contains a template instance, then the template instance can be changed by changing the
 parameter values associated with it.  The TreeConditionValueDefinition can
 also be changed to use a different template instance to define its value.

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT
    - Method Summary Methods Modifier and Type Method and Description java.util.List<TreeConditionValueTemplate > getAvailableValueTemplates () Get the value templates available for use by this condition value. TreeNode getChildNode () Get the child node of this case edge. ConditionNode getContainingConditionNode () Get the condition node that contains this case edge. java.lang.String getUserPresentation () Get the user presentation string for this case edge. TreeConditionValueDefinition getValueDefinition () Get the value definition associated with this case edge. TemplateInstanceExpression getValueTemplateInstance () Get the template instance defining the value for this case edge. void setValueTemplateInstance (TemplateInstanceExpression valueTemplateInstance) Set the template instance defining the value for this case edge.

### Method Summary

| Modifier and Type                          | Method and Description                                                                                                                      |
|--------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| java.util.List<TreeConditionValueTemplate> | getAvailableValueTemplates() Get the value templates available for use by this condition value.                                             |
| TreeNode                                   | getChildNode() Get the child node of this case edge.                                                                                        |
| ConditionNode                              | getContainingConditionNode() Get the condition node that contains this case edge.                                                           |
| java.lang.String                           | getUserPresentation() Get the user presentation string for this case edge.                                                                  |
| TreeConditionValueDefinition               | getValueDefinition() Get the value definition associated with this case edge.                                                               |
| TemplateInstanceExpression                 | getValueTemplateInstance() Get the template instance defining the value for this case edge.                                                 |
| void                                       | setValueTemplateInstance(TemplateInstanceExpression valueTemplateInstance) Set the template instance defining the value for this case edge. |

- Methods inherited from interface com.ibm.wbiserver.brules.mgmt.BusinessRuleValidateable
validate

- Methods inherited from interface com.ibm.wbiserver.brules.mgmt.BusinessRuleChangeDetector
hasChanges