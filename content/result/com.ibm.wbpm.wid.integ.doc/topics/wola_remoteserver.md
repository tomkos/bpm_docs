<!-- image -->

# Testing WOLA-enabled applications on a remote server

You must specify the remote connection properties in the connection
factory specified by the JNDI name, or in the New External
Service wizard, on the Security and Configuration
Properties page under the Remote connection properties
area, you must select Remote connection properties and
select Use remote to perform remote testing.

To communicate with a COBOL, PL/I, C, or C++ program on the target
system (CICS or IMS) from a remote WebSphere Application Server for z/OS,
you must set the appropriate connections properties in addition to
the following remote properties:

- Host name - Specifies the host name where
the JNDI lookup of the OLA proxy EJB is directed when applications
run on a remote WebSphere Application Server for z/OS.
- Port - Specifies the ORB listener port number
for the remote server where the OLA proxy EJB runs. To determine this
value, log in to the administrative console for the proxy application
server and click Servers > Server
Types > WebSphere application servers > Server\_Name > Ports and search for ORB\_LISTENER\_ADDRESS.
- JNDI name - Specifies the JNDI name on the
remote server where the OLA proxy EJB is bound. The default OLA proxy
JNDI name is com.ibm.ws390.ola.jca.ProxyEJBRemote.
This can be modified if there are namespace issues. If overriding
this JNDI name, you must change the ola\_remote\_ejb\_proxy\_indiname environmental
variable for the OLA proxy EJB.
- JNDI realm - Specifies the security realm
that the EJB proxy runs. The security realm is the collection of users
and groups that are controlled by the same authentication policy.
- JNDI user name - Specifies the user name
that is used to obtain the JNDI initial context on the remote server.
- JNDI password - Specifies the password to
be used with the JNDI user name.
- User name - Specifies the name of the user
who sends requests to an external address space (batch program or
a CICS or IMS transaction) over WOLA. This user name identifies the
z/OS user ID. If no z/OS user ID is associated with the user name,
no identity is set on the request. If no user name is specified, the
identity of the OLA proxy server for WebSphere® Application Server
for z/OS is used.
- Password - Specifies the password for the
user name.

For more information about the remote properties, see Configuring optimized local adapters in development
mode on the local node.

1 Ensure that the JNDI realm name is defined in the local applicationserver that the WOLA proxy EJB runs on. To set the JNDI name:
    1. Log in to the administrative console.
    2. Select Security > Global
Security > CSIv2 Outbound Communications > Add external realm.
2 Connect to the application server that runs the WOLA proxy EJBover an SSL-enabled connection, ensuring that the local applicationserver has retrieved and stored a valid signature certificate fromthe application server on z/OS.

1. Log in to the administrative console for the proxy application
server and select Security > SSL certificate and key management > Key
stores and certificates > NodeDefaultTrustStore > Signer certificates, and then
select retrieve from port.
2. Provide the host name of the proxy server and the port number
for an SSL-enabled port.