<!-- image -->

# Using a resource reference in an assembly diagram

## About this task

## Procedure

1. In the Business Integration view,
select the module that contains your web service import.
2. Right-click the selected module and select Open
Deployment Editor. The module deployment editor opens.
3. Click the Design tab.
4 Create a resource reference by completing the followingsteps:
    1. Select the Resource References node.
    2. Click Add and select Resource Reference. A Resource Reference Wrapper and
a Resource Reference node is added under the Resource References node.
    3. Select the Resource Reference node.
    4. In the Name field, type the name
that you want to assign to the resource reference. For example, jdbc/DataSourceRefOnModule.
    5. In the Authentication field,
select the type of authentication that you want to use. For example, Container.
    6. In the Sharing scope field, select
the sharing scope that you want to use. For example, Shareable.
    7. In the Description field, type
a description for the data source reference.
5 Set a WebSphere-specific binding on the resource referenceby completing the following steps:

1. Select the Resource Reference Wrapper node.
2. Click Add and select WebSphere Binding. The Resource Reference WebSphere Binding
window opens.
3. In the JNDI name field, type
a JNDI name. For example, jdbc/li536pip.
4. Set the JAAS Configuration as
needed. Note that JAAS Configuration can only be set for specific
types of resource references that have authentication fields that
have been set to Container.
5. Click OK to close the window
box. A WebSphere Binding node is added under Resource Reference Wrapper.
6. Add properties under the WebSphere Binding node as needed.
6 Set a WebSphere-specific extension on the resource referenceby completing the following steps:

1. Select the Resource Reference Wrapper node.
2. Click Add and select WebSphere Extension. The WebSphere Extension node is
added under Resource Reference Wrapper.
3. In the Isolation level field,
select an isolation level.
4. In the Connection policy field,
select a connection policy.
7. Press Ctrl-S to save your changes
and then close the module deployment editor.
8. If your server is already running in the Servers view,
click the Build Activities tab to open the
Build Activities view and then click Update Running Servers.