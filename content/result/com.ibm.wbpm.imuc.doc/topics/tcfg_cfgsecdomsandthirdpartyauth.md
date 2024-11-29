# Configuring security domains and third-party authentication

## About this task

## Procedure

1. Create the deployment environments.
2 Select one of the following methods to create unique HTTPendpoints:
    - Use a dedicated virtual host for each deployment environment.
See Step
3.
    - Use dedicated context root prefixes for each deployment environment.
See Step
4.
    - Use dedicated Web servers for each deployment environment.
See Customizing Business Automation Workflow to work with a web server.
3 If you have multiple deployment environments in a single cell, and ifyou want to use the same web server, create a dedicated virtual host for each deploymentenvironment. For each deployment environment (dep\_env\_name ) in the cell, completethe following actions. For more information, see Virtual hosts in the WebSphere® ApplicationServer information center.

1. Decide on the virtual host name, virtual\_host\_name.
2. Create a dedicated virtual host. Using the administrative console, navigate to
Environment > Virtual hosts and click New.
3. Specify a name for the new virtual host. For example,
vh\_de1.
4. If you are using an external HTTP server, you must add the HTTP server's virtual host
alias. Navigate to Environment > Virtual hosts > Name of the virtual host created in previous step > Host Aliases and click New. For example,
navigate to vh\_de1 and click New. Then enter the host name
of your HTTP server and associate it with the HTTP or HTTPS port.
5 If you want to access the web container of the cluster members, add the host name ofthe cluster member as a host alias. Navigate toEnvironment > Virtualhosts > Name of the virtual host created in previousstep > Host Aliases and click New . Enter the host name of the cluster member andassociate it with the WC\_defaulthost\_secure port. Here is an example of the host aliases that must be added for a single cluster deploymentenvironment that contains two members: Deployment environment name: de1 Cluster name: de1.AppTarget Cluster member 1: de1.AppTarget.Member1 Cluster member 2: de1.AppTarget.Member2 Virtual host name: vh\_de1 Virtual host aliases in vh\_de1 :

Here is an example of the host aliases that must be added for a single cluster deployment
environment that contains two members:

Deployment environment name: de1

Cluster name: de1.AppTarget

Cluster member 1: de1.AppTarget.Member1

Cluster member 2: de1.AppTarget.Member2

Virtual host name: vh\_de1

    - To access IBM® Business AutomationWorkflow overHTTPS, add the cluster member host names and WC\_defaulthost\_secure ports tothe host alias:
        - Cluster member host name for de1.AppTarget.Member1 on
the WC\_defaulthost\_secure port . For example
9443.
        - Cluster member host name for de1.AppTarget.Member2 on
the WC\_defaulthost\_secure port. For example
9443.
- To access IBM Business AutomationWorkflow overHTTP, add the WC\_defaulthost ports.
    - Cluster member host name for de1.AppTarget.Member1 on the
WC\_defaulthost port. For example
9080.
    - Cluster member host name for de1.AppTarget.Member2 on the
WC\_defaulthost port. For example
9080.
- If you use an external HTTP server, add the HTTP server's virtual host alias. This is mandatoryif you are using an external HTTP server.

- Virtual host that corresponds to your HTTP server. For example
ihs.virtual.host.for.de1.ibm.com on port
80
- Virtual host that corresponds to your HTTP server. For example
ihs.virtual.host.for.de1.ibm.com on port
443.
6. Map the virtual host name, virtual\_host\_name, to the deployment
environment, dep\_env\_name, by running the BPMConfig
command: 
install\_root/bin/BPMConfig.sh -update -profile profile\_name -de dep\_env\_name -virtualHost virtual\_host\_name
install\_root\bin\BPMConfig.bat -update -profile profile\_name -de dep\_env\_name -virtualHost virtual\_host\_name
Tip: If there is only one deployment environment in the WebSphere cell, you can omit the
-de option. For more information about the BPMConfig command,
see  BPMConfig command-line utility. For information on the Business Automation Workflow virtual host, see Configuring endpoints to match your topology.
7 If you are using an external HTTP server, regenerate and propagate the HTTP serverplug-in.

1. In the administrative console, navigate to Servers > Server Types > Web Servers.
2. Select the name of your HTTP server, then click Generate Plug-in.
3. Select the name of your HTTP server, then click Propagate Plug-in. Tip: The administration service must be running on your HTTP server.
4. Configure dedicated context root prefixes
for each deployment environment by running the BPMConfig command.
For more information about the BPMConfig command,
see BPMConfig command-line utility.
5 Create and configure a dedicated security domain for each deployment environment and mapeach cluster and service integration bus to the dedicated security domain. See Configuring multiple security domains .

- Every cluster and service integration bus in the deployment environment must be mapped to
the same security domain.
- If you use a dedicated user registry for each security domain, the user realm name for the
security domain must be unique.
- Users that are configured for the deployment environment must exist in the user
registry.
6 To have a user from the security domain of the deploymentenvironment in the bus connector role, you must replace the user inthe bus connector role with the users from the realm of the securitydomain. For each user:

1. Click Service integration > Buses > BPM.yourDE.Bus > Security > Users and groups in the
bus connector role.
2. Select the user from the global realm. For example, de1Admin and
click Delete.
3. Click New.
4. Select Users and click Next.
5. Select the user from the security domain realm.
7. Click Security > Global
security > Custom Properties and set the com.ibm.websphere.security.useAppContextForServletInit 
custom property to true.  com.ibm.websphere.security.useAppContextForServletInit  = true
8 Configure trusted authentication realms:

1. Click Security > Global security > Configure > Trusted authentication realms - inbound.
2. Select the realm name that is associated with the security
domain and click Trusted.
9 Configure Virtual Member Manager (VMM) access for the securitydomain: Note: The next steps are required only if you want to havededicated administrators for each deployment environment.

1. From the Deployment Manager, launch wsadmin with
the following command:   wsadmin -lang jython -user AdminUserID - password AdminUserIDPassword
2. At the wsadmin prompt, run following
command:  AdminTask.mapIdMgrGroupToRole('[-roleName IdMgrReader -groupId ALLAUTHENTICATED
      -securityDomainName your\_security\_domain\_name]')
3. Save the configuration changes by running the following
command:  AdminConfig.save()
10 For each deployment environment, create a dedicated WebSphere ApplicationServer usersthat are used to perform WebSphere ApplicationServer administrativefunctions from either the administrative console or the wsadmin systemmanagement scripting interface. These users must be created in theglobal user registry as only cell scope user are allowed to run wsadmin.If you are using the file registry:

1. Click Users and Groups > Manage Users > Create.
2 Create four additional users for each deployment environment. For example: For more information, see Role-based authorization .
    - de1WASAdministrator
    - de1WASDeployer
    - de1WASMonitor
    - de1WASOperator
11 Create a dedicated Administrative Authorization Group (AAG)for each deployment environment:

1. Click Security > Administrative Authorization Groups > New and input a name for the AAG.
2. Click the new AAG.
3. Expand Clusters and select all
clusters that belong to the deployment environment.
4. Expand Business-level applications and
select all business level applications that belong to the deployment
environment.
5. Expand Applications and select
all applications that belong to the deployment environment. Note:  Do
not map any nodes or node groups.
6. Save and synchronize your changes.
7. Click Administrative user roles and
press Add.
8 Assign administrative roles to users:
    - de1WASAdministrator -
Administrator
    - de1WASDeployer - Deployer
    - de1WASMonitor - Monitor
    - de1WASOperator - Operator
9 Add the de1Admin@depenv1\_realm deploymentenvironment administrator with the following privileges: Note: The security domain realm must be selected when addingthe de1Admin@depenv1\_realm user.

- Operator
- Deployer
- Configurator
- Monitor
- Administrator
- Admin Security Manager
10 You can have different user registries in an environmentwith multiple security domains. To perform certain Process Admin LifeCycle(PAL) administrative functions you must have a user in the securitydomain of the deployment environment. However, to connect to the wsadminscripting interface or to call MBeans, the user must be in the userregistry of the global security domain. The BPMADminJobUser role mapsto an authentication alias for a user that requires the authorityto perform actions on the Process Admin LifeCycle (PAL) Admin task.If specified, the system will execute PAL actions from the MBean oftype PALService as this user. Create a J2C authentication alias forthe BPMAdminJobUser role:

1. Click Security > Global
security > Java Authentication and Authorization
Service > J2C authentication data.
2. - Click New and specify an arbitrary alias
name, and the deployment environment administrator user ID and password. Note: You
must use the password that was specified for the deployment environment
administrator during the deployment environment creation.
11 Map the J2C authentication alias to the BPMAdminJobUser role:

1. Click Servers > Deployment
Environment > yourDE > Authenticatin Aliases.
2. Select the new J2C authentication alias and map it to the BPMAdminJobUser role.
12. Configure an endpoint for the remote
artifact loader (REMOTE\_AL scenario) in each deployment
environment. See Configuring endpoints to match your topology.
13. Configure the third-party trust association interceptors
(TAI) for each dedicated security domain. See Configuring third-party authentication products.
14. Optional: Configure InvokeTAIbeforeSSO for each dedicated security domain.
See Security custom properties in the WebSphere
Application Server Version 8.5 documentation.