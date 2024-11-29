# Creating implicit SOAP headers for outbound web service integrations

## About this task

The SOAP 1.2 protocol is not supported in the Header tab. The
Parameter Details and Header Details cannot be used if
you select the SOAP 1.2 protocol from the Implementation tab.

All the variables that you declare in  the designer are JavaScript variables. You can use them inside service definitions and also in expression
evaluations inside JavaScript code snippets.

- Adding SOAP headers to a SOAP request message

You can add a SOAP header to a request message by creating a variable of type SOAPHeader or SOAPHeaders. You can then map that variable to the SOAP header request.
- Retrieving SOAP headers from the SOAP response message

You can retrieve SOAP headers from a response message by creating a variable of type SOAPHeaders and then mapping that variable to the SOAP header response.