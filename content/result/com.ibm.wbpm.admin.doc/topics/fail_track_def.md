# Failure when sending tracking definitions

In Microsoft SQL Server, the default schema name associated with
a user must be the same as the user name. For example, if the Performance
Data Warehouse database user name is perfDB then
the default schema name associated with the user perfDB must
also be named perfDB. When the Performance Data
Warehouse database user name is sa, the default
schema name is required to besa. However, sa is
a super user in Microsoft SQL server, and the default schema for the
super user is dbo and this schema name cannot be
changed.

You must create an ordinary database user and assign the required
rights to the user instead of using a super user, such as sa.

1. On the Workflow Server network
deployment environment, change the Performance Data Warehouse data
source to use the Performance Data Warehouse user name perfDB instead
of the username sa .
2. Stop the Workflow Server  deployment
environment.
3. Drop the Workflow Server Performance
Data Warehouse database on SQL Server.
4. Using db scripts, recreate the Performance Data Warehouse database
with the user perfDB instead of the user sa.
5. The Performance Data Warehouse tables in the database are created
under the user schema perfDB.
6. Restart the Workflow Server  deployment
environment.
7. In the Process Admin console, run Update tracking definitions for
each process application that is deployed. This may take some time
to complete.