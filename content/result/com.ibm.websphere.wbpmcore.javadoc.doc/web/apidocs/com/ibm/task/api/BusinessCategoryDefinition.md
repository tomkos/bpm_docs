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

## Interface BusinessCategoryDefinition

- All Superinterfaces:
java.io.Serializable

public interface BusinessCategoryDefinition
extends java.io.Serializable
Accesses and sets the properties of a business category definition.
 A business category definition is used to create or update a persistently stored business category.
 
Since:
6.2.0.3

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT 

static java.lang.String
DEFAULT\_CONTAINER\_JNDI\_NAME\_OF\_STAFF\_PLUGIN\_PROVIDER
States the default value for getJNDINameOfStaffPluginProvider.

static int
SUBSTITUTION\_POLICY\_NO\_SUBSTITUTION
States that no substitution should take place.

static int
SUBSTITUTION\_POLICY\_SELECT\_USER\_IF\_PRESENT
States that only present users should act for absent users.

static int
SUBSTITUTION\_POLICY\_SUBSTITUTE\_IF\_ABSENT
States that substitutes should act for absent users.
    - Method Summary

Methods 

Modifier and Type
Method and Description

java.lang.String
getCustomText1()
Returns the custom text specified as custom text one.

java.lang.String
getCustomText2()
Returns the custom text specified as custom text two.

java.lang.String
getCustomText3()
Returns the custom text specified as custom text three.

java.lang.String
getCustomText4()
Returns the custom text specified as custom text four.

java.lang.String
getCustomText5()
Returns the custom text specified as custom text five.

java.lang.String
getCustomText6()
Returns the custom text specified as custom text six.

java.lang.String
getCustomText7()
Returns the custom text specified as custom text seven.

java.lang.String
getCustomText8()
Returns the custom text specified as custom text eight.

java.lang.String
getDefaultQueryTable()
Returns the name of the default query table associated to the business category.

java.lang.String
getDescription(java.util.Locale arg0)
Returns the description in the specified locale.

java.lang.String
getDisplayName(java.util.Locale arg0)
Returns the display name in the specified locale.

java.lang.String
getJNDINameOfStaffPluginProvider()
Returns the JNDI name of a user-defined people directory configuration.

java.util.List
getLocalesOfDescriptions()
Returns the locales of all descriptions.

java.util.List
getLocalesOfDisplayNames()
Returns the locales of all display names.

java.lang.String
getName()
Returns the name of the business category.

BCID
getParentID()
Returns the object ID of the parent business category if the business category
 is part of a hierarchy.

PeopleAssignment
getPeopleAssignment(int arg0)
Returns the staff assignments for the passed role.

java.lang.Integer
getPriority()
Returns the priority of the business category.

java.util.List
getReasonsOfPeopleAssignment()
Returns a list of Integer objects that state the assignment reasons.

int
getSubstitutionPolicy()
Returns the substitution policy that takes place when people assignments are performed.

boolean
isCustomText1Updateable()
Signals whether the custom text 1 property can be changed for the kind and current state of the object.

boolean
isCustomText2Updateable()
Signals whether the custom text 2 property can be changed for the kind and current state of the object.

boolean
isCustomText3Updateable()
Signals whether the custom text 3 property can be changed for the kind and current state of the object.

boolean
isCustomText4Updateable()
Signals whether the custom text 4 property can be changed for the kind and current state of the object.

boolean
isCustomText5Updateable()
Signals whether the custom text 5 property can be changed for the kind and current state of the object.

boolean
isCustomText6Updateable()
Signals whether the custom text 6 property can be changed for the kind and current state of the object.

boolean
isCustomText7Updateable()
Signals whether the custom text 7 property can be changed for the kind and current state of the object.

boolean
isCustomText8Updateable()
Signals whether the custom text 8 property can be changed for the kind and current state of the object.

boolean
isDefaultQueryTableUpdateable()
Signals whether the default query table property can be changed for the kind and current state of the object.

boolean
isDescriptionUpdateable()
Signals whether the description property can be changed for the kind and current state of the object.

boolean
isDisplayNameUpdateable()
Signals whether the display name property can be changed for the kind and current state of the object.

boolean
isJNDINameOfStaffPluginProviderUpdateable()
Signals whether the jndi name staff provider property can be changed for the kind and current state of the object.

boolean
isPeopleAssignmentUpdateable()
Signals whether the custom text 8 property can be changed for the kind and current state of the object.

boolean
isPriorityUpdateable()
Signals whether the priority property can be changed for the kind and current state of the object.

boolean
isSubstitutionPolicyUpdateable()
Signals whether the substitution policy property can be changed for the kind and current state of the object.

void
setCustomText1(java.lang.String customText1)
Sets the custom text specified as custom text one.

void
setCustomText2(java.lang.String customText2)
Sets the custom text specified as custom text two.

void
setCustomText3(java.lang.String customText3)
Sets the custom text specified as custom text three.

void
setCustomText4(java.lang.String customText4)
Sets the custom text specified as custom text four.

void
setCustomText5(java.lang.String customText5)
Sets the custom text specified as custom text five.

void
setCustomText6(java.lang.String customText6)
Sets the custom text specified as custom text six.

void
setCustomText7(java.lang.String customText7)
Sets the custom text specified as custom text seven.

void
setCustomText8(java.lang.String customText8)
Sets the custom text specified as custom text eight.

void
setDefaultQueryTable(java.lang.String defaultQueryTable)
Sets the default query table associated to the business category.

void
setDescription(java.lang.String description,
              java.util.Locale locale)
Sets the description in the specified locale.

void
setDisplayName(java.lang.String displayName,
              java.util.Locale locale)
Sets the display name in the specified locale.

void
setJNDINameOfStaffPluginProvider(java.lang.String jndiNameStaffProvider)
Sets the JNDI name of a user-defined people directory configuration.

void
setPeopleAssignment(int assignmentReason,
                   PeopleAssignment people)
Sets the assignment reason for the specified people.

void
setPriority(java.lang.Integer priority)
Sets the priority of the business category.

void
setSubstitutionPolicy(int substitutionPolicy)
Sets the substitution policy that takes place when people assignments are performed.

- ============ FIELD DETAIL =========== ============ METHOD DETAIL ==========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
See Also:Constant Field Values

- DEFAULT\_CONTAINER\_JNDI\_NAME\_OF\_STAFF\_PLUGIN\_PROVIDER
static final java.lang.String DEFAULT\_CONTAINER\_JNDI\_NAME\_OF\_STAFF\_PLUGIN\_PROVIDER
States the default value for getJNDINameOfStaffPluginProvider.
See Also:Constant Field Values

- SUBSTITUTION\_POLICY\_SELECT\_USER\_IF\_PRESENT
static final int SUBSTITUTION\_POLICY\_SELECT\_USER\_IF\_PRESENT
States that only present users should act for absent users.
 If all users and their subsitutes are absent or excluded by people assignment criteria,
 users originally resolved are returned.
See Also:Constant Field Values

- SUBSTITUTION\_POLICY\_NO\_SUBSTITUTION
static final int SUBSTITUTION\_POLICY\_NO\_SUBSTITUTION
States that no substitution should take place.
 All users resolved by people assignment criteria are returned.
See Also:Constant Field Values

- SUBSTITUTION\_POLICY\_SUBSTITUTE\_IF\_ABSENT
static final int SUBSTITUTION\_POLICY\_SUBSTITUTE\_IF\_ABSENT
States that substitutes should act for absent users.
 If all substitutes are absent or explicitely excluded by people assignment criteria,
 default people assignments are performed, for example, task administrators become potential owners.
See Also:Constant Field Values

- Method Detail

### Method Detail

    - getName
java.lang.String getName()
Returns the name of the business category.
    - getParentID
BCID getParentID()
Returns the object ID of the parent business category if the business category
 is part of a hierarchy. Returns null if there is no parent.
    - getPriority
java.lang.Integer getPriority()
Returns the priority of the business category.
    - getDisplayName
java.lang.String getDisplayName(java.util.Locale arg0)
Returns the display name in the specified locale.
 Returns the display name in the default locale when a display name in
 the specified locale is not found.
 
 If no locale is specified, the display name in the default locale is returned
 or any available display name, if there is only a single display name.
 
Parameters:arg0 - The locale for which the display name is to be provided.
    - getLocalesOfDisplayNames
java.util.List getLocalesOfDisplayNames()
Returns the locales of all display names.
 Returns an empty list when there are no display names.
    - getDescription
java.lang.String getDescription(java.util.Locale arg0)
Returns the description in the specified locale.
 Returns the description in the default locale when a description in
 the specified locale is not found.
 
 If no locale is specified, the description in the default locale is returned
 or any available description, if there is only a single description.
 
Parameters:arg0 - The locale for which the description is to be provided.
    - getLocalesOfDescriptions
java.util.List getLocalesOfDescriptions()
Returns the locales of all descriptions.
 Returns an empty list when there are no descriptions.
    - getDefaultQueryTable
java.lang.String getDefaultQueryTable()
Returns the name of the default query table associated to the business category.
 Returns null if no query table is associated.
    - getJNDINameOfStaffPluginProvider
java.lang.String getJNDINameOfStaffPluginProvider()
Returns the JNDI name of a user-defined people directory configuration.
    - getSubstitutionPolicy
int getSubstitutionPolicy()
Returns the substitution policy that takes place when people assignments are performed.
 
 Possible substitution policies are SUBSTITUTION\_POLICY\_NO\_SUBSTITUTION, SUBSTITUTION\_POLICY\_SUBSTITUTE\_IF\_ABSENT,
 SUBSTITUTION\_POLICY\_SELECT\_USER\_IF\_PRESENT.
    - getCustomText1
java.lang.String getCustomText1()
Returns the custom text specified as custom text one.
 Returns null if not specified.
    - getCustomText2
java.lang.String getCustomText2()
Returns the custom text specified as custom text two.
 Returns null if not specified.
    - getCustomText3
java.lang.String getCustomText3()
Returns the custom text specified as custom text three.
 Returns null if not specified.
    - getCustomText4
java.lang.String getCustomText4()
Returns the custom text specified as custom text four.
 Returns null if not specified.
    - getCustomText5
java.lang.String getCustomText5()
Returns the custom text specified as custom text five.
 Returns null if not specified.
    - getCustomText6
java.lang.String getCustomText6()
Returns the custom text specified as custom text six.
 Returns null if not specified.
    - getCustomText7
java.lang.String getCustomText7()
Returns the custom text specified as custom text seven.
 Returns null if not specified.
    - getCustomText8
java.lang.String getCustomText8()
Returns the custom text specified as custom text eight.
 Returns null if not specified.
    - getPeopleAssignment
PeopleAssignment getPeopleAssignment(int arg0)
Returns the staff assignments for the passed role. Possible roles are:
 WorkItem.REASON\_READER.
 
Parameters:arg0 - The role for which the people assignment is to be provided.
    - getReasonsOfPeopleAssignment
java.util.List getReasonsOfPeopleAssignment()
Returns a list of Integer objects that state the assignment reasons.
 Returns an empty list when there are no people assignments.
    - setPriority
void setPriority(java.lang.Integer priority)
Sets the priority of the business category. No special meaning is associated
 with this property. But a caller can, for example, use it
 for sorting a list of business categories.
 
Parameters:priority - The priority of the business category. The priority must be a non-negative number.
 It can be null in order to be reset.
    - isPriorityUpdateable
boolean isPriorityUpdateable()
Signals whether the priority property can be changed for the kind and current state of the object.
    - setDisplayName
void setDisplayName(java.lang.String displayName,
                  java.util.Locale locale)
Sets the display name in the specified locale.
 
Parameters:displayName - The new value of the display name.locale - The locale for which the display name is set.
 Note that there is a special locale called default which can be used to set
 the display name in the default language. The default language is specified
 by passing null or new Locale("default").
    - isDisplayNameUpdateable
boolean isDisplayNameUpdateable()
Signals whether the display name property can be changed for the kind and current state of the object.
    - setDescription
void setDescription(java.lang.String description,
                  java.util.Locale locale)
Sets the description in the specified locale.
 
Parameters:description - The new value of the description.locale - The locale for which the description is set.
 Note that there is a special locale called default which can be used to set
 the description in the default language. The default language is specified
 by passing null or new Locale("default").
    - isDescriptionUpdateable
boolean isDescriptionUpdateable()
Signals whether the description property can be changed for the kind and current state of the object.
    - setDefaultQueryTable
void setDefaultQueryTable(java.lang.String defaultQueryTable)
Sets the default query table associated to the business category.
 
Parameters:defaultQueryTable - The default query table associated to the business category.
    - isDefaultQueryTableUpdateable
boolean isDefaultQueryTableUpdateable()
Signals whether the default query table property can be changed for the kind and current state of the object.
    - setJNDINameOfStaffPluginProvider
void setJNDINameOfStaffPluginProvider(java.lang.String jndiNameStaffProvider)
Sets the JNDI name of a user-defined people directory configuration.
 
Parameters:jndiNameStaffProvider - The JNDI name of the user-defined people directory configuration.
    - isJNDINameOfStaffPluginProviderUpdateable
boolean isJNDINameOfStaffPluginProviderUpdateable()
Signals whether the jndi name staff provider property can be changed for the kind and current state of the object.
    - setSubstitutionPolicy
void setSubstitutionPolicy(int substitutionPolicy)
Sets the substitution policy that takes place when people assignments are performed.
 
 Possible substitution policies are SUBSTITUTION\_POLICY\_NO\_SUBSTITUTION, SUBSTITUTION\_POLICY\_SUBSTITUTE\_IF\_ABSENT,
 SUBSTITUTION\_POLICY\_SELECT\_USER\_IF\_PRESENT.
 
Parameters:substitutionPolicy - The substitution policy that should take place.
    - isSubstitutionPolicyUpdateable
boolean isSubstitutionPolicyUpdateable()
Signals whether the substitution policy property can be changed for the kind and current state of the object.
    - setCustomText1
void setCustomText1(java.lang.String customText1)
Sets the custom text specified as custom text one.
 
Parameters:customText1 - The custom text.
    - isCustomText1Updateable
boolean isCustomText1Updateable()
Signals whether the custom text 1 property can be changed for the kind and current state of the object.
    - setCustomText2
void setCustomText2(java.lang.String customText2)
Sets the custom text specified as custom text two.
 
Parameters:customText2 - The custom text.
    - isCustomText2Updateable
boolean isCustomText2Updateable()
Signals whether the custom text 2 property can be changed for the kind and current state of the object.
    - setCustomText3
void setCustomText3(java.lang.String customText3)
Sets the custom text specified as custom text three.
 
Parameters:customText3 - The custom text.
    - isCustomText3Updateable
boolean isCustomText3Updateable()
Signals whether the custom text 3 property can be changed for the kind and current state of the object.
    - setCustomText4
void setCustomText4(java.lang.String customText4)
Sets the custom text specified as custom text four.
 
Parameters:customText4 - The custom text.
    - isCustomText4Updateable
boolean isCustomText4Updateable()
Signals whether the custom text 4 property can be changed for the kind and current state of the object.
    - setCustomText5
void setCustomText5(java.lang.String customText5)
Sets the custom text specified as custom text five.
 
Parameters:customText5 - The custom text.
    - isCustomText5Updateable
boolean isCustomText5Updateable()
Signals whether the custom text 5 property can be changed for the kind and current state of the object.
    - setCustomText6
void setCustomText6(java.lang.String customText6)
Sets the custom text specified as custom text six.
 
Parameters:customText6 - The custom text.
    - isCustomText6Updateable
boolean isCustomText6Updateable()
Signals whether the custom text 6 property can be changed for the kind and current state of the object.
    - setCustomText7
void setCustomText7(java.lang.String customText7)
Sets the custom text specified as custom text seven.
 
Parameters:customText7 - The custom text.
    - isCustomText7Updateable
boolean isCustomText7Updateable()
Signals whether the custom text 7 property can be changed for the kind and current state of the object.
    - setCustomText8
void setCustomText8(java.lang.String customText8)
Sets the custom text specified as custom text eight.
 
Parameters:customText8 - The custom text.
    - isCustomText8Updateable
boolean isCustomText8Updateable()
Signals whether the custom text 8 property can be changed for the kind and current state of the object.
    - setPeopleAssignment
void setPeopleAssignment(int assignmentReason,
                       PeopleAssignment people)
Sets the assignment reason for the specified people. Possible reasons are:
 WorkItem.REASON\_READER.
 
Parameters:assignmentReason - The assignment reason to be set.people - The staff to be associated.
    - isPeopleAssignmentUpdateable
boolean isPeopleAssignmentUpdateable()
Signals whether the custom text 8 property can be changed for the kind and current state of the object.