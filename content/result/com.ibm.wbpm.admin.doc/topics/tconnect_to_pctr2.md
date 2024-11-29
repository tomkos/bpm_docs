# Using the administrative console to customize the Workflow Server used
to connect to Workflow Center

## About this task

Workflow Server
initially connects to Workflow Center by using a connection
defined in processCenterUrl. Workflow Center then tells Workflow Server which URL to connect
with depending on the endpoint resolution for the INTERNAL\_CLIENT and WS\_TO\_WC endpoint scenarios.
So you don't have multiple URLs used during each connection, set up the settings to generate the
same URLs. For more information about this connection, see Connections from IBM Process Server to Workflow Center.

- Modify the environment type of the workflow server.
- Change a workflow server from an offline server to a workflow center connected server (online
server), and vice-versa.
- Modify the connection properties to enable a workflow server to connect to a different workflow
center.

## Procedure

To customize the settings that are used by a workflow server to connect to a workflow
center, complete the following steps.

1. Log into the administrative console.
2. If your environment has not yet been started, start the environment by following the
instructions in the topic Starting and stopping your environment.
3. In the tree view, select Servers > Deployment Environments > Deployment environment name > Additional Properties > Workflow Server Settings. The Workflow Server Settings page
opens.
4. In the Environment name field, specify
the name by which the server or cluster will be known to a Workflow Center user.
5. In the Environment type drop-down list, select the environment type for
the workflow server that you are configuring.

The environment type specifies whether the workflow server will be used for development, test,
staging, or production. For example, you could select Test if load testing
will be performed on the server. Or you could select Staging if the server is
to be used as a temporary location to host changes before putting the changes into production. You
might also select Staging if the workflow server that you are configuring
will be accessed and used to review content and new functionality.
6. If you are configuring an offline server, select Use
server offline. An offline server is a workflow server that is not connected to the workflow center. Offline
servers can still be used when deploying snapshots of process applications. However, the method for
deploying process applications to an offline workflow server differs from the method for deploying
process applications to an online workflow server.
7. In the Protocol drop-down list, select either
http:// or https:// as the connection protocol to the
workflow center. Configure a full URL path by selecting http:// or
https:// and then setting the host and port.

 In an environment with a load balancer or proxy server between the browser and the Workflow Server services, make sure that what you designate
here matches the browser URL for accessing the workflow center.
8. In the Host name or virtual host in a load-balanced environment field,
specify the host or virtual host that the workflow server needs to communicate with the process
center. Use a fully qualified host name.

In an environment with a load balancer or proxy server between the workflow server and the
Workflow Center services, make sure that what you
designate here matches the URL for accessing the workflow center. Note: Ensure that you specify the
host name instead of localhost for the server name when you configure the
workflow server. This is required when you are using Process Designer remotely.
9. In the Port field, specify the port number of the workflow center.

In an environment with a load balancer or proxy server between the workflow server and the
workflow center, make sure that what you designate here matches the URL for accessing the workflow
center.
10. In the Context root prefix field, specify the prefix of the default
context root for the workflow center (if any). The prefix value requires a leading forward slash
(/). Leave this field blank if no context root prefix is set for the workflow center.
11. In the User name field, specify a valid user name that exists on the
workflow center. The workflow server will connect to the workflow center as this user.

An authentication alias will be created using this user name and password. The authentication
alias will be automatically mapped to the ProcessCenterUser role. The user name and password of the
ProcessCenterUser for Workflow Server must be a
valid user from the Workflow Center user
repository.
12. In the Password and Confirm
Password fields, specify the password of the user.
13. Save your changes and restart the workflow server.

## Results