# Restarting and verifying the migration

After you migrate to IBM® Business Automation Workflow, restart
the deployment environment and verify that the migration was successful.

Figure 1. Sample environment after migration. The
source environment is not running. The target environment is running
and transferring data to and from its databases.

<!-- image -->

<!-- image -->

## Procedure

1 IBM Business Automation Workflow 24.x uses the moresecure HTTPS protocol instead of HTTP.
    - If you are connecting an online server to Workflow Center, you must import the
Workflow Server root SSL
certificate into Workflow Center to enable HTTPS before
you start the environment. Follow the instructions in steps 1 and 2 in Configuring Secure Sockets Layer (SSL) communication in a network deployment environment.
    - Alternatively, if you want to switch back to using HTTP between Workflow Center and online servers,
run the following wsadmin commands on the Workflow Center and each server. Run
the commands from the bin directory of the deployment manager. In the following
example, bpdServer is the name of the Workflow Center.wsadmin -connType NONE -lang jython
wsadmin>bpdServer=AdminConfig.list("BPMProcessCenter").split()  # Use "BPMProcessServer" for Workflow Server
wsadmin>bpdServer  # You see the Workflow Center and Workflow Servers that you listed
wsadmin>print AdminConfig.showAttribute(bpdServer[0],'useHTTPSURLPrefixes') # You see the current value
wsadmin>AdminConfig.modify(bpdServer[0],[['useHTTPSURLPrefixes','false']]) # Set the value to false
wsadmin>AdminConfig.save()Restart all deployment managers, nodes, and deployment
environments for Workflow Center and workflow
servers.
2 Restart the target environment: If you are migrating three clusters and using a DB2 for z/OS database, you might receive anerror and exception in the Performance Admin console when you select any option other than theWelcome or View Instrumentation option. For example:An error occurred while trying to view business performance server statisticscom/lombardisoftware/server/tracking/statistics/RecordCounts This problem is intermittent, but you can generally resolve the problem by stopping and thenstarting the servers in the correct order to resolve cross-dependencies between the three clusters.To stop and then start the servers in the correct order, stop AppCluster ,SupportCluster , and MECluster , then startMECluster , SupportCluster , andAppCluster .

1. Stop the target environment.
2. Stop the deployment manager and the nodes.
3. Start the deployment manager and the nodes.
4. Start the target environment.

An error occurred while trying to view business performance server statistics

com/lombardisoftware/server/tracking/statistics/RecordCounts

This problem is intermittent, but you can generally resolve the problem by stopping and then
starting the servers in the correct order to resolve cross-dependencies between the three clusters.
To stop and then start the servers in the correct order, stop AppCluster,
SupportCluster, and MECluster, then start
MECluster, SupportCluster, and
AppCluster.

3. For a Workflow Center migration, use
Workflow Center and the
Designer view in IBM Process
Designer to verify that
all process applications, toolkits, and assets are available in the repository.  From
Workflow Center, verify that
connected servers are showing up and that previously installed snapshots are accurately listed. Use
the Inspector view in IBM Process
Designer to check active
instances.If you are using or converting to responsive coach views in the Responsive Coaches or
Content Management Toolkits, you must add a dependency on the System Data V8.5.7.0 toolkit or a
toolkit or process application that has a theme. The responsive coach views require theme
definitions. The BPM Theme in the System Data toolkit provides these theme definitions and it is the
default theme for new process applications.
4. To verify that Heritage Process Portal is working, complete
the steps in Verifying Process Portal.

Attention: Starting with IBM Business Process Manager
 V8.5.7, there is a
new default Process Portal.
The Process Portal
application from earlier versions is available as Heritage Process Portal. The information in
the referenced topics applies to both Process Portal and Heritage Process Portal.Starting with Cumulative Fix
2016.12, Heritage Process Portal is
deprecated.

The Process Portal index
is rebuilt on server restart. In the SystemOut.log file, look for the
CWLLG0764I and CWLLG0765I messages that identify the start and
completion of the index rebuild.Important: While the index is being rebuilt, the search
facility in Process Portal is unavailable.

If you want to customize the index creation, for example, calculate the completion dates for
instances that are migrated from previous versions of Business Automation Workflow, follow the instructions
in Updating the Process Portal index.

If you migrated to IBM BPM Advanced and the other spaces
(globe) icon in Heritage Process Portal does not work to navigate to other Heritage Process Portal spaces, delete your
browser cache and reload the page.

Restriction: If you created a saved search that has a condition with an empty value in
an earlier version of Business Automation Workflow, you will see a blank
page when you select the saved search. You must re-create the saved search.
5. If you are migrating from IBM Business Process Manager
 V8.0 or later, the
cleanup of shared business objects is automatically disabled. If you are using shared business
objects in the source version, you might want to change the
cleanupMaxVersionCount property to explicitly enable cleanup. See Cleaning up shared business objects for instructions.
6. After the migration is complete and the server is started, if you want to use the case
management features, run the command in  createObjectStoreForContent command before
you can use the embedded Content Platform Engine. Follow the instructions
in Configuring your system for case management Configuring your system for case management to configure your system
for case management before using case management. Then, to design and configure case management, see
Case management in IBM Business Automation Workflow.

## What to do next

If you cloned your databases to
test the migration, and you are satisfied with the results of your
testing, retarget your new environment to point to the original source
databases.

1. Restore and edit the previous BPMConfig configuration
properties file that pointed to your source databases.
2. Create any new
databases that are required and validate your database connections.
Follow the instructions under Creating new databases and validating database connections for
your specific database type. Alternatively, you can keep the databases
that you created the first time that you went through the steps, especially
if you want to keep the test data that you put into them.
3. Make sure that your target environment
is shut down. Run the following command to retarget your target environment
to point to your original source databases:install\_root/bin/BPMConfig -update -dataSource path\_to\_properties fileImportant: To use this retarget feature, keep the user and schema
name for each component the same in the cloned database as in the
original database. This command updates only the host, port, and database
name. It does not update the associated user authentication and schema.
4. Run the following command to generate the
Upgrade SQL scripts again:install\_root/bin/BPMGenerateUpgradeSchemaScripts -propertiesFile target\_migration\_properties\_filewhere target\_migration\_properties\_file 
is the full path to the migration properties file in which you specified
the configuration information for the target environment
5. Back up your source databases before upgrading.
6. Copy the whole folder target\_deployment\_manager\_profile/dbscripts/Upgrade/ to
your database computer. On the database computer, run the following
command to upgrade all schemas:upgradeSchemaAll\_de\_name.sh
7. Run the DBUpgrade utility to modify your
existing database schemas and data for use with IBM Business Automation Workflow
24.x. Follow the
instructions under Upgrading existing databases for your specific database type. Only perform
the steps necessary to run the DBUpgrade utility.

## Related information

- Starting and stopping your environment
- BPMGenerateUpgradeSchemaScripts command-line utility