# Adding a web services server in the designer

## About this task

- Security tokens: Security tokens contain authentication information that flows with the
message.
- Signature elements: Digital signature information for all or part of the message verifies that
the original request is not modified.
- Encryption elements: Messages can be encrypted, either completely or partially, so that only the
intended recipient can read it.

## Procedure

1. Open the process application in the designer.
2. Select the Servers tab from the Process App
Settings editor.
3. In the Servers section, click +. In the
Details section, enter a meaningful name for the server. In the
Type field, select Web Service Server. Add a
meaningful description of the server in the Description field. This field is
optional
4 Enter the server binding properties for the Default environment:
    - The Default settings are used if nothing is specified for the otherenvironments. You can have several environment types, which are added by clicking+ . The other environment types that you can add are as follows: You can modify the environment type after deployment by using theupdateBPMConfig administrative command. See Modifying the IBM Workflow Server environment type .
        - Development: The environment where you develop your services.
        - Test: The environment where you test your services.
        - Staging: The environment where you deploy your services for
pre-production testing.
        - Production: The environment where your services are deployed for use by
your organization.
- WSDL URL: The URL of the web service. For example:
http://mycorporation.com/webservice/financialstatements?wsdl. You can enter a
URL or discover a URL. Note:  Traditional:  Specifying a URL that
is computed at run time by using a JavaScript expression in the <#= #> syntax, as described in
Syntax for text with embedded JavaScript is deprecated. If you have URLs that are environment specific (for
example, for test and production), add a configuration for each environment as described previously.
At runtime, change the URL in the Servers tab of the snaphot in the Process
Admin Console, or change it by using the wsadmin command
BPMSetWebServiceServerProperties.
- For protected services, click Protected WSDL and enter a userid and
password. Important: Because the endpoint is not read from a protected WSDL, you must
select Override Endpoint and specify the endpoint address
manually.
- Select Discover to discover a web service and generate an external
service.
- Select View to view the WSDL source code of a WSDL file.
- Override Endpoint : If selected, you can override the WSDL URL field usingthe fields beneath the check box. This selection can be useful if you use different endpoints fordevelopment and testing, for example. Note: If the endpointaddress uses the https protocol, make sure that the certificate is trusted. If necessary, add it tothe trust store related to the default ssl configuration. Containers: Toadd a certificate, perform the following actions:
    - Endpoint Address: The URL of the web service you want to use. You can use
the same format as the WSDL URL field that you are overriding. Traditional:  In this field, you can
specify a value that is computed at run time, by using a JavaScript expression in the <#= #>
syntax, as described in Syntax for text with embedded JavaScript.
    - Traditional: 
Endpoint Port: If there are multiple ports that are defined in the WSDL file
and there is a specific port for the web service that you want to use, then enter the port name in
this field.
    1. Download the certificate that you want to trust.
    2 Create a secret for the certificate that you want to trust by running the following command inthe project where you plan to invoke the web service.
        - On
OpenShift:oc create secret generic secretName --from-file=tls.crt=your\_cert\_path/external-service-cert.crt
        - On
Kubernetes:kubectl create secret generic secretName --from-file=tls.crt=your\_cert\_path/external-service-cert.crt
3. Add the secret to the custom resource in the variable
baw\_configuration.tls.tls\_trust\_list. For example:baw\_configuration:
  … 
    tls: 
      tls\_trust\_list: [secretName1, secretName2]This variable is an array and multiple
values can be specified by separating them with a comma as shown in the example.
4 If you already completed installation and applied your custom resource, you must apply thecustom resource again to validate the exchange of TLS certificates. For example:
    - On OpenShift:oc apply -f descriptors/my\_custom\_resource.yaml
    - On Kubernetes:kubectl apply -f descriptors/my\_custom\_resource.yaml
- Traditional: 
Dynamically load WSDL at run time: Determines whether the WSDL is loaded at
run time, for External Services that were discovered in Business Automation Workflow V18.0.0.2 or later. For
External Services that were discovered in earlier releases, you might still see dynamic loading of
WSDL at run time even if this field is unchecked.Important:  Containers:  This field is not
displayed. WSDL is not loaded at run time.
- Authentication : Specifies the type of authentication. Authenticationensures that the parties in a transaction are who they claim to be.

- None: No authentication is required.
- HTTP Authentication: User name and password are passed in a header
element of a message.  Traditional:  You can also specify a
user name that is computed at run time by using a JavaScript expression in the <#= #> syntax,
as described in Syntax for text with embedded JavaScript.
- Traditional: 
UsernameToken (password in plaintext): The username token passes the user
name and password. The password is in text.
- Traditional: 
UsernameToken (password in digest): The username token passes the user name
and password. The password is in digest form, which means it is a hash value. A hash value for a
user name and password makes these values more difficult to detect.
- Username: The user name that is registered at the server.  Traditional:  You can also specify a
user name that is computed at run time by using a JavaScript expression in the <#= #> syntax,
as described in Syntax for text with embedded JavaScript.
- Password: The password that is registered at the server.
- Traditional: 
Client certificate alias: The alias for the client certificate; that is the
alias name in the keystore that identifies where the client certificate is located. For more
information, see Setting up message-level encryption.
- Traditional: 
Sign request: Select if you require messages from the client to be
signed.
- Traditional: 
Expect encrypted response: Select if the client expects an encrypted response
message.
- Traditional: 
Server certificate alias: The alias for the server certificate; that is the
alias name in the keystore that identifies where the server certificate is located. . For more
information, see Setting up message-level encryption.
- Traditional: 
Encrypt request: Select if you require the request message to be
encrypted.
- Traditional: 
Expect signed response: Select if you want to verify a signed response
message from the server.
- Traditional: Use Policy Set : This selection means that a policy set is used to define theconfiguration and security requirements for the web service.

- Policy Set: Specifies the name of the application policy set. Click
Select to choose the policy set. The list that you will see depends on the
policies available on the server. Some default application policy sets include: WSHTTPS default,
WSAddressing default, and Username WSSecurity default. You can also create more application policy
sets in the WebSphere Application Server Administrative Console. Deselecting a policy set also
removes the policy binding.
- Policy Binding: Specifies the name of the general client policy set
binding, which contains system-specific configuration parameters like username and password
information. Click Select to choose the policy binding. The list you see
depends on the policy set bindings available on the server. Default policy set bindings include:
Client sample and Client sample V2. You can also create more policy set bindings in the WebSphere
Application Server Administrative Console. Deselecting removes the policy binding.
5. Click Save or Finish Editing.