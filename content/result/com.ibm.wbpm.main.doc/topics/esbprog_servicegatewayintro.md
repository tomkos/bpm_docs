<!-- image -->

# Service gateway

1. Common processing - once the message is received by the gateway, common processing occurs
for all messages, such as adding protocol level headers or logging the message.
2. Service identification - the message that is processed by the gateway needs to be
identified as a certain service type. For example, the message is queried to determine if it is for
service provider A, B, or C.
3. Endpoint routing - when it is known that a message will be delivered to a particular
service provider, it is mapped to a network-addressable endpoint so that the message can be
forwarded to the service provider.
4. Service-specific processing - any processing that is required for the particular target
service is performed.

1. Dynamic service gateway pattern
2. Static service gateway pattern
3. Proxy gateway pattern

Each of these patterns follow a general format within the tooling environment in
IBM Integration
Designer, as shown in Figure 1. The service gateway
is represented as an SCA module. An export exposes the endpoint and has the service gateway
interface attached. The service gateway interface instructs the runtime that it is in the service
gateway mode.

Figure 1. General pattern for a service gateway module

<!-- image -->

The service gateway interface has two operations: requestOnly and requestResponse. Both
operations use messages that have an anyType structure. An anyType message structure allows it to be
one of five core structures that represent raw data that is sent to the mediation flow component, as
shown in Figure 2. This is
not to accommodate any business object. Implement one or both of the interface operations.

Figure 2. Five structures that represent raw data

<!-- image -->

| Binding type                           | Business object created   |
|----------------------------------------|---------------------------|
| WebSevice Binding                      | TextBody                  |
| HTTP Binding                           |                           |
| HTTP Content-Type=text/*               | TextBody                  |
| HTTP Content-Type=application/soap+xml | TextBody                  |
| HTTP Other                             | BytesBody                 |
| JMS Binding                            |                           |
| JMS TextMessage                        | TextBody                  |
| JMS BytesMessage                       | BytesBody                 |
| JMS StreamMessage                      | StreamBody                |
| JMS MapMessage                         | MapBody                   |
| JMS ObjectMessage                      | ObjectBody                |
| MQ Binding                             |                           |
| MQ Format = MQSTR                      | TextBody                  |
| Other                                  | BytesBody                 |

The content of the message is in a serialized form (such as XML) when it reaches the mediation
flow component and is held within a TextBody structure. Header information is parsed as a business
object and can be found in the header section of the Service Message Object (SMO). To change the
body of the message, it can be parsed within the mediation flow component and changed using
transformation mediation primitives and then serialized before it is passed to the service gateway
import. To parse the message within the mediation flow component, the schema information associated
with the message type should be available to the module.

1. Manual parsing of the gateway message
2. Automatic parsing and any message type support

## Manual parsing of the gateway message

The DataHandler mediation primitive can be used to convert a message from a serialized form (such
as XML) to a business object structure. This mediation primitive differs from other transformation
primitives such as the Mapping
 or the BO Mapper, which convert one business object into
another business object.

Figure 3. DataHandler mediation primitive used in a service gateway

<!-- image -->

## Automatic parsing and any message type support

Figure 4. Automatic parsing used in a service gateway

<!-- image -->

- Patterns Explorer

IBM Integration Designer provides patterns that accelerate the development of a service gateway. Each pattern includes a wizard that generates a service gateway implementation, which is based on a set of parameters you provide. You can make updates to the generated implementation to complete your service gateway.
- Dynamic service gateway pattern

With the dynamic service gateway, you can enter new services into a gateway without any modification to the deployed module.
- Static service gateway pattern

The static service gateway provides a single access point for many service requesters and service providers.
- Proxy gateway pattern

The proxy gateway provides a generic capability across web service only service providers. This pattern has no dependencies on other products, such as a registry.
- Selecting service gateway patterns

This section looks at some generic scenarios where you can use each of the service gateway patterns.

<!-- image -->