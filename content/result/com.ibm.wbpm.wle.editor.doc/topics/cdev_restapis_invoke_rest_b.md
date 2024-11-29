# Specifying authentication, modifying binding information, and
working with response headers

- Invoking a REST service and overriding the service binding information specified for the REST server
- Working with response headers

## Invoking a REST service and overriding
the service binding information specified for the REST server

By
default the JavaScript API invokeREST() uses the
service binding specifications provided for the REST server of the
external service. You can use the BPMRESTRequest object
to selectively override any of these settings.

The following
example illustrates how to specifying the endpoint address, user name,
password, SSL configuration, request timeout, and response timeout
properties of the request object.

```
// Prepare REST request
var request = new BPMRESTRequest();
request.externalServiceName = "MyExternalService";
request.operationName = "echo";

// Overwrite the endpoint address provided by external service and swagger
request.endpointAddress = "https://localhost:9080/restBasePath";

// Provide operation-specific user credentials using user name/password overriding 
// what is provided by the REST service server of the external service. 
// Note: Web Process Designer does not support operation-level credential specifications.
request.username = "user";
request.password = "password";

// Instead of using username/password, provide invocationCredential, 
// overriding what is specified by the REST service server of the external service
// request.invocationCredential = "MyAuthenticationAlias";

// Set SSL configuration or overwrite the SSL configuration provided by the external service
request.sslConfiguration = "MySSLConfiguration";

// Overwrite the default request and response timeout in milliseconds
request.requestTimeout = 7200;
request.responseTimeout = 7200;

// Provide input parameters needed for the REST request
request.parameters = {"text": "hello world!"};

// invoke the REST service returning a BPMRESTResponse instance
var response = tw.system.invokeREST(request);

// Evaluate the response
log.info("Response - httpStatusCode: " + response.httpStatusCode);
log.info("Response - httpStatusMessage: " + response.httpStatusMessage);
log.info("Response - httpHeaders: " + response.httpHeaders);
log.info("Response - content: " + response.content);
```

## Working with response headers

```
var response = tw.system.invokeREST(request);
 var expires = response.httpHeaders.expires; // retrieve the 'expires' header
```

```
var response = tw.system.invokeREST(request);
 var contentTypes = response.httpHeaders["Content-Type"]; // retrieve the 'Content-Type' header
```