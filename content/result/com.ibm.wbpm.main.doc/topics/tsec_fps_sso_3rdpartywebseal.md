# Configuring single sign-on for federated environments by using IBM Security Access
Manager WebSEAL

## Before you begin

- The Process Federation Server, the federated
servers, including the server that hosts Process Portal, and WebSEAL must be in the same domain.
(This condition is recommended, but not mandatory.)
- SSO must be enabled for the federated servers. See Configuring SSO for federated environments by using LTPA keys. (This
condition is recommended, but not mandatory.)
- WebSEAL is installed, configured, and integrated in the environment.
- The federated  servers and Process Federation Server use the same user registry as WebSEAL.
- The realm ID that the user registry uses and the realm ID in the
LTPA key file must be the same. (This condition is recommended, but
not mandatory.)

## About this task

The federated environment supports cookie-based LTPA for user authentication. For federated
environments that include WebSEAL, the user must first authenticate to WebSEAL when a user requests
a resource.

After the authentication is successful, WebSEAL generates the LTPA cookie for the user. This
cookie is the authentication token for the federated environment. WebSEAL inserts the cookie in the
HTTP header of the request that is sent across the junction to a federated server. The server
receives the request, decrypts the cookie, and authenticates the user based on the identity
information in the cookie.

## Procedure

1. Import the signer certificates for the federated servers and Process Federation Server into WebSEAL. 
For information, see the IBM Security Access
Manager
WebSEAL documentation.
2. Add junctions in WebSEAL for the federated servers and Process Federation Server.

For information, see the IBM Security Access
Manager
WebSEAL documentation.
3. Add user groups and group members to the WebSEAL access
control list (ACL). For information, see the IBM Security Access
Manager WebSEAL
documentation.
4 Update the Process Federation Server server.xml configurationfile with WebSEAL configuration information:
    1. Open the server.xml configuration file for
editing.
By default, the configuration file is in the
pfs\_install\_root/usr/servers/server\_name directory on
Process Federation Server.
    2. In the usr\_federatedSystem section,
update the groupUrlTemplate, restUrlPrefix,
and taskCompletionUrlPrefix properties to use
the WebSEAL host name. For information about the configuration
properties, see Configuration properties for the Process Federation Server index.