<!-- image -->

# Overview of cross-component tracing

When you enable cross-component tracing on a server, invocation
records are generated during Service Component Architecture (SCA)
processing of modules and components. The invocation records include
information about any errors or events that had occurred during processing,
such as runtime exceptions. If you choose to enable cross-component
tracing with the data snapshot feature, the generated invocation records
will also contain the invocation input and output data that was passed
between the components during processing.

You can enable or disable cross-component tracing for a server
from either the Server Logs view or the server administrative console.
If you enable cross-component tracing from the Server Logs view, the
tracing is only enabled for the duration of the server session. When
you next stop or restart the server, the cross-component trace state
will automatically be disabled by default. By comparison, if you enable
cross-component tracing for a server from the server administrative
console, the cross-component tracing will remain enabled for all sessions
of the server until you choose to disable it again.

When you enable or disable cross-component tracing, you can choose
from one of the following options: