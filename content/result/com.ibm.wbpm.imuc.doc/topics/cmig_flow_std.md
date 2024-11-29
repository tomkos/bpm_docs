# High-level task flow for migrating business data and applications from IBM BPM Express

1 Preparing to migrate Figure 1. Sample environment before migration begins.The source environment is running and transferring data to and fromits databases. The deployment environment has three clusters and isconfigured across two nodes.
    - Verify that your target installation environment
fulfills all requirements.
    - Prepare applications for migration, checking
for resources (such as data sources, JMS configurations, schedulers,
and environment variables), and application-specific authentication
aliases.

Figure 1. Sample environment before migration begins.
The source environment is running and transferring data to and from
its databases. The deployment environment has three clusters and is
configured across two nodes.

<!-- image -->

<!-- image -->

2 Installing IBM Business Automation Workflow 24.x Figure 2. Sample environment after 24.x is installed on the target. The source environment isrunning and transferring data to and from its databases. The target has been created but does notcontain a deployment environment.

- Prepare the operating system for installation.
- Install IBM Business Automation Workflow
24.x using Installation Manager.
- If you are migrating to a different computer,
package the remote migration utilities into an image using the BPMCreateRemoteMigrationUtilities command
and copy the image back to the source computer.

Figure 2. Sample environment after 24.x is installed on the target. The source environment is
running and transferring data to and from its databases. The target has been created but does not
contain a deployment environment.

<!-- image -->

<!-- image -->

3 Migrating the configuration from the source environment Figure 3. Sample environment after 24.x is installed onthe target and BPMConfig -migrate is run. The output folder is being copied to the targetenvironment. The source environment is running and transferring data to and from its databases. Thetarget has been created but does not contain a deployment environment.

- Run the BPMConfig -migrate command
to export the configuration information from the source environment
and generate the properties file.
- Copy the output folder to the target environment.

Figure 3. Sample environment after 24.x is installed on
the target and BPMConfig -migrate is run. The output folder is being copied to the target
environment. The source environment is running and transferring data to and from its databases. The
target has been created but does not contain a deployment environment.

<!-- image -->

<!-- image -->

4 Configuring IBM Business Automation Workflow 24.x and creatingthe target deployment environment Figure 4. Sample environment after 24.x is configured onthe target. The source environment is running and transferring data to and from its databases. Thetarget is not running but contains a deployment environment. The deployment environment has threeclusters and is configured across two nodes.

- Open a browser and graphically configure your new deployment environment with the IBM Business Automation
Workflow Configuration editor, by loading the
properties file and interacting with the topology diagram.
- Create a new empty database for each new database capability that
you added.
- Validate that all database connections are correctly configured
by running the BPMConfig -validate command.
- Create the target deployment environment using the BPMConfig -create command
and the properties file that you configured with the IBM Business Automation
Workflow Configuration editor. In addition to
creating the deployment manager, creating the nodes and federating the node profiles, and creating
the deployment environment, the command generates SQL scripts for upgrading and creating the
databases and puts them into the correct directories for you. You will run the scripts in a later
step.

Figure 4. Sample environment after 24.x is configured on
the target. The source environment is running and transferring data to and from its databases. The
target is not running but contains a deployment environment. The deployment environment has three
clusters and is configured across two nodes.

<!-- image -->

<!-- image -->

5 Upgrading the existing databases Figure 5. Sample environment after existing schemas and data are updated.The source environment is not running and the databases are not inuse. The databases contain updated schemas and data. The target isnot running but contains a deployment environment.

- To initialize the new database components and
upgrade the schemas of the existing databases, run the
upgradeSchemaAll\_de\_name command
that you generated previously.
- To upgrade the data in the source databases to 24.x, run the
DBUpgrade command.

Figure 5. Sample environment after existing schemas and data are updated.
The source environment is not running and the databases are not in
use. The databases contain updated schemas and data. The target is
not running but contains a deployment environment.

<!-- image -->

<!-- image -->

6 Moving your custom configuration to the target environment

- Start the deployment manager in the target
environment. Start the nodes. Start the clusters.
- Complete the configuration of IBM Business Automation Workflow.
- Complete the configuration of Business Space.
7 Restarting the target environment and verifying the migration Figure 6. Sample environment after migration. Thesource environment is not running. The target environment is runningand transferring data to and from its databases.

- Stop and restart the target environment.
- Verify that the migration was successful.

Figure 6. Sample environment after migration. The
source environment is not running. The target environment is running
and transferring data to and from its databases.

<!-- image -->

<!-- image -->