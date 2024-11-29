<!-- image -->

# Using the Server Logs view for problem determination

## About this task

- Overview of cross-component tracing

By default, the Server Logs view displays standard server console and log records. However, if you enable cross-component tracing, the Server Logs view will also display invocation records that can contain the invocation data that was passed between the components in your application. The invocation records are displayed in hierarchical format in the Server Logs view, which enables you to more easily understand the relationships that exist between the records. When you enable cross-component tracing, the Server Logs view becomes an even more powerful tool for problem determination.
- Server Logs view

The Server Logs view is used to display server console and log file records. Although the Server Logs view automatically displays console records for each server that is started, you can also manually load and display the server console and log file records for any server. When cross-component tracing is enabled, the Server Logs view will also display invocation records that can contain the invocation data that passed between components. The Server Logs view is the recommended tool for working with server console and log records. It provides several advantages over the traditional Console view, such as the ability to filter records, display invocation records in hierarchical format, and load invocation records directly into the integration test client.
- Getting started with the Server Logs view

In IBM Integration Designer, the Server Logs view is the designated tool for working with server console and log records. Typically, the process of using the Server Logs view for problem determination begins when you encounter problems when testing your application using the integration test client or another tool. In this end-to-end introduction to the Server Logs view, it is assumed that you are working with the test client when you encounter problems in your application.
- Working with server console and log records in the Server Logs view

The Server Logs view provides numerous tools that enable you to effectively work with server console and log records.