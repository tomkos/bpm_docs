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

## Interface BusinessRule

- All Superinterfaces:
BusinessRuleChangeDetector, BusinessRuleValidateable, java.io.Serializable

All Known Subinterfaces:
DecisionTable, RuleSet

public interface BusinessRule
extends BusinessRuleValidateable, BusinessRuleChangeDetector, java.io.Serializable
This interface represents a business rule, which can be either a ruleset or a 
 decision table.  New business rules can be created by creating a copy of an existing
 business rule using the createCopy method.  This is the only way to create
 a new business rule using the API.

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT
    - Method Summary Methods Modifier and Type Method and Description BusinessRule createCopy (java.lang.String newTargetNameSpace, java.lang.String newName) Create a copy of this BusinessRule with a new name. Operation getAssociatedOperation () Get the Operation for which this business rule is defined. java.lang.String getDescription () Get the description associated with this business rule. java.lang.String getDisplayName () Get the display name for this business rule. java.lang.String getName () Get the name of the business rule. PropertyList getProperties () Get the list of properties associated with this business rule. Property getProperty (java.lang.String name) Get the property on this business rule that has the specified name. java.lang.String getPropertyValue (java.lang.String name) Get the value of the property on this business rule that has the specified name. java.lang.String getRuntimeID () Returns a globally unique ID for the business rule. java.util.Date getSaveDate () Get the date and time that the information in this copy of the business rule was saved to persistent storage. java.lang.String getTargetNameSpace () Get the target name space of the business rule. BusinessRuleType getType () Get the type of this business rule. boolean isDisplayNameSynchronizedToName () Check to see if the display name is synchronized to the name for this business rule. void setDescription (java.lang.String newDescription) Set the description associated with this business rule. void setDisplayName (java.lang.String newDisplayName) Set the display name for this business rule. void setDisplayNameIsSynchronizedToName (boolean newDisplayNameIsSynchronizedToName) Change the value of the flag that determines whether or not the display name is synchronized to the name for this business rule. void setPropertyValue (java.lang.String name, java.lang.String value) Set the value of the property with the specified name to the specified value.

### Method Summary

| Modifier and Type   | Method and Description                                                                                                                                                                                           |
|---------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| BusinessRule        | createCopy(java.lang.String newTargetNameSpace,           java.lang.String newName) Create a copy of this BusinessRule with a new name.                                                                          |
| Operation           | getAssociatedOperation() Get the Operation for which this business rule is defined.                                                                                                                              |
| java.lang.String    | getDescription() Get the description associated with this business rule.                                                                                                                                         |
| java.lang.String    | getDisplayName() Get the display name for this business rule.                                                                                                                                                    |
| java.lang.String    | getName() Get the name of the business rule.                                                                                                                                                                     |
| PropertyList        | getProperties() Get the list of properties associated with this business rule.                                                                                                                                   |
| Property            | getProperty(java.lang.String name) Get the property on this business rule that has the specified name.                                                                                                           |
| java.lang.String    | getPropertyValue(java.lang.String name) Get the value of the property on this business rule that has the specified name.                                                                                         |
| java.lang.String    | getRuntimeID() Returns a globally unique ID for the business rule.                                                                                                                                               |
| java.util.Date      | getSaveDate() Get the date and time that the information in this copy of the business rule  was saved to persistent storage.                                                                                     |
| java.lang.String    | getTargetNameSpace() Get the target name space of the business rule.                                                                                                                                             |
| BusinessRuleType    | getType() Get the type of this business rule.                                                                                                                                                                    |
| boolean             | isDisplayNameSynchronizedToName() Check to see if the display name is synchronized to the name for this business rule.                                                                                           |
| void                | setDescription(java.lang.String newDescription) Set the description associated with this business rule.                                                                                                          |
| void                | setDisplayName(java.lang.String newDisplayName) Set the display name for this business rule.                                                                                                                     |
| void                | setDisplayNameIsSynchronizedToName(boolean newDisplayNameIsSynchronizedToName) Change the value of the flag that determines whether or not the display name is  synchronized to the name for this business rule. |
| void                | setPropertyValue(java.lang.String name,                 java.lang.String value) Set the value of the property with the specified name to the specified value.                                                    |

- Methods inherited from interface com.ibm.wbiserver.brules.mgmt.BusinessRuleValidateable
validate

- Methods inherited from interface com.ibm.wbiserver.brules.mgmt.BusinessRuleChangeDetector
hasChanges