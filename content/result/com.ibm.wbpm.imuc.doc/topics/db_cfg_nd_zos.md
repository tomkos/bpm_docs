# Creating and configuring DB2 for z/OS databases after network deployment
profile creation

After creating or augmenting profiles, you or your database
administrator must create the databases and their tables manually, and you must also run the
bootstrapProcessServerData command before you try to start or use the IBM® Business Automation
Workflow server.

If you want to use case management for V19.0.0.1 or later, see Configuring case management for Db2 on z/OS for instructions for configuring the databases.

- DB2 for z/OS authorization prerequisites

A set of user authorizations are required for your IBM Business Automation Workflow databases. Depending on your DB2® for z/OS® version, view authorizations might also be required.
- Creating databases in the DB2 for z/OS subsystem

You can use the BPMConfig script to generate the database scripts that are required to create the databases for the IBM Business Automation Workflow components.
- Granting table privileges to the JCA authentication alias user ID

If the schema name you are using is not the same as the JCA authentication alias user ID, you must grant a subset of DB2 for z/OS privileges to the JCA authentication alias user ID.