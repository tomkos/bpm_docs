<!-- image -->

# Process instances

Business processes defined in Web Services Business Process Execution
Language (WS-BPEL) represent stateful web services, and as such, they
can have long-running interactions with other web services. Whenever
a BPEL process is started, a new instance of that process is created
that can communicate with other business partners. An instance completes
when its last activity completes, a terminate activity runs, or a
fault occurs that is not handled by the process.

Many process instance properties are inherited from the corresponding
process template. Others, such as the state of the process instance,
are assigned and modified during the lifetime of the process instance.
All of these properties are stored in the runtime database. They can
be accessed using the Business Process Choreographer database views,
such as the PROCESS\_INSTANCE view or QUERY\_PROPERTY view, or using
query tables.

- Correlation sets

Correlation is used to track the multiple, long-running exchanges of messages that typically take place between a BPEL process and its partner services. Correlation sets help to route messages to the appropriate process instance based on the contents of the message body thus enabling the process instance to hold a conversation with the partner service.