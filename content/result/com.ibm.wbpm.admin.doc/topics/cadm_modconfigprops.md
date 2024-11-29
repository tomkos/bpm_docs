# Modifying runtime server configuration properties

- Changing server settings in the Process Admin Console

You can edit the settings for process application snapshots.
- The 100Custom.xml file and configuration

Some workflow server configuration settings in are saved in a set of XML files. You can modify many of these settings for your server environment to, for example, modify the SMTP server address and tune the event manager. You update security configuration properties, database configuration properties, and URLs by using wsadmin commands.
- Using wsadmin commands to customize the Workflow Server settings used to connect to Workflow Center

 Traditional: 
 Using the WebSphere wsadmin command-line administration tool, you can run commands to update the server configuration that is used to connect a workflow server in your runtime environment to a different workflow center. You can also use wsadmin commands to connect an offline server or to modify other connection properties. Although a few settings are updated using authentication alias configuration, the rest of the properties can be updated using wsadmin commands.
- Using the administrative console to customize the Workflow Server used to connect to Workflow Center

 Traditional: 
 After you install and configure IBM® Business Automation Workflow, you can use the Workflow Server Settings page in the administrative console to change the Workflow Server settings that are used for connecting to Workflow Center.
- Modifying the IBM Workflow Server environment name

 Traditional: 
 If you want to modify the environment name that was specified during initial configuration, update the configuration using the updateBPMConfig administrative command.
- Modifying the IBM Workflow Server environment type

 Traditional: 
 If you want to modify the environment type that was specified during initial configuration, update the configuration using the updateBPMConfig administrative command. The environment type indicates how IBM Business Automation Workflow is used (for example, in a development, test, staging or production environment). Process authors can set environment-specific variables for each process application and then define values for each type of environment in which a process runs.
- Accessing an Enterprise Content Management server using the Secure Socket Layer (SSL)

 Traditional: 
 You can set up your ECM server connection to use SSL for security protection.
- Accessing an Enterprise Content Management server using single sign on (SSO)

If the same people use IBM Business Automation Workflow and Enterprise Content Management, you might be able to use single sign on to allow them to access both systems with a single log on ID.