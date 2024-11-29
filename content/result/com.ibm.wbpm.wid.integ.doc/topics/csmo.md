<!-- image -->

# Service message objects

Service message objects are enhanced business
objects that include the application data and header information related
to the transport protocol used to invoke a service such as SOAP or
JMS. A service message object is composed of a body that contains
the application data (also known as the payload or operation message)
in a business object, and headers containing additional context information.
You can use XPath 1.0 expressions to access elements in a message.
The following picture represents a service message object:

<!-- image -->

1 context : is the message context whereinformation that is unrelated to the payload is stored. The contexthas these elements. correlation makes the property persist throughout the duration of the requestand response flows, and is used for passing values from the requestflow to the response flow. transient makes the property available for the duration of the currentflow (either the request flow or the response flow), and is used topass values between mediation primitives in the same flow. shared makes the property available during aggregation operations usingthe Fan Out / Fan In combination. It is not intended for general datastorage. failInfo contains exception information about execution failure in a mediationprimitive; it contains the message exception chain, and identifiesthe primitive where the failure occurred. This information is propagatedto the fail terminal. primitiveContext contains context information for primitives.
    - EndpointLookupContext contains the result of a WebSphere® Service Registryand Repository query.
        - endpointReference  contains the information needed to access
the service endpoint.
        - registryAnnotations   contains information for the user-defined
properties.
2 headers contain header information associatedwith the message. These are the elements in the headers section: SMOHeader contains information that defines the message; such as the uniquemessage id, message version and message type. An SMO header is alwayspresent in a service message object. JMSHeader contains JMS headers, when a JMS import or export binding is used. SOAPHeader contains SOAP header information when a web services import orexport binding is used. SOAPFaultInfo contains information about SOAP faults such as fault code andfault string Properties[] properties put in the message header by the application MQHeader contains WebSphere MQheader information, when an MQ binding is used. HTTPHeader contains HTTP Headers, when a HTTP import or export binding isused.

- Target contains the dynamic endpoint used by the runtimeif the Use dynamic endpoint property is set and there is a valid endpointin the field.
    - address the address of the target.
3. body contains the application data in a business
object. Application data is also known as the payload, or operation
message type.
4. attachments contains SOAP attachments of various types.
For more information , see SMO attachments.

- See "Building XPath expressions" in the topic "Building mediation
flows" for an example of the relationship between a business object
in an interface and an XPath 1.0 condition.