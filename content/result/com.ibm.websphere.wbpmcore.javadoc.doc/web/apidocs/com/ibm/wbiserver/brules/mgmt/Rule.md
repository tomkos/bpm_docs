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

## Interface Rule

- All Superinterfaces:
BusinessRuleChangeDetector, BusinessRuleValidateable, java.io.Serializable

All Known Subinterfaces:
DecisionTableRule, DecisionTableTemplateInstanceRule, RuleSetRule, RuleSetTemplateInstanceRule, TemplateInstanceRule

public interface Rule
extends BusinessRuleValidateable, BusinessRuleChangeDetector, java.io.Serializable
This interface represents one rule within either a ruleset or a decision table.  The rule may 
 be a hard-coded rule or may be a rule instance created from a rule template.  A hard-coded rule 
 is represented by an instance of this interface; there is no sub-interface for a hard-coded 
 rule.  A rule that was created from a template is represented by an instance of 
 TemplateInstanceRule.
 
 A rule has a name and a user presentation string.  The user presentation string specifies
 how the rule should be presented to the end user.

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT
    - Method Summary Methods Modifier and Type Method and Description java.lang.String getDescription () Get the description associated with this rule. java.lang.String getDisplayName () Get the display name for this rule. java.lang.String getExpandedUserPresentation () Get the user presentation for this rule with any placeholders for template parameters filled in with the actual value of the parameter. java.lang.String getName () Get the name of this rule. java.lang.String getUserPresentation () Get the user presentation for this rule. boolean isDisplayNameSynchronizedToName () Check to see if the display name is synchronized to the name for this rule. void setDescription (java.lang.String newDescription) Set the description associated with this rule. void setDisplayName (java.lang.String newDisplayName) Set the display name for this rule. void setDisplayNameIsSynchronizedToName (boolean newDisplayNameIsSynchronizedToName) Change the value of the flag that determines whether or not the display name is synchronized to the name for this rule.

### Method Summary

| Modifier and Type   | Method and Description                                                                                                                                                                                  |
|---------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| java.lang.String    | getDescription() Get the description associated with this rule.                                                                                                                                         |
| java.lang.String    | getDisplayName() Get the display name for this rule.                                                                                                                                                    |
| java.lang.String    | getExpandedUserPresentation() Get the user presentation for this rule with any placeholders for template parameters  filled in with the actual value of the parameter.                                  |
| java.lang.String    | getName() Get the name of this rule.                                                                                                                                                                    |
| java.lang.String    | getUserPresentation() Get the user presentation for this rule.                                                                                                                                          |
| boolean             | isDisplayNameSynchronizedToName() Check to see if the display name is synchronized to the name for this rule.                                                                                           |
| void                | setDescription(java.lang.String newDescription) Set the description associated with this rule.                                                                                                          |
| void                | setDisplayName(java.lang.String newDisplayName) Set the display name for this rule.                                                                                                                     |
| void                | setDisplayNameIsSynchronizedToName(boolean newDisplayNameIsSynchronizedToName) Change the value of the flag that determines whether or not the display name is  synchronized to the name for this rule. |

- Methods inherited from interface com.ibm.wbiserver.brules.mgmt.BusinessRuleValidateable
validate

- Methods inherited from interface com.ibm.wbiserver.brules.mgmt.BusinessRuleChangeDetector
hasChanges