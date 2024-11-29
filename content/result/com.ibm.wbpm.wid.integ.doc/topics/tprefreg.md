<!-- image -->

# Setting up preferences to connect to an IBM WebSphere Service
Registry and Repository

## Before you begin

## About this task

## Procedure

1. From the menu, select Window > Preferences.
The Preferences window opens.
2. Select IBM WebSphere Service Registry and Repository.
On the right side beneath WebSphere® Service
Registry and Repository Servers, click Add.
The Add WebSphere Service Registry and Repository Server window
box opens.
3. In the Name field, enter a name for the service
registry. In the Query service host address field, enter the
URL address of the IBM® WebSphere Service Registry
and Repository web service endpoint. If you do not know the URL address
of the IBM WebSphere Service Registry and Repository
web service endpoint, then contact your IBM WebSphere Service Registry
and Repository administrator. In the Classification service host
address field, enter the URL address of the IBM WebSphere Service
Registry and Repository Classification Service endpoint. If you do
not know the URL address of the IBM WebSphere Service Registry
and Repository endpoints, then contact your IBM WebSphere Service
Registry and Repository administrator. In the Description field,
you can enter a description of the service registry though it is not
necessary.
4. If your organization does not require any security to access
the registry, then click Test Connection to
see if you can connect to the registry. Could you connect? Then click OK and
you are returned to the previous page with the connection information
listed beneath WebSphere Service
Registry and Repository servers. A check mark indicates if this
is the default registry location. An edit button lets you edit the
information now or later. A remove button lets you delete the registry.
Click OK in the Preferences window
to close the Preferences window.
5. If your organization does require some security to access
the registry, then select Enable security.
Complete all the fields in a similar manner to the following screen
capture. These fields include the userid and password of the web service.
For encryption purposes, the fields also include the location of the
key store file used for digital signatures, the key store type and
key store password; and the location of the trust store file containing
the public keys, the trust store type and the trust store password.
When setting up this security, the information on your server
can help with the key store and trust file locations such as in this securing communications information. Use Hypertext
Transfer Protocol Secure (HTTPS) if using security rather than the
simpler and unsecure HTTP protocol. Finally, you can find important
port number information on WebSphere servers in the following file: 
<WebSphere profile directory>/logs/AboutThisProfile.txt
 Your IBM WebSphere Service Registry and Repository
administrator can also be of help in finding these security settings.
Click Test
Connection to see if you can connect to the registry.
Could you connect? Then click OK and you are
returned to the previous page with the connection information listed
beneath WebSphere Service
Registry and Repository Servers. A check mark indicates if this
is the default registry location. Click OK in
the Preferences window to close the Preferences window.