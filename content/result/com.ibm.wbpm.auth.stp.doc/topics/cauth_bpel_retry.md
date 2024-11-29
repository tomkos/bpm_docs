<!-- image -->

# BPEL process retries

If an error occurs, and the transaction is marked for rollback,
the process engine rolls back the transaction and attempts to invoke
each activity in its own transaction to advance the state of the process,
essentially performing a retry.

If you want a set of activities to be invoked in one transaction,
use a microflow instead of a long-running BPEL process.

When an activity in a long-running BPEL process asynchronously
invokes a partner operation, if a runtime exception occurs, retries
occur as specified by the retry count for the module. On the last
retry, if a runtime exception is raised, the exception flows back
to the BPEL process for error handling. However, the error handling
for a store and forward qualifier takes precedence if you have it
configured.