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

## Interface ProcessTemplateActions

- public interface ProcessTemplateActions
This interface defines symbolic constants for all actions that can be performed on
 process templates. These constants are to be used when determining the actions
 allowed on the process template by the current user.
 Currently allowed actions are returned
 when calling the getAvailableActions()
 method on a process template.
Since:
5.0

- =========== FIELD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static int
CALL
Symbolic constant for process template action call.

static java.lang.String
COPYRIGHT 

static int
CREATEMESSAGE
Symbolic constant for process template action create message.

static int
GETCUSTOMATTRIBUTE
Deprecated. 
Use GETCUSTOMPROPERTY.

static int
GETCUSTOMPROPERTY
Symbolic constant for process template action get customer property.

static int
GETENDPOINTFORPROCESSTEMPLATE
Symbolic constant for process template action get endpoint reference for process template.

static int
GETGRAPHICALPROCESSMODEL
Symbolic constant for process template action get graphical representation for process template.

static int
GETMIGRATIONTARGETS
Symbolic constant for process template action get migration targets for process template.

static int
GETPROCESSTEMPLATE
Symbolic constant for process template action get process template.

static int
GETQUERYPROPERTIES
Symbolic constant for process template action get query properties for process template.

static int
GETSTARTACTIVITIES
Symbolic constant for process template action get start activities.

static int
GETUISETTINGS
Symbolic constant for process template action get UI settings.

static int
INITIATE
Symbolic constant for process template action initiate.

static int
QUERYPROCESSTEMPLATE
Symbolic constant for querying process templates.

- ============ FIELD DETAIL ===========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
See Also:Constant Field Values

- CALL
static final int CALL
Symbolic constant for process template action call.
See Also:Constant Field Values

- INITIATE
static final int INITIATE
Symbolic constant for process template action initiate.
See Also:Constant Field Values

- QUERYPROCESSTEMPLATE
static final int QUERYPROCESSTEMPLATE
Symbolic constant for querying process templates.
See Also:Constant Field Values

- GETCUSTOMATTRIBUTE
static final int GETCUSTOMATTRIBUTE
Deprecated. Use GETCUSTOMPROPERTY.
Symbolic constant for process template action get customer attribute.
See Also:Constant Field Values

- GETCUSTOMPROPERTY
static final int GETCUSTOMPROPERTY
Symbolic constant for process template action get customer property.
See Also:Constant Field Values

- GETPROCESSTEMPLATE
static final int GETPROCESSTEMPLATE
Symbolic constant for process template action get process template.
See Also:Constant Field Values

- GETUISETTINGS
static final int GETUISETTINGS
Symbolic constant for process template action get UI settings.
See Also:Constant Field Values

- CREATEMESSAGE
static final int CREATEMESSAGE
Symbolic constant for process template action create message.
See Also:Constant Field Values

- GETSTARTACTIVITIES
static final int GETSTARTACTIVITIES
Symbolic constant for process template action get start activities.
See Also:Constant Field Values

- GETENDPOINTFORPROCESSTEMPLATE
static final int GETENDPOINTFORPROCESSTEMPLATE
Symbolic constant for process template action get endpoint reference for process template.
See Also:Constant Field Values

- GETGRAPHICALPROCESSMODEL
static final int GETGRAPHICALPROCESSMODEL
Symbolic constant for process template action get graphical representation for process template.
See Also:Constant Field Values

- GETQUERYPROPERTIES
static final int GETQUERYPROPERTIES
Symbolic constant for process template action get query properties for process template.
See Also:Constant Field Values

- GETMIGRATIONTARGETS
static final int GETMIGRATIONTARGETS
Symbolic constant for process template action get migration targets for process template.
See Also:Constant Field Values