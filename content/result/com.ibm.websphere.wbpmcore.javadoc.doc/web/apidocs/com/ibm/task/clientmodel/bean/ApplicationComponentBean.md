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

## Class ApplicationComponentBean

- java.lang.Object
    - com.ibm.task.clientmodel.bean.ApplicationComponentBean

- All Implemented Interfaces:
ApplicationComponent, java.io.Serializable

public class ApplicationComponentBean
extends java.lang.Object
implements ApplicationComponent
Accesses the properties of an ApplicationComponent object
 and adds metadata for national language support and converters. 
An ApplicationComponentBean object can be instantiated from
 an ACOID object.
 
 Use the static method getLabel(String, Locale) to
 retrieve the localized label for a property.
 Use the static method getConverter(String) to
 retrieve a converter for a property. The return value may be null because converters
 are optional.
 
See Also:ApplicationComponent, 
Serialized Form

- =========== FIELD SUMMARY =========== ======== CONSTRUCTOR SUMMARY ======== ========== METHOD SUMMARY ===========
    - Field Summary Fields Modifier and Type Field and Description static java.lang.String BUSINESSRELEVANT\_PROPERTY Use the property name to determine labels and converters for the property BusinessRelevant. static java.lang.String COPYRIGHT (C) Copyright IBM Corporation 2007. static java.lang.String DURATIONUNTILDELETED\_PROPERTY Use the property name to determine labels and converters for the property durationUntilDeleted. static java.lang.String EVENTHANDLERNAME\_PROPERTY Use the property name to determine labels and converters for the property eventHandlerName. static java.lang.String ID\_PROPERTY Use the property name to determine labels and converters for the property ID. static java.lang.String NAME\_PROPERTY Use the property name to determine labels and converters for the property name. static java.lang.String SUBSTITUTIONPOLICY\_PROPERTY Use the property name to determine labels and converters for the property substitutionPolicy. static java.lang.String SUPPORTSAUTOMATICCLAIM\_PROPERTY Use the property name to determine labels and converters for the property supportsAutomaticClaim. static java.lang.String SUPPORTSCLAIMIFSUSPENDED\_PROPERTY Use the property name to determine labels and converters for the property supportsClaimIfSuspended. static java.lang.String SUPPORTSDELEGATION\_PROPERTY Use the property name to determine labels and converters for the property supportsDelegation. static java.lang.String SUPPORTSFOLLOWONTASKS\_PROPERTY Use the property name to determine labels and converters for the property supportsFollowOnTasks. static java.lang.String SUPPORTSSUBTASKS\_PROPERTY Use the property name to determine labels and converters for the property supportsSubTasks.

### Field Summary

| Modifier and Type       | Field and Description                                                                                                                  |
|-------------------------|----------------------------------------------------------------------------------------------------------------------------------------|
| static java.lang.String | BUSINESSRELEVANT\_PROPERTY Use the property name to determine labels and converters for the property  BusinessRelevant.                 |
| static java.lang.String | COPYRIGHT (C) Copyright IBM Corporation 2007.                                                                                          |
| static java.lang.String | DURATIONUNTILDELETED\_PROPERTY Use the property name to determine labels and converters for the property  durationUntilDeleted.         |
| static java.lang.String | EVENTHANDLERNAME\_PROPERTY Use the property name to determine labels and converters for the property  eventHandlerName.                 |
| static java.lang.String | ID\_PROPERTY Use the property name to determine labels and converters for the property  ID.                                             |
| static java.lang.String | NAME\_PROPERTY Use the property name to determine labels and converters for the property  name.                                         |
| static java.lang.String | SUBSTITUTIONPOLICY\_PROPERTY Use the property name to determine labels and converters for the property  substitutionPolicy.             |
| static java.lang.String | SUPPORTSAUTOMATICCLAIM\_PROPERTY Use the property name to determine labels and converters for the property  supportsAutomaticClaim.     |
| static java.lang.String | SUPPORTSCLAIMIFSUSPENDED\_PROPERTY Use the property name to determine labels and converters for the property  supportsClaimIfSuspended. |
| static java.lang.String | SUPPORTSDELEGATION\_PROPERTY Use the property name to determine labels and converters for the property  supportsDelegation.             |
| static java.lang.String | SUPPORTSFOLLOWONTASKS\_PROPERTY Use the property name to determine labels and converters for the property  supportsFollowOnTasks.       |
| static java.lang.String | SUPPORTSSUBTASKS\_PROPERTY Use the property name to determine labels and converters for the property  supportsSubTasks.                 |

- Fields inherited from interface com.ibm.task.api.ApplicationComponent
SUBSTITUTION\_POLICY\_NO\_SUBSTITUTION, SUBSTITUTION\_POLICY\_SELECT\_USER\_IF\_PRESENT, SUBSTITUTION\_POLICY\_SUBSTITUTE\_IF\_ABSENT

- Constructor Summary

Constructors 

Constructor and Description

ApplicationComponentBean(ApplicationComponent applicationComponent)
Constructs a ApplicationComponentBean from an id.

- Method Summary Methods Modifier and Type Method and Description java.lang.String getCalendarName () Returns the property calendarName . static SimpleConverter getConverter (java.lang.String propertyName) Returns the default converter for a given property. java.lang.String getDurationUntilDeleted () Returns the property durationUntilDeleted . java.lang.String getEventHandlerName () Returns the property eventHandlerName . ACOID getID () Returns the property ID . java.lang.String getJNDINameOfCalendar () Returns the property jNDINameOfCalendar . java.lang.String getJNDINameOfStaffPluginProvider () Returns the property jNDINameOfStaffPluginProvider . static java.lang.String getLabel (java.lang.String propertyName) Returns the resource bundle key for a property static java.lang.String getLabel (java.lang.String propertyName, java.util.Locale locale) Returns the label for a property from the resource bundle. java.lang.String getName () Returns the property name . int getSubstitutionPolicy () Returns the property substitutionPolicy . boolean isBusinessRelevant () Returns the property isBusinessRelevant . boolean isSupportsAutomaticClaim () Returns the property supportsAutomaticClaim . boolean isSupportsClaimIfSuspended () Returns the property supportsClaimIfSuspended . boolean isSupportsDelegation () Returns the property supportsDelegation . boolean isSupportsFollowOnTasks () Returns the property supportsFollowOnTasks . boolean isSupportsSubTasks () Returns the property supportsSubTasks . static boolean isValid (java.lang.String propertyName) Checks if the property is valid. boolean supportsAutomaticClaim () Returns the property supportsAutomaticClaim . boolean supportsClaimIfSuspended () Returns the property supportsClaimIfSuspended . boolean supportsDelegation () Returns the property supportsDelegation . boolean supportsFollowOnTasks () Returns the property supportsFollowOnTasks . boolean supportsSubTasks () Returns the property supportsSubTasks .

### Method Summary

| Modifier and Type       | Method and Description                                                                                                              |
|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| java.lang.String        | getCalendarName() Returns the property calendarName.                                                                                |
| static SimpleConverter  | getConverter(java.lang.String propertyName) Returns the default converter for a given property.                                     |
| java.lang.String        | getDurationUntilDeleted() Returns the property durationUntilDeleted.                                                                |
| java.lang.String        | getEventHandlerName() Returns the property eventHandlerName.                                                                        |
| ACOID                   | getID() Returns the property ID.                                                                                                    |
| java.lang.String        | getJNDINameOfCalendar() Returns the property jNDINameOfCalendar.                                                                    |
| java.lang.String        | getJNDINameOfStaffPluginProvider() Returns the property jNDINameOfStaffPluginProvider.                                              |
| static java.lang.String | getLabel(java.lang.String propertyName) Returns the resource bundle key for a property                                              |
| static java.lang.String | getLabel(java.lang.String propertyName,         java.util.Locale locale) Returns the label for a property from the resource bundle. |
| java.lang.String        | getName() Returns the property name.                                                                                                |
| int                     | getSubstitutionPolicy() Returns the property substitutionPolicy.                                                                    |
| boolean                 | isBusinessRelevant() Returns the property isBusinessRelevant.                                                                       |
| boolean                 | isSupportsAutomaticClaim() Returns the property supportsAutomaticClaim.                                                             |
| boolean                 | isSupportsClaimIfSuspended() Returns the property supportsClaimIfSuspended.                                                         |
| boolean                 | isSupportsDelegation() Returns the property supportsDelegation.                                                                     |
| boolean                 | isSupportsFollowOnTasks() Returns the property supportsFollowOnTasks.                                                               |
| boolean                 | isSupportsSubTasks() Returns the property supportsSubTasks.                                                                         |
| static boolean          | isValid(java.lang.String propertyName) Checks if the property is valid.                                                             |
| boolean                 | supportsAutomaticClaim() Returns the property supportsAutomaticClaim.                                                               |
| boolean                 | supportsClaimIfSuspended() Returns the property supportsClaimIfSuspended.                                                           |
| boolean                 | supportsDelegation() Returns the property supportsDelegation.                                                                       |
| boolean                 | supportsFollowOnTasks() Returns the property supportsFollowOnTasks.                                                                 |
| boolean                 | supportsSubTasks() Returns the property supportsSubTasks.                                                                           |

    - Methods inherited from class java.lang.Object
clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait