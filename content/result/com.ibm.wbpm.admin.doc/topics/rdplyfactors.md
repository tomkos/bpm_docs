<!-- image -->

# More deployment factors

## Third-party libraries

- You must add the library to the classpath of the connector project by
importing the library into the connector project. Then, update the classpath of
the project to include the library and export it.
- If the library is native: You must determine where the native library must be placed. It is
sometimes placed on the PATH variable of your machine. It might also be in the
bin folder of the workbench. In the case of SAP, place the third-party library
in the lib folder of the application server.

When you use the external service wizard for the adapters included with Business Automation Workflow, you are prompted for these libraries if they
are required.

## Changes to EIS systems

When the enterprise information system (EIS) you access from the discovery wizard or an adapter
changes, it affects the application that you created in IBM® Integration
Designer. Typically, this EIS change alters a
business object in some way. For example, if you add a column on a table in an EIS system and then
rediscover the EIS system or edit a service, you find a new element in the business object for the
column. This addition in turn might appear as an unmapped field in a map. Because most EIS systems
change, expect to see differences when you use the tools at different times.

If the third-party JAR files or connection properties change, you might have to update the
related activation specification or library JAR file.

## Federated namespaces

A federated namespace is a logical namespace where elements of the logical namespace can exist in
other places. Federated namespaces are supported in Integration Designer. Although, generally, federated namespaces do not
pose a problem to you, ensure that no types you specified in a namespace collide.

## Grouping import or export components

Group the import and export components for one EIS system. For example, do not mix components
that are created from querying a PeopleSoft server with components created from querying a CICS
server. If you have different PeopleSoft systems referred to in the same module, group the
components.