# Configuring Content Platform Engine for the Business Automation Workflow content store

## About this task

The Content Platform Engine
configuration consists of creating data sources to connect the Enterprise Content Manager (ECM)
domain and object store to the IBM® Business Automation
Workflow database. Then,
using the graphical user interface, you complete the configuration. The configuration includes
creating an identical authentication alias for the Content Platform Engine administrator as you did
for the Business Automation Workflow server.
Then, you must configure the log-in modules. Finally, you must deploy the Content Platform Engine, and start and test your
configuration.

The steps that you must do to configure Content Platform Engine with the Business Automation Workflow server are listed. See Configuring Content Platform Engine
instances by using the graphical user interface for the complete use of the graphical user
interface to configure Content Platform Engine instances.

## Procedure

1. Start the Configuration Manager graphical user interface. See Starting the Configuration
Manager graphical user interface.
2. Create six data sources, as described in Configuring the global
configuration database JDBC data source settings, two for DOCS, two for DOS (design
object store), and two for TOS (target object store). Ensure that you use the same JNDI names (for
example, jdbc/ECMDB, jdbc/ECMDBXA,
jdbc/FNDOSDS, jdbc/FNDOSXA,
jdbc/FNTOSDS, jdbc/FNTOSDSXA) and database connection
information as in the Business Automation Workflow server.
3. Create a configuration profile. See Creating a new configuration
profile.
4. Configure your licenses. See Choosing licenses.
5. Add an identical Authentication Alias as created on the Business Automation Workflow server for the Content Platform Engine administrator with LDAP credentials. In the
WebSphere administrative console, select Security > Global Security. Expand Java Authentication and Authorization Service, and
select J2C authentication data to create the alias.
6. Grant the user, who is defined by the alias you created in the previous step, the
WebSphere Application Server administrator role.
7. Configure the log-in modules, as described in the topic Configuring the login modules
(WebSphere only).
8. Configure Lightweight Directory Access Protocol (LDAP). Right-click
AppSrv01, and then click Add New
Task > Configure LDAP.
9. Deploy Content Platform Engine, as described in the
topic Deploying Content Platform
Engine instances.
10 Start Content Platform Engine and verify that it isworking with the existing Business Automation Workflow contentstore.
    1. Start Content Platform Engine.
    2. Open the IBM Administration Console for Content Platform Engine. For a configuration that uses a direct
connection to IBM Security Directory
Suite, log in by using
the credentials of the LDAP user who is configured for the Directory service bind username in the
Configure LDAP step.
    3. Verify that you do not see the wizard that prompts you to create a new domain. You can
see the BPM domain and three object stores: DOS, TOS, and DOCS.
    4. Verify that you can browse the documents object store. This verification is an
important checkpoint to make certain that the external Content Platform Engine is configured properly and can access the
existing documents object store.
    5. Check for errors in the Content Platform Engine
logs. Resolve any issues that you discover before you proceed.