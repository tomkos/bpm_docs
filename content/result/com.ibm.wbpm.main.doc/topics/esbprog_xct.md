<!-- image -->

# Cross-component trace

The Server Logs view displays standard server console and log records. However, if you enable
cross-component tracing, the Server Logs view also displays invocation records that contain the
invocation data that was passed between the components in your application. The invocation records
are displayed in hierarchical format in the Server Logs view, which enables you to more easily
understand the relationships that exist between the records. When you enable cross-component
tracing, the Server Logs view becomes an even more powerful tool for problem determination.
Typically, the process of using the Server Logs view for problem determination begins when you
encounter problems when testing your application using the integration test client or another tool.

1. Start the administrative console on a running server by right-clicking the server and from the
menu select Run administrative console.
2. Log on to the console, expand Troubleshooting and click Cross-Component Trace. Select your
server. For the Configuration values, select Enable with data snapshot as this collects the most
data, which is the recommended setting for tracing.
3. Save the configuration.
4. Log out of the administrative console and restart your server so the changes take effect.

<!-- image -->

<!-- image -->

<!-- image -->

The Server Logs view provides powerful filtering and searching capabilities to help you locate
useful information from a large number of log records. Detailed information about working with
server console and log records in the Server Logs view is found in the Integration Designer topic
FUsing the Server Logs view for problem determination.

Note that turning on the cross component trace has a performance impact on the server. When the
tracing is completed, you can turn off the cross component trace via the administrative console.