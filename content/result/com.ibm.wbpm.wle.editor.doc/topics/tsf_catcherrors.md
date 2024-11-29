# Catching errors by using error boundary
events

## About this task

In a service flow, for example, the activity to which
you attach the error event can be either a service task or a linked
service flow.

## Procedure

To add an error boundary event to an activity, complete the following
steps:

1. Open the designer.
2. From the library, create or open the service that you want to work with. To create the
service, see  Creating a service flow or Building a heritage human service.
3. In the Diagram view, drag an error
event  onto the activity node. The
error event attaches itself to the boundary of the activity.
4. Select the error boundary event and, on the Implementation tab,
under Error Properties, select Catch
all errors or Catch specific errors to
specify the type of errors you want the error event to catch.
5. If you selected Catch specific errors,
click the pickers next to Error code and Error
mapping to filter on the error code for the specific errors
that can be caught and map the error data to a local variable. 
If you have a service task that uses an external
service to invoke a web service, the external service might have faults based on the WSDL
definition. You can choose to catch and handle errors that are related to these specific
faults.Note: The error data cannot be mapped to a variable that is of a list type. If you want to
pass information that has the structure of a sequence as error data, create a business object that
contains a parameter that is of a list type and then use this business object as the variable's
type.
6. Connect the error boundary event to the logic you want
to run when the error occurs.  For example,
if your service flow invokes a REST service, wire your catch all error
event to a script task that handles HTTP errors that the REST service
returns. The error information returned by the REST service is returned
in the RESTResponseException node in the tw.system.error variable:<error type="com.ibm.bpm.externalservice.rest.api.UnexpectedRESTResponseException" 
       description="UnexpectedRESTResponseException">
    <HTTPHeaderNames type="java.util.Collection" description="HTTPHeaderNames"></HTTPHeaderNames>
    <HTTPStatus type="java.lang.Integer" description="Integer">500</HTTPStatus>
    <RESTResponseException type="com.ibm.bpm.externalservice.rest.api.RestResponseData" description="RestResponseData">
        <HTTPStatusCode type="java.lang.Integer" description="Integer">409</HTTPStatusCode>
        <HTTPStatusMessage type="java.lang.String" description="String">Conflict</HTTPStatusMessage>
        <content type="java.lang.String" description="String">{
            "code" : 409,
            "error" : "Classifier not ready",
            "description" : "The classifier is not ready. The status of the classifier is 'Training'."
            }
        </content>
    </RESTResponseException>
    <cause type="java.lang.Throwable" description="cause"></cause>
    <localizedMessage type="java.lang.String" 
                      description="String">CWXSD1028E: The operation classify\_get with HTTP method GET returned an unexpected response status code 409 with response message Conflict
    </localizedMessage>
    <message type="java.lang.String" 
             description="String">CWXSD1028E: The operation classify\_get with HTTP method GET returned an unexpected response status code 409 with response message Conflict
    </message>
    <messageKey type="java.lang.String" description="String">Api.UnexpectedResponseStatus</messageKey>
    ...
</error>
Your JavaScript can
access the HTTPStatusCode, HTTPStatusMessage,
and content elements of the RESTResponseException node
in the tw.system.error variable. For example, to
test whether the REST service returned an HTTP status code 404, use
the following statement in your script task implementation:if (tw.system.error.RESTResponseException[0].HTTPStatusCode[0].getText()=='404') { ... }
7. Click Save or Finish Editing.