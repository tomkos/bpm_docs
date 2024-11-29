<!-- image -->

# Working with Cognos reports

- JAX-WS handler for a SOAP header

When using the Java API for XML Web Services (JAX-WS) a JAX-WS handler is needed to serialize and deserialize SOAP header information.
- JAX-RPC handler for a SOAP header

When using the Java API for XML-based RPC (JAX-RPC) a JAX-RPC handler is needed to serialize and deserialize SOAP header information.
- JAX-WS single sign-on security handler

A JAX-WS security handler is required when using the Java API for XML Web Services (JAX-WS) with single sign-on security. Single sign-on security is only available if Cognos is running on WebSphere Application Server.
- JAX-RPC single sign-on security handler

A JAX-RPC security handler is required when using the Java API for XML-Based RPC (JAX-RPC) with single sign-on security. Single sign-on security is only available if Cognos is running on WebSphere Application Server.
- Log on properties for a secure server

When authentication is required and single sign-on security cannot be used then you must use the authentication web service to logon to Cognos providing the appropriate security credentials.
- Log on properties for a server without security

Logging on to a Cognos server without security requires the Uniform Resource Locator (URL) for the Cognos server. No security credentials are needed.
- Retrieving a Cognos report

Retrieving a Cognos report may require a while loop construct invoking report retrieval, as a connection to the server may time out before the report is sent. An example using a short running business process is provided.

## Related tasks

- Setting up the preferences page for Cognos reports
- Viewing and importing a Cognos report as a web service