<!-- image -->

# Service Message Object (SMO) headers

In order to perform the data transformation, some data handlers
need access to protocol headers. These headers could be protocol neutral
like DataBindingDescriptor or they can be protocol specific like JMSType.
Some examples of protocol neutral headers are JMS user properties,
HTTP custom headers, MQRFH2 user properties, and so on. The programming
model to access these headers is a Service Message Object (SMO) in
the context service which is essentially data object APIs. The protocol
neutral headers are stored in the context in a protocol neutral manner
such that the data handler can access it with a uniform XPath expression
independent of whether this information came from a JMS header, a
MQ header, and so on.

- Service Message Object (SMO) headers at run time

The behavior of the Service Message Object (SMO) headers at run time differ depending on whether they are used by an export or import.
- Binding-specific headers in a Service Message Object (SMO)

Where data handlers can find the header information for a binding is described.
- Code to access binding-specific headers

Accessing the binding-specific headers from a SMO header in a data handler requires only a few lines of code.