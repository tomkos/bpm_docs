<!-- image -->

# Considerations for multiple deployment environments in the
same cell

## Isolation considerations

- The contents of the CellOnlyDB schema and the runtimes of the corresponding components (like
Business Rules) are shared by all of the deployment environments. For information about the
components that exist in the shared CellOnlyDB schema of the CMNDB database, see the topic Planning the number of databases. Note: With the exception of the CellOnlyDB schema, you cannot share databases
across multiple deployment environments.
- The Service Component Architecture (SCA) module names are cell-scoped, which means that the
namespaces of the modules are shared across all of the deployment environments. For additional
information, see the Application considerations section.
- The Module Browser widget can be used to list all the deployed SCA modules in a cell and select
one for detailed inspection or administration. For more information, see the topic  Module Browser Widget.
- In a multibus environment, such as a deployment environment that was migrated from WebSphere
Workflow Server 7.0 or IBM Business Process Manager 7.5 or 8.0, the component-specific buses have the
following naming conventions:

Workflow Server
PROCSVR.cell\_name.Bus
Performance Data Warehouse
PERFDW.cell\_name.Bus
Business Process Choreographer
BPC.cell\_name.Bus
SCA
SCA.APPLICATION.cell\_name.Bus and
SCA.SYSTEM.cell\_name.Bus

These buses are shared among all deployment environments in the cell, which is not the case
for the Business Automation Workflow 8.5 deployment
environment-scoped default bus BPM.de\_name.Bus.
Note: Regardless of whether the service integration buses are shared, the messaging engines are not
shared between deployment environments.

## Application considerations

- You cannot install two instances of the same Service Component Architecture (SCA) application inthe cell with the same name. You can install many SCA applications, but they must have differentmodule names. How you provide them with unique names in the cell depends on how you are installingthe module into the deployment environment:
    - If module is a stand-alone module, use the -uniqueCellID parameter in
serviceDeploy utility to give it an unique identifier within the cell.
    - If the module is advanced content within a process application, set the
AdvancedDeploymentDEScoped property for each deployment environment. By setting
this property, the deployment environment name is automatically added to the module name to create a
unique name for the module in the cell.For information, see the step that describes how to set
the AdvancedDeploymentDEScoped property in Isolating deployment environments.
- For late binding to work, new versions of a BPEL business process or human task (template) must
be deployed to the same deployment environment as the earlier version. The correct target to bind to
must be found in the same deployment environment. Make sure that parent-child relationships between
processes or between human tasks are scoped to the deployment environment. There are some
relationships, like parent-child flows, that should not cross JVMs.
- Each Process Portal has one view to each
deployment environment and requires unique context roots. Consider whether to use a different web
server for each deployment environment. If not, you must provide different virtual hosts to ensure
unique context roots for applications.

## Administration considerations

- Each application cluster must have a corresponding support cluster
and messaging engine cluster.
- Selecting the correct failed event manager to retry events might
be difficult when you have more than one deployment environment.
- You must ensure unique names for all applications that contain
SCA modules such as BPEL processes, calendars, rules, selectors, and
relationships.
- You must ensure unique names for Business Automation Workflow applications as well
as for customer applications.
- You must add databases and schemas for each set of clusters, whichincreases administration responsibilities. Each set of clusters requiresdatabases and schemas for:
    - Process database
    - Performance Data Warehouse database
    - Common database at the deployment environment level

## Maintenance considerations

- If there is an issue with one application in the cell, it is not
possible to apply an interim fix only to the affected deployment environment.
Interim fixes affect all servers, deployment environments, and clusters
in the cell. Fixes for one application might have an unanticipated
effect on the other applications that are running in the cell.
- Testing an interim fix from IBM is more difficult when several
deployment environments are in the same cell. Separate cells help
ensure that fixes do not break other applications.
- You might have to bring down all your servers to apply interim
fixes for one set of clusters, resulting in downtime across all the
sets of clusters using the cell. Although the exact arrangement of
servers varies, a common arrangement of servers is to have one member
of each cluster on each node. In such an arrangement, all servers
and cluster members that share the node are affected by the steps
to apply the interim fix.