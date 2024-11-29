# Adding a case with a second project area user

## Procedure

To add a case with a second project area user in the Case Client, complete the following steps:

1. Follow the instructions in Creating the DB2® database and table spaces for a Content Platform Engine object
store.
2 Create JDBC data sources in either of the following ways: Note: For the XA data source, you need only the webSphereDefaultIsolationLevel custom property. But for the non-XA data source, you need both properties.
    - Manually. For each object store, configure its two data sources (XA and non XA) under the
Custom Properties panel in the WebSphere administrative console with the
following custom
properties:resultSetHoldability (value: 1)
webSphereDefaultIsolationLevel (value: 2)
    - Follow the instructions in Creating additional object store data sources by using the graphical user
interface.
3. Follow the instructions in Creating a database connection.
4. Follow the instructions in Creating an object store.
5. Following the instructions in Creating a workflow system.
6. Follow the instructions in Creating a target object store.