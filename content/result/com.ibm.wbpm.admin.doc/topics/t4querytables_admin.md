<!-- image -->

# Administering query tables

## About this task

When query tables are deployed, the query table definition
is stored in the Business Process Choreographer database. Additional
database artifacts are not created in the current version of Workflow Server. Any changes
to composite and supplemental query tables, including deployment,
update, and undeployment, are visible to the query table API without
restarting the server.

Query tables are deployed on a stand-alone
server that is running or in a cluster with at least one member running.
The undeployment of supplemental and composite query tables is performed
also on running servers. For supplemental query tables, the related
physical database objects, typically a database view or database table,
must be created if they do not exist before the usage of the query
table.

For supplemental query tables, the user, or administrator,
is responsible for providing the related database table or view.

For
composite query tables, the information is composed of the existing
database tables or views that relate to the predefined or supplemental
query tables. Data is not duplicated in the current version of Workflow Server.

Supplemental
query tables which are referenced by deployed composite query tables
must not be updated or undeployed.

Using manageQueryTable.py you
can update composite and supplemental query tables and get their XML
definitions. You can also get a list of query tables that are available
on your system. For supplemental query tables, the related physical
database objects, typically a database view or a database table, must
be created if they do not exist before the usage of the query table.

- Deploying composite and supplemental query tables

Use the manageQueryTable.py administrative script to deploy supplemental and composite query tables before using them in Business Process Choreographer. Before query tables can be used with the query table API they must be deployed on the related Business Process Choreographer container. Query tables do not need to be started, and the server or cluster does not need to be restarted for them to be available after deployment.
- Undeploying composite and supplemental query tables

Use the manageQueryTable.py administrative script to remove composite and supplemental query tables in Business Process Choreographer.
- Updating composite and supplemental query tables

Use the manageQueryTable.py administrative script to update composite and supplemental query tables in Business Process Choreographer. Updates to query tables can be made while applications are running, and they are available after the update, without restarting the cluster.
- Retrieving a list of query tables

Use the manageQueryTable.py administrative script to get a list of query tables that are available in Business Process Choreographer. You can list predefined, supplemental, and composite query tables.
- Retrieving the XML definitions of query tables

Use the manageQueryTable.py administrative script to get the XML definition of composite and supplemental query tables in Business Process Choreographer.

<!-- image -->