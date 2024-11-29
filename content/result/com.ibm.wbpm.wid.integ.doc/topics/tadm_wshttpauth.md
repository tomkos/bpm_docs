<!-- image -->

# Invoking web services that require HTTP basic authentication

## About this task

- When configuring the import binding in an SCA module, you can
select the supplied HTTP authentication policy set named BPMHTTPBasicAuthentication
(which is provided with the web service (JAX-WS) import binding) or
any other policy set that includes the HTTPTransport policy.
- When constructing the SCA module, you can use mediation flow capabilities
to dynamically create a new HTTP authentication header and specify
the user name and password information in the header.

For more information about web service
policy sets and policy bindings and how they are used, see Web services policy sets for
WebSphere Application Server.

## Procedure

- To use the supplied policy set, perform the following steps:
    1. Optional: In the administrative console,
create a client general policy binding or edit an existing one that
includes the HTTPTransport policy with the required user ID and password
values.
    2. In IBM® Integration
Designer,
generate a web service (JAX-WS) import binding and attach the BPMHTTPBasicAuthentication
policy set.
    3 Perform one of the following steps:
        - In IBM Integration
Designer, in the web service (JAX-WS) import binding properties,
specify the name of an existing client general policy binding that
includes the HTTPTransport policy.
        - After deploying the SCA module, use the administrative console
to either select an existing client policy binding, or create a new
client policy binding and then associate it with the import binding.
4. Optional: In the administrative console
of the process server, edit the selected policy set binding to specify
the required ID and password.
- To specify the user name and password in the HTTP authenticationheader, perform one of the following sets of steps:

- Use the HTTP Header Setter mediation primitive in IBM Integration
Designer to
create the HTTP authentication header, and specify the user name and
password.
- If additional logic is required, use Java code in a custommediation primitive (as shown in the following example) to: //Get the HeaderInfoType from contextService ContextService contextService = (ContextService) ServiceManager.INSTANCE .locateService("com/ibm/bpm/context/ContextService"); HeaderInfoType headers = contextService.getHeaderInfo(); if(headers == null){ headers = ContextObjectFactory.eINSTANCE.createHeaderInfoType(); } //Get the HTTP header and HTTP Control from HeaderInfoType HTTPHeaderType httpHeaderType = headers.getHTTPHeader(); HTTPControl cp = httpHeaderType.getControl(); HeadersFactory factory = HeadersFactory.eINSTANCE; if(cp == null){ cp = factory.createHTTPControl(); } //Create new HTTPAuthentication and set the HTTPCredentials HTTPAuthentication authorization = factory.createHTTPAuthentication(); HTTPCredentials credentials = factory.createHTTPCredentials(); authorization.setAuthenticationType(HTTPAuthenticationType.BASIC\_LITERAL); credentials.setUserId("USERNAME"); credentials.setPassword("PASSWORD"); authorization.setCredentials(credentials); cp.setAuthentication(authorization); httpHeaderType.setControl(cp); // Set header info back to the current execution context. contextService.setHeaderInfo(headers);
    1. Create an HTTP authentication header.
    2. Specify the user name and password information.
    3. Add the new HTTP authentication header to HTTPControl.
    4. Set the updated HTTPControl back in the Context service.

```
//Get the HeaderInfoType from contextService
        ContextService contextService = (ContextService) ServiceManager.INSTANCE
        .locateService("com/ibm/bpm/context/ContextService");        
        HeaderInfoType headers = contextService.getHeaderInfo();
        if(headers == null){ 
            headers = ContextObjectFactory.eINSTANCE.createHeaderInfoType();
        }
        //Get the HTTP header and HTTP Control from HeaderInfoType
        HTTPHeaderType httpHeaderType = headers.getHTTPHeader();
        HTTPControl cp = httpHeaderType.getControl();
        HeadersFactory factory = HeadersFactory.eINSTANCE;
        if(cp == null){
            cp = factory.createHTTPControl();
        }
        //Create new HTTPAuthentication and set the HTTPCredentials
        HTTPAuthentication authorization = factory.createHTTPAuthentication();
        HTTPCredentials credentials = factory.createHTTPCredentials();
        authorization.setAuthenticationType(HTTPAuthenticationType.BASIC\_LITERAL);
        credentials.setUserId("USERNAME");
        credentials.setPassword("PASSWORD");
        authorization.setCredentials(credentials);
        cp.setAuthentication(authorization);
        httpHeaderType.setControl(cp);
        // Set header info back to the current execution context.
        contextService.setHeaderInfo(headers);
```