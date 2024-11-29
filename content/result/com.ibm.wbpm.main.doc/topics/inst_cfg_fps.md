# Installing IBM Process Federation
Server on Business Automation Workflow

## About this task

- Verify that your migrated IBM BPM
environments are enabled for indexing. For information about enabling indexing, see Enabling indexing of BPD-related data in a federated environment, Enabling indexing of BPEL-related data in a federated environment, and Enabling indexing of Case-related data in a federated environment.
- Verify that the values in the Process Federation Server
server.xml file are still valid. For example, in the new migrated environment,
verify that the URLs for the federated Business Automation Workflow
and IBM BPM systems are correct and that the
security configuration, including SSO and SSL, is correct.

- Preparing to install and configure IBM Process Federation Server

Before you prepare to install and configure the software, create a plan for the federated environment that you want to create.
- Installing IBM Process Federation Server

You can install Process Federation Server interactively by using IBM Installation Manager, or silently by using the command line or a response file.
- Creating the Process Federation Server database

Process Federation Server requires a database to store federated saved searches that are created in Process Portal. After you install Process Federation Server, the database scripts for creating the database are available in the installation directory. Customize the scripts for your database environment, for example, the schema name and the table spaces.
- Creating a process federation server

A template is provided to help you create a server. The template includes all the runtime features that are needed for Process Federation Server, a jvm.options file containing JVM settings to tune performance, and a server.xml configuration file to get you started.