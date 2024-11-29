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

## Interface WorkItemData

- All Superinterfaces:
java.io.Serializable

public interface WorkItemData
extends java.io.Serializable
Accesses the properties of a work item.
 
 A work item represents a relationship between a person or group of persons and an
 object, typically an activity or task instance. The relationship is described by attributes
 such as the type of the associated object and the reason why the object is assigned.
 
 For example,
 work items are created whenever a human task (staff), receive, or pick activity is encountered
 during the navigation of a process instance. The associated people assignment is
 performed and returns a list or group of persons. Each person on the list or the group receives a work
 item for the activity instance. Similarly, work items are created for the starter,
 process administrators, editors, and readers of a process instance.
 
 Beginning with Version 7.0.0.3, shared work items are used for authorization instead of
 non-shared work items.
 To benefit from the performance benefits of shared work items,
 do not use the deprecated methods.
 
Since:
5.0

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT 

static int
OBJECT\_TYPE\_ACTIVITY
States that the work item has been created for an activity instance.

static int
OBJECT\_TYPE\_APPLICATION\_COMPONENT
Do not use - internal only.

static int
OBJECT\_TYPE\_BUSINESS\_CATEGORY
States that the work item has been created for a business category.

static int
OBJECT\_TYPE\_ESCALATION\_INSTANCE
States that the work item has been created for an escalation instance.

static int
OBJECT\_TYPE\_ESCALATION\_TEMPLATE
Do not use - internal only.

static int
OBJECT\_TYPE\_EVENT
States that the work item has been created for a receive event.

static int
OBJECT\_TYPE\_MAX
Do not use - internal only.

static int
OBJECT\_TYPE\_PROCESS\_INSTANCE
States that the work item has been created for a process instance.

static int
OBJECT\_TYPE\_PROCESS\_TEMPLATE
Do not use - internal only.

static int
OBJECT\_TYPE\_STATE\_MACHINE\_EVENT
Do not use - internal only.

static int
OBJECT\_TYPE\_STATE\_MACHINE\_INSTANCE
Do not use - internal only.

static int
OBJECT\_TYPE\_STATE\_MACHINE\_TEMPLATE
Do not use - internal only.

static int
OBJECT\_TYPE\_TASK\_INSTANCE
States that the work item has been created for a task instance.

static int
OBJECT\_TYPE\_TASK\_TEMPLATE
Do not use - internal only.

static int
OBJECT\_TYPE\_WORK\_BASKET
States that the work item has been created for a work basket.

static int
REASON\_ADMINISTRATOR
States that operations can be executed on the associated object that require
 administrator rights, for example, deletion of an object.

static int
REASON\_APPENDER
States that operations can be executed on the associated object that require
 appender rights.

static int
REASON\_CUSTOMROLE\_1
States that operations can be executed on the associated object that require
 rights defined by custom role 1.

static int
REASON\_CUSTOMROLE\_10
States that operations can be executed on the associated object that require
 rights defined by custom role 10.

static int
REASON\_CUSTOMROLE\_11
States that operations can be executed on the associated object that require
 rights defined by custom role 11.

static int
REASON\_CUSTOMROLE\_12
States that operations can be executed on the associated object that require
 rights defined by custom role 12.

static int
REASON\_CUSTOMROLE\_13
States that operations can be executed on the associated object that require
 rights defined by custom role 13.

static int
REASON\_CUSTOMROLE\_14
States that operations can be executed on the associated object that require
 rights defined by custom role 14.

static int
REASON\_CUSTOMROLE\_15
States that operations can be executed on the associated object that require
 rights defined by custom role 15.

static int
REASON\_CUSTOMROLE\_16
States that operations can be executed on the associated object that require
 rights defined by custom role 16.

static int
REASON\_CUSTOMROLE\_17
States that operations can be executed on the associated object that require
 rights defined by custom role 17.

static int
REASON\_CUSTOMROLE\_18
States that operations can be executed on the associated object that require
 rights defined by custom role 18.

static int
REASON\_CUSTOMROLE\_19
States that operations can be executed on the associated object that require
 rights defined by custom role 19.

static int
REASON\_CUSTOMROLE\_2
States that operations can be executed on the associated object that require
 rights defined by custom role 2.

static int
REASON\_CUSTOMROLE\_20
States that operations can be executed on the associated object that require
 rights defined by custom role 20.

static int
REASON\_CUSTOMROLE\_3
States that operations can be executed on the associated object that require
 rights defined by custom role 3.

static int
REASON\_CUSTOMROLE\_4
States that operations can be executed on the associated object that require
 rights defined by custom role 4.

static int
REASON\_CUSTOMROLE\_5
States that operations can be executed on the associated object that require
 rights defined by custom role 5.

static int
REASON\_CUSTOMROLE\_6
States that operations can be executed on the associated object that require
 rights defined by custom role 6.

static int
REASON\_CUSTOMROLE\_7
States that operations can be executed on the associated object that require
 rights defined by custom role 7.

static int
REASON\_CUSTOMROLE\_8
States that operations can be executed on the associated object that require
 rights defined by custom role 8.

static int
REASON\_CUSTOMROLE\_9
States that operations can be executed on the associated object that require
 rights defined by custom role 9.

static int
REASON\_DISTRIBUTOR
States that operations can be executed on the associated object that require
 distributor rights, for example, distributing objects to a work basket.

static int
REASON\_EDITOR
States that operations can be executed on the associated object that require
 editor authority, for example, setting the output message of an object.

static int
REASON\_ESCALATION\_RECEIVER
States that operations can be executed on the associated object that require
 escalation receiver rights, for example, reading properties of an object that is escalated.

static int
REASON\_INHERITANCE\_ADMINISTRATOR
States that operations can be executed on the associated object that require
 administrator rights.

static int
REASON\_INHERITANCE\_EDITOR
States that operations can be executed on the associated object that require
 editor rights.

static int
REASON\_INHERITANCE\_POTENTIAL\_OWNER
States that operations can be executed on the associated object that require
 potential owner rights.

static int
REASON\_INHERITANCE\_READER
States that operations can be executed on the associated object that require
 reader rights.

static int
REASON\_MAX
Do not use -internal only.

static int
REASON\_OPENER
States that operations can be executed on the associated object that require
 opener rights.

static int
REASON\_ORIGINATOR
States that operations can be executed on the associated object that require
 originator rights.

static int
REASON\_OWNER
States that the associated object can be completed.

static int
REASON\_POTENTIAL\_INSTANCE\_CREATOR
States that operations can be executed on the associated object that require
 instance creator rights, for example, creating objects.

static int
REASON\_POTENTIAL\_OWNER
States that the associated object can be claimed.

static int
REASON\_POTENTIAL\_SENDER
Deprecated. 
Not used.

static int
REASON\_POTENTIAL\_STARTER
States that operations can be executed on the associated object that require
 potential starter rights, for example, creating objects.

static int
REASON\_READER
States that operations can be executed on the associated object that require
 reader authority, for example, reading the properties of an object.

static int
REASON\_STARTER
States that operations can be executed on the associated object that require
 starter authority.

static int
REASON\_STATE\_MACHINE\_END
Do not use -internal only.

static int
REASON\_STATE\_MACHINE\_EVENT\_AVAILABLE
Do not use -internal only.

static int
REASON\_STATE\_MACHINE\_START
Do not use -internal only.

static int
REASON\_TRANSFER\_INITIATOR
States that operations can be executed on the associated object that require
 transfer initiator rights, for example, transferring objects into a work basket.
    - Method Summary

Methods 

Modifier and Type
Method and Description

int
getAssignmentReason()
Returns the reason why the work item is assigned.

int
getAssociatedObjectType()
Deprecated. 
As of version 7.0,0.3, obsolete for shared work items.

OID
getAssociatedOid()
Deprecated. 
As of version 7.0,0.3, obsolete for shared work items.

java.util.Calendar
getCreationTime()
Deprecated. 
As of version 7.0,0.3, obsolete for shared work items.

java.lang.String
getGroupName()
Returns the name of the group of persons associated with the work item.

com.ibm.bpe.api.WIID
getID()
Deprecated. 
As of version 7.0,0.3, obsolete for shared work items.

boolean
getIsAssignedToEverybody()
Returns whether the workitem is assigned to everybody.

OID
getObjectID()
Deprecated. 
As of version 7.0,0.3, obsolete for shared work items.

int
getObjectType()
Deprecated. 
As of version 7.0,0.3, obsolete for shared work items.

java.lang.String
getOwnerID()
Returns the user ID of the workitem owner if the
 work item is not assigned to everybody or to a group of persons.

- ============ FIELD DETAIL =========== ============ METHOD DETAIL ==========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
See Also:Constant Field Values

- OBJECT\_TYPE\_STATE\_MACHINE\_TEMPLATE
static final int OBJECT\_TYPE\_STATE\_MACHINE\_TEMPLATE
Do not use - internal only.
See Also:Constant Field Values

- OBJECT\_TYPE\_MAX
static final int OBJECT\_TYPE\_MAX
Do not use - internal only.
See Also:Constant Field Values

- OBJECT\_TYPE\_WORK\_BASKET
static final int OBJECT\_TYPE\_WORK\_BASKET
States that the work item has been created for a work basket.
See Also:Constant Field Values

- OBJECT\_TYPE\_TASK\_INSTANCE
static final int OBJECT\_TYPE\_TASK\_INSTANCE
States that the work item has been created for a task instance.
See Also:Constant Field Values

- OBJECT\_TYPE\_ESCALATION\_INSTANCE
static final int OBJECT\_TYPE\_ESCALATION\_INSTANCE
States that the work item has been created for an escalation instance.
See Also:Constant Field Values

- OBJECT\_TYPE\_ESCALATION\_TEMPLATE
static final int OBJECT\_TYPE\_ESCALATION\_TEMPLATE
Do not use - internal only.
See Also:Constant Field Values

- OBJECT\_TYPE\_TASK\_TEMPLATE
static final int OBJECT\_TYPE\_TASK\_TEMPLATE
Do not use - internal only.
See Also:Constant Field Values

- OBJECT\_TYPE\_STATE\_MACHINE\_INSTANCE
static final int OBJECT\_TYPE\_STATE\_MACHINE\_INSTANCE
Do not use - internal only.
See Also:Constant Field Values

- OBJECT\_TYPE\_APPLICATION\_COMPONENT
static final int OBJECT\_TYPE\_APPLICATION\_COMPONENT
Do not use - internal only.
See Also:Constant Field Values

- OBJECT\_TYPE\_ACTIVITY
static final int OBJECT\_TYPE\_ACTIVITY
States that the work item has been created for an activity instance.
See Also:Constant Field Values

- OBJECT\_TYPE\_PROCESS\_INSTANCE
static final int OBJECT\_TYPE\_PROCESS\_INSTANCE
States that the work item has been created for a process instance.
See Also:Constant Field Values

- OBJECT\_TYPE\_STATE\_MACHINE\_EVENT
static final int OBJECT\_TYPE\_STATE\_MACHINE\_EVENT
Do not use - internal only.
See Also:Constant Field Values

- OBJECT\_TYPE\_PROCESS\_TEMPLATE
static final int OBJECT\_TYPE\_PROCESS\_TEMPLATE
Do not use - internal only.
See Also:Constant Field Values

- OBJECT\_TYPE\_BUSINESS\_CATEGORY
static final int OBJECT\_TYPE\_BUSINESS\_CATEGORY
States that the work item has been created for a business category.
See Also:Constant Field Values

- OBJECT\_TYPE\_EVENT
static final int OBJECT\_TYPE\_EVENT
States that the work item has been created for a receive event.
See Also:Constant Field Values

- REASON\_POTENTIAL\_SENDER
static final int REASON\_POTENTIAL\_SENDER
Deprecated. Not used.
See Also:Constant Field Values

- REASON\_DISTRIBUTOR
static final int REASON\_DISTRIBUTOR
States that operations can be executed on the associated object that require
 distributor rights, for example, distributing objects to a work basket.
See Also:Constant Field Values

- REASON\_ESCALATION\_RECEIVER
static final int REASON\_ESCALATION\_RECEIVER
States that operations can be executed on the associated object that require
 escalation receiver rights, for example, reading properties of an object that is escalated.
See Also:Constant Field Values

- REASON\_INHERITANCE\_ADMINISTRATOR
static final int REASON\_INHERITANCE\_ADMINISTRATOR
States that operations can be executed on the associated object that require
 administrator rights. The right is inherited from an enclosing object.
See Also:Constant Field Values

- REASON\_STARTER
static final int REASON\_STARTER
States that operations can be executed on the associated object that require
 starter authority.
See Also:Constant Field Values

- REASON\_INHERITANCE\_EDITOR
static final int REASON\_INHERITANCE\_EDITOR
States that operations can be executed on the associated object that require
 editor rights. The right is inherited from an enclosing object.
See Also:Constant Field Values

- REASON\_STATE\_MACHINE\_EVENT\_AVAILABLE
static final int REASON\_STATE\_MACHINE\_EVENT\_AVAILABLE
Do not use -internal only.
 (deprecated) As of version 7.5, no replacement.
See Also:Constant Field Values

- REASON\_ORIGINATOR
static final int REASON\_ORIGINATOR
States that operations can be executed on the associated object that require
 originator rights.
See Also:Constant Field Values

- REASON\_CUSTOMROLE\_11
static final int REASON\_CUSTOMROLE\_11
States that operations can be executed on the associated object that require
 rights defined by custom role 11.
See Also:Constant Field Values

- REASON\_CUSTOMROLE\_10
static final int REASON\_CUSTOMROLE\_10
States that operations can be executed on the associated object that require
 rights defined by custom role 10.
See Also:Constant Field Values

- REASON\_CUSTOMROLE\_13
static final int REASON\_CUSTOMROLE\_13
States that operations can be executed on the associated object that require
 rights defined by custom role 13.
See Also:Constant Field Values

- REASON\_CUSTOMROLE\_12
static final int REASON\_CUSTOMROLE\_12
States that operations can be executed on the associated object that require
 rights defined by custom role 12.
See Also:Constant Field Values

- REASON\_OPENER
static final int REASON\_OPENER
States that operations can be executed on the associated object that require
 opener rights.
See Also:Constant Field Values

- REASON\_APPENDER
static final int REASON\_APPENDER
States that operations can be executed on the associated object that require
 appender rights.
See Also:Constant Field Values

- REASON\_STATE\_MACHINE\_START
static final int REASON\_STATE\_MACHINE\_START
Do not use -internal only.
 (deprecated) As of version 7.5, no replacement.
See Also:Constant Field Values

- REASON\_INHERITANCE\_POTENTIAL\_OWNER
static final int REASON\_INHERITANCE\_POTENTIAL\_OWNER
States that operations can be executed on the associated object that require
 potential owner rights. The right is inherited from an enclosing object.
See Also:Constant Field Values

- REASON\_ADMINISTRATOR
static final int REASON\_ADMINISTRATOR
States that operations can be executed on the associated object that require
 administrator rights, for example, deletion of an object.
See Also:Constant Field Values

- REASON\_STATE\_MACHINE\_END
static final int REASON\_STATE\_MACHINE\_END
Do not use -internal only.
 (deprecated) As of version 7.5, no replacement.
See Also:Constant Field Values

- REASON\_OWNER
static final int REASON\_OWNER
States that the associated object can be completed.
See Also:Constant Field Values

- REASON\_READER
static final int REASON\_READER
States that operations can be executed on the associated object that require
 reader authority, for example, reading the properties of an object.
See Also:Constant Field Values

- REASON\_INHERITANCE\_READER
static final int REASON\_INHERITANCE\_READER
States that operations can be executed on the associated object that require
 reader rights. The right is inherited from an enclosing object.
See Also:Constant Field Values

- REASON\_CUSTOMROLE\_1
static final int REASON\_CUSTOMROLE\_1
States that operations can be executed on the associated object that require
 rights defined by custom role 1.
See Also:Constant Field Values

- REASON\_CUSTOMROLE\_2
static final int REASON\_CUSTOMROLE\_2
States that operations can be executed on the associated object that require
 rights defined by custom role 2.
See Also:Constant Field Values

- REASON\_CUSTOMROLE\_3
static final int REASON\_CUSTOMROLE\_3
States that operations can be executed on the associated object that require
 rights defined by custom role 3.
See Also:Constant Field Values

- REASON\_POTENTIAL\_INSTANCE\_CREATOR
static final int REASON\_POTENTIAL\_INSTANCE\_CREATOR
States that operations can be executed on the associated object that require
 instance creator rights, for example, creating objects.
See Also:Constant Field Values

- REASON\_CUSTOMROLE\_4
static final int REASON\_CUSTOMROLE\_4
States that operations can be executed on the associated object that require
 rights defined by custom role 4.
See Also:Constant Field Values

- REASON\_CUSTOMROLE\_5
static final int REASON\_CUSTOMROLE\_5
States that operations can be executed on the associated object that require
 rights defined by custom role 5.
See Also:Constant Field Values

- REASON\_CUSTOMROLE\_6
static final int REASON\_CUSTOMROLE\_6
States that operations can be executed on the associated object that require
 rights defined by custom role 6.
See Also:Constant Field Values

- REASON\_EDITOR
static final int REASON\_EDITOR
States that operations can be executed on the associated object that require
 editor authority, for example, setting the output message of an object.
See Also:Constant Field Values

- REASON\_CUSTOMROLE\_7
static final int REASON\_CUSTOMROLE\_7
States that operations can be executed on the associated object that require
 rights defined by custom role 7.
See Also:Constant Field Values

- REASON\_CUSTOMROLE\_8
static final int REASON\_CUSTOMROLE\_8
States that operations can be executed on the associated object that require
 rights defined by custom role 8.
See Also:Constant Field Values

- REASON\_CUSTOMROLE\_20
static final int REASON\_CUSTOMROLE\_20
States that operations can be executed on the associated object that require
 rights defined by custom role 20.
See Also:Constant Field Values

- REASON\_CUSTOMROLE\_9
static final int REASON\_CUSTOMROLE\_9
States that operations can be executed on the associated object that require
 rights defined by custom role 9.
See Also:Constant Field Values

- REASON\_MAX
static final int REASON\_MAX
Do not use -internal only.
 (deprecated) As of version 7.5, no replacement.
See Also:Constant Field Values

- REASON\_CUSTOMROLE\_18
static final int REASON\_CUSTOMROLE\_18
States that operations can be executed on the associated object that require
 rights defined by custom role 18.
See Also:Constant Field Values

- REASON\_CUSTOMROLE\_19
static final int REASON\_CUSTOMROLE\_19
States that operations can be executed on the associated object that require
 rights defined by custom role 19.
See Also:Constant Field Values

- REASON\_CUSTOMROLE\_16
static final int REASON\_CUSTOMROLE\_16
States that operations can be executed on the associated object that require
 rights defined by custom role 16.
See Also:Constant Field Values

- REASON\_CUSTOMROLE\_17
static final int REASON\_CUSTOMROLE\_17
States that operations can be executed on the associated object that require
 rights defined by custom role 17.
See Also:Constant Field Values

- REASON\_CUSTOMROLE\_14
static final int REASON\_CUSTOMROLE\_14
States that operations can be executed on the associated object that require
 rights defined by custom role 14.
See Also:Constant Field Values

- REASON\_TRANSFER\_INITIATOR
static final int REASON\_TRANSFER\_INITIATOR
States that operations can be executed on the associated object that require
 transfer initiator rights, for example, transferring objects into a work basket.
See Also:Constant Field Values

- REASON\_CUSTOMROLE\_15
static final int REASON\_CUSTOMROLE\_15
States that operations can be executed on the associated object that require
 rights defined by custom role 15.
See Also:Constant Field Values

- REASON\_POTENTIAL\_STARTER
static final int REASON\_POTENTIAL\_STARTER
States that operations can be executed on the associated object that require
 potential starter rights, for example, creating objects.
See Also:Constant Field Values

- REASON\_POTENTIAL\_OWNER
static final int REASON\_POTENTIAL\_OWNER
States that the associated object can be claimed.
See Also:Constant Field Values

- Method Detail

### Method Detail

    - getID
com.ibm.bpe.api.WIID getID()
Deprecated. As of version 7.0,0.3, obsolete for shared work items.
Returns the object identifier.
    - getOwnerID
java.lang.String getOwnerID()
Returns the user ID of the workitem owner if the
 work item is not assigned to everybody or to a group of persons.
    - getIsAssignedToEverybody
boolean getIsAssignedToEverybody()
Returns whether the workitem is assigned to everybody. If assigned to
 everybody, the owner ID and the group name are null strings.
    - getObjectType
int getObjectType()
Deprecated. As of version 7.0,0.3, obsolete for shared work items.
Returns the type of the associated object.
    - getObjectID
OID getObjectID()
Deprecated. As of version 7.0,0.3, obsolete for shared work items.
Returns the object ID of the associated object.
    - getAssociatedObjectType
int getAssociatedObjectType()
Deprecated. As of version 7.0,0.3, obsolete for shared work items.
Returns the type of the object associated to or containing the work item's
 associated object.
    - getAssociatedOid
OID getAssociatedOid()
Deprecated. As of version 7.0,0.3, obsolete for shared work items.
Returns the object ID of the object associated to or containing the work item's
 associated object. For example, the PIID of the process instance containing the
 activity instance for which this work item has been created.
    - getAssignmentReason
int getAssignmentReason()
Returns the reason why the work item is assigned.
    - getCreationTime
java.util.Calendar getCreationTime()
Deprecated. As of version 7.0,0.3, obsolete for shared work items.
Returns the creation time of the work item.
    - getGroupName
java.lang.String getGroupName()
Returns the name of the group of persons associated with the work item. If there is no
 group associated, null is returned.