<!-- image -->

# API event handlers

If the pre-event method throws an ApplicationVetoException exception,
the API action is not performed, the exception is returned to the
API caller, and the transaction associated with the event is rolled
back. If the pre-event method was triggered by an internal event and
an ApplicationVetoException exception is thrown, the internal event,
such as an automatic claim, is not performed but an exception is not
returned to the client application. In this case, an information message
is written to the SystemOut.log file. If the API method throws an
exception during processing, the exception is caught and passed to
the post-event method. The exception is passed again to the caller
after the post-event method returns.

- Pre-event methods receive the parameters of the associated API
method or internal event.
- Pre-event methods can throw an ApplicationVetoException exception
to prevent processing from continuing.

- Post-event methods receive the parameters that were supplied to
the API call, and the return value. If an exception is thrown by the
API method implementation, the post-event method also receives the
exception.
- Post-event methods cannot modify return values.
- Post-event methods cannot throw exceptions; runtime exceptions
are logged and prevent processing from continuing.

To implement API event handlers, you can implement either the APIEventHandlerPlugin3 interface,
which extends the APIEventHandlerPlugin interface,
or extend the default com.ibm.task.spi.APIEventHandler SPI
implementation class. If your event handler inherits from the
default implementation class, it always implements the most recent
version of the SPI. If you upgrade to a newer version of Business
Process Choreographer, fewer changes are necessary if you want to
exploit new SPI methods.

If you have both a notification event handler and an API event
handler, both of these handlers must have the same name because you
can register only one event handler name.

## Stand-alone human tasks and the transactional behavior
of the event methods

To prevent the execution of the corresponding
API method, a pre-event method can throw a com.ibm.task.api.ApplicationVetoException checked
exception. In this case, the exception is reported to the calling
API client unchanged, and the current transaction is marked for rollback.
If a pre-event method does transactional work, such as updating database
tables, the updates will be rolled back if a com.ibm.task.api.ApplicationVetoException exception
is thrown.

Use the java.lang.RuntimeException and java.lang.Error exceptions
with care in API event handler implementations because they affect
the current transaction. If a pre-event or post-event method throws
a java.lang.RuntimeException or java.lang.Error exception,
the current transaction is marked for rollback. If the API event handler
does transactional work, such as updating database tables, this work
will be rolled back if one of these exceptions is thrown.

## Inline human tasks and the transactional behavior
of the event methods

Business Flow Manager also uses the
Human Task Manager API to control the lifecycle of inline human tasks.
For these calls, the API event handler is also invoked. In long running
processes, process navigation is driven by a chain of single transactions.

If
a rollback occurs, the transaction chain rolls back to the beginning
of the current individual transaction, and the navigation step is
retried. However, if an API event handler throws an exception,
it would lead to repeated rollbacks and retries after the transaction
is retried. To avoid these rollback-retry loops during navigation,
Business Flow Manager does not roll back if an exception is thrown
by an API event handler method. Instead, the transaction is committed
and the human task activity is put into the stopped state (continueOnError='false'),
or the corresponding fault handler is run.