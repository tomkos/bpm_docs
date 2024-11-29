<!-- image -->

# Business Process Choreographer
administrative scripts

Look up a script by its name to find detailed syntax and
usage of that script. A list of administrative tasks related to each
script is also available.

- cleanupUnusedStaffQueryInstances.py administrative script

Use the cleanupUnusedStaffQueryInstances.py administrative script to remove from the database unused results from people queries.
- dbUtility.py administrative script

Use the dbUtility.py administrative script to check for and repair problems in the Business Process Choreographer database.
- deleteAuditLog.py administrative script

Use the deleteAuditLog.py administrative script to selectively delete audit log entries for the Business Flow Manager.
- deleteCompletedProcessInstances.py administrative script

Use the deleteCompletedProcessInstances.py administrative script to selectively delete from the Business Process Choreographer database any top-level process instances that have reached an end state of finished, terminated, expired, or failed.
- deleteCompletedTaskInstances.py administrative script

Use the deleteCompletedTaskInstances.py administrative script to selectively delete from the Business Process Choreographer database any top-level task instances that have reached an end state of finished, terminated, expired, or failed.
- deleteInvalidProcessTemplate.py script

Use the deleteInvalidProcessTemplate.py administrative script to delete process templates and their instances from the database.
- deleteInvalidTaskTemplate.py administrative script

Use the deleteInvalidTaskTemplate.py administrative script to delete, from the database, human task templates that are no longer valid.
- listTemplates.py administrative script

Use the listTemplates.py administrative script to display which versions of applications are deployed, and for each version, how many instances there are of it. This helps you to identify applications that can be uninstalled.
- manageQueryTable.py administrative script

Use the manageQueryTable.py administrative script to deploy, undeploy, and update query tables in Business Process Choreographer. This script can also list query tables and to list the XML definition of a query table.
- manageTemplates.py command

 Traditional: 
Use the manageTemplates.py administrative script to start, or stop, process and task templates that belong to a particular application. It can also uninstall BPEL applications and human task applications.
- migrateProcessInstances.py administrative script

Use the migrateProcessInstances.py administrative script to migrate running instances.
- queryNumberOfFailedMessages.py administrative script

Use the queryNumberOfFailedMessages.py administrative script to determine whether there are any failed messages for BPEL processes or human tasks, and, if there are, to retry processing them.
- refreshStaffQuery.py administrative script

Use the refreshStaffQuery.py administrative script to refresh people queries, because the query results are static.
- replayFailedMessages.py administrative script

Use the replayFailedMessages.py administrative script to retry processing failed messages.
- setStateObserver.py administrative script

Use the setStateObserver.py administrative script to enable or disable Dynamic Event Framework (DEF), audit events for Business Process Choreographer, or the task history log for the Human Task Manager. In addition, for federated environments that include Process Federation Server, you can enable or disable change logging for BPEL indexes.