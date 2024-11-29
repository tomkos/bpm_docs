# Specifying a REST server

## About this task

External services must provide connection information and authentication information to invoke a
service on the host. The connection information, as well as defaults for basic authentication
information, are defined in a server. Server configurations can be shared by multiple external
services in a process app
or toolkit. A server lets you maintain the connection
information in one place so that you need to update it only once if something changes. If the API
changes but the server is the same, you can rediscover the service without changing the server.

When you discover a REST service, you can choose to use an existing REST server or create a new
one. The host, port and secure server properties are added for you if the Swagger definition
specifies them.

## Procedure

To modify an existing REST server, perform the following steps.

1. Select the Servers tab from the Process App
Settings editor. You see the Process App Settings editor when you
first open a newly created process application in the Workflow Center.
2 Select the server that you want to modify. You can change the following bindingproperties.
    - The Name of the server.
    - The Description of the server.
    - The Default settings are used if nothing is specified for the otherenvironments. You can have several environment types, which are added by clicking+ . The other environment types that you can add are as follows: Tip: You can also modify the environment type after deployment by usingthe updateBPMConfig administrative command. See Modifying the IBM Workflow Server environment type .
        - Development: The environment where you develop your services. This is any
Workflow Center or
a workflow server that has its environment type set to Development.
        - Test: The environment where you test your services.
        - Staging: The environment where you deploy your services for
pre-production testing.
        - Production: The environment where your services are deployed for use by
your organization.
- Host name: The host name of the server that hosts the REST service.
Specify an IP address or a host name and domain. For example:
myHost.labwide.ibm.com.
- Port: The port number of the server.
- Secure Server: Specify whether you want your service to be secure, that
is, to use the Hypertext Transfer Protocol Secure (HTTPS) protocol by selecting this check box. If
you select the HTTPS protocol, make sure that you have the security certificate that the REST
service requires and that you specify the correct port number for the secure server.
- SSL Configuration : Check the server certificate for the REST service thatyou want to invoke.
    - If the server certificate is signed by a public certification authority, you can use the
preconfigured SSL configuration that is named  PublicInternetSSLSettings.
    - If the server certificate is not signed by one of the public certification authorities that areincluded in the preconfigured SSL configuration:
        - Traditional:  An administrator
should create a new SSL configuration for this service and import the server certificate into a new
trust store. For information about administering SSL configurations, see Creating a Secure Sockets Layer configuration and Retrieving signers from a remote SSL port.
        - Containers:
            1. Leave the SSL Configuration field empty.
            2. Download the certificate that you want to trust.
            3 Create a secret for the certificate that you want to trust by running the following command inthe project where you plan to invoke the external service.
                - On
OpenShift:oc create secret generic secretName --from-file=tls.crt=your\_cert\_path/external-service-cert.crt
                - On
Kubernetes:kubectl create secret generic secretName --from-file=tls.crt=your\_cert\_path/external-service-cert.crt
        4. Add the secret to the custom resource in the variable
baw\_configuration.tls.tls\_trust\_list. For example:baw\_configuration:
  … 
    tls: 
      tls\_trust\_list: [secretName1, secretName2]This variable is an array and multiple
values can be specified by separating them with a comma as shown in the example.
        5 If you already completed installation and applied your custom resource, you must apply thecustom resource again to validate the exchange of TLS certificates. For example:
            - On OpenShift:oc apply -f descriptors/my\_custom\_resource.yaml
            - On Kubernetes:kubectl apply -f descriptors/my\_custom\_resource.yaml
- Authentication : The defaults for the basic authentication method that isused to invoke the REST service. These settings take effect when no basic authentication settingsare configured in the Binding tab of the external service. You can use one ofthe following options:None No credentials are required. Basic - user name and password Authenticate by using the user name and password that are specified. Basic - invocation credential Authenticate by using the J2C authentication alias that holds the username and password.

- Traditional:  The alias is defined
by the administrator in the WebSphere administrative console security settings. See Managing Java 2 Connector Architecture authentication .
- Containers:
    1. Create a secret for the Liberty server
configuration trust, see Creating secrets to protect sensitive
configuration data, and add an authentication alias to the configuration.
    2. Add the secret under baw\_configuration[x].custom\_xml\_secret\_name.
- Request and Response Timeout: The amount of time before a connection to
the server times out.
Request timeout 
The amount of time, in milliseconds, that the client attempts to establish a connection before
it times out. The default is 30000. If you choose None, the client attempts
to open a connection indefinitely. 

Response timeout
The amount of time, in milliseconds, that the client waits for a response before it times out.
The default is 60000. If you choose None, the client waits indefinitely.