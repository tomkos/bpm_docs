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

## Interface ReplyHandler

- All Superinterfaces:
java.io.Serializable

public interface ReplyHandler
extends java.io.Serializable
This interface supports an asynchronous mode of operation.
 A reply handler implementation has to be provided for methods that support reply handler parameters.
 
 A client that uses these API methods has to create an object that implements the ReplyHandler interface
 so that the Human Task Manager knows where to send the results of operation.
 When a task that was started with a reply handler reaches an end state,
 the Human Task Manager calls replyResult() or replyException() depending on the result of processing.
 It is the responsibility of the implementation of this interface to perform the necessary actions
 in order to inform the caller about the result of processing.
Since:
6.0

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

void
replyException(TKIID tkiid,
              TaskException faultException)
Signals the unsuccessful processing of a task.

void
replyResult(TKIID tkiid,
           java.io.Serializable resultMessage)
Signals the successful processing of a task.

- ============ FIELD DETAIL =========== ============ METHOD DETAIL ==========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
See Also:Constant Field Values

- Method Detail

### Method Detail

    - replyResult
void replyResult(TKIID tkiid,
               java.io.Serializable resultMessage)
Signals the successful processing of a task. For an unsuccessful processing, see
 the replyException() method.
Parameters:tkiid - The ID of the task whose output message is to be returned.resultMessage - The output message that represents the result of processing.
    - replyException void replyException(TKIID tkiid, TaskException faultException) Signals the unsuccessful processing of a task. That is, returns a fault message. The fault message may wrap an exception thrown when starting the task or during processing. Successful completion messages are replied using the replyResult() method. Parameters: tkiid - The ID of the task whose fault is to be returned. faultException - The task exception to be reported. The following children of TaskException have a special meaning: Further children of TaskException can signal unexpected runtime faults.

#### replyException

```
void replyException(TKIID tkiid,
                  TaskException faultException)
```

    - TaskBusinessException
          is used when the task is completed with a fault message.
          The exception carries fault name, fault message, and further fault data.
    - TaskTerminatedException
          is used when the task has been terminated with the
          terminate() method.
    - TaskExpiredException
          is used when the task has expired.