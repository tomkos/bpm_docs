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

## Interface ReplyContext

- All Superinterfaces:
java.io.Serializable

public interface ReplyContext
extends java.io.Serializable
This interface supports an asynchronous mode of operation.
 A reply context has to be provided for callWithReplyContext methods.
 
 A client that uses these API methods has to create an object that implements the ReplyContext interface
 so that the process engine knows where to send results to.
 When a process instance that was started via the callWithReplyContext() API reaches its end,
 the process engine calls replyProcessResult() or replyException() depending on the result of processing.
 It is the responsibility of the implementation of this interface to perform the necessary actions
 in order to inform the caller about the result of processing.
Since:
5.0

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT 

static long
serialVersionUID
    - Method Summary

Methods 

Modifier and Type
Method and Description

void
replyException(int processState,
              java.lang.String processInstanceName,
              java.lang.Exception exception)
Signals the unsuccessful execution of a process.

void
replyProcessResult(int processState,
                  java.lang.String processInstanceName,
                  java.lang.Object resultMessage)
Signals the successful end of process execution and returns an output message.

- ============ FIELD DETAIL =========== ============ METHOD DETAIL ==========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
See Also:Constant Field Values

- serialVersionUID
static final long serialVersionUID
See Also:Constant Field Values

- Method Detail

### Method Detail

    - replyProcessResult
void replyProcessResult(int processState,
                      java.lang.String processInstanceName,
                      java.lang.Object resultMessage)
                        throws SendReplyErrorException
Signals the successful end of process execution and returns an output message.
 For an unsuccessful processing, refer to the replyException method.
Parameters:processState - The final state of the process instance, either finished, failed, terminated, or compensated.processInstanceName - The name of the process instance.resultMessage - The output message that represents the result of execution.
Throws:
SendReplyErrorException - if the process instance result cannot be returned.
    - replyException
void replyException(int processState,
                  java.lang.String processInstanceName,
                  java.lang.Exception exception)
                    throws SendReplyErrorException
Signals the unsuccessful execution of a process. That is, either returns a fault message
 or signals that a system exception terminated process instance execution.
 Successful completion messages are returned using the replyProcessResult method.
Parameters:processState - The state of the process instance.processInstanceName - The name of the process instance.exception - The exception that terminated processing. Can be any subclass of ProcessException or
    ProcessError or one of its subclasses.
Throws:
SendReplyErrorException - if the exception cannot be returned.