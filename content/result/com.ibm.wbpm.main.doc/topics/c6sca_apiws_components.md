<!-- image -->

# Web service components and sequence of control

A typical sequence of control is as follows.

1 On the client side:
    1. A client application (provided by the user) issues a request for
a web service.
    2. A web service proxy (also
provided by the user, but which can be automatically generated using
client-side utilities) wraps the service request in a SOAP request
envelope and forwards the request to a URL defined as the web service
endpoint.
2. The network transmits the request to the web service endpoint
using HTTP, HTTPS, or JMS for SOAP/JMS.
3 On the server side:

1. The generic web services API receives and decodes the request.
2. The request is either handled directly by the generic Business
Flow Manager or Human Task Manager component, or forwarded to the
specified BPEL process or human task.
3. The returned data is wrapped in a SOAP response envelope.
4. The network transmits the response to the client-side environment
using HTTP, HTTPS, or JMS for SOAP/JMS.
5 Back on the client side:

1. The client-side development infrastructure unwraps the SOAP response
envelope.
2. The web service proxy extracts
the data from the SOAP response and passes it to the client application.
3. The client application processes the returned data as necessary.

## Example

The following outline shows how
a client application might access the Human Task Manager web services
API using the HTTP transport layer to process a to-do task:

1. The client application issues a query web service
call to the process server requesting a list of to-do tasks to be
worked on by a user.
2. The process server returns the list of to-do tasks.
3. The client application then issues a claim web
service call to claim one of the to-do tasks.
4. The process server returns the input message for the task.
5. The client application issues a complete web
service call to complete the task with an output or fault message.