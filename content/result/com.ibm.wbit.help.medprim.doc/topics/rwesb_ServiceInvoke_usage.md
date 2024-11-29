# Usage patterns

## Service Invoke patterns

The following patterns
let the Service Invoke mediation primitive: act as a proxy, retry
or combine services, augment messages, and aggregate responses.

## Act as a proxy to an external service

You
can use the Service Invoke mediation primitive to act as a proxy to
an external service.

The Service Invoke mediation primitive
calls the service provider and the response is returned directly to
the user; you do not need to explicitly wire a response flow.

Figure 1. The
Service Invoke mediation primitive acting as a proxy to an external
service

<!-- image -->

## Retry the same service

You
can use the Service Invoke mediation primitive to retry the same service
if the initial call is unsuccessful.

| Property                | Setting                                                                                                                                                                                         |
|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Retry On                | Any fault if you want to retry after any fault. Modeled fault if you want to retry after faults defined by the WSDL. Unmodeled fault if you want to retry after faults not defined by the WSDL. |
| Retry Count             | Number of times you want to retry.                                                                                                                                                              |
| Retry Delay             | Delay (in seconds) between retry attempts.                                                                                                                                                      |
| Try Alternate Endpoints | false (unchecked).                                                                                                                                                                              |

## Combine multiple services with
the same interface

You can use the Service Invoke mediation
primitive to provide a service that combines the availability of multiple
equivalent services.

If you want to retry alternate services
that all use the same service interface, the alternate endpoints must
be placed in the AlternateTarget field of the service
message object (SMO). The alternate endpoints must have the same WSDL
portType (set of operations and associated messages).

The Endpoint
Lookup mediation primitive automatically puts alternate endpoints
in the AlternateTarget field, but you can use other
mediation primitives to populate the AlternateTarget field.

If
any fault is returned by the initial service request, and the retry
count is greater than zero, the first endpoint from the alternate
endpoint list is used for the retry. If the retry returns a fault,
and the next retry would not exceed the retry count, the next alternate
endpoint is used. After the last endpoint in the alternate endpoints
list is used, the initial endpoint is used again. For example, suppose
that the first endpoint is ServiceA, and the alternate
endpoints are ServiceB and ServiceC.
If the retry count is 5, then the sequence of service
calls is as follows: ServiceA, ServiceB, ServiceC, ServiceA, ServiceB, ServiceC.

| Mediation Primitive   | Property                | Setting                                                                                                                                                                                         |
|-----------------------|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Endpoint Lookup       | Match Policy            | Return all matching endpoints, and set alternate routing targets                                                                                                                                |
| Service Invoke        | Retry On                | Any fault if you want to retry after any fault. Modeled fault if you want to retry after faults defined by the WSDL. Unmodeled fault if you want to retry after faults not defined by the WSDL. |
| Service Invoke        | Retry Count             | Number of times you want to retry.                                                                                                                                                              |
| Service Invoke        | Retry Delay             | Delay (in seconds) between retry attempts.                                                                                                                                                      |
| Service Invoke        | Use Dynamic Endpoint    | true (checked). This is the default provided by the WebSphere® Integration Developer tools.                                                                                                     |
| Service Invoke        | Try Alternate Endpoints | true (checked). This is the default provided by the WebSphere Integration Developer tools.                                                                                                      |

Figure 2. The Service Invoke mediation primitive
retrying alternate services

<!-- image -->

1. A list of all the endpoints is put in the service message object
(SMO) context.
2. The first matching endpoint is stored in the SMO Target field.
3. The remaining matches are put in the SMO AlternateTarget field.
4. The Service Invoke uses the Target field to make
the initial service call.
5. If no fault is returned, this is the end of the Service Invoke
processing.
6 If a fault is returned, the following actions occur:
    1. The first endpoint from the AlternateTarget list
is used for the first retry.
    2. If the retry returns a fault and the next retry would not exceed
the Retry Count, the next endpoint from the AlternateTarget list
is called.
    3. After the last endpoint in the AlternateTarget list
has been tried, the next retry uses the Target field.
    4. If the Target field call returns a fault, the
first endpoint from the AlternateTarget list is used.
    5. The calls carry on using the same algorithm until a successful
call is made, or the Retry Count is reached.

## Combine multiple services with different
interfaces

You can use the Service Invoke mediation primitive
to provide a service that combines the availability of multiple equivalent
services.

If you want to retry alternate services that use
different service interfaces, you can use multiple Service Invoke
mediation primitives. On the first Service Invoke you wire the fail terminal,
or a modeled fault output terminal, to a mediation primitive that
can change the message format. Then you wire the format-changing mediation
primitive to another Service Invoke mediation primitive, or to the
callout.

| Property                | Setting                                                                           |
|-------------------------|-----------------------------------------------------------------------------------|
| Retry On                | Never. This is the default provided by the WebSphere Integration Developer tools. |
| Retry Count             | 0. This is the default provided by the WebSphere Integration Developer tools.     |
| Use Dynamic Endpoint    | false (unchecked).                                                                |
| Try Alternate Endpoints | false (unchecked).                                                                |

Figure 3. The Service Invoke mediation primitive
retrying an alternate service

<!-- image -->

1. The mediation primitive ServiceInvoke1 invokes Service A.
2. If the call is successful, the response is passed through the out terminal
to a Mapping mediation primitive, XSLT1, to transform the response
into the format needed by the Message Logger mediation primitive,
Logger1.
3 If the call causes a modeled fault, the original message is passedthrough the modeled fault terminal to another Mapping mediation primitive,XSLT2. XSLT2 transforms the message into the format required by thenext Service Invoke primitive, ServiceInvoke2.
    1 The mediation primitive ServiceInvoke2 invokes Service B.
        - If the call is successful, the output is passed through the out terminal
to a Mapping mediation primitive, XSLT3, to transform the response
into the format needed by the Message Logger mediation primitive,
Logger1.
        - If the call causes a modeled fault, the output is passed through
the modeled fault terminal to the Fail mediation primitive, which
halts the mediation flow.

## Augment an input message

You
can use the Service Invoke mediation primitive to augment an input
message, in a similar way to the Database Lookup mediation primitive.

You
use the Service Invoke mediation primitive to call an intermediate
service that adds information to a message. The amended message is
sent to an external service using the callout mechanism.

The
following figure shows how you can save the original message in the
SMO context, call a service, and then create a new message from the
original message and the call response.

Figure 4. The Service
Invoke mediation primitive augmenting an input message

<!-- image -->

1. The Mapping mediation primitive, XSLTransformation1, saves the
input message to the transient context, and creates a new input message
for the mediation primitive ServiceInvoke1.
2. ServiceInvoke1 invokes Service A.
3. If the call is successful, the response is passed through the out terminal
to another Mapping mediation primitive, XSLTransformation2.
4. XSLTransformation2 creates a new message by combining the service
response, and the original message stored in the transient context.

## Aggregate service responses
into a single message

You can use the Service Invoke mediation
primitive to aggregate a number of service responses into a single
message. There are many aggregation patterns that you can use, many
of which use the Fan In and Fan Out mediation primitives. For more
information, see: Fan Out mediation primitive

The
implication of this aggregation pattern is that the response from
the first service call provides the basis for the second service call.
If the response from the first service call does not match the request
to the next service call, some mapping must take place.

Figure 5. The Service Invoke mediation primitive
aggregating service responses

<!-- image -->

1. The mediation primitive ServiceInvoke1 invokes Service A.
2. If the call is successful, the response is passed through the out terminal
to a Mapping mediation primitive, XSLT1.
3. XSLT1 maps the service response (which is now the input message)
to the shared context or transient context.
4. Additionally, XSLT1 creates a new message by mapping some of the
source SMO body to the target SMO body.
5. The mediation primitive ServiceInvoke2 invokes Service B, using
the message created by XSLT1.
6. If the call is successful, the response is passed through the out terminal
to a Mapping mediation primitive, XSLT2.
7. XSLT2 creates another message by combining the response from Service
B, and the original message stored in the shared context or transient
context.