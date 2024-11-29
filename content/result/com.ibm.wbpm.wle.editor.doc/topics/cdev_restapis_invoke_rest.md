# Invoking a REST service by using JavaScript

## About this task

## Procedure

1. Make sure that you have the URL or a local copy of the OpenAPI (formerly known as Swagger)
specification file for the REST service and any necessary invocation credentials to be able to call
the REST service.
2 Create an external service and discover which operations are supported:
    1. Open the designer, and select Services > + > External Service > Discover an existing service, then select the OpenAPI specification file as input. For more information about
discovering an external REST service, see Invoking a REST service.
    2. If any of the discovered operations cannot be called from a service task, you can click
View explanation for more information. If the discovered service operation
that you want to invoke can be selected as an implementation of a service task in a service flow,
that is simpler. If you want to use types other than application/json (or
application/x-www-form-urlencoded with primitive values or arrays with primitive
values, or text/plain with schema type string), you must use the JavaScript API to
invoke the service.
    3. To find the information that you need about the REST service that you want to invoke,
such as operation name, parameters (including headers), security requirements, and response object
structure, click the Source tab for the External
service to view the OpenAPI specification source.
For other information about the service, see the REST server configuration for the external
service.
3 Check the server certificate for the REST service that you want toinvoke. By using JavaScript you can override any SSL configuration that is specified aspart of the REST server.

1. If the server certificate is signed by a public certification authority, you can use
the preconfigured SSL configuration that is named
PublicInternetSSLSettings.
2. If the server certificate is not signed by one of the public certification
authorities that are included in the preconfigured SSL configuration, an administrator should create
a new SSL configuration for this service and import the server certificate into a new trust store.
For information about administering SSL configurations, see Creating a Secure Sockets Layer configuration and Retrieving signers from a remote SSL port.
4. If you already have a service flow defined, select it. Otherwise create a service flow by
clicking Services > + > Service flow. For more information about creating a service flow, see Creating a service flow.
5. Add a script task to your service flow.
6 Add JavaScript to the script task to perform the following actions. For more information about the BPMRESTRequest() request object andthe BPMRESTResponse response object, see JavaScript API .

1. Create a new instance of the request object. For example:

var request = new BPMRESTRequest();
2 Set the request object's attributes as necessary, such as the mandatory externalservice name, operation name, HTTP headers, and parameters for the operation, and optionalattributes such as credentials and SSL configuration name. Any attributes that youspecify in the request object override any corresponding values that are specified as part of theREST server and the binding for the external service in the designer. The request object has thefollowing attributes:externalServiceName The name of the REST service. Forexample:request.externalServiceName = "language-translator-v2"; operationName If the OpenAPI specification file specifies an operationId for the operationthat you want to invoke, you must specify it as the operationName , otherwise, youmust specify httpMethod and path . Forexample:request.operationName="checkout"; httpMethod and path If the OpenAPI specification file does not specify an operationId for theoperation, to identify the operation to be invoked you must specify the HTTP method and path insteadof the operationName property. Forexample:request.httpMethod = "GET";request.path = "/v1/orders"; endpointAddress Optionally overrides the scheme, hostname, port, and base path that are specified in the OpenAPIspecification file. Forexample:request.endpointAddress = "https://localhost:9080/restBasePath"; httpHeaders A JSON object that specifies HTTP headers. For example:request.httpHeaders = {"Content-Type": "application/json", "Accept": "text/plain"}; Important: If the operation that you want to invoke has a body parameter, you mustspecify the Content-Type header to match the content type that you provide,otherwise you might get unpredictable results. The request header field names and values are notvalidated. For formData: Important: If you specify an API key in an HTTP header, it overrides any dynamicAPI key that is specified on the data mapping tab of the service task, which overrides any API keythat is specified on the external REST service binding tab. parameters A JSON object that contains all necessary parameters for the operation. Forexample:request.parameters = {"priority": "high", "customer": "Max", "age" : 23}; The parameters can also be complex types. In this case, specify them in one of the followingways:request.parameters = {"priority": "high", "customerInfo": { "customerFirstName" : "Max", "customerLastName" : "Smith", "amount" : 100.56, "isActive" : true }}; orrequest.parameters = {"priority": "high", "customerInfo": tw.local.customerInfo}; where the variablecustomerInfo is of complex type CustomerInfo, with properties customerLastName (String),customerFirstName (String), amount (Decimal) and isActive (Boolean).Important: To makesure that a property of type integer within a complex type is interpreted correctlyas an integer it must be specified as a variable of type Integer . requestTimeout The time in milliseconds to wait until the request will timeout. Forexample:request.requestTimeout = 2000; responseTimeout The time in milliseconds to wait until the response will timeout. Forexample:request.responseTimeout = 7200; username and password The user name and password, when using basic authentication. Forexample:request.username = "user";request.password = "password"; invocationCredential Provide the invocation credentials instead of the username andpassword for basic authentication. Forexample:request.invocationCredential = "MyAuthenticationAlias"; sslConfiguration The name of the SSL configuration to use. Forexample:request.sslConfiguration = "MySSLConfiguration"; Important: Make sure that you pass in the correct values that are required for asuccessful REST invocation. Values are passed onto the REST service without validation.

```
request.externalServiceName = "language-translator-v2";
```

```
request.operationName="checkout";
```

```
request.httpMethod = "GET";
request.path = "/v1/orders";
```

```
request.endpointAddress = "https://localhost:9080/restBasePath";
```

```
request.httpHeaders = {"Content-Type": "application/json", 
                       "Accept": "text/plain"};
```

    - If it includes a file, specify content type multipart/form-data.
    - If it does not include a file, specify content type multipart/form-data or
application/x-www-form-urlencoded.

```
request.parameters = {"priority": "high",
                      "customer": "Max", 
                      "age" : 23};
```

```
request.parameters = {"priority": "high",
                      "customerInfo": { "customerFirstName" : "Max",
                                        "customerLastName" : "Smith",
                                        "amount" : 100.56,
                                        "isActive" : true }};
```

```
request.parameters = {"priority": "high",
                      "customerInfo": tw.local.customerInfo};
```

```
request.requestTimeout = 2000;
```

```
request.responseTimeout = 7200;
```

```
request.username = "user";
request.password = "password";
```

```
request.invocationCredential = "MyAuthenticationAlias";
```

```
request.sslConfiguration = "MySSLConfiguration";
```

3. Call the tw.system.invokeREST() function on the request object,
assigning the result to a new response object of type BPMRESTResponse().
 For example:var response = tw.system.invokeREST(request);Tip: If you get the following error:
javax.net.ssl.SSLHandshakeException: com.ibm.jsse2.util.h:
PKIX path building failed ...You must get your administrator to create an SSL
configuration and import the server certificate, as described in step 3.b.
Tip: If
you get the following error:
javax.net.ssl.SSLHandshakeException: Remote host closed connection during handshakeThe
SSL/TLS protocol that is specified in the SSL configuration and the range of SSL/TLS protocols
supported by the server do not match. You must get your server administrator to change the SSL/TLS
protocol, in the Quality of protection (QoP) settings section of the SSL
configuration.
4. Process the response as necessary. Typically you check the HTTP status code
to see if the request was successful. If there was an error, you can either handle it in the script
task itself, or assign values to variables to allow handling different errors in your service flow.
Note that you can also catch exceptions in your Java script code using a try/catch block, otherwise
the exception will end the script. The following example snippet shows how to access the HTTP status
code, HTTP status message, HTTP headers of the response as well as the content of the response in
your script task.// Evaluate the response and process as necessary
var httpStatusCode = response.httpStatusCode;
var httpStatusMessage = response.httpStatusMessage;
var httpHeaders = response.httpHeaders;
var content = response.content;Remember: You cannot store the response in a
service flow variable directly; this would produce the error Java Class
com.lombardisoftware.core.script.js.BPMRESTResponseScriptable is not registered as supported class
for the SymbolTable. Instead, you can extract the properties of this object and store them
in service flow variables either individually or as part of a Business Object.
Tip: For an example of error handling code, see Handling REST service errors.
7. Click Save or Finish Editing.

- Passing input parameters

How to use JavaScript to specify different input parameters for a REST service.
- Specifying authentication, modifying binding information, and working with response headers

How to use JavaScript to specify authentication information for REST services, override the external service binding information, and work with response headers.
- Passing files

How to use JavaScript to invoke REST services that have an input parameter or a response of type file or of type string and format binary.
- Handling REST service errors

After invoking a REST service by using JavaScript, you need to parse the error information that is returned within the response.