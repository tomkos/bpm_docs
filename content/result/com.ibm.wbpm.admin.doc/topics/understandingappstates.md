<!-- image -->

# Application states for advanced process applications

In Business Automation Workflow,
the snapshot information is updated with each heartbeat from Workflow Server to Workflow Center. The
snapshot information includes the following data:

- The number of active process instances for the snapshot.
- Whether the snapshot is installed on the workflow server.
- The installation status of the snapshot, which indicates the specific
point in the installation process where the snapshot currently resides.

When an advanced process application is in an installed state, all artifacts have been imported
into the Workflow Center or Workflow Server database. When an advanced process
application is in a deployed state, all advanced artifacts have been extracted from the database and
packaged as a business-level application, which has been deployed to, and is started on, Workflow Center or Workflow Server.

An advanced process application must be installed to be deployed,
but it does not need to be deployed to be installed. For example,
if you have an advanced process application that is installed (and
exists in the database) but you have undeployed it (which removes
the advanced content from the server), Workflow Center will
report that the process application is installed.