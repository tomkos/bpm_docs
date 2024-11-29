# Passing input parameters

- Invoking a REST service with a simple-typed parameter
- Invoking a REST service with a complex-typed JSON parameter
- Invoking a REST service with an XML parameter
- Invoking a REST service with multiple parameters
- Invoking a REST service with an array parameter

## Invoking a REST service with a simple-typed
parameter

In the following example, an operation that is named echo is invoked for a
service that is named MyExternalService, and the response attributes are output to
the log file.

```
// prepare REST request
var request = new BPMRESTRequest();

request.externalServiceName = "MyExternalService";
request.operationName = "echo";

// prepare the one string parameter that is needed for the REST request
request.parameters = {"text": "hello world!"};

// invoke the REST request, which returns a BPMRESTResponse instance.
var response = tw.system.invokeREST(request);

// have a look at the response
log.info("Response - httpStatusCode: " + response.httpStatusCode);
log.info("Response - httpStatusMessage: " + response.httpStatusMessage);
log.info("Response - httpHeaders: " + response.httpHeaders);
log.info("Response - content: " + response.content);
```

## Invoking a REST service with a
complex-typed JSON parameter

The following example illustrates
how to specify a JSON object as an input parameter. It also parses
the response content into a new variable.

```
// prepare REST request
var request = new BPMRESTRequest();

request.externalServiceName = "MyExternalService";
request.operationName = "addCustomer";

// set http headers
var headers = {"Content-Type": "application/json", 
               "Accept": "application/json"};
request.httpHeaders = headers;

// prepare the complex-typed input parameter that is needed for the REST request
// we provide the complex type (BO) as JSON object.
request.parameters = {"customer": {"name" : "Hugo", 
                                   "age" : "32", 
                                   "since" : "2016-08-14T22:44:53Z"}};

// invoke the REST request, which returns a BPMRESTResponse instance.
var response = tw.system.invokeREST(request);

// have a look at the response
log.info("Response - httpStatusCode: " + response.httpStatusCode);
log.info("Response - httpStatusMessage: " + response.httpStatusMessage);
log.info("Response - httpHeaders: " + response.httpHeaders);
log.info("Response - content: " + response.content);

var content = JSON.parse(response.content);
log.info("Response - content.message: " + content.message);
```

## Invoking a REST service with an
XML parameter

The following example illustrates how to provide
an XML document as input parameter for a REST service. A business
object is converted into an XML string that serves as the body of
the REST request.

```
// prepare REST request
var request = new BPMRESTRequest();

request.externalServiceName = "MyExternalService";
request.operationName = "addCustomer";

// set http headers
var headers = {"Content-Type": "application/xml", 
               "Accept": "application/xml"};
request.httpHeaders = headers;

// prepare a custom business object that has been discovered or modeled
tw.local.customer = new tw.object.Customer();
tw.local.customer.name = "Hugo";
tw.local.customer.age = 32;
var date = new TWDate();
tw.local.customer.since = date;

// prepare the input parameter for the REST request
// because the 'content-type' is set to 'application/xml', provide the business object as an XML string.
request.parameters = {"customer": tw.local.customer.toXMLString()};

// invoke the REST request, which returns a BPMRESTResponse instance.
var response = tw.system.invokeREST(request);

// have a look at the response
...
```

## Invoking a REST service with multiple
parameters

The following example illustrates how the previous
example could be extended if the REST service required a customerId parameter
in addition to the customer parameter.

```
// prepare REST request
var request = new BPMRESTRequest();

request.externalServiceName = "MyExternalService";
request.operationName = "addCustomer";

// set the http headers
var headers = {"Content-Type": "application/json", 
               "Accept": "application/json"};
request.httpHeaders = headers;

// prepare all input parameters that are needed for the REST request
// the parameters are handed over in the parameters object
request.parameters = {"customer": {"name" : "Hugo", 
                                   "age" : "32", 
                                   "since" : "2016-08-14T22:44:53Z"}, 
                      "customerId": "1234"};

// invoke the REST request, which returns a BPMRESTResponse instance.
var response = tw.system.invokeREST(request);

// have a look at the response
...
```

## Invoking a REST service with an array
parameter

The following example illustrates how an array
of customer information can be passed as a customers array
parameter.

```
// prepare REST request
var request = new BPMRESTRequest();

request.externalServiceName = "MyExternalService";
request.operationName = "addCustomers";

// prepare array parameters for the REST request
request.parameters = {"customers": 
                        [{"customer": {"name" : "Hugo", 
                                       "age" : "32", 
                                       "since" : "2016-08-14T22:44:53Z"}}, 
                         {"customer": {"name" : "Max", 
                                       "age" : "23", 
                                       "since" : "2016-08-14T22:44:53Z"}}]};

// invoke the REST request, which returns a BPMRESTResponse instance.
var response = tw.system.invokeREST(request);

// have a look at the response
log.info("Response - httpStatusCode: " + response.httpStatusCode);
log.info("Response - httpStatusMessage: " + response.httpStatusMessage);
log.info("Response - httpHeaders: " + response.httpHeaders);
```