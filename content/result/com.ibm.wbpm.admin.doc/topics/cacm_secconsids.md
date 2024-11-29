<!-- image -->

# Security considerations for integrating BPEL processes with IBM Business Automation
Workflow tasks

User name and password credentials are also required on the response
of a long-running BPEL process from IBM Business Automation Workflow to IBM Business Automation
Workflow and
are facilitated by the import.

The following sections provide information on the security token
that includes the user name and password as well as information about
SSL.

## Username security token

The user name and
password credentials make up the security token for communication
between a web services module and a case management task.

A
security token represents a set of claims made by a client. The security
token is embedded in the SOAP message within the SOAP header and is
propagated from the message sender to the intended message receiver.
On the receiving side, the web services security handler authenticates
the security token and sets up the caller identity on the running
thread.

By default, the FileNet® P8
Component Manager service user credentials are used for authentication
with the service.  The Component Manager provides an option to configure
different credentials for the service on Workflow Server.

Because it is possible for the SOAP header from the message
sender to contain more than one security token, you must indicate
which token should be used for authenticating the caller's identity.

1. From the administrative console, click Services > Service providers.
2. From the Service provider pages, click the name of the web service.
3. From the web service page, click the policy set binding.
4. Click WS-Security.
5. Click Caller.
6 On the Callers page, perform the following steps:
    1. Click New.
    2. In the Name field, enter an arbitrary name
for the security token that identifies the caller.
    3. In the Caller identity local part field,
enter: http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-username-token-profile-1.0#UsernameToken
7. Click OK.

```
set psm [$AdminControl queryNames type=PolicySetManager,*] 
$AdminControl invoke $psm refresh
```

If you select Create a long-running business process,
the response to IBM Business Automation
Workflow occurs
in a separate flow, and you need to specify the client user name security
token on the import by configuring the callback handler.

1. From the administrative console, click Services > Service clients.
2. On the Service clients page, click the web service module you
deployed.
3. In the Policy Set Attachments section of
the Configuration tab, click BPM FileNet Web Services -
Client.
4. On the binding page, click WS-Security.
5. On the WS-Security page, click Authentication and protection.
6. On the Authentication and protection page, click gen\_unametoken.
7 On the gen\_unametoken page, perform the following steps:
    1. From the Token type list, select Username
Token v1.0.
    2. From the JAAS login list, select wss.generate.unt.
    3. In the Additional Bindings section, click Callback
handler.
8. In the Basic Authentication section, enter a user name. Then enter
a password in the Password field and the Confirm
password field.The user name and password for the invocation
back to Case Manager must be a valid FileNet P8
account with the appropriate permissions for this operation, as described
in the #AUTHENTICATED-USERS topic of the FileNet P8 documentation. Only authenticated
users have the correct permissions to view and edit a case.
9. Select OK.

```
set psm
[$AdminControl queryNames type=PolicySetManager,*] $AdminControl
invoke $psm refresh
```

For additional information,
see the Callback handler settings topic in the WebSphere® Application Server Information
Center.

## SSL configuration

- Do not create a business process The
SSL setting applies to the request and response.
- Create a microflow The SSL setting applies
to the request and response.
- Create a long running business process The
SSL setting applies, by default, only to the request.
The response
flow on a long running BPEL process does not automatically use SSL.
The setting on the response is governed by the SSL configuration on
the FileNet P8 system. 
You
should ensure that the FileNet P8
Component Manager is configured to use a secure socket connection
so that the response data is encrypted. The callback address that
you use to reply to IBM Business Automation
Workflow must
include https and a secure port in the address.

To establish secure communications, a certificate
and an SSL configuration must be specified for the endpoint. To set
up SSL configuration on Workflow Server, see Creating
a Secure Sockets Layer configuration in the WebSphere Application Server Information
Center.