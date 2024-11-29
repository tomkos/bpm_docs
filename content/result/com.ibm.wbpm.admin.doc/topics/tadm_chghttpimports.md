<!-- image -->

# Viewing and updating HTTP import bindings

## About this task

## Procedure

1. Select the module
that contains the binding by navigating to Applications > SCA Modules and clicking the
module name.
2 Selectthe binding by performing the following steps:
    1. In the Module components section,
expand Imports.
    2. Expand the import, and then
expand Binding.
    3. Click the binding to view
information about its properties.
3 Select the scope for thechanges you want to make. When both configurations exist, the method scope configurationtakes precedence over the binding scope configuration.

- To change the configuration on the binding scope, click the Binding
Scope tab.
- To change the configuration at the method scope, click the Method
Scope tab.

When both configurations exist, the method scope configuration
takes precedence over the binding scope configuration.

4 Make changes to one or more of the following properties:

- Select method (Method scope only)Choose the method that you want
to review or configure. Click the arrow in the Select method field to see the
list of methods that can be configured.
- Endpoint URLSpecifies the URL for the target service.
- HTTP Method
Specifies the method to use for the endpoint URL.
- HTTP versionSpecifies the HTTP version to use for this endpoint
URL. The choices are 1.0 and 1.1. The default is
1.1.
- Number of connection retriesSpecifies the number of times the
request is retried when the system receives an error response. The default is
0, which means that, after a failure, no attempt is made.
- Basic HTTP authenticationSpecifies the authentication alias to use
with the HTTP server on this binding. 
To choose the authentication alias, select the alias
name from the list. To change the attributes of a selected authentication alias, click
Edit. To create a new authentication alias, click
New.
- Authorization header propagationTo enable this custom property
(com.ibm.ws.http.PropagateAuthorizationHeader), you must define the system JVM
property. The header will be propagated across a module and, if you do not explicitly remove the
header, the header will be used in subsequent invocations in the same thread. Note, however, that
the values you set are not checked or validated. Therefore, an improper or incorrect header might
cause HTTP invocation problems at run time. When Authorization header propagation is enabled and the
HTTPAuthentication is also set, the Authorization header propagation has the
higher priority.
- SSL authenticationSpecifies the Secure Sockets Layer (SSL)
configuration to use for this binding. 
To edit an existing configuration, select the name
from the list and click Edit. To create a new configuration, click
New.
- Transfer EncodingSpecifies how information is transferred between
the endpoints. Choices are chunked or identity.

The chunked encoding modifies the body of a message in order to transfer it as a series of
chunks, each with its own size. This allows dynamically produced content to be transferred along
with the information necessary for the recipient to verify that it has received the full message.
Important: If you set this parameter to chunked, Content Encoding
is set to identity and you will be unable to change Content
Encoding.
- Content EncodingSpecifies how the content that traverses the
binding is encoded. Choose either gzip, x-gzip,
deflate, or identity.
- HTTP proxy settings or HTTPS proxysettings Specifies the settings for bindings that do not require securityauthorization for access (HTTP proxy settings ) or that do requireauthorization for access (HTTPS proxy settings ).
    - Proxy hostSpecifies the host name or IP address of an HTTP proxy
server through which to connect to the endpoint URL.
    - Proxy portSpecifies the port used to connect to an HTTP proxy server
for this binding.
    - Proxy credentialsSpecifies the Java2 Connectivity (J2C) authentication
alias to use for the proxy settings. 
To change an existing alias, select the alias from the
list and click Edit. To add a new alias, click
New.
    - Non-proxied hostsSpecifies a list of hosts on this binding that do not
use proxies. Enter each host on a separate line (use the Enter key). 
To add a host to the
list, type the host at the end of the list, separating it from the previous entry by clicking the
Enter key. To remove a host from the list, delete the host from the list.
- Response read timeoutSpecifies the time, in seconds, that the
binding waits to read the response message from the HTTP transport channel. Setting this field to
0 causes the binding to wait indefinitely.Note: The HTTP transport channel
has its own Read timeout value, which is the amount of time that the channel waits for a read
request to complete on a socket after the first read request occurs. This setting is described in
 HTTP transport channel settings in the WebSphere Application Server
documentation.
5. Save your changes to the master configuration.

## Results

To ensure
that the changes you made remain with the module across deployments,
use IBM Integration Designer to make the changes in the source code
for the module.