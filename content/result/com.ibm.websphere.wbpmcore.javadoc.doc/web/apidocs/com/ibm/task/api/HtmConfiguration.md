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

## Interface HtmConfiguration

- All Superinterfaces:
java.io.Serializable

public interface HtmConfiguration
extends java.io.Serializable
This interface returns Human Task Manager configuration settings.
Since:
6.1

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static int
CASE\_CONVERSION\_LOWER
Symbolic constant which states that a conversion to lower case may be required 
 for users or groups related to case sensitivity.

static int
CASE\_CONVERSION\_NONE
Symbolic constant which states that no user or group conversion is required 
 related to case sensitivity.

static int
CASE\_CONVERSION\_UPPER
Symbolic constant which states that a conversion to upper case may be required 
 for users or groups related to case sensitivity.

static java.lang.String
COPYRIGHT 

static int
SYSTEM\_TYPE\_WLE
Not used for this configuration.

static int
SYSTEM\_TYPE\_WPS
Symbolic constant for the system type described by this configuration.
    - Method Summary

Methods 

Modifier and Type
Method and Description

boolean
areBusinessCategoriesEnabled()
States whether business categories are enabled.

boolean
areWorkBasketsEnabled()
States whether work baskets are enabled.

java.lang.String
getBuildLevel()
Returns the build level of the Human Task Manager configuration.

int
getCaseSensitivityOfGroups()
Returns the type of case conversion that is to be applied to groups of users.

int
getCaseSensitivityOfUsers()
Returns the type of case conversion that is to be applied to user IDs.

java.util.Locale
getServerLocale()
Returns the locale of the server.

java.lang.String
getSystemID()
Returns the system ID of the Human Task Manager installation.

int
getSystemType()
Returns the type of the Human Task Manager installation.

java.lang.String
getVersion()
Returns the version of the Human Task Manager configuration.

boolean
isGroupWorkItemsEnabled()
States whether group work items can be used.

boolean
isSubstitutionEnabled()
States whether substitution is enabled.

boolean
isSubstitutionManagementRestrictedToAdministrators()
States whether substitution settings can be set or queried by system administrators or by all users.

boolean
isTaskHistoryEnabled()
States whether writing a task history is enabled.

- ============ FIELD DETAIL =========== ============ METHOD DETAIL ==========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
See Also:Constant Field Values

- SYSTEM\_TYPE\_WPS
static final int SYSTEM\_TYPE\_WPS
Symbolic constant for the system type described by this configuration.
Since:
7.5
See Also:Constant Field Values

- SYSTEM\_TYPE\_WLE
static final int SYSTEM\_TYPE\_WLE
Not used for this configuration.
Since:
7.5
See Also:Constant Field Values

- CASE\_CONVERSION\_NONE
static final int CASE\_CONVERSION\_NONE
Symbolic constant which states that no user or group conversion is required 
 related to case sensitivity.
Since:
7.5.1
See Also:Constant Field Values

- CASE\_CONVERSION\_UPPER
static final int CASE\_CONVERSION\_UPPER
Symbolic constant which states that a conversion to upper case may be required 
 for users or groups related to case sensitivity.
Since:
7.5.1
See Also:Constant Field Values

- CASE\_CONVERSION\_LOWER
static final int CASE\_CONVERSION\_LOWER
Symbolic constant which states that a conversion to lower case may be required 
 for users or groups related to case sensitivity.
Since:
7.5.1
See Also:Constant Field Values

- Method Detail

### Method Detail

    - isSubstitutionEnabled
boolean isSubstitutionEnabled()
States whether substitution is enabled.
 
 If substitution is enabled, then substitutes or the absence flag can be set and queried.
 If substitution is not enabled, then substitutes or the absence flag cannot be set or queried.
 If tried, StaffServiceSubstitutionNotEnabledException
 is raised.
 Refer to getAbsence,
 setAbsence,
 getSubstitutes,
 setSubstitutes.
 
Returns:boolean -
   True states that substitution is enabled.
   False states that substitution is not enabled.Since:
6.1
    - isSubstitutionManagementRestrictedToAdministrators
boolean isSubstitutionManagementRestrictedToAdministrators()
States whether substitution settings can be set or queried by system administrators or by all users.
 The logged-on user can always manage personal substitution settings.
 
 Refer to getAbsence,
 setAbsence,
 getSubstitutes,
 setSubstitutes.
 
Returns:boolean -
   True states that only system administrators can set or query substitution settings
         of other people.
   False states that substitution settings can be changed by all users for all users.Since:
6.1
    - isGroupWorkItemsEnabled
boolean isGroupWorkItemsEnabled()
States whether group work items can be used.
 
Returns:boolean -
   True states that group work items can be used.
   False states that group work items cannot be used.Since:
6.1
    - isTaskHistoryEnabled
boolean isTaskHistoryEnabled()
States whether writing a task history is enabled.
 
Returns:boolean -
   True states that writing task history records is enabled.
   False states that writing task history records is not enabled.Since:
7.5
    - areWorkBasketsEnabled
boolean areWorkBasketsEnabled()
States whether work baskets are enabled.
 
Returns:boolean -
   True states that work baskets are enabled.
   False states that work baskets are not enabled.Since:
7.5
    - areBusinessCategoriesEnabled
boolean areBusinessCategoriesEnabled()
States whether business categories are enabled.
 
Returns:boolean -
   True states that business categories are enabled.
   False states that business categories are not enabled.Since:
7.5
    - getVersion
java.lang.String getVersion()
Returns the version of the Human Task Manager configuration.
 
Returns:String -
   The version of the Human Task Manager configuration, for example, 7.5.0.Since:
7.5
    - getBuildLevel
java.lang.String getBuildLevel()
Returns the build level of the Human Task Manager configuration.
 
Returns:String -
   The build level of the Human Task Manager configuration.Since:
7.5
    - getSystemID
java.lang.String getSystemID()
Returns the system ID of the Human Task Manager installation.
 
Returns:String -
   The system ID of the Human Task Manager installation.Since:
7.5
    - getSystemType
int getSystemType()
Returns the type of the Human Task Manager installation.
 
Returns:int -
   The type of the Human Task Manager installation, in this case, SYSTEM\_TYPE\_WPS.Since:
7.5
    - getCaseSensitivityOfUsers
int getCaseSensitivityOfUsers()
Returns the type of case conversion that is to be applied to user IDs.
 See QueryHelper.convertUserIfNeeded or
 QueryHelper.convertUsersIfNeeded for
 conversion helper methods.
 
Returns:int -
   The case sensitivity of users.Since:
7.5.1
    - getCaseSensitivityOfGroups
int getCaseSensitivityOfGroups()
Returns the type of case conversion that is to be applied to groups of users.
 See QueryHelper.convertGroupIfNeeded or
 QueryHelper.convertGroupsIfNeeded for
 conversion helper methods.
 
Returns:int -
   The case sensitivity of groups.Since:
7.5.1
    - getServerLocale
java.util.Locale getServerLocale()
Returns the locale of the server.
 
Returns:Locale -
   The server locale.Since:
7.5.1