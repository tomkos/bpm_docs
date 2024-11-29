<!-- image -->

# Pure dynamic invocation

No additional information is required apart from the details in the message. An example is where
the intended service is identified by a name, which is looked up at run time. Pure dynamic
invocation assumes a specific set of configuration parameters.

Web services and SCA URLs are supported, but other types are not because of
their need for additional configuration that is provided by an import binding.

The default for pure dynamic invocation using a Web Service binding is SOAP 1.1, using HTTP or
JMS as specified in the target URL. Pure dynamic invocation is also supported
for SOAP 1.2 when using HTTP by specifying an appropriate value for the bindingType field of the
EPR. Pure dynamic invocation using SOAP 1.2 and JMS is not supported.

- For pure dynamic invocation using SOAP 1.1 and HTTP or JMS, the binding type should either beunset or it should be set to one of the following values:
    - Using the SCA Endpoint Reference API:
        - EndpointReference.BINDING\_TYPE\_WEB\_SERVICE
        - EndpointReference.BINDING\_TYPE\_WEB\_SERVICE\_SOAP\_1\_1
- Using the SMO structure
    - Target@bindingType=WS
    - Target@bindingType=WS1.1
- 
- For pure dynamic invocation using SOAP 1.2 and HTTP, the EndpointReference binding type shouldbe set to:

- EndpointReference.BINDING\_TYPE\_WEB\_SERVICE\_SOAP\_1\_2 using the SCA Endpoint Reference API
- Target@bindingType=WS1.2 using the SMO structure

Figure 1. Pure dynamic invocation

<!-- image -->

An example of when pure dynamic invocation could be used is with a search engine. Figure 1 shows how a call can be made to the mediation flow
component. An Endpoint Lookup mediation primitive is used to retrieve all endpoints from a public
WSRR. A public WSRR allows companies to register themselves with service providers on an ongoing
basis. This indicates that the endpoint is constantly changing, and so a pure dynamic environment is
required. The advantage of pure dynamic invocation, is that the mediation module does not need to be
changed in order to respond to new service providers.