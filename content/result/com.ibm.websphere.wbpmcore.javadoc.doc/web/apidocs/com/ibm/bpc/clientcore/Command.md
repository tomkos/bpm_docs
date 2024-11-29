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

## Interface Command

- public interface Command
Represents an action on Business Process Choreographer application objects.
 
 Implement this interface to add commands to the Business Process Choregrapher
 client application.
 The action's functionality is to be encapsulated in execute(List).
 The command implementation must check any preconditions and the context before it performs the 
 execute method. If the execute method succeeds, it returns a String to indicate the result. 
 The caller can use this string to determine the following actions, e.g. determine the next
 view on the user interface. If the execute method fails, it throws a ClientException.
 If the command is used as a batch command, the command can report several exceptions that relate to diverent items using an   
 ErrorsInCommandException.

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT
(C) Copyright IBM Corporation 2005.
    - Method Summary

Methods 

Modifier and Type
Method and Description

java.lang.String
execute(java.util.List selectedObjects)
Excutes the command on a list of Business Process Choregrapher application objects.

boolean[]
isApplicable(java.util.List itemsOnList)
Checks if the command's preconidtions are met for the list of selected objects.

boolean
isMultiSelectEnabled()
Indicates if the command is enabled for multiple selection.

void
setContext(java.lang.Object context)
Sets the context object for the Command.

- ============ FIELD DETAIL =========== ============ METHOD DETAIL ==========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
(C) Copyright IBM Corporation 2005.
See Also:Constant Field Values

- Method Detail

### Method Detail

    - execute
java.lang.String execute(java.util.List selectedObjects)
                         throws ClientException
Excutes the command on a list of Business Process Choregrapher application objects.
Parameters:selectedObjects - The environment must provide the list of application objects on which the Command is to be executed.
Returns:A String indicating the outcome of the command.
Throws:
ClientException
    - isMultiSelectEnabled
boolean isMultiSelectEnabled()
Indicates if the command is enabled for multiple selection.
Returns:true if the command can handle multiple objects. false if the command can only handle a single object.
    - isApplicable
boolean[] isApplicable(java.util.List itemsOnList)
Checks if the command's preconidtions are met for the list of selected objects.
Parameters:itemsOnList - The list of objects to be checked.
Returns:An array of boolean values which indicate if the Command is applicable to the corresponding item in the list.
    - setContext
void setContext(java.lang.Object context)
Sets the context object for the Command. A context object provides required information to the command implementation during
 its execute(List) method.
Parameters:context - The context object which the command implementation uses.