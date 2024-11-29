<!-- image -->

# SOAP data handler

## Export behavior

The SOAP data handler looks
at the binding context to determine if this message is a normal response
or a fault. If a normal response, it converts the data object to XML
and adds it to the SOAP body.  If a fault, it creates a SOAP fault,
converts the data object to XML and adds it to the SOAP details. It
gets the fault name from the binding context and adds a custom SOAP
header as follows:

```
<ibmSoap:BusinessFaultName 
	xmlns:ibmSoap="http://www.ibm.com/soap">CustomerAlreadyExists</ibmSoap:BusinessFaultName>
```

If the SOAP data handler is called for a service
runtime exception (SRE), then the SOAP data handler creates a custom
SOAP header as follows: <ibmSoap:RuntimeFault xmlns:ibmSoap="http://www.ibm.com/soap"/>,
create the SOAP fault, set the status code to Server and set
the fault string from the message of the ServiceRuntimeException.

## Import behavior

The SOAP data handler converts
the InputStream or Reader to a data object in the case of a normal
response and service business exception. In the case of a service
runtime exception (SRE), it reads the fault string from the SOAP fault,
creates a ServiceRuntimeException and sets the fault string as the
message of the ServiceRuntimeException

## Limitations

The following limitations apply
to the SOAP data handler currently:

- The SOAP 1.2 message format is not supported.
- Multiple-part messages are not supported.

## Related reference

- Atom feed format
- Delimited format
- Fixed width format
- JavaScript Object Notation (JSON) format