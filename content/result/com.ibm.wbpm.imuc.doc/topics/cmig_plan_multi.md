<!-- image -->

<!-- image -->

# Planning to migrate multiple deployment environments or extra
clusters

## Two deployment environments in one cell

You
have two full deployment environments that share common database tables.
Your applications might include business process definitions (BPDs),
Business Process Execution Language (BPEL) processes (both long-running
processes and microflows), and Service Component Architecture (SCA)
applications.

- For each deployment environment in your source,make a copy of the migration properties file that is used as inputfor most of the migration commands. If you are migrating multiple deployment environments,you must use a different source migration properties file for eachone where you assign values to the following parameters: These cluster name parameters must have different values betweendeployment environments. However, within the same migration propertiesfile, the values can be the same. If you are migrating from a single cluster environment,enter a value for the application cluster name, for example: If you are migrating from a network deploymentenvironment, input the names of the clusters that exist in your sourceenvironment, for example: In addition, you must specify values for thefollowing parameters in each file:
    - source.application.cluster.name
    - source.messaging.cluster.name
    - source.support.cluster.name
    - source.web.cluster.name
    - source.application.cluster.name=SingleCluster
    - source.messaging.cluster.name=
    - source.support.cluster.name=
    - source.web.cluster.name=
    - source.application.cluster.name=ApplicationCluster
    - source.messaging.cluster.name=MessagingCluster
    - source.support.cluster.name=SupportCluster
    - source.web.cluster.name=
    - admin.username
    - admin.password
    - bpm.home
    - profile.name
- For configuring multiple deployment environments:

- Run the BPMConfig -migrate command in each of your deployment
environments to generate separate properties files. Modify your version of each properties file in
the IBM® Business Automation
Workflow Configuration editor, editing
the properties for user credentials, database information, hostname, and installation path.
- One of the new deployment environments can reuse the common database
for both the cell-scoped and deployment-environment-scoped data, but
you must create a new deployment-environment-scoped database for the
extra deployment environment.
- Create two three-cluster deployment environments by running the BPMConfig
-create command with each of the configuration files that
you created.
- Make sure that the name of the authentication alias
for each database is different if there is a different user name in
each deployment environment. Otherwise, the creation of the second
deployment environment will fail because the authentication alias
uses a different user name. For example, your first deployment
environment has the authentication alias BPM\_DB\_ALIAS with user1 as
the user name.bpm.de.authenticationAlias.3.name=BPM\_DB\_ALIAS
bpm.de.authenticationAlias.3.user=user1
bpm.de.authenticationAlias.3.password=
Before you
create the second deployment environment, check the BPMConfig properties
file to make sure that the same authentication alias does not exist
with a different user name. If so, change the name of the authentication
alias. For example:bpm.de.authenticationAlias.3.name=BPM\_DB\_ALIAS\_2
bpm.de.authenticationAlias.3.user=user2
bpm.de.authenticationAlias.3.password=
- Each time that the migration steps are for one
deployment environment, you must repeat the steps for each deployment
environment that you want to migrate.
- You must empty the failed event tables before migrating. Resubmit or delete the failed events
before migration.
- For the new deployment-environment-scoped database that you created
for one of your deployment environments, you must export the data
from the jdbc/WPSDB data source (JNDI) name in the
source and import it into the event sequencing table (PERSISTENTLOCK)
in the new database.

## Deployment environment and WebSphere Application
Server cluster

You
have a deployment environment and an extra WebSphere® Application
Server cluster
that is used to run WebSphere Application
Server applications.

- Complete the migration to Business Automation Workflow following the
normal steps to migrate your deployment environment.
- Create a WebSphere Application
Server cluster
in the target environment and redeploy your WebSphere Application
Server applications.
- Make sure that the name of the authentication alias
for each database is different if there is a different user name in
each deployment environment. Otherwise, the creation of the second
deployment environment will fail because the authentication alias
uses a different user name. For example, your first deployment
environment has the authentication alias BPM\_DB\_ALIAS with user1 as
the user name.bpm.de.authenticationAlias.3.name=BPM\_DB\_ALIAS
bpm.de.authenticationAlias.3.user=user1
bpm.de.authenticationAlias.3.password=
Before you
create the second deployment environment, check the BPMConfig properties
file to make sure that the same authentication alias does not exist
with a different user name. If so, change the name of the authentication
alias. For example:bpm.de.authenticationAlias.3.name=BPM\_DB\_ALIAS\_2
bpm.de.authenticationAlias.3.user=user2
bpm.de.authenticationAlias.3.password=