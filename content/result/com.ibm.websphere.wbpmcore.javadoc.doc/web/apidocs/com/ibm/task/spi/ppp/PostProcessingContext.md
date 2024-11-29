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

## Interface PostProcessingContext

- public interface PostProcessingContext
This interface provides for access to the post processing context.
Since:
7.0.0.2
Version:
7.0.0.2

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

ApplicationComponent
getApplicationComponent()
Returns the application component associated with the context.

int
getAssignmentReason()
Returns the assignment reason associated with the context.

Escalation
getEscalation()
Returns the escalation instance associated with the context.

EscalationTemplate
getEscalationTemplate()
Returns the escalation template associated with the context.

Task
getTask()
Returns the task instance associated with the context.

TaskTemplate
getTaskTemplate()
Returns the task template associated with the context.

- ============ FIELD DETAIL =========== ============ METHOD DETAIL ==========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
See Also:Constant Field Values

- Method Detail

### Method Detail

    - getAssignmentReason
int getAssignmentReason()
Returns the assignment reason associated with the context.
Returns:The assignment reason.
    - getTaskTemplate
TaskTemplate getTaskTemplate()
Returns the task template associated with the context.
Returns:The task template.
    - getEscalationTemplate
EscalationTemplate getEscalationTemplate()
Returns the escalation template associated with the context.
Returns:The escalation template.
    - getApplicationComponent
ApplicationComponent getApplicationComponent()
Returns the application component associated with the context.
Returns:The application component.
    - getTask
Task getTask()
Returns the task instance associated with the context.
Returns:The task object.
    - getEscalation
Escalation getEscalation()
Returns the escalation instance associated with the context.
Returns:The escalation instance.