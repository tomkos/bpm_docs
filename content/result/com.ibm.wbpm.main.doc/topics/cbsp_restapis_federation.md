# REST APIs and federated environments

## Process Federation Server
REST APIs

The Process Federation Server REST APIs take
advantage of the Elasticsearch indexes that are created for the systems in the federated
environment. The entire Process Federation Server environment and
federated workflow systems comprise the ‘domain’ of data that can be queried.

Because the Process Federation Server index is used
instead of distributed queries to the workflow systems, queries against high volumes of tasks are
efficient. Client requests for individual resources, such as specific process instances and tasks,
are directed to the Business Automation Workflow system that manages the
resource. Use this set of federated APIs for task worker scenarios where a federated task list and
federated launch list are needed.

For information about Process Federation Server, see Getting started with Process Federation Server.

For information about the Process Federation Server REST APIs, see
The Process Federation Server REST APIs.

## Federated Business Automation Workflow
REST APIs (deprecated)

The federated Business Automation Workflow
REST APIs distribute client requests to the various Business Automation Workflow systems that are included
in a federation domain. The federation domain is a set of one or more systems that are configured to
access the different categories of resources. Business Automation Workflow provides predefined
domains, but you can also configure your own domains. Federated queries can be considered to be
"virtual queries" against the whole domain.

Federated queries are propagated to the individual systems as system-specific queries. These
queries are mapped to saved searches for the business process definition engine, and query tables
for the Business Process Choreographer engine. The query result sets from the individual systems are
merged and sorted into a single result set.

1 Request preprocessing and propagation: The resulting request is routed to one or more systems in the domain.
    - Federation URI parameters (domain and systemID) are
removed from the request.
    - For query entity list (count) requests, interaction filters and query filters are preprocessed
to optimize the subsequent requests that are distributed to individual systems in the domain.
    - For bulk requests, individual system-specific bulk requests are created by filtering the
resource list by the target system.
2 Response post-processing and HTTP status codes:

- The lists that are returned by the requests to the individual systems are consolidated into a
single response. A systemID property is added to each list entry so that
subsequent requests for singular resources can be routed to the hosting system.
- For most distributed requests, a federationResult property is added to the
federated response. This property contains the system ID, the HTTP status code, and the error
response content.
- The federated HTTP status code is determined. The resulting status code is the minimum of the
status codes for the individual requests. For example, if a request was distributed to three systems
that responded with HTTP status codes 200, 200, and 404, then the federated HTTP status code is 200.
You can use the federationResult property to check the results of each of the
individual systems.

For information about the individual federated REST APIs, see REST APIs.