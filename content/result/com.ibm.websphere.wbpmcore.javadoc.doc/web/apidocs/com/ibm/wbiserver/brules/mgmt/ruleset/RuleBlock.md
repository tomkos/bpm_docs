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

## Interface RuleBlock

- All Superinterfaces:
BusinessRuleChangeDetector, BusinessRuleValidateable, java.lang.Iterable<RuleSetRule>, java.io.Serializable

public interface RuleBlock
extends BusinessRuleValidateable, BusinessRuleChangeDetector, java.io.Serializable, java.lang.Iterable<RuleSetRule>
This interface represents a rule block within a ruleset.  A rule block contains a list of rules
 that are executed at runtime to perform the function of the rule block.  The order of the
 rules in the list determines the order in which they are executed.  Each rule is either a
 hard-coded rule or is a rule that was created based on a rule template.  Hard-coded rules
 cannot be changed, added, or removed by this API.  They can, however, be reordered using  
 either the moveUp, moveDown, or move methods.  Rules 
 created from a rule template (template instance rules) can be reordered, just like hard-coded 
 rules.  They can also be created, added to the rule block, and removed from the rule block.  
 The removeRule method can be used to remove a given template instance rule from 
 the rule block.  To add a new template instance rule, first create a rule based on the 
 template using the 
 createRuleFromTemplate
 method on the RuleTemplate class and then add it to the rule block using one of 
 the addRule methods.

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT
    - Method Summary Methods Modifier and Type Method and Description void addRule (int index, RuleSetTemplateInstanceRule newRule) Insert the specified rule at the specified index in the list of rules in this rule block. void addRule (RuleSetTemplateInstanceRule newRule) Add the specified rule to the end of the list of rules in this rule block. RuleSet getParentRuleSet () Get the ruleset that contains this rule block. RuleSetRule getRule (int index) Get the rule at the specified index in the list of rules for this rule block. java.util.Iterator<RuleSetRule > iterator () Get an iterator over the list of rules in this rule block. void move (RuleSetRule ruleToMove, int newIndex) Move the specified rule to the specified index in the list of rules for this rule block. void moveDown (RuleSetRule ruleToMove) Move the specified rule down in the list of rules for this rule block. void moveUp (RuleSetRule ruleToMove) Move the specified rule up in the list of rules for this rule block. int numberOfRules () Get the number of rules in this rule block. boolean removeRule (RuleSetTemplateInstanceRule rule) Remove the specified rule from the list of rules in this rule block.

### Method Summary

| Modifier and Type               | Method and Description                                                                                                                                   |
|---------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| void                            | addRule(int index,        RuleSetTemplateInstanceRule newRule) Insert the specified rule at the specified index in the list of rules in this rule block. |
| void                            | addRule(RuleSetTemplateInstanceRule newRule) Add the specified rule to the end of the list of rules in this rule block.                                  |
| RuleSet                         | getParentRuleSet() Get the ruleset that contains this rule block.                                                                                        |
| RuleSetRule                     | getRule(int index) Get the rule at the specified index in the list of rules for this rule block.                                                         |
| java.util.Iterator<RuleSetRule> | iterator() Get an iterator over the list of rules in this rule block.                                                                                    |
| void                            | move(RuleSetRule ruleToMove,     int newIndex) Move the specified rule to the specified index in the list of rules for this rule  block.                 |
| void                            | moveDown(RuleSetRule ruleToMove) Move the specified rule down in the list of rules for this rule block.                                                  |
| void                            | moveUp(RuleSetRule ruleToMove) Move the specified rule up in the list of rules for this rule block.                                                      |
| int                             | numberOfRules() Get the number of rules in this rule block.                                                                                              |
| boolean                         | removeRule(RuleSetTemplateInstanceRule rule) Remove the specified rule from the list of rules in this rule block.                                        |

- Methods inherited from interface com.ibm.wbiserver.brules.mgmt.BusinessRuleValidateable
validate

- Methods inherited from interface com.ibm.wbiserver.brules.mgmt.BusinessRuleChangeDetector
hasChanges