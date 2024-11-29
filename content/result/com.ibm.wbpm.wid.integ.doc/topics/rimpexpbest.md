<!-- image -->

# Trade-offs when developing adapter imports and exports

## Using connection properties specified
on a server or using the discovered ones

When using the
external service wizard with adapters that access EIS systems, the
wizard will detect the connection properties and towards the end of
building your import or export component, you can use these properties
or you can specify your own. Using the connection properties specified
on a server means that someone, usually a system administrator, has
set up the connection properties ahead of time. The system administrator
provides you with the Java™ Naming
and Directory Interface (JNDI) lookup name and Java Authentication and Authorization Service
(JAAS) alias name. You insert the information and continue using the
wizard. The advantage to this method is that you and others do not
waste your development time in this area, security is maintained by
one person, the system administrator, and there is one central control
area to maintain. However, you may not have such a person, particularly
if you are in a smaller organization, or you do not have many servers
to maintain. In this case, the external service wizard provides you
with the connection information it has found and you need to only
add a few extra values. For example, the adapter you use might require
that you add the password and national language information.

## Deploying or not deploying the
adapter in the module

When you build a component using the
external service wizard, you are given the option of including the
adapter in your module. Why might you consider this option and what
is the trade-off? Sometimes you may have several versions of the same
adapter. Including the adapter with the module could be a way of handling
the different versions. There is also a security consideration. You
may not want a user accessing an adapter and so you could contain
it in the module. Is the user accessing the adapter from the same
application? Then you might include it. But if the user is accessing
the adapter from another application, then it needs to be separate
from the module.

The trade-off for including the adapter in
the module is that with each deployed service you are carrying the
cost of an additional adapter, which can occupy considerable space
on your application server. Also, there is a higher maintenance cost.
When you have to upgrade an adapter, if it is installed on a server
then you only have to make a single update. One more point: some adapters
may only support being deployed embedded in a module or on the server.

## Federated namespaces

A federated namespace is a logical namespace where elements of the logical namespace may reside in other places. Federated namespaces are supported in IBM® Integration
Designer. Generally, federated namespaces will not pose a problem to you, however, you must be careful that you do not have collisions of types within a single namespace you have specified.

## Grouping import or export components

It
is good practice to group the import and export components for a single
EIS system. For example, you should not mix components created from
querying a PeopleSoft server with components created from querying
a CICS® server. If you have
different PeopleSoft systems referred to in the same module, the components
should be grouped accordingly.

## Related concepts

- Pattern of accessing external services with adapters
- Developing services with adapters
- Simple adapter wizard
- Migrating applications using previous adapter levels

## Related tasks

- Configuring and using adapters
- Creating a business object from a source file

## Related reference

- J2C data bindings
- A closer look at business objects from data structures
- J2C imports and exports at run time
- Considerations when using adapters
- Considerations when refactoring
- Contributing your own external service or data wizard plug-in
- Limitations for adapter imports and exports