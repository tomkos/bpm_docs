# Upgrading your IBM Case
Manager system by using
the embedded IBM Content
Navigator

## Before you begin

## About this task

Figure 1. Topology before and after augmentation

<!-- image -->

<!-- image -->

1. Back up your source databases.
2. Update your IBM Content
Navigator and Content Platform Engine.
3. If you haven't already, install and configure Business Automation Workflow.
4. Configure Business Automation Workflow to use your
Content Platform Engine.
5. Run the case configuration tasks.
6. Update custom extension packages and custom case widgets if you are using them.
7. Restart the deployment environment.

## Procedure

1. Back up your IBM Case
Manager databases,
including the databases for the IBM Content
Navigator, the design
object store, and the target object store. For example, ICNDB, DOSDB, and TOSDB.
2. Update your IBM Content
Navigator and Content Platform Engine to the version supported
by Business Automation Workflow. See Detailed system requirements for a specific product.
For instructions, see Upgrading IBM Content Navigator and Upgrading Content Platform Engine.
3 Optional: If you already installed Business Automation Workflow and created a deploymentenvironment, make sure that you configure IBM ContentNavigator to reuseyour previous IBM ContentNavigator database.
    1. Start the deployment manager and nodes.
    2. Log in to the WebSphere Application
Server administrative console. 
The URL is
http://hostname:port1/admin or
https://hostname:port2/admin.
    3 Click Resources > JDBC > datasources . Click the IBM BPM Content Navigator ECM client datasource . In the Common and required data source properties table, change thefollowing properties: Save your changes.
        - Server name: The hostname of the computer where your previous IBM Content
Navigator is
located.
        - Database name: The name of your previous IBM Content
Navigator
database.
        - Port number: The port that is used for the database.
4. Make the same changes as in the previous substep for the IBM BPM Content Navigator
task manager data source.
4 Optional: If you did not yet install Business Automation Workflow , install it.

1. Choose a sample properties file from the
Workflow\_install\_root\BPM\samples\config\externalcpe
directory, based on your database and the type of deployment environment you want.
For a development environment, choose a properties file with
bpm.de.environment=Process Center. These files do not contain the Content Platform Engine configuration. You must
configure the newly installed Business Automation Workflow to reuse your previous
Content Platform Engine
configuration.
2 Modify the properties file by using your real environment values. Pay special attention to the following properties and make sure that they are configuredcorrectly:
    - To use the embedded IBM Content
Navigator and the
external Content Platform Engine, make
sure that you set the following properties as shown:bpm.de.deferSchemaCreation=true
bpm.de.useExternalNavigator=false
bpm.de.useExternalCPE=true
    - To configure your previous IBM Content
Navigator database to
work with the embedded IBM Content
Navigator, set the
value of bpm.de.db.number.hostname to the hostname of the
previous IBM Content
Navigator server. Set
the value of  bpm.de.db.number.schema to the schema of the
previous IBM Content
Navigator database.
Set the value of bpm.de.db.number.tsicn to the table space name
of the previous IBM Content
Navigator database.
Set the type and port number based on the database that you are intending to
use.bpm.de.db.number.type=database\_type
bpm.de.db.number.hostname=host\_name
bpm.de.db.number.portNumber=port\_number
bpm.de.db.number.databaseName=ICNDB\_name
bpm.de.db.number.schema=ICNDB\_schema
bpm.de.db.number.tsicn=ICNDB\_tablespace
    - Set the ECMTechnicalUserAlias as the user from the LDAP shared user repository that will be used
as the administrator for the object store, for
example:###########################################
# ECM technical user authentication alias #
###########################################
bpm.de.authenticationAlias.number.name=ECMTechnicalUserAlias
bpm.de.authenticationAlias.number.user=user from LDAP shared user repository
bpm.de.authenticationAlias.number.password=password of the user
3 Create the Business Automation Workflow deployment environment byusing the BPMConfig command-line utility . Follow the instructions for your database type under the following link:

- Configuring profiles and creating a network deployment environment on Linux
- Configuring profiles and creating a network deployment environment on Windows
4. After you create the deployment environment, before you try to start it, run the
BPMConfig -create command to generate the SQL scripts that create the schemas and
tables for the applications. Then, run the scripts, except for the scripts for the databases for
IBM Content
Navigator and
Content Platform Engine (usually called
CPEDB, or ICNDB, DOSDB, and TOSDB).  See the BPMConfig command-line utility for
instructions.
5 Run the bootstrapProcessServerData command to load theconfiguration data into the database. Follow the instructions for your environment:

- Loading the database with system information in a network deployment environment on AIX or Linux
- Loading the database with system information in a network deployment environment on Windows
6. Start the environment and run a health check for the deployment environment.
Follow the instructions in Starting your environment and Verifying the status of your environment using the Health Center.
5. Configure Business Automation Workflow
to use your previous Content Platform Engine, namely the same
environment that IBM Case
Manager uses for the
design object store (DOS) and target object store (TOS). Follow the instructions in Configuring an existing external Content Platform Engine. 
For considerations on object store configuration, see Planning for an external Content Platform Engine.
6 Configure properties for Lightweight Directory Access Protocol (LDAP) so that the sameconfiguration is used by both Business Automation Workflow and FileNet ContentManager. For example, the user and group name attributes: For more information, see Configuring the user registry and Directory service providers .

- Business Automation Workflow - user-full-name-prop and group-name-prop
- Content Platform Engine - userShortNameAttribute and
GroupNameAttribute
7 Run the Case configuration tool to deploy the case plug-ins onto the IBM ContentNavigator server. For information about the Case configuration tool, see the topic for your environment: Important:

- Workflow Center: Preparing to run the case configuration tasks
- Workflow Server: Preparing to run the configuration tasks

- For the Edit Profile Properties task, on the second panel, enter the values
that you used for the embedded IBM Content
Navigator. However,
for the IBM Content
Navigator
administrator username and password, you must enter the values for the previous IBM Content
Navigator. Otherwise,
you cannot test the connection successfully.
- For the Configure Business Rules task, specify the same path that you used in
IBM Case
Manager.
- Make sure that the Network Shared Directory property value in the Edit
Development Environment Profile Properties wizard is the same as the one that you set in
the Business Automation Workflow properties
file. If you want to change this network shared directory value, then after you change the value in
the wizard, you must also rerun the BPMConfig command, for example:
BPMConfig  -update -profile DmgrProfile -de De1 -networkDirectory new network directory -component CaseManager
- If you previously configured IBM Content
Navigator or Content Platform Engine related plug-ins (such as
the Content Platform Engine Applets
Support plug-in), you must run the related task in the configuration tool (such as
Register the IBM Content Platform Engine Applets Support
plug-in) to redeploy the plug-ins using the new path to the network shared directory. If
the mapped tasks are disabled, enable and run them.

1 Optional: If you are using custom extension packages, updatethem. In the Case configuration tool, run the Deploy & Register ExtensionsPackage task to deploy the custom extension package plug-in to the IBM ContentNavigator .
    1. Right-click the task and select Enable Task.
    2. Enter and check the properties.
    3. Run the task.
2 Optional: If you are using case custom widgets that refer to IBM CaseManager resources, youmust update the implementation code because, after augmentation, the resources are located on theremote Business Automation Workflow computerinstead of the IBM CaseManager computer. In the Case configuration tool, run the Deploy & Register CustomWidgets Package task to deploy the Case custom widget plug-in to the IBM ContentNavigator . For troubleshooting information, see Troubleshooting IBM Case Manager system upgrades .

1. Right-click the task and select Enable Task.
2. Enter and check the properties.
3. Run the task.
8 To avoid encountering problems when you deploy yourcase management solutions in Business Automation Workflow , make sure the followingfiles are present in the Content Platform Engine directory:

1. Copy the ODMMessages.jar file from the Business Automation Workflow home directory
<install\_root>/lib/ext to the external Content Platform Engine directory at
<WAS-home>/lib/ext. The ODMMessages.jar is
required for the embedded IBM Operational Decision
Manager rules
SDK.
2. Copy the ejb-lookup.jar file from the Business Automation Workflow directory
<install\_root>/CaseManagement/configure/deploy to the
Content Platform Engine directory at
<WAS-home>/lib/ext.
3. Restart the external Content Platform Engine for changes to take
effect.
9. Restart the Business Automation Workflow deployment
environment.
10 To avoid accidentally editing solutions in the previous version of Case Builder or logging in to theprevious version of the navigator after the upgrade, remove the previous CaseBuilder and navigatorapps.

1 In the WebSphere administrative console for IBM CaseManager (https://case\_computer :9043/ibm/console ) go to Applications > All Applications .
    - Select CaseBuilder and click Remove.
    - Select navigator and click Remove.
2. Save the changes to the WebSphere Application
Server configuration, and restart
the WebSphere Application
Server profile.
11. Upgrade and convert your existing case solutions, see Upgrading and converting case solutions.

## Results

You must reconfigure other systems that rely on IBM Content
Navigator.

<!-- image -->

- Workflow Task:
https://Workflow\_hostName:SSL\_port/teamworks/navigator-plugins/workflow-icn-plugin.jar
- Case Client:
https://Workflow\_hostName:SSL\_port/ICMClient/ICMClient.jar
- Case API:
https://Workflow\_hostName:SSL\_port/ICMClient/ICMAPIPlugin.jar
- Case Administration:
https://Workflow\_hostName:SSL\_port/ICMClient/ICMAdminClientPlugin.jar
- Case Monitor Dashboard:
https://Workflow\_hostName:SSL\_port/ICMClient/ICMMonitor.jar

## What to do next

If you encounter case management problems after you install or upgrade to IBM Business Automation
Workflow, see Troubleshooting IBM Case Manager system upgrades.

After a successful upgrade, you can promote your case solutions to workflow projects, which you
can easily manage in Business Automation Workflow. See Promoting case solutions to the Workflow Center.