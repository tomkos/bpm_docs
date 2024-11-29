# Upgrading your IBM Case
Manager system
using an external IBM Content
Navigator

## Before you begin

## About this task

This upgrade requires IBM Case
Manager and a new
separate installation of Business Automation Workflow and WebSphere® Application
Server. Do not install and
configure Business Automation Workflow into
an existing WebSphere Application
Server Network Deployment
where Content Platform Engine or
IBM Content
Navigator is
configured. It is not recommended to install Business Automation Workflow, Content Platform Engine and IBM Content
Navigator into single
WebSphere® Application Server cell. In case you insist to install them into one single WebSphere®
Application Server cell, you must install Business Automation Workflow on each node machine, and
external Content Platform Engine and
external IBM Content
Navigator must use a
Websphere profile (non-bpm profile) template.

Figure 1. Topology before and after augmentation

<!-- image -->

<!-- image -->

1. Back up your source databases.
2. Update your IBM Content
Navigator and Content Platform Engine.
3. If you haven't already, install and configure Business Automation Workflow.
4. Configure Business Automation Workflow to use your
Content Platform Engine.
5. Configure Business Automation Workflow to use your
IBM Content
Navigator.
6. Run the case configuration tasks.
7. Update custom extension packages and custom case widgets if you are using them.
8. Restart the deployment environment.

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
3 Optional: If you have already installed Business Automation Workflow andcreated a deployment environment, skip this step. Otherwise, install Business Automation Workflow and configure the Business Automation Workflow deployment environment with no IBM ContentNavigator or Content Platform Engine feature enabled.
    1. Choose a sample properties file from the
Workflow\_install\_root\BPM\samples\config\externalicnexternalcpe
directory, based on your database and the type of deployment environment you want.
For a development environment, choose a properties file with
bpm.de.environment=Process Center. For a production environment, choose a file with
bpm.de.environment=Process Server. These files do not contain the IBM Content
Navigator or Content Platform Engine database configurations.
    2 Modify the properties file by using your real environment values. Pay special attention to the following properties and make sure that they are configured correctly:
        - Set the ECMTechnicalUserAlias as the user from the LDAP shared user repository that is used as
the administrator for the object store, for
example:###########################################
   # ECM technical user authentication alias #
   ###########################################
   bpm.de.authenticationAlias.2.name=ECMTechnicalUserAlias
   bpm.de.authenticationAlias.2.user=admin
   bpm.de.authenticationAlias.2.password=admin
        - Modify the network shared directory that is used by the external IBM Content
Navigator, for
example:# The network directory shared among multiple process servers in the deployment environment.
   bpm.de.caseManager.networkSharedDirectory=${WAS\_INSTALL\_ROOT}/CaseManagement/properties

For setting up a network shared directory, see step 4 in Configuring IBM Business Automation Workflow with an external IBM Content Navigator.
3 Create the Business Automation Workflow deployment environment byusing the BPMConfig command-line utility . Follow the instructions for your database type under the following link:
    - Configuring profiles and creating a network deployment environment on Linux
    - Configuring profiles and creating a network deployment environment on Windows
4. Start the environment and run a health check for the deployment environment.
Follow the instructions in Starting your environment and Verifying the status of your environment using the Health Center.
4. Configure Business Automation Workflow
to use your previous Content Platform Engine, namely the same
environment that IBM Case
Manager uses for the
design object store (DOS) and target object store (TOS). Follow the instructions in Configuring an existing external Content Platform Engine. 
For considerations on object store configuration, see Planning for an external Content Platform Engine.
5 Configure properties for Lightweight Directory Access Protocol (LDAP) sothat the same configuration is used by both Business Automation Workflow and FileNet® ContentManager . Forexample, the user and group name attributes: For more information, see Configuring the user registry and Directory service providers .

- Business Automation Workflow - user-full-name-prop and group-name-prop
- Content Platform Engine - userShortNameAttribute and
GroupNameAttribute
6 To continue using the same configurations and customizations in IBM ContentNavigator after theupgrade, configure Business Automation Workflow to use your IBM ContentNavigator .

1. Follow the instructions in Configuring IBM Business Automation Workflow with an external IBM Content Navigator.
2. Restart the Business Automation Workflow
deployment manager profile.
3. Synchronize the custom profiles with the deployment manager profile.
For each custom profile, run the following command on the custom
node:custom\_profile\_install\_root/bin/syncNode.bat dmgr\_hostname dmgr\_soap\_port -user de\_admin\_user -password de\_admin\_password
4. Start the custom profile.
5. Start the deployment manager environment.
6. Restart the IBM Content
Navigator
environment. 
Important: Make sure that the Business Automation Workflow server is available
before you restart the IBM Content
Navigator
environment.
7 Run the Case configuration tool to deploy the case plug-ins onto the IBM ContentNavigator server. For information about the Case configuration tool, which is located underWorkflow\_install\_root /CaseManagement/configure/ , see thetopic for your environment: Important:

- Workflow Center: Preparing to run the case configuration tasks
- Workflow Server: Preparing to run the configuration tasks

- For the Configure Business Rules task, specify the same path that you used in
IBM Case
Manager.
- Make sure that the Network Shared Directory property value in the Edit
Development Environment Profile Properties wizard is the same as the one that you set in
the Business Automation Workflow properties
file. If you want to change this network shared directory value, then after you change the value in
the wizard, you must also rerun the BPMConfig command, for example:
BPMConfig  -update -profile DmgrProfile -de De1 -networkDirectory new network directory -component CaseManager

1 If you are using custom extension packages, update them. Note: After deploying the package and by using the custom case extensions in Case Builder , it is suggested that youadd an exception to your browser to handle an invalid server certificate for the external IBM ContentNavigator server. Thiscan be accomplished by opening the IBM ContentNavigator URL in thesame browser session as Case Builder and then adding theexception for the invalid server certificate when prompted. The IBM ContentNavigator URL uses thefollowing format:https://ICN\_hostName:ICN\_portNumber/navigator
    1. Update the previous case resource path with the absolute path for the IBM Content
Navigator in the
Extension.json file. For example, use
https://ICN\_hostName:ICN\_portNumber/navigator/plugin
instead of /navigator/plugin.
    2 Enable cross-origin resource sharing (CORS) settings for this custom extension package, which isinstalled and deployed in IBM ContentNavigator . This isdone by enabling and configuring the CORS filter servlet in IBM ContentNavigator .
        1 Add the filter-mapping for custom extension plug-ins from IBM ContentNavigator
            1. Modify the <IBM Content Navigator installation
location>\configure\explodedformat\navigator\WEB-INF\web.xml to add
<filter-mapping>
        <filter-name>CORSFilter</filter-name>
        <url-pattern>/plugin/*</url-pattern>
    </filter-mapping>
            2. Run IBM Content
Navigator
configuration tool to rebuild and redeploy the application.
    2 Create a new CORS.properties .
        1. Add the following text for CORS cors.origin.hostname=[bawserver]
cors.origin.port=[bawserver port]
cors.allow.methods=GET, OPTIONS, HEAD, PUT, POST
cors.allow.credentials.boolean=true
cors.options.status=202[bawserver] - the URL that client users access Workflow Center, Case Builder.
[bawserver port] -
the PORT that client users access Workflow Center, Case Builder.
3. Add a com.ibm.ecm.icn.cors.file JVM parameter that points to the
CORS.properties file that you created in (b)For
example,
-Dcom.ibm.ecm.icn.cors.file=/tmp/CORS.properties
3 In the Case configuration tool, run the Deploy & Register ExtensionsPackage task to deploy the custom extension package plug-in to the IBM ContentNavigator .

1. Right-click the task and select Enable Task.
2. Enter and check the properties.
3. Run the task.

```
https://ICN\_hostName:ICN\_portNumber/navigator
```

2 If you are using case customwidgets that refer to IBM CaseManager resources, youmust update the implementation code because, after augmentation, the resources are on the remoteBusiness Automation Workflow computer insteadof the IBM CaseManager computer. For more information about how to specify the CORS filter, see CORSFilter .

1. Update the previous case resource path with the absolute path for the remote Case Client in the custom plug-in. JAR
file. For example, use
https://Workflow\_hostName:CaseClient\_portNumber/ICMClient/icm
instead of /ICMClient/icm. Make this replacement in each place that refers to
case resources.
2 Enable CORS settings for this custom widget, for example,
    1. Manually place the following CORS filter servlet in the web.xml file in the
custom widget EAR file:<filter>
	<description>Handling Cross Origin Resource Sharing</description>
	<display-name>CORSFilter</display-name>
	<filter-name>CORSFilter</filter-name>
	<filter-class>com.ibm.casemgmt.cors.filter.CaseCORSFilter</filter-class>
      </filter>
    <filter-mapping>
	<filter-name>CORSFilter</filter-name>
	<url-pattern>/*</url-pattern>
    </filter-mapping>
    2. Put the casecors.jar file in the custom widgets application EAR
lib  folder. You can get the casecors.jar file from the
following locations:On-premise
Workflow\_install\_root/BPM/Case/lib/
Container - In
the workflow pod (for example -
workflow-authoring-baw-server)/opt/ibm/wlp/usr/servers/defaultServer/case/lib/casecors.jar
3 In the Case configuration tool, run the Deploy & Register Custom WidgetsPackage task to deploy the Case custom widget plug-in to the IBM ContentNavigator .

1. Right-click the task and select Enable Task.
2. Enter and check the properties.
3. Run the task.
8. Restart the Business Automation Workflow deployment
environment.
9 To avoid accidentally editing solutions in the previous version of Case Builder after they are alreadyupgraded, remove the previous CaseBuilder app.

1. In the WebSphere administrative console for IBM Case
Manager
(https://case\_computer:9043/ibm/console) goes to Applications > All Applications, select CaseBuilder and click
Remove.
2. Save the changes to the WebSphere Application
Server configuration, and restart
the WebSphere Application
Server profile.
10. Upgrade and convert your existing case solutions, see Upgrading and converting case solutions.

## Results

All the desktops that you previously had are augmented to the Business Automation Workflow environment and you can continue to use them as
before. The default desktop is baw. You can change the desktop in the IBM Content
Navigator administration console.

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

Now that Business Automation Workflow is configured with an external IBM Content
Navigator, both Process Designer in Case Builder and case forms are disabled. See Enabling the case management features to enable them.

## What to do next

If you encounter case management problems after you install or upgrade to IBM Business Automation
Workflow, see Troubleshooting IBM Case Manager system upgrades.

After a successful upgrade, you can promote your case solutions to workflow projects, which you
can easily manage in Business Automation Workflow. See Promoting case solutions to the Workflow Center.