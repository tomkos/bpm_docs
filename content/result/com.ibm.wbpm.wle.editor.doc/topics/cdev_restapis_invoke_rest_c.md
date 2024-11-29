# Passing files

## Invoking a REST service with an input parameter of type
file

If the OpenAPI specification (formerly known as Swagger) for a REST service specifies
an input parameter of type file, it is mapped to the document type
IBM\_BPM\_Document. This means that your process or service flow uses a reference to
a document in the BPM document store and the ECMDocumentInfo input object refers to that file. For more information about using the embedded BPM document store, see Working with BPM documents.

The
following example illustrates how to provide a reference to a document in the BPM document store.

```
// Prepare REST request
var request = new BPMRESTRequest();

// Specify the external service and its operation to be invoked
request.externalServiceName = "MyExternalService";
request.operationName = "addContract";

// 
// Set the http headers
var headers = {"Content-Type": "multipart/form-data"};
request.httpHeaders = headers;

// Provide a reference to the document that is to be used as input parameter of the REST service
var contractFile = new tw.object.ECMDocumentInfo();
contractFile.objectId = "idd\_808F0A58-0000-C214-BE0C-E24DEF2EA51E"; 

// Prepare all parameters that are needed for the REST request
request.parameters = {"file": contractFile};

// Execute the REST request, which returns a BPMRESTResponse instance.
var response = tw.system.invokeREST(request);

// have a look at the response
```

## Invoking a REST service with an input parameter of type
string and format binary

If the OpenAPI specification (formerly known as Swagger) for
a REST service specifies an input parameter of type string and format
binary, it is mapped to the document type IBM\_BPM\_Document. This
means that your process or service flow uses a reference to a document in the BPM document store and the
ECMDocumentInfo input object refers to that file. For more
information about using the embedded BPM document store, see Working with BPM documents.

The
following example illustrates how to provide a reference to a document in the BPM document store.

```
// Prepare REST request
var request = new BPMRESTRequest();

// Specify the external service and its operation to be invoked
request.externalServiceName = "MyExternalService";
request.operationName = "addContract";

// Provide a reference to the document that is to be used as input parameter of the REST service
var contractFile = new tw.object.ECMDocumentInfo();
contractFile.objectId = "idd\_808F0A58-0000-C214-BE0C-E24DEF2EA51E"; 

// Prepare all parameters that are needed for the REST request
request.parameters = {"file": contractFile};

// Execute the REST request, which returns a BPMRESTResponse instance.
var response = tw.system.invokeREST(request);

// have a look at the response
```

## Invoking a REST service that returns a file as
response

If the OpenAPI specification for a REST service specifies a response of type
file, the file is stored as a document of type IBM\_BPM\_Document in the BPM document store. A reference to the
document is returned to your service flow in an object of business object type
ECMDocumentInfo.

The following example illustrates how to receive a file as
response from a REST service invocation.

```
// Prepare REST request
var request = new BPMRESTRequest();

// Specify the external service and its operation to be invoked
request.externalServiceName = "MyExternalService";
request.operationName = "getContract";

// Set the accept header
var headers = {"Accept": "application/pdf"};
request.httpHeaders = headers;

// Prepare the parameters that are needed for the REST request
request.parameters = {"contractId": "1234567890"};

// Execute REST request which returns a BPMRESTResponse instance.
var response = tw.system.invokeREST(request);

// Have a look at the response
log.info("Response - httpStatusCode: " + response.httpStatusCode);
log.info("Response - httpStatusMessage: " + response.httpStatusMessage);
log.info("Response - httpHeaders: " + response.httpHeaders);
log.info("Response - content: " + response.content);

// The response file is stored as a document in the BPM document store. 
// An instance of ECMDocumentInfo is returned that contains the details.
var documentInfo = JSON.parse(response.content);
log.info("Response - documentInfo.objectId: " + documentInfo.objectId);
```

For more information about using the BPM document store, see Working with BPM documents.

## Invoking a REST service that returns a response of type
string and format binary

If the OpenAPI specification for a REST service specifies a
response of type string and format binary, the response is stored
as a document of type IBM\_BPM\_Document in the BPM document store. A reference to the
document is returned to your service flow in an object of business object type
ECMDocumentInfo.

For more information about using the BPM document store, see Working with BPM documents.