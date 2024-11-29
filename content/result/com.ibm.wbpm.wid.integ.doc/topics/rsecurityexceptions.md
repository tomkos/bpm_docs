<!-- image -->

# Security for exports and imports used with IBM Business Automation
Workflow tasks

In the final step of creating your web
service, you have the option of selecting some check boxes for security.
The following topics will help you with the setup and administration
of security as a result of making those selections.

- Implications of selecting the security check boxes
- Lifecycle of a web service export

## Implications of selecting the security
check boxes

If you select the Use security to access the web service from the case management
task check box, a default policy set will be applied to the web service export when it
is deployed to the server. This policy set can be found if you select the export in the assembly
editor and then select the Properties view. You will see the
Default policy set field set to BPM FileNet Web
Services. You can also find this policy set and related BPM FileNet web services policy
sets in the Service Policies section of the
Preferences page, which is found on the menu bar by clicking
Window > Preferences. You will need to set up a Java Authentication and
Authorization Service (JAAS) alias in the token you will be passing. It must have the credentials
provided on the call from the case manager task.

When you select the Use a secure socket
(SSL) connection check box and also have chosen to create
a long running BPEL process, the encryption of the response flow from
the process back to the FileNet system is governed by the SSL configuration
of the P8 Component Manager. You should ensure that the P8 Component
Manager is configured to use a secure socket connection in order for
the response data to be encrypted as well.

When you select the Use security to access the web service from the case management task check box, it is also important to also use the Use a
secure socket (SSL) connection check box as well, otherwise
the user credentials will not be encrypted and flow in the clear;
that is, the user credentials can be viewed.

If you select the Use a secure socket (SSL) connection check box, the
secure port on the server will be used. The keys and certificates needed for the Secure Sockets
Layer (SSL) must be used.

## Lifecycle of a web service export

When you add security to a web service, it affects the service
as it moves from a test environment to a production environment. Typically,
when you are working with the test client in Integration Designer, you are
in that test environment. When that web service is deployed to a production
server or any server, you will need to do the following tasks:

- If either or both of the security options were selected, you will
need to perform the same setup on the new server as you did with the
previous server, as discussed in Implications of selecting the security check boxes.
- You will need to update the endpoint address in the FileNet repository.
To update the endpoint for the FileNet repository, see the information in IBM Case Manager.