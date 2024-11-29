# Handling REST service errors

```
// prepare REST request 
var request = new BPMRESTRequest(); 
  
request.externalServiceName = "MyExternalService"; 
request.operationName = "echo"; 
  
// prepare the one string parameter that is needed for the REST request 
request.parameters = {"text": "hello world!"}; 
  
// invoke the REST request, which returns a BPMRESTResponse instance. 
var response = tw.system.invokeREST(request); 
  
// check response for failure or success 
log.info("Response - httpStatusCode: " + response.httpStatusCode); 
log.info("Response - httpStatusMessage: " + response.httpStatusMessage); 
//check the http status codes that are returned by the REST service 
if (response.httpStatusCode >= 400) { 
  // failure – in this example the service returns a JSON object with additional error information. Handle the error in JavaScript or assign values to variables to handle errors in your service flow. 
  var content = JSON.parse(response.content); 
  var error\_number\_from\_external\_service = content.error\_number; 
  var error\_message\_from\_external\_service = content.error\_message; 
  log.info("Response - error number from external service: " + error\_number\_from\_external\_service); 
  log.info("Response - error message from external service: " + error\_message\_from\_external\_service); 
} else { 
  // success – process the response as needed 
  log.info("Response - content: " + response.content); 
}
```