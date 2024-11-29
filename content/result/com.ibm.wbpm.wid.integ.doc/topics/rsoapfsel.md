<!-- image -->

# SOAP fault selector

Since SOAP has a first class representation
of faults, the fault selector can easily determine if the response
message is a normal message or a fault. There is no standard way to
further classify the fault to a business fault or runtime fault hence
the soap header is used to indicate whether the fault is business
or runtime.

A business fault can be sent as part of the SOAP
message with the following custom SOAP header. CustomerAlreadyExists is
the name of the fault in this case.

```
<ibmSoap:BusinessFaultName xmlns:ibmSoap="http://www.ibm.com/soap">CustomerAlreadyExists</ibmSoap:BusinessFaultName>
```

If the
fault name returned in the business fault case does not match to any
native faults on the operation, then the binding will throw this as
a service runtime exception.

A runtime fault can be sent as
part of the SOAP message with the following custom SOAP header <ibmSoap:RuntimeFault
xmlns:ibmSoap="http://www.ibm.com/soap"/> and the data in
the details part of the SOAP fault.

If no custom business or
runtime fault header is present and the fault code has a Server in
it, then it is considered a runtime exception.

If the SOAP
body is a fault and there is no business fault or runtime exception
header present, then it is considered a business fault.

This
fault selector can be used with JMS, MQ JMS, MQ, generic JMS and HTTP
imports.