# Servers
and recovery mode processing

These recovery logs, which each transactional resource
maintains,
are used to rerun any Indoubt transactions and return the overall
system to a self-consistent state. An indoubt transaction is
one that has encountered environmental or other errors during commit
processing.  Logging occurs for normal inflight transactions, but
those log entries are removed upon successful commit processing.

This
recovery process begins as soon as all of the necessary subsystems
within the application server are available during a server startup.
If the application server is not restarted in recovery mode, the application
server can start accepting new work as soon as the server is ready,
which might occur before the recovery work has completed. This might
be okay in many cases, but the more conservative option is provided
here. To be clear, recovery will run on a server restart even
if the server is started in 'normal' start model.