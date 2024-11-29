# Maintaining an external Content Platform Engine
configuration

## The administrative role

The administrative role in Content Platform Engine is used
to run administration tasks. However, since the Business Automation Workflow object store is a shared resource between
Business Automation Workflow and Content Platform Engine, the user of this role must not change its
properties. A change to the Business Automation Workflow object
store by the administrative role makes the Business Automation Workflow object store inconsistent with the Content Platform Engine system.

## Shutting down and starting the systems in order

- Business Automation Workflow API calls that include access to
content artifacts will fail if the Content Platform Engine
environment is not available.
- The navigation of case instances will fail if, for example, the instance is at a point where it
synchronizes case folder properties; but the Content Platform Engine environment is not available.
- If the Business Automation Workflow environment is not
available, operations in the content repository will fail. For example, the content information
needs to be synchronized with Business Automation Workflow. This
situation might happen when a document is filed into a case folder, or when case folder properties
are updated.

1. When you shut down the Business Automation Workflow system, use the BPMconfig
-stop command. This command automatically shuts down the system in the correct
order: support cluster first, then application cluster, and, finally, messaging cluster. See BPMConfig command-line utility.
2. To shut down Content Platform Engine,
see Starting and stopping FileNet
P8 components.
3. Starting the systems occurs in the reverse order. Use BPMconfig -start to
start the Business Automation Workflow system. See BPMConfig command-line utility.

## Applying maintenance

If you need to apply maintenance, such as fix packs or updates to your environments, a few
dependencies must be considered for a Business Automation Workflow
environment that is connected to a Content Platform Engine
environment.

- Business Automation Workflow and Content Platform Engine are installed in separate WebSphere® Application
Server cells, which means that fixes can be applied
independently. A common WebSphere Application
Server level is not
required. Check the system requirements of each system.
- Content Platform Engine: The administrator must realize
that applying a maintenance update impacts Business Automation Workflow, because Business Automation Workflow must also be shut down. See Shutting down and starting the systems in order. Some Content Platform Engine fixes or upgrades might also need to be applied
to Business Automation Workflow. Refer to the documentation for the
fix or upgrade for special instructions with regards to dependencies.
- IBM Business Automation Workflow: The administrator must realize
that applying a maintenance update impacts Content Platform Engine, since Content Platform Engine must also be shut down. See Shutting down and starting the systems in order. Some Business Automation Workflow fixes and upgrades might also need to be applied
to Content Platform Engine. Refer to the documentation for the
fix or upgrade for special instructions with regards to dependencies.

- Backup and restore considerations with an external Content Platform Engine environment

When IBM Business Automation Workflow is configured with an external Content Platform Engine environment, these two environments share a resource, the object store. This shared resource affects backup and restore procedures. Depending on how the two environments are configured and how applications are designed to work with them, a backup of one environment may require a backup of the other. In some cases, a time-synchronized backup is advisable.
- Administering cluster members with an external Content Platform Engine

Adding and removing cluster members requires more consideration when IBM Business Automation Workflow is connected to an external Content Platform Engine (also known as external ECM) environment. A cluster member change might be required on either the Business Automation Workflow environment or the Content Platform Engine environment.