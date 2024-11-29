# Reassigning the BPM document store

## Before you begin

- You can configure your Business Automation Workflow deployment
environment to use an empty object store in an external Content Platform Engine. This configuration is useful if you set up a
new Business Automation Workflow deployment environment. For
instructions, see Configuring an existing external Content Platform Engine.
- You can configure your Business Automation Workflow deployment environment to
reassign the BPM document store to
the domain of an existing Content Platform Engine installation. This
configuration is useful if you already have an Business Automation Workflow deployment environment
setup. The instructions are in this set of steps.

- On IBM
FileNet® Content Manager,
a domain must be already set up. There might be multiple object stores already set up. When you
configure Business Automation Workflow with
FileNet Content
Manager, there
is a one-to-one correlation between the Business Automation Workflow server and the FileNet Content
Manager object
store.
- As an application server, only WebSphere® Application
Server is supported. In addition,
the WebSphere Application
Server used by
IBM Business Automation
Workflow and the WebSphere Application
Server used by FileNet Content
Manager must be using
the same JVM version.
- The same Lightweight Directory Access Protocol (LDAP) user repository must be used by both
IBM Business Automation Workflow and FileNet Content
Manager. It must be
connected by using Federated Repositories (also referred to as Virtual Member Manager (VMM)) in the
WebSphere Application Server security configuration for both Business Automation Workflow and FileNet Content
Manager. The FileNet Content
Manager domain must use
Federated Repositories (VMM) as the directory configuration.

## About this task

Back up your system configuration and databases before you begin this configuration. This backup
means you can roll back your configuration if needed. See Backing up and restoring administrative configuration files.

The steps that you must do to configure an existing FileNet Content
Manager with the IBM Business Automation Workflow server are listed. For a complete description
of reassigning an object store on FileNet Content Platform Engine, see Reassigning an object
store.

## Procedure

1. Check the version level of the FileNet Content
Manager. It must be a
supported version to work with Business Automation Workflow.  The external Content Platform Engine version must be the same or later than the Content Platform Engine version embedded in
IBM Business Automation Workflow. For example
in V19.0.0.2, the version of embedded Content Platform Engine is 5.5.2, therefore, the
external Content Platform Engine must be
5.5.2 or later.
2. Configure single sign-on (SSO) security for the external FileNet Content Manager,
including the configuration of the user registry and trusted realm. To configure single sign-on
security with a common user repository, see Configuring single sign-on with LTPA for an external Content Platform Engine. 
Check that the shared stand-alone Lightweight Directory Access Protocol (LDAP) server is
connected by using Federated Repositories (VMM).
3. Make the necessary updates to the Business Automation Workflow authentication and authorization settings. See
Preparing Business Automation Workflow for an external Content Platform Engine.
4 Reassign the BPM document store to the external ECM system.
    1 On the FileNet ContentManager server, create three newConfigure Object Store JDBC Data Sources tasks, one for DOS, one for TOS, and onefor DOCS. Use the Business Automation Workflow database informationin these tasks. See Configuring the initialobject store data sources by using the graphical user interface .
        - For DOS, use jdbc/FNDOSDS for the JCBC data source name and
jdbc/FNDOSDSXA for the JDBC XA data source name.
        - For TOS, use jdbc/FNTOSDS for the JCBC data source name and
jdbc/FNTOSDSXA for the JDBC XA data source name.
        - For DOCS, use jdbc/ECMDB for the JDBC data source name and
jdbc/ECMDBXA for the JDBC XA data source name.
2. Pause the Event Manager in each application cluster member. Pausing the Event Manager
temporarily stops the navigation of running instances. See Monitoring the Event Manager.
3 Reassign the Business Automation Workflow object store by usingeither the FileNet Deployment Manager graphical user interface or the command-line interface. SeeReassigning an objectstore . The source domain in the reassign operation is the BPM document store . The target domainexists in the external ECM server that hosts the BPM document store . When you specify theconnection information for the source, note these values:
    - Port: use the WC\_defaulthost port that is defined in
your Business Automation Workflow cluster
member.
    - Account: use the technical user credentials as defined in step 3.
5 Rename the reassigned object store and update the data sources.

1. Log in to the WebSphere administrative console on the FileNet
Content Platform Engine server and update the data sources that
were created in substep 4.a.
2. Change the JNDI Name attributes. Default Business Automation Workflow values for these attributes were used for the
reassign operation to complete. These default values must be changed to allow another Business Automation Workflow object store to be assigned to the same ECM
domain in the future. For example, another Business Automation Workflow deployment environment in the future might also
be reassigned to the external ECM domain.
3. Log on to the IBM Administration Console for Content Platform Engine (ACCE) on FileNet Content
Manager.
4 Update the connection information that references the data sources to match theupdates in substep 5.a .
    1. Find the database configuration. Global
Configuration > Administration > Database Connections > Database configuration for BPM document store.
    2. Update the values for the JNDI data source and the JNDI XA
data source. Update the Display Name value, as the FileNet Content
Manager administrator must understand that it
is the reassigned Business Automation Workflow object store.
    3. Save your updates. Click Save.
5 Rename the object store that was reassigned in step 4 . Like the data sources, the object store name ischanged so that other Business Automation Workflow object stores canbe assigned to the same external ECM system in the future.

1. Open the docs object store.
2. In the Properties tab of that object store, update the
Symbolic Name and Display Name properties.
3. Save your updates. Click Save.
6 Running a command and then starting IBM Business Automation Workflow finishes the configuration. However, you mustalso verify that the configuration is working.

1. Open the ACCE for the external  Content Platform Engine. Rename docs to another
name; for example, newdocs. The setBPMExternalECM  command
doesn't allow the object store name for DOCS to be the same as the internal default DOCS name in
IBM Business Automation Workflow.
2 Run the setBPMExternalECM admin command to configure Business Automation Workflow to use an external ECM server.
    1. Shut down the Business Automation Workflow deployment
environment; for example, by using the BPMConfig command. BPMConfig
-stop. See BPMConfig command-line utility. In the case of a Network Deployment (ND)
environment, the deployment manager, and node agents can be left running. The FileNet Content
Platform Engine must be running.
    2. Run wsadmin. In the case of an Business Automation Workflow
Express server or if you stopped the deployment manager of your Network Deployment (ND) environment,
run wsadmin in local mode; that is, by using the parameter -conntype
none.
    3. Run the setBPMExternalECM admin command. See setBPMExternalECM command. Use REASSIGN\_OBJECT\_STORE as the value for the
-ecmEnvironment parameter.
    4. Save the configuration by starting AdminConfig.save().
    5. If you stopped the deployment manager and node agents, you need to manually restart them.
    6. In the case of a Network Deployment (ND) environment, synchronize the configuration of the
nodes.
    7. Restart the Business Automation Workflow deployment environment
by using the BPMConfig command. BPMConfig
-start. See BPMConfig command-line utility.
3 Start the IBM Business AutomationWorkflow Case configuration tool and reconfigure case.

- Update the Content Platform Engine properties in the
profile to the external Content Platform Engine hostname and
connection information. Test the connection.
- Rerun all enabled tasks. The Configure Case Integration with IBM Business Automation
Workflow and
Configure the Case Management Object Stores tasks install IBM Business Automation
Workflow add-ons on the external
Content Platform Engine domain and
object stores.Note: If you are using Content Platform Engine 5.5.2, the workflow
system credentials are encrypted using the domain password. When the object store is reassigned, the
credentials on the workflow system region are encrypted with the encryption key of the source domain
(the embedded Content Platform Engine).
The destination domain (the external Content Platform Engine) has a different
encryption key, which can't decrypt the credentials. In 5.5.3, the problem is fixed by enhancing
ACCE to update the encrypted credentials even though the original credentials can't be decrypted. If
you are using 5.5.2 then before you run the Register Project Area and
Configure Business Rules tasks, log on to the external ACCE, open the workflow
system in TOS, and update the administrator group to the real LDAP group.
In the
Configure Business Rules task, make sure that you create the rules repository
directory on the Content Platform Engine
server before you run the task.
- After all the tasks are finished, sync the nodes and restart the whole environment.
4. Check for errors in the Business Automation Workflow
logs. If you discover errors, resolve them and restart the Business Automation Workflow server.
5. Check the CMIS component in the Component Health Center to verify that your external
ECM server is up and running. The switch to the external ECM server removes the BPM document store configuration that was
available as part of EmbeddedECM. Therefore, you cannot check the EmbeddedECM component anymore.
Instead, check the CMIS component. The CMIS component also reports errors for the connection to the
external ECM.
7 To validate that the reassignment was successful, make sure that the LDAP user (forexample, P8Admin) can do the following tasks:

1. Log in to the IBM Business Automation
Workflow
administration client for case management:  
http://virtual\_server\_name:port/navigator?desktop=bawadmin
2. Import a solution.
3. Delete a solution.
4. Log in to Case Builder and create a
solution.
5. Go to the IBM Business Automation
Workflow
desktop: http://virtual\_server\_name:port/navigator?desktop=baw
and run the solution.
8 Log in to the IBM Business AutomationWorkflow administrationclient for case management.

1. Make sure that the LDAP user (for example, P8Admin) has read and write permissions on
the DOS and TOS object stores in ACCE.
2. Make sure that the LDAP user has read and write permissions in the "workflow system"
of TOS in ACCE.

## Results