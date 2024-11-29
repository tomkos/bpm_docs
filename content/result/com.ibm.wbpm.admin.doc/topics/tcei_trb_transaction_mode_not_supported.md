# Transaction mode not supported (message CEIEM0016E)

## Cause

- The event source is specifying a transaction mode that is not
valid.
- The event source is specifying a synchronization mode that is
not supported by the emitter environment. Transactions are supported
only in a Java EE container.

## Remedy

- If the emitter is running in a Java EE container, make sure the methodparameters specify one of the valid transaction modes: These constants are defined by the com.ibm.events.emitter.TransactionModeinterface.
    - TransactionMode.NEW
    - TransactionMode.SAME
    - TransactionMode.DEFAULT
- If the emitter is not running in a Java EE container, make sure the
method parameters specify TransactionMode.DEFAULT.