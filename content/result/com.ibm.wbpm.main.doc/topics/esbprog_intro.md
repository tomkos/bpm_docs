<!-- image -->

# Introduction

## Service-oriented architecture

Service-oriented architecture (SOA) is an architectural approach that supports the flexible
integration of IT systems. It does this by providing a method to disconnect the service provider
(service capability which delivers a defined action) from the service requester (client that sends
the request). This enables the substitution of one service provider for another, without the
requester being aware of the change and without the need to alter the architecture as shown in Figure 1.

Figure 1. Shows the connection between the service requester, service provider and ESB

<!-- image -->

By adopting an SOA approach and implementing it using supporting technologies, companies can
build flexible systems that implement changing business processes quickly, and make extensive use of
reusable components.

Services are the building blocks of SOA, providing function as a base point for building
distributed systems. Services can be invoked independently by either external or internal service
consumers to process single functions, or can be linked together to form more complex functionality
and so quickly devise new functionality.

## The Enterprise Service Bus

An ESB is used to connect a service requester to a service provider so that messages can be
routed between the two platforms. The ESB is a collection of software components that manage
messaging from one part of the network to another. The ESB handles mismatches between the requesters
and providers, including protocol, interface or quality of service mismatches.

The ESB processes messages exchanged between the service endpoints. A service endpoint is a
location where the service is available on the network. In contrast with regular business
application components, the ESB is concerned with the flow of the messages through the
infrastructure and not just with the business content of the messages. Rather than performing
business functions, the ESB performs mediation capabilities including routing, transformation, and
logging operations on the messages.

<!-- image -->