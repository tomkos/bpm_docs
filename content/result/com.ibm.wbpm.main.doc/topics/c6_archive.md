<!-- image -->

# Business Process Archive Manager EJB API support

## API functions supported

The Business Process
Archive Manager supports a subset of the API functions offered by
Business Process Choreographer. They use the same packages, so binary
compatibility is ensured. For more information about the Business
Process Archive Manager API refer to the JavaDoc for the packages
com.ibm.bpe.api and com.ibm.task.api.

Whereas Business Process
Choreographer provides several API renderings (EJB, REST, JAX-WS,
JAX-RPC, and JMS), the Business Process Archive Manager only offers
an EJB version of the APIs.

The following table summarizes
which kinds of API operations can be performed on objects in an archive
database.

| API operations on   | Business Process Choreographer   | Business Process Archive Manager   |
|---------------------|----------------------------------|------------------------------------|
| Templates           | Read, start instance             | Read                               |
| BPEL processes      | Create, read, update, delete     | Read, delete                       |
| Human tasks         | Create, read, update, delete     | Read, delete                       |
| Query tables        | Create, read, update, delete     | Create, read, update, delete       |
| Stored queries      | Create, read, update, delete     | Create, read, update, delete       |
| Work items          | Create, read, update, delete     | None                               |
| Work baskets        | Create, read, update, delete     | Read, delete                       |
| Business categories | Create, read, update, delete     | Read, delete                       |

## Making a custom client work with archived data

If
you want to implement a client that can work with completed instances
that have been moved to an archive database, consider the following
points:

- A new method, OperationMode getOperationMode() is
provided, which indicates whether the client is connected to a Business
Process Choreographer configuration or a Business Process Archive
Manager configuration. You can use it to write custom clients that
can connect to and operate appropriately on runtime configurations
and archive configurations.
- Although the Business Process Archive Explorer can only connect
to a single Business Process Archive Manager configuration, it is
possible to develop a client application that can connect to, and
allow a user to work with multiple Business Process Choreographer
and Business Process Archive Manager configurations.
- Plan which users will use the client to access an archive database.
By default, authorization is based on Java EE roles, which restricts
access to administrators and monitors. Because work items are not
stored in the archive database, it is not possible, for example, to
give normal users access to just the instances that they started or
worked on. If you want normal users to be able to use a custom client
to access an archive database, you cannot use the queryAll() API,
which requires an administrator or monitor role. If you can accept
having no authorization checking, you could use the query table API
calls queryEntities() and queryEntityCount() together with either
a custom or predefined query table that takes into account that no
work item information is available.