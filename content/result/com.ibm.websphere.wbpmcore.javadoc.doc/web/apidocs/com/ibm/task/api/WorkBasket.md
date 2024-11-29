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

## Interface WorkBasket

- All Superinterfaces: java.io.Serializable public interface WorkBasket extends java.io.Serializable Accesses the properties of a work basket. Work baskets provide for a means to deal with a large number of tasks in an organization. They allow to group tasks into meaningful subsets based, for example, on responsibilities, organizational units, or topics. Tasks are then routed from one work basket to another until eventually ending up in a work basket from where a business user takes the task, works on it and completes it. Work baskets thus provide an alternate way of assigning tasks to people. They can be used instead or combined with people resolution on tasks. Work baskets not only structure the entire set of tasks into smaller pieces but also help control the processing of these tasks by monitoring the remaining tasks in the work basket. In work basket scenarios, all tasks are residing in a specific work basket. There are no tasks without a work basket association. The initial assignment to a work basket is done based on the type of work, that is, the type of the task. There are typically four types of work baskets: Tasks are usually first assigned to a group work basket or a topic work basket. From there they are transferred to a more specific work basket, which is in the end an individual work basket. The tasks are then processed by the individual, Since: 6.2.0.3

```
public interface WorkBasket
extends java.io.Serializable
```

Work baskets provide for a means to deal with a large number of tasks in an organization.
 They allow to group tasks into meaningful subsets based, for example, on responsibilities,
 organizational units, or topics.
 Tasks are then routed from one work basket to another until eventually ending up in a work basket
 from where a business user takes the task, works on it and completes it.
 
 Work baskets thus provide an alternate way of assigning tasks to people. They can be used instead
 or combined with people resolution on tasks. Work baskets not only structure the
 entire set of tasks into smaller pieces but also help control the processing of these
 tasks by monitoring the remaining tasks in the work basket.
 
 In work basket scenarios, all tasks are residing in a specific work basket.
 There are no tasks without a work basket association. The initial assignment to a work basket
 is done based on the type of work, that is, the type of the task.
 
 There are typically four types of work baskets:
 
Group work baskets
 

 Group work baskets contain all tasks which are to be processed by a certain group of people,
 for example, teams or departments. The work basket defines the responsibility for the task and
 the associated service level.
 Topic work baskets
 

 Topic work baskets contain all tasks that belong to a certain theme or topic.
 The users to process the tasks change quite often, dependent on their current priorities
 or availability.
 Individual work baskets
 

 Individual work baskets contain all tasks assigned to a specific person.
 Clearing work baskets
 

 Clearing work baskets are used for tasks that cannot be processed as they are,
 but require special care.
 
 Tasks are usually first assigned to a group work basket or a topic work basket.
 From there they are transferred to a more specific work basket, which is in the end an
 individual work basket. The tasks are then processed by the individual,

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

static int
TYPE\_CLEARANCE
States that tasks contained in this work basket cannot be processed as they are,
 but require special care.

static int
TYPE\_GROUP
States that tasks contained in this work basket are to be processed
 by a certain group of people, for example, teams or departments.

static int
TYPE\_INDIVIDUAL
States that tasks contained in this work basket are assigned to a specific person.

static int
TYPE\_TOPIC
States that tasks contained in this work basket belong to a certain theme or topic.
    - Method Summary

Methods 

Modifier and Type
Method and Description

java.util.Calendar
getCreationTime()
Returns the creation time of the work basket.

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
Returns the name of the default query table associated to the work basket.

java.lang.String
getDescription(java.util.Locale arg0)
Returns the description in the specified locale.

java.lang.String
getDisplayName(java.util.Locale arg0)
Returns the display name in the specified locale.

java.util.List
getDistributionTargets()
Returns a list of object IDs (WBIDs) of work baskets that are distribution targets of this work basket.

WBID
getID()
Returns the object identifier.

java.lang.String
getJNDINameOfStaffPluginProvider()
Returns the JNDI name of a user-defined people directory configuration.

java.util.Calendar
getLastModificationTime()
Returns the last time a property of the work basket changed.

java.util.List
getLocalesOfDescriptions()
Returns the locales of all descriptions.

java.util.List
getLocalesOfDisplayNames()
Returns the locales of all display names.

java.lang.String
getName()
Returns the name of the work basket.

java.lang.String
getOwner()
Returns the owner of the work basket.

int
getSubstitutionPolicy()
Returns the substitution policy that takes place when people assignments are performed.

int
getType()
Returns the type of the work basket.

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

- TYPE\_GROUP
static final int TYPE\_GROUP
States that tasks contained in this work basket are to be processed
 by a certain group of people, for example, teams or departments.
See Also:Constant Field Values

- TYPE\_CLEARANCE
static final int TYPE\_CLEARANCE
States that tasks contained in this work basket cannot be processed as they are,
 but require special care.
See Also:Constant Field Values

- TYPE\_TOPIC
static final int TYPE\_TOPIC
States that tasks contained in this work basket belong to a certain theme or topic.
See Also:Constant Field Values

- TYPE\_INDIVIDUAL
static final int TYPE\_INDIVIDUAL
States that tasks contained in this work basket are assigned to a specific person.
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
WBID getID()
Returns the object identifier.
    - getName
java.lang.String getName()
Returns the name of the work basket.
    - getType
int getType()
Returns the type of the work basket.
 
 Possible types are TYPE\_GROUP, TYPE\_TOPIC, TYPE\_INDIVIDUAL, or TYPE\_CLEARANCE.
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
    - getOwner
java.lang.String getOwner()
Returns the owner of the work basket.
    - getDistributionTargets
java.util.List getDistributionTargets()
Returns a list of object IDs (WBIDs) of work baskets that are distribution targets of this work basket.
 Returns an empty list when there are no distribution targets.
    - getDefaultQueryTable
java.lang.String getDefaultQueryTable()
Returns the name of the default query table associated to the work basket.
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
Returns the creation time of the work basket.
    - getLastModificationTime
java.util.Calendar getLastModificationTime()
Returns the last time a property of the work basket changed.