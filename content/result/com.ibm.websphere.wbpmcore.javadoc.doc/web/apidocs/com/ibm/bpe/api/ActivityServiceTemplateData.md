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

## Interface ActivityServiceTemplateData

- All Superinterfaces:
java.io.Serializable

All Known Implementing Classes:
ActivityServiceTemplateBean

public interface ActivityServiceTemplateData
extends java.io.Serializable
Accesses the properties of an activity service.
 
 An activity service template is a description of a service a process interacts with.
 
 Interactions are either inbound receive or pick activities or outbound reply
 or invoke activities.
 
Since:
5.1

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT
    - Method Summary

Methods 

Modifier and Type
Method and Description

java.lang.String
getActivityDescription()
Returns the description of the associated activity.

java.lang.String
getActivityDisplayName()
Returns the display name of the associated activity.

java.lang.String
getActivityName()
Returns the name of the associated activity.

ATID
getActivityTemplateID()
Returns the object ID of the associated activity.

int[]
getAvailableActions()
Returns the actions that can be called in the current activity instance execution state.

java.lang.String
getInputMessageTypeName()
Returns the name of the input message type.

java.lang.String
getInputMessageTypeTypeSystemName()
Deprecated. 
As of version 6.0, no replacement.

java.lang.String
getOperationName()
Returns the name of the operation.

java.lang.String
getPartnerLinkName()
Returns the name of the partner.

java.lang.String
getPortTypeName()
Returns the name of the partner's port type.

java.lang.String
getPortTypeNamespace()
Returns the namespace of the operation.

PTID
getProcessTemplateID()
Returns the object ID of the process template this activity is part of.

java.lang.String
getProcessTemplateName()
Returns the name of the process template this activity is part of.

VTID
getServiceTemplateID()
Returns the object ID of the activity service described.

TKTID
getTaskTemplateID()
Returns the object ID of the associated task template.

boolean
isTwoWayOperation()
Returns whether the service to be called is a two-way
 operation or not.

- ============ FIELD DETAIL =========== ============ METHOD DETAIL ==========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
See Also:Constant Field Values

- Method Detail

### Method Detail

    - getAvailableActions
int[] getAvailableActions()
Returns the actions that can be called in the current activity instance execution state.
 Refer to ActivityServiceTemplateActions for the set
 of possible actions.
    - getPartnerLinkName
java.lang.String getPartnerLinkName()
Returns the name of the partner.
    - getPortTypeName
java.lang.String getPortTypeName()
Returns the name of the partner's port type.
    - getOperationName
java.lang.String getOperationName()
Returns the name of the operation.
    - getActivityName
java.lang.String getActivityName()
Returns the name of the associated activity. If there is no name,
 a null string is returned.
    - getActivityDisplayName
java.lang.String getActivityDisplayName()
Returns the display name of the associated activity. If there is no display name,
 a null string is returned.
    - getActivityDescription
java.lang.String getActivityDescription()
Returns the description of the associated activity. If there is no description,
 a null string is returned.
    - getServiceTemplateID
VTID getServiceTemplateID()
Returns the object ID of the activity service described.
    - getActivityTemplateID
ATID getActivityTemplateID()
Returns the object ID of the associated activity.
    - getProcessTemplateID
PTID getProcessTemplateID()
Returns the object ID of the process template this activity is part of.
    - getTaskTemplateID
TKTID getTaskTemplateID()
Returns the object ID of the associated task template. This is the ID of an
 invocation aka originating task template for incoming requests.
    - getPortTypeNamespace
java.lang.String getPortTypeNamespace()
Returns the namespace of the operation.
    - getInputMessageTypeName
java.lang.String getInputMessageTypeName()
Returns the name of the input message type.
    - getInputMessageTypeTypeSystemName
java.lang.String getInputMessageTypeTypeSystemName()
Deprecated. As of version 6.0, no replacement.
Returns the name of the type system of the input message type.
    - getProcessTemplateName
java.lang.String getProcessTemplateName()
Returns the name of the process template this activity is part of.
    - isTwoWayOperation
boolean isTwoWayOperation()
Returns whether the service to be called is a two-way
 operation or not.
Since:
7.0.