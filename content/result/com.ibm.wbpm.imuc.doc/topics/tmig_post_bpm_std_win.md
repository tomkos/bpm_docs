# Completing configuration for IBM Business Automation Workflow

After migration, you must check and possibly change
some configuration settings.

Figure 1. Sample environment after the target is
started. The source environment is not running. The target can read
from the databases.

<!-- image -->

<!-- image -->

## Procedure

WebSphere® Application
Server updates:

1. Using the administrative console, manually update any hard-coded port
numbers or IP addresses in your applications according to the new settings. Because the
target version recreates the topology, the port numbers and IP addresses might not be the same as in
the source version. From the administrative console, click
Servers > WebSphere application
servers > Server\_Name > Communications >  Ports > Detail. For additional information, refer to the WebSphere Application
Server
documentation.
2. Required: If you are migrating from a deployment environment using
LDAP, you must configure LDAP with the same settings in the target environment. See Configuring the user registry. 
Note: If you are using a federated repository and an unencrypted LDAP connection in the source
environment, the LDAP settings are migrated automatically and you can skip this step. If you
configured any LDAP repository additional properties or LDAP attributes, you must customize them to
be the same as before.
3. Apply the same proxy or HTTP server configurations that were present in your
source environment, and also update the virtual host configuration as needed. See the
WebSphere Application
Server documentation for
information about Setting up the proxy server and Configuring virtual hosts.If you have any related customization in
100Custom.xml files, such as URL prefixes, they are automatically migrated to
the Business Automation Workflow virtual host
during migration. See  Security configuration properties for more
information.

Database updates:

1. If you are using DB2, make sure that the CUR\_COMMIT parameter is set to
ON.
2. Restructure disorganized database tables and update database
statistics. See the documentation that came with your specific database. Tip: For DB2, you can use the reorgchk utility to find disorganized tables and
indexes. If the tool suggest a reorganization, run the reorg utility. After the
reorganization, run the runstats utility to reflect the reorganized tables and
indexes in the optimizer statistics. You can update statistics manually by using the following
command: runstats on table schema\_table on all columns
with distribution and detailed indexes all

Business Automation Workflow updates:

1 If you have customized data sources in the source environment,check the custom properties on the data sources and if necessary apply the same properties to thetarget environment. The following data sources must be analyzed:
    - jdbc/mashupDS (if Business Space was configured in the source environment)
    - jdbc/TeamworksDB
    - jdbc/PerformanceDB
    - jdbc/MEDB or jdbc/messaging\_engine\_database\_name
2 If you changed properties in one of these XML files in the sourceenvironment, you must move the changes to the 100Custom.xml file in the targetenvironment. For instructions for modifying the100Custom.xml file, see The 100Custom.xml file and configuration .Note: Some properties might be missing in the target XML file if they belong to the set that hasbeen moved to the WebSphere ApplicationServer configuration files. Use the WebSphere command-line administration tool (wsadmin) AdminConfigcommands to update the values in the target environment. Refer to Security configuration properties for a list of the properties that have been moved to WebSphere ApplicationServer configurationfiles.

- 00Static.xml
- 50AppServer.xml
- 60Database.xml
- 80EventManager.xml
- 98Database.xml
- 99Local.xml
- 99Sharepoint.xml
3. If you customized the search variables in the source environment, you must apply the same
customization in the target environment. For instructions, see Setting the location of the
index in Configuring the Process Portal index.
4 Apply the user-to-role mappings and the RunAs role user assignments forthe IBM Business Automation Workflow systemapplications to match the source environment. The following system applications must be analyzed: See Business Automation Workflow security roles and Defining RunAs roles user assignments for system applications .

- BPMAdministrationWidgets
- BPM\_BPM\_Help
- BSpaceEAR (if Business Space was configured in the source environment)
- BSpaceForms (if Business Space was configured in the source environment)
- BSpaceHelp (if Business Space was configured in the source environment)
- IBM\_BPM\_PerformanceDW
- IBM\_BPM\_Portal
- IBM\_BPM\_ProcessAdmin
- IBM\_BPM\_ProcessPortal
- IBM\_BPM\_Repository
- IBM\_BPM\_ResponsivePortal
- IBM\_BPM\_TeamWorks
- IBM\_BPM\_WebAPI
- mm.was (if Business Space was configured in the source environment)
- PageBuilder2 (if Business Space was configured in the source environment)
- RestServicesGateway
5. If you migrated from a IBM Business Process Manager
 version earlier than
V8.0, be aware that authorization for actions on processes and tasks now gets enforced correctly in
cases where it was not enforced previously. Before V8.0, if you use the Expose to
start setting in a business process definition (BPD) to restrict who can start a
process, this setting was ignored, and anyone could start a process. If you want to retain this
behavior in IBM Business Automation Workflow,
you must create a new version of your process, and change the Expose to start
setting so that all users can start the process.
6. If you subscribed to Blueworks Live processes in previous releases, the
tags on the process in Process Designer are labeled Blueprint. In 24.0.0.0 or V20.x, Blueworks
Live processes that are subscribed to are tagged Blueworks Live. In Process
Designer, you can right-click the process and change the tag.
7. To prevent performance problems, you must perform regular maintenance on
artifacts that accumulate over time, such as process instances, named snapshots, unnamed snapshots,
task instances, and durable messages.  To customize the settings for system maintenance,
see Configuring notifications and actions for system maintenance.

Application updates:

1 Make required changes to your applications.
    1. Some authentication aliases have been removed from IBM Business Automation Workflow. If your applications
are using aliases that have been removed, you must re-create them manually in the target
environment. See Default users and authentication aliases removed from Business Automation Workflow.
    2 As mentioned in the premigration steps, if your applications reply on specificWebSphere ApplicationServer configuration,the applications might fail to start or fail to work correctly in IBM Business Automation Workflow unless you re-createany required resources in the target environment. These include the following resources:
        - JMS configurations
        - Schedulers
        - Environment variables
        - Shared library configurations
        - Work Manager
        - Mail sessions
2. Re-create external data sources. The migration utility does
not migrate extra data sources. If your applications depend on data sources that you added in the
source environment, you must re-create them in the target environment using the same configuration
as the source. For instructions, see Configuring a data source using the administrative console in the WebSphere Application
Server
documentation.
3. If you used the exportWASConfig.py script to
export customized WebSphere Application
Server
configuration, you can use the importWASConfig.py script to import the customized
configuration to the target environment.
4. If you customized the IBM Process Federation
Server in the source
environment, the databases and artifacts are migrated for you, but you should check your Process Federation Server configuration
on both the Process Federation Server side and the
Business Automation Workflow side to ensure
that the configuration is the same in the source and target environments.