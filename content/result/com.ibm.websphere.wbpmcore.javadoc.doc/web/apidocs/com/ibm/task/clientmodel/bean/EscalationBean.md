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

## Class EscalationBean

- java.lang.Object
    - com.ibm.task.clientmodel.bean.EscalationBean

- All Implemented Interfaces: Escalation , java.io.Serializable public class EscalationBean extends java.lang.Objectimplements Escalation Accesses the properties of the original Escalation object and adds metadata for national language support and converters. An EscalationBean object can be instantiated from a QueryResultSet object. Only the following properties are loaded from the query result set: If the property is not found in the query result set, the property remains empty. Accessing an empty property requires the bean to load the missing information from the server. Use the static method getLabel(String, Locale) to retrieve the localized label for a property. Use the static method getConverter(String) to retrieve a converter for a property. The return value might be null because converters are optional. See Also: Escalation , QueryResultSet , Serialized Form

```
public class EscalationBean
extends java.lang.Object
implements Escalation
```

Accesses the properties of the original Escalation object 
 and adds metadata for national language support and converters.

An EscalationBean object can be instantiated from
 a QueryResultSet object.
 

 Only the following properties are loaded from the query result set:
 
ID
taskInstanceID
action
activationState
activationTime
atLeastExpectedState
name
priorityIncrease
state
taskName
taskOwner
escalationReceiver

 If the property is not found in the query result set, the property remains empty.
 Accessing an empty property requires the bean to load the missing information 
 from the server.

Use the static method getLabel(String, Locale) to
 retrieve the localized label for a property. 
 Use the static method getConverter(String) to
 retrieve a converter for a property. The return value might be null because converters 
 are optional.

- =========== FIELD SUMMARY =========== ======== CONSTRUCTOR SUMMARY ======== ========== METHOD SUMMARY ===========
    - Field Summary Fields Modifier and Type Field and Description static java.lang.String ACTION\_PROPERTY Use the property name to determine labels and converters for the action property . static java.lang.String ACTIVATIONSTATE\_PROPERTY Use the property name to determine labels and converters for the activationState property. static java.lang.String ACTIVATIONTIME\_PROPERTY Use the property name to determine labels and converters for the activationTime property. static java.lang.String ATLEASTEXPECTEDSTATE\_PROPERTY Use the property name to determine labels and converters for the atLeastExpectedState property. static java.lang.String COPYRIGHT (C) Copyright IBM Corporation 2005, 2011. static java.lang.String DESCRIPTION\_PROPERTY Use the property name to determine labels and converters for the description property. static java.lang.String DURATIONUNTILESCALATED\_PROPERTY Use the property name to determine labels and converters for the durationUntilEscalated property. static java.lang.String DURATIONUNTILREPEATED\_PROPERTY Use the property name to determine labels and converters for the durationUntilRepeated property. static java.lang.String ESCALATION\_RECEIVER\_PROPERTY Use the property name to determine labels and converters for the escalationReceiver property. static java.lang.String FIRST\_ESCALATION\_ID\_PROPERTY Use the property name to determine labels and converters for the firstEscalationID property. static java.lang.String NAME\_PROPERTY Use the property name to determine labels and converters for the name property. static java.lang.String PRIORITY\_INCREASE\_PROPERTY Use the property name to determine labels and converters for the priorityIncrease property. static java.lang.String STATE\_PROPERTY Use the property name to determine labels and converters for the state property. static java.lang.String TASK\_OWNER\_PROPERTY Use the property name to determine labels and converters for the taskOwner property.

### Field Summary

| Modifier and Type       | Field and Description                                                                                                               |
|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| static java.lang.String | ACTION\_PROPERTY Use the property name to determine labels and converters for the action property .                                  |
| static java.lang.String | ACTIVATIONSTATE\_PROPERTY Use the property name to determine labels and converters for the    activationState property.              |
| static java.lang.String | ACTIVATIONTIME\_PROPERTY Use the property name to determine labels and converters for the   activationTime property.                 |
| static java.lang.String | ATLEASTEXPECTEDSTATE\_PROPERTY Use the property name to determine labels and converters for the   atLeastExpectedState property.     |
| static java.lang.String | COPYRIGHT (C) Copyright IBM Corporation 2005, 2011.                                                                                 |
| static java.lang.String | DESCRIPTION\_PROPERTY Use the property name to determine labels and converters for the   description property.                       |
| static java.lang.String | DURATIONUNTILESCALATED\_PROPERTY Use the property name to determine labels and converters for the   durationUntilEscalated property. |
| static java.lang.String | DURATIONUNTILREPEATED\_PROPERTY Use the property name to determine labels and converters for the   durationUntilRepeated property.   |
| static java.lang.String | ESCALATION\_RECEIVER\_PROPERTY Use the property name to determine labels and converters for the   escalationReceiver property.        |
| static java.lang.String | FIRST\_ESCALATION\_ID\_PROPERTY Use the property name to determine labels and converters for the   firstEscalationID property.         |
| static java.lang.String | NAME\_PROPERTY Use the property name to determine labels and converters for the   name property.                                     |
| static java.lang.String | PRIORITY\_INCREASE\_PROPERTY Use the property name to determine labels and converters for the   priorityIncrease property.            |
| static java.lang.String | STATE\_PROPERTY Use the property name to determine labels and converters for the   state property.                                   |
| static java.lang.String | TASK\_OWNER\_PROPERTY Use the property name to determine labels and converters for the   taskOwner property.                          |

- Fields inherited from interface com.ibm.task.api.Escalation
ACTION\_CREATE\_EVENT, ACTION\_CREATE\_WORK\_ITEM, ACTION\_SEND\_EMAIL, ACTIVATION\_STATE\_CLAIMED, ACTIVATION\_STATE\_READY, ACTIVATION\_STATE\_RUNNING, ACTIVATION\_STATE\_WAITING\_FOR\_SUBTASK, AT\_LEAST\_EXPECTED\_STATE\_CLAIMED, AT\_LEAST\_EXPECTED\_STATE\_ENDED, AT\_LEAST\_EXPECTED\_STATE\_SUBTASKS\_COMPLETED, INCREASE\_PRIORITY\_NO, INCREASE\_PRIORITY\_ONCE, INCREASE\_PRIORITY\_REPEATED, STATE\_ESCALATED, STATE\_INACTIVE, STATE\_SUPERFLUOUS, STATE\_WAITING

- Constructor Summary

Constructors 

Modifier
Constructor and Description

 
EscalationBean(Escalation esc,
              HTMConnection htmConnection)
Constructs a EscalationBean from an original Task object.

protected 
EscalationBean(ESIID id,
              HTMConnection htmConnection,
              java.util.Locale locale)
Constructs a EscalationBean from an escalation instance id.

 
EscalationBean(QueryResultSet resultSet,
              HTMConnection htmConnection)
Constructs a new EscalationBean from a QueryResultSet.

- Method Summary Methods Modifier and Type Method and Description int getAction () Returns the action property. int getActivationState () Returns the activationState property. java.util.Calendar getActivationTime () Returns the activationTime property. int getAtLeastExpectedState () Returns the atLeastExpectedState property. OID getContainmentContextID () Returns the containmentContextID property. static SimpleConverter getConverter (java.lang.String propertyName) Returns the default converter for a given property. com.ibm.bpc.clientcore.util.LocalisedString getDescription () Returns the localised description. java.lang.String getDescription (java.util.Locale locale) Returns the description property. com.ibm.bpc.clientcore.util.LocalisedString getDisplayName () Returns the localised display name. java.lang.String getDisplayName (java.util.Locale locale) Returns the displayName property. java.lang.String getDurationUntilEscalated () Returns the durationUntilEscalated property. java.lang.String getDurationUntilRepeated () Returns the durationUntilRepeated property. java.lang.String getEscalationReceiver () Returns the escalationReceiver property. ESTID getEscalationTemplateID () Returns the escalationTemplateID property. java.util.Calendar getEscalationTime () Returns the escalationTime property. ESIID getFirstEscalationID () Returns the firstEscalationID property. ESIID getID () Returns the ID property. static java.lang.String getLabel (java.lang.String propertyName) Returns the resource bundle key for a property static java.lang.String getLabel (java.lang.String propertyName, java.util.Locale locale) Returns the label of a property from the resource bundle. java.util.List getLocalesOfDescriptions () Returns the localesOfDescriptions property. java.util.List getLocalesOfDisplayNames () Returns the localesOfDisplayNames property. java.lang.String getName () Returns the name property. ESIID getNextEscalationID () Returns the nextEscalationID property. ESIID getPreviousEscalationID () Returns the previousEscalationID property. int getPriorityIncrease () Returns the priorityIncrease property. int getState () Returns the state property. TKIID getTaskInstanceID () Returns the taskInstanceID property. java.lang.String getTaskName () Returns the taskName property. java.lang.String getTaskOwner () Returns the taskOwner property. TKTID getTaskTemplateID () Returns the property tktid . boolean isDurationUntilEscalatedUpdateable () Signals whether the duration until escalation property can be changed for the kind and current state of the object. boolean isDurationUntilRepeatedUpdateable () Signals whether the duration until repeats property can be changed for the kind and current state of the object. boolean isEscalationTimeUpdateable () Signals whether the escalation time property can be changed for the kind and current state of the object. boolean isNameUpdateable () Signals whether the name property can be changed for the kind and current state of the object. static boolean isValid (java.lang.String propertyName) Checks whether the property is valid. void setDurationUntilEscalated (java.lang.String durationUntilEscalation) Sets the durationUntilRepeated property. void setDurationUntilRepeated (java.lang.String durationUntilRepeats) Sets the durationUntilRepeated property. void setEscalationTime (java.util.Calendar escalationTime) Sets the name property. void setName (java.lang.String arg0) Sets the name property.

### Method Summary

| Modifier and Type                           | Method and Description                                                                                                                                   |
|---------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| int                                         | getAction() Returns the action property.                                                                                                                 |
| int                                         | getActivationState() Returns the activationState property.                                                                                               |
| java.util.Calendar                          | getActivationTime() Returns the activationTime property.                                                                                                 |
| int                                         | getAtLeastExpectedState() Returns the atLeastExpectedState property.                                                                                     |
| OID                                         | getContainmentContextID() Returns the containmentContextID property.                                                                                     |
| static SimpleConverter                      | getConverter(java.lang.String propertyName) Returns the default converter for a given property.                                                          |
| com.ibm.bpc.clientcore.util.LocalisedString | getDescription() Returns the localised description.                                                                                                      |
| java.lang.String                            | getDescription(java.util.Locale locale) Returns the description property.                                                                                |
| com.ibm.bpc.clientcore.util.LocalisedString | getDisplayName() Returns the localised display name.                                                                                                     |
| java.lang.String                            | getDisplayName(java.util.Locale locale) Returns the displayName property.                                                                                |
| java.lang.String                            | getDurationUntilEscalated() Returns the durationUntilEscalated property.                                                                                 |
| java.lang.String                            | getDurationUntilRepeated() Returns the durationUntilRepeated property.                                                                                   |
| java.lang.String                            | getEscalationReceiver() Returns the escalationReceiver property.                                                                                         |
| ESTID                                       | getEscalationTemplateID() Returns the escalationTemplateID property.                                                                                     |
| java.util.Calendar                          | getEscalationTime() Returns the escalationTime property.                                                                                                 |
| ESIID                                       | getFirstEscalationID() Returns the firstEscalationID property.                                                                                           |
| ESIID                                       | getID() Returns the ID property.                                                                                                                         |
| static java.lang.String                     | getLabel(java.lang.String propertyName) Returns the resource bundle key for a property                                                                   |
| static java.lang.String                     | getLabel(java.lang.String propertyName,         java.util.Locale locale) Returns the label of a property from the resource bundle.                       |
| java.util.List                              | getLocalesOfDescriptions() Returns the localesOfDescriptions property.                                                                                   |
| java.util.List                              | getLocalesOfDisplayNames() Returns the localesOfDisplayNames property.                                                                                   |
| java.lang.String                            | getName() Returns the name property.                                                                                                                     |
| ESIID                                       | getNextEscalationID() Returns the nextEscalationID property.                                                                                             |
| ESIID                                       | getPreviousEscalationID() Returns the previousEscalationID property.                                                                                     |
| int                                         | getPriorityIncrease() Returns the priorityIncrease property.                                                                                             |
| int                                         | getState() Returns the state property.                                                                                                                   |
| TKIID                                       | getTaskInstanceID() Returns the taskInstanceID property.                                                                                                 |
| java.lang.String                            | getTaskName() Returns the taskName property.                                                                                                             |
| java.lang.String                            | getTaskOwner() Returns the taskOwner property.                                                                                                           |
| TKTID                                       | getTaskTemplateID() Returns the property tktid.                                                                                                          |
| boolean                                     | isDurationUntilEscalatedUpdateable() Signals whether the duration until escalation property can be changed for the kind and current state of the object. |
| boolean                                     | isDurationUntilRepeatedUpdateable() Signals whether the duration until repeats property can be changed for the kind and current state of the object.     |
| boolean                                     | isEscalationTimeUpdateable() Signals whether the escalation time property can be changed for the kind and current state of the object.                   |
| boolean                                     | isNameUpdateable() Signals whether the name property can be changed for the kind and current state of the object.                                        |
| static boolean                              | isValid(java.lang.String propertyName) Checks whether the property is valid.                                                                             |
| void                                        | setDurationUntilEscalated(java.lang.String durationUntilEscalation) Sets the durationUntilRepeated property.                                             |
| void                                        | setDurationUntilRepeated(java.lang.String durationUntilRepeats) Sets the durationUntilRepeated property.                                                 |
| void                                        | setEscalationTime(java.util.Calendar escalationTime) Sets the name property.                                                                             |
| void                                        | setName(java.lang.String arg0) Sets the name property.                                                                                                   |

    - Methods inherited from class java.lang.Object
clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait