# Managing deployment environment resources

## Before you begin

- Verify that the deployment environments exist on this deployment
manager.
- On the administrative console of the deployment manager, click Servers > Deployment Environments.
- You must completely stop any nodes you are removing from the deployment
environment before removing those nodes.

## About this task

As your deployment environment needs evolve, you can manage
its resources to address new demands and processing requirements.

In
managing the resources of a deployment environment, you can do the
following:

- Add or remove nodes or cluster members.
- Obtain information on how to configure databases or tables if
you previously deferred that operation.
- Use failed event manager to query and manage failed events.
- Check the configuration status of the deployment environment.
- If the deployment environment type is Process Server, change the settings related to IBM® Workflow
Server.
- Change authentication aliases.

## Procedure

1 Select the deployment environment for which you want tomanage resources by clicking the name. The systemdisplays the Deployment Environment Configuration pagewhich lists:
    - Deployment Environment
    - Deployment Environment Pattern
    - Description
    - Deployment Environment Status
    - Deployment Environment Functions
    - Links to the configuration pages
2. Select the configuration area of the deployment environment
to manage. Select each link until you complete your changes.

Configuration area
Available actions

Additional Properties

Deployment Topology
To change the configuration of a deployment environment based
on IBM-supplied patterns.
Deferred Configuration
To determine any manual steps needed to complete the configuration
of this deployment environment.
Failed Event Manager
To find and manage failed events on all servers in a deployment
environment. The interface enables you to view (and in some cases,
edit) the data for a failed event, resubmit a failed event, or delete
a failed event.
Health Center
To check the status of the configured components in an IBM Business Automation
Workflow deployment environment, such as IBM Workflow
Server, Workflow Center, and Performance Data Warehouse.
Workflow Server Settings
To update the workflow server configuration and modify connection properties, such as the
properties for connecting the server to a different workflow  center or changing it to an offline
server.

Related Items

Authentication Aliases
To change the authentication alias or password for components
within the deployment environment.
3. Complete the configuration by choosing the option for the
result needed. 
Action
Result

Click OK or Apply
Both options save the configuration. Apply leaves
you on the current page, OK returns you to
the Deployment Environments page.

## What to do next