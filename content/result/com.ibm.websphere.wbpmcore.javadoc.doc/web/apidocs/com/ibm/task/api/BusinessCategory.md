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

## Interface BusinessCategory

- All Superinterfaces:
java.io.Serializable

public interface BusinessCategory
extends java.io.Serializable
Accesses the properties of a business category.
 
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

java.util.Calendar
getCreationTime()
Returns the creation time of the business category.

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

BCID
getID()
Returns the object identifier.

java.lang.String
getJNDINameOfStaffPluginProvider()
Returns the JNDI name of a user-defined people directory configuration.

java.util.Calendar
getLastModificationTime()
Returns the last time a property of the business category changed.

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

java.lang.Integer
getPriority()
Returns the priority of the business category.

int
getSubstitutionPolicy()
Returns the substitution policy that takes place when people assignments are performed.

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

    - getID
BCID getID()
Returns the object identifier.
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
    - getCreationTime
java.util.Calendar getCreationTime()
Returns the creation time of the business category.
    - getLastModificationTime
java.util.Calendar getLastModificationTime()
Returns the last time a property of the business category changed.