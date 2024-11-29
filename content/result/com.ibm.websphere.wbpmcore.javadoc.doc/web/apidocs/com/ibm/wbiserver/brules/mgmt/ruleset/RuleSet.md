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

## Interface RuleSet

- All Superinterfaces:
BusinessRule, BusinessRuleChangeDetector, BusinessRuleValidateable, java.io.Serializable

public interface RuleSet
extends BusinessRule
This interface represents a ruleset.  A ruleset consists of a rule block and 0 or more rule
 templates.  The rule block contains the rule instances (both hard-coded and teamplatized)
 that are executed at runtime to perform the ruleset's function.  The rule templates, if 
 any, are used to create rule instances whose parameters can be changed at runtime.  
 These new rule instances can be added to the rule block for this ruleset.
 
 A new ruleset based on this one can be created using the createCopy method.
 The new ruleset is automatically added to the list of available targets for the operation
 that this ruleset is associated with.  It can then be added as a default target or a date-qualified
 target for the operation.

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT
    - Method Summary Methods Modifier and Type Method and Description RuleBlock getFirstRuleBlock () Get the first rule block within this ruleset. java.util.List<RuleBlock > getRuleBlocks () Get all rule blocks contained within this ruleset. java.util.List<RuleSetRuleTemplate > getRuleTemplates () Get all rule templates contained within this ruleset.

### Method Summary

| Modifier and Type                   | Method and Description                                                   |
|-------------------------------------|--------------------------------------------------------------------------|
| RuleBlock                           | getFirstRuleBlock() Get the first rule block within this ruleset.        |
| java.util.List<RuleBlock>           | getRuleBlocks() Get all rule blocks contained within this ruleset.       |
| java.util.List<RuleSetRuleTemplate> | getRuleTemplates() Get all rule templates contained within this ruleset. |

- Methods inherited from interface com.ibm.wbiserver.brules.mgmt.BusinessRule
createCopy, getAssociatedOperation, getDescription, getDisplayName, getName, getProperties, getProperty, getPropertyValue, getRuntimeID, getSaveDate, getTargetNameSpace, getType, isDisplayNameSynchronizedToName, setDescription, setDisplayName, setDisplayNameIsSynchronizedToName, setPropertyValue

- Methods inherited from interface com.ibm.wbiserver.brules.mgmt.BusinessRuleValidateable
validate

- Methods inherited from interface com.ibm.wbiserver.brules.mgmt.BusinessRuleChangeDetector
hasChanges