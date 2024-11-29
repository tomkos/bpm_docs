# Adding a web services server in the desktop Process Designer (deprecated)

## Before you begin

To perform
this task, you must be in the IBM® Process
Designer desktop
editor, which is deprecated.

## About this task

- Security tokens: Security tokens contain authentication information
that flows with the message.
- Signature elements: Digital signature information for all or part
of the message verifies that the original request is not modified.
- Encryption elements: Messages can be encrypted, either completely
or partially, so that only the intended recipient can read it.

## Procedure

1. Open the desktop Process Designer (deprecated).
2. Open a process application.
3. Select the Servers tab from the Process
App Settings editor. You see the Process App
Settings editor when you first click Open in
Designer from a newly created process application in the Workflow Center. Alternatively
you can select Process App Settings from the
drop-down list on the toolbar in Process Designer.
4. Beneath the Servers heading click Add.
Beneath the Server Details heading, enter a
meaningful name for the server. From the drop-down list in the Type field,
select Web Service. Add a meaningful description
of the server in the Description field.
5 Beneath the Server Locations heading,enter the following information:
    - Environment Type : The environment of theweb service server. Add the server location information (host name,port, context path, whether it is a secure server, repository name,user ID, and password) for each environment type. These environmentsare described in the IBM Business Automation Workflow editions . If youdo not provide values for these environments, the values from thedefault environment type are used.
        - Default: If you do not provide values for
the following environment types, default values are used.
        - Development: The environment where you
develop your services.
        - Test: The environment where you test your
services.
        - Staging: The environment where you deploy
your services for pre-production testing.
        - Production: The environment where your
services are deployed for use by your organization.
- WSDL URL : The URL of the web service. Forexample: http://mycorporation.com/webservice/financialstatements?wsdl .You can enter a URL or browse to retrieve a URL.
    - Select Browse to launch the Registry Explorer. If you use the Registry Explorer, the WSDL URL , ProtectedWSDL , Username , and Password fieldsare populated automatically. If you enter the URL manually, you mustprovide the other information about the WSDL file. You can use textin the fields or text that is wrapped by <# ... #> control characters;that is, as JavaScript code.
        1. Select a registry type from the list and select a registry URL
or enter a new one.
        2. For protected services, click Is Protected and
enter a userid and password. Click Next.
        3. Enter the name of the web service and click Search
services. You can include wildcard characters in the name.
For a Universal Description Discovery and Integration (UDDI) registry
use the percent sign (%) and for a WebSphere Service Registry and
Repository (WSRR) registry use an asterisk (*).
        4. Select a web service, click Next to see
the detailed information and then click Finish.
- Select View to view the WSDL source code
of a WSDL file.
- Select Discover to verify that the URL
is correct. The Discovery Status field shows
Successfully Discovered.
- Discovery Status: Confirms if you have
made a connection to the server and successfully read the WSDL file.
- Override Endpoint : If selected, you canoverride the WSDL URL field using the fields beneath the check box.This selection can be useful if you use different endpoints for developmentand testing, for example. You can enter text in these fields or text that is wrapped by <#... #> control characters; that is, as JavaScript code.

- Endpoint Address: The URL of the web service
you want to use. You can use the same format as the WSDL URL field
that you are overriding.
- Port: If there are multiple ports that
are defined in the WSDL file and there is a specific port for the
web service that you want to use, then enter the port name in this
field.
- Security and Policy : Determines the typeof security you use. Restriction: If you create multipleWeb Service integrations that share the same WSDL URI, you must usethe same policy set and bindings for each of the integrations.

- Use Basic Security : This selection meanseither no security or security through a combination of user nameand password, digital signatures, and encryption certificates.
    - Authentication : Specifies the type of authentication.Authentication ensures that the parties in a transaction are who theyclaim to be.
        - None: No authentication is required.
        - HTTP Authentication: User name and password
are passed in a header element of a message.
        - UsernameToken (password in plaintext):
The username token passes the user name and password. The password
is in text.
        - UsernameToken (password in digest): The
username token passes the user name and password. The password is
in digest form, which means it is a hash value. A hash value for a
user name and password makes these values more difficult to detect.
- Username: The user name that is registered
at the server.
- Password: The password that is registered
at the server.
- Client certificate alias: The alias for
the client certificate; that is the alias name that identifies where
the client certificate is located.
- Sign request: Select if you require messages
from the client to be signed.
- Expect encrypted response: Select if the
client expects an encrypted response message.
- Server certificate alias: The alias for
the server certificate; that is the alias name that identifies where
the server certificate is located.
- Encrypt request: Select if you require
the request message to be encrypted.
- Expect signed response: Select if you want
to verify a signed response message from the server.
- Use Policy Set : This selection means thata policy set is used to define the configuration and security requirementsfor the web service.

- Policy Set: Specifies the name of the application
policy set. Click Select to choose the policy
set. The list that you will see depends on the policies available
on the server. Some default application policy sets include: WSHTTPS
default, WSAddressing default, and Username WSSecurity default. You
can also create more application policy sets in the WebSphere Application
Server Administrative Console. Deselecting a policy set also removes
the policy binding.
- Policy Binding: Specifies the name of the
general client policy set binding, which contains system-specific
configuration parameters like username and password information. Click Select to
choose the policy binding. The list you see depends on the policy
set bindings available on the server. Default policy set bindings
include: Client sample and Client sample V2. You can also create more
policy set bindings in the WebSphere Application Server Administrative
Console. Deselecting removes the policy binding.
6. Click Save or Finish Editing.

## Related concepts

- WS-Security specification