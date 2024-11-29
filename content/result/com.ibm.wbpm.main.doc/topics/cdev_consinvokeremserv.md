<!-- image -->

# Considerations when invoking services on different servers

One of the advantages of Workflow Server is the
ability to distribute the application workload across multiple servers in a cell. This distribution
allows for better workload balancing among the various servers in the cell and maximizes the
maintainability of the computing resources because there is only one copy of an application or
service in the server. Thus, an application on server A could require a service installed in server
B in the cell. To use services in this manner, you must configure communications between the
servers. The type of configuration you perform depends on whether the calling service component
invokes the service asynchronously or synchronously.

Related topics describe how to configure the systems for both asynchronous and synchronous
invocations.

- Configuring servers to invoke services asynchronously

To enable service components on different servers to communicate, you must configure the servers similarly to enable the communication for applications that asynchronously invoke services on a different server.
- Configuring servers to invoke services synchronously

When a service component invokes another service component synchronously, you must configure the invoking service component to point to the system running the target so the target service can communicate results to the invoking service component.