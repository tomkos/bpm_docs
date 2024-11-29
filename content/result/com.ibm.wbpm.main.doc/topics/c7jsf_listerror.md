<!-- image -->

# Error handling in the List component

## Errors that occur when queries are run or commands
are run

If an error occurs while running a query, the BPCListHandler class
distinguishes between errors that were caused by insufficient access
rights and other exceptions. To catch errors due to insufficient access
rights, the rootCause parameter of the ClientException that
is thrown by the execute method of the query must
be a com.ibm.bpe.api.EngineNotAuthorizedException or
a com.ibm.task.api.NotAuthorizedException exception.
The List component displays the error message instead
of the result of the query.

If the error is
not caused by insufficient access rights, the BPCListHandler class
passes the exception object to the implementation of the com.ibm.bpc.clientcore.util.ErrorBean interface
that is defined by the BPCError key in your JSF application configuration
file. When the exception is set, the error navigation target is called.

## Errors that occur when working with items that are
displayed in a list

The BPCListHandler class
implements the com.ibm.bpe.jsf.handler.ErrorHandler interface. You
can provide information about these errors with the map parameter
of type java.util.Map in the setErrors method.
This map contains identifiers as keys and the exceptions as values.
The identifiers must be the values returned by the getID method
of the object that caused the error. If the map is set and any of
the IDs match any of the items displayed in the list, the list handler
automatically adds a column containing the error message to the list.

- The refreshList method BPCListHandler class
is called.
- A new query is set on the BPCListHandler class.
- The CommandBar component is used to trigger
actions on items of the list. The CommandBar component
uses this mechanism as one of the methods for error handling.