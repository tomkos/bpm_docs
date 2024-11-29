<!-- image -->

# Service Message Object (SMO) headers at run time

## Export request and import response

An export
will create an SMO header and put the protocol neutral and protocol
specific headers in the SMO header. It will then set the SMO header
in the binding context and set the binding context on the data handler.
Once the data handler returns, it will read the headers from the SMO
header (since they could have been modified by the data handler) and
populate them in the SCA message.

## Import request and export response

An import
will read the headers from the SCA message, create a Service message
Object and put the headers in the SMO header. The SMO header will
then be put in the binding context and set on the data handler. Once
the data handler returns, it will read the headers from the Service
Message Object and populate them in the outgoing protocol specific
message.