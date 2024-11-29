<!-- image -->

# Common Usage Patterns

- Simple service proxy pattern
- Service selector pattern
- Service translator pattern
- Service gateway pattern
- Message enrichment pattern
- Batch aggregation pattern
- Multiple source aggregation pattern

## Simple service proxy pattern

The simple service proxy pattern creates a one-to-one mapping between a service requester and
service provider. By placing an ESB between the two services it hides the real location of the
service provider. The simple service proxy pattern is also of particular value in providing a point
for access control, request tracking or auditing.

- You want to provide access to a service through a control point without exposing the actual
location (endpoint address) of the service to the clients.
- You must apply some form of control (access management, authorization, auditing or logging)
every time a service is accessed.

Figure 1 shows the simple service
proxy pattern. The target service is hidden by deploying an ESB mediation which implements the same
interface. This mediation acts as a virtual service (or proxy) which redirects all requests to the
real service provider.

A service registry is a repository of data describing a set of services and their associated
properties and behaviors. This registry can be queried by the ESB to determine the endpoint of the
service provider.

Figure 1.  Simple service proxy pattern

<!-- image -->

For example, operations within a bank application often need to be audited as a legal
requirement. The simple service proxy pattern can be used to implement this business requirement
that ensures all requests are audited, and removes the need for the service provider to implement
the capability.

## Service selector pattern

The service selector pattern provides multiple implementations of the same service interface to
be grouped behind a single endpoint address. Each implementation can have a different quality of
service or behavior, and each client request can be matched to a particular implementation
determined by different criteria, such as the content of the message into the ESB.

- There are multiple implementations of a particular service all sharing the same interface.
- Different implementations provide different qualities of service.
- Requests from different clients are to be routed to a particular implementation in accordance
with some set of predefined criteria.

Figure 2 shows the service selector
pattern, which implements the required logic to select a specific endpoint address based on the
context or content of each client request.

A service registry is a repository of data describing a set of services and their associated
properties and behaviors. This registry can be queried by the ESB to determine the endpoint of the
service provider.

Figure 2. Service selector pattern

<!-- image -->

An example of when the service selector pattern would be used is if a fictitious company wants to
differentiate itself from its competition by offering tiered levels of service. The company's goal
is to offer delayed stock quotes to their standard customers and real-time quotes to their premium
customers, who pay a fee.

The service requester application provides a query containing a stock symbol and customer ID to
the content based router, which processes the query. The customer's subscription level is
determined, and depending on the level of subscription, the query is routed to the appropriate
service provider. The quote that is returned from the service provider is then returned to the
client application. More on this scenario is found in the Example scenarios.

## Service translator pattern

The service translator pattern provides access to a service implementation with a different
interface or protocol than the interface or protocol used by the service requester. You can select
operations to be restricted or restructured on some interfaces, and you can convert and format data
for users of specific interfaces.

- You want to restrict access to certain functions on the user interface.
- The interface needs to be modified to conform to the requirements of certain departments.
- Requesting services expect to use different interfaces or protocols.

Figure 3 shows the service translator
pattern, which transforms the request and then routes it to the actual service provider. The
mediation must also process the responses from the target service, transforming them back into the
form expected by the client.

Figure 3. Service translator pattern

<!-- image -->

An example of the service translator pattern, is if a fictitious company, Personal
Holidays book flights, and the flight availability must be checked against a fictitious airline
company, My Airways, flight schedule. The Personal Holidays booking system represents
information differently to the My Airways booking system. The service translator pattern within the
ESB mediation is able to transform incoming messages from the service requester into the format that
My Airways represent their information. More information about this scenario is found in the Example scenarios.

## Service gateway pattern

The service gateway pattern introduces a point of control and can bring a range of services under
the control of an ESB without the need to develop individual mediations for each service. The
service gateway provides a single access point and acts as a proxy for multiple services. In
addition, service gateways encapsulate transformations, routing, and common processing across all
the services.

- You want to route messages to multiple endpoints using a variety of protocols.
- A set of services needs to be accessed in the same way without the need for multiple
mediations.
- You want to provide generic processing (for example auditing, security enforcement point) across
all the services.

Figure 4 shows the service gateway pattern.
Messages enter the gateway and the target service is identified. Common processing is completed
(such as auditing) before the message is routed onwards to an end provider.

A service registry is a repository of data describing a set of services and their associated
properties and behaviors. This registry can be queried by the ESB to determine the endpoint of the
service provider.

Figure 4. Service gateway pattern

<!-- image -->

For example a bank have a number of completely different services that need to be audited as a
legal requirement. They want the same level of audit across all the services. The service gateway
pattern is used to implement this business requirement.

## Message enrichment pattern

The message enrichment pattern provides a method to modify or add to the existing content in a
message before it is forwarded onto the service provider. An example of message enrichment is to
retrieve data from a database and add the data to a given location in a message.

You can use this pattern when messages are sent, in order to obtain further information from a
database.

Figure 5 shows the message enrichment
pattern. The message that arrives into the ESB does not contain all the data required by the service
provider. Data is added by the ESB before the message is sent to the service provider. For example,
the service requester only knows the customer ID and product ID. Message enrichment provides the
full product and customer details for the order to be processed.

Figure 5. Message enrichment pattern

<!-- image -->

An example of when the service enrichment pattern can be used is if a particular field does not
exist within a message structure. A Database Lookup mediation primitive can be used to establish the
details of the field in any given instance. More information about this scenario is found in the
Service enrichment.

## Batch aggregation pattern

The batch aggregation pattern provides a method for an inbound request to be mapped into several
individual outbound requests to the service provider. The responses from these requests can be
collected (aggregated) into a single response for the original request.

You can use this pattern when there is a need for messages that include multiple records and each
of which can be forwarded onto the service provider individually.

Figure 6 shows the batch aggregation
pattern, where the inbound message to the mediation is split into several outbound requests to the
service provider, and then collected back into a single message to send back to the service
requester. The service requester receives all the relevant information required in one batch
message.

Figure 6. Batch aggregation pattern

<!-- image -->

## Multiple source aggregation pattern

The multiple source aggregation pattern provides a method for an inbound request to be mapped
into several individual outbound requests to multiple service providers. The responses from these
requests can be collected (aggregated) into a single response for the original request.

You can use this pattern when a single message is sent into the ESB that requires two or more
service providers to process the message, or parts of the message. An aggregated response is sent
back to the service requester.

Figure 7 shows the multiple source
aggregation pattern, where the inbound message to the mediation is split into several outbound
requests for several service providers. The results are then collected back into a single message to
send back to the service requester. You can use this pattern if the inbound request needs
information from many different service providers, for example a quote comparison web site.

Figure 7. Multiple source aggregation pattern

<!-- image -->

<!-- image -->