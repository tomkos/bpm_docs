# Installing and configuring IBM Business Automation
Workflow with
an Oracle database server

- Configuring XA transactions for Oracle

You must configure XA transactions after the Oracle database is installed and before you start the server.
- Creating users for Oracle databases

You must create the users for Oracle databases before you install IBM Business Automation Workflow. Create the cell-scoped user, the Process database user, the Performance Data Warehouse user, and the three users for the Content database: design object store user, target object store user, and IBM Content Navigator user. The Process, Performance Data Warehouse, and Content database users are not needed for an AdvancedOnly deployment environment.
- Installing and configuring Workflow Center with an Oracle database server

Workflow Center includes a repository for all processes, services, and other assets that were created in the IBM Business Automation Workflow authoring environments. You can use the integrated Workflow Server in Workflow Center to run processes as you build them. When you are ready, you can install and run those same processes on the Workflow Server in your runtime environments.
- Installing and configuring Workflow Server with an Oracle database server

Workflow Server provides one business process management runtime environment that can support a range of business processes for development, test, staging, or production.