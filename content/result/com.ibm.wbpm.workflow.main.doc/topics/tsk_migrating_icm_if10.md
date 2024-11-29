# Moving from on-premises IBM Case
Manager to Cloud Pak for Business Automation

## About this task

The Case Manager
system is composed of the IBM FileNet Content Platform Engine, IBM Content
Navigator, and
Case Manager. To
move Case Manager
from on-prem to cloud, you must also move the FileNet Content Platform Engine and IBM Content
Navigator to Cloud Pak for Business Automation.

When you move to Cloud Pak for Business Automation, the case development
environment is migrated to the Business Automation Workflow Authoring
environment and the case production environment is moved to the Business Automation Workflow Runtime environment.

Before you move to any Cloud Pak for Business Automation capability, it is
important to understand what you need, what options you have, and your license entitlements.
Complete the following steps in the specified sequence.

<!-- image -->

- 1. Assessing your readiness
- 2. Preparing to move
    - 2a. Preparing the case solutions
    - 2b. Preparing the cluster
- 3. Generating the CR
- 4. Deploying the CR
- 5. Performing required post-migration steps
- 6. Optional: Completing post-migration tasks

## 1. Assessing your readiness

At the start of your transformation journey, assess your current readiness to adopt
Cloud Pak for Business Automation.

### About this task

Before you move IBM Case
Manager to Business Automation Workflow in Cloud Pak for Business Automation, be aware of the
prerequisites.

- For Case Manager production or development environments:
    - It is recommended that you install Case Manager 5.3.3 interim
fix *10* or later. For more information about creating a development or production deployment, see
Configuring IBM Case Manager.
    - When you configure the Case Manager profile, select
the development environment or production environment and deploy Case Manager with the default
configuration tasks.
    - The Content Platform Engine and
IBM Content
Navigator
versions in the on-prem environment must be the same version or earlier than what is supported by
Cloud Pak for Business Automation. If the
versions of Content Platform Engine and
IBM Content
Navigator are
later than the one supported by Cloud Pak for Business Automation, database conflicts
might occur.
- For databases and object stores:

- The database that has the global configuration (GCD) database, IBM Content
Navigator, design
object store (DOS), and target object store (TOS) is the same database that is used after the
migration. Ensure that the database is available after the migration. If you use file storage object
stores, take a backup.
- The same LDAP is used in the on-prem and container environments.
- The DOCS (Documents Object Store) and AEOS (Application Engine object store) must be created
in the on-prem environment before the migration.

- Solutions that use forms do not work as expected in container environments because forms are not
supported.
- Migrated object stores from the on-prem environment are not used after migration. The IBM Content
Navigator URL of the
on-prem environment no longer works.
- The traditional Content Platform Engine cannot be used along with
the container Content Platform Engine
after migration.

Back to top

## 2. Preparing to move

After you assess your readiness, prepare for the move from IBM Case
Manager to Cloud Pak for Business Automation. Make sure that the
required databases are online.

### Before you begin

The databases of Content Platform Engine and IBM Content
Navigator are used
after the move, so make sure that the databases are online. The Lightweight Directory Access
Protocol (LDAP) server that is used in the on-prem environment is also used after the move, so make
sure that the LDAP server is running. When you are ready to start the move, stop the Content Platform Engine, IBM Content
Navigator, and
Case Manager
applications that are hosted on WebSphere Application
Server or Oracle WebLogic
Server.

### About this task

This document describes the Content Platform Engine and IBM Content
Navigator actions
required for moving Case Manager. If you require
any other capabilities of FileNet Content Manager, see Moving from on-premises FileNet Content Manager to Cloud Pak for Business
Automation.

- 2a. Preparing the case solutions
- 2b. Preparing the cluster

Back to top

### 2a. Preparing the case solutions

Export the case solutions and prepare them for moving from IBM Case
Manager to Cloud Pak for Business Automation.

#### About this task

Use the migration planning sheet to gather the on-prem environment configuration data that is
required for migration. After you generate the custom resource, check that all the values listed in
the migration planning sheet are entered. See Migration planning sheet.

Back to top

#### Procedure

To prepare your case solutions:

1. On the Content Platform Engine server, create and initialiize the required object stores, with the default add-ons. One object
store is used for Documents (DOCS) and the other for Application Engine. If data persistence is
configured in Cloud Pak for Business Automation,
create Application Engine object store
(AEOS). It must exist before you migrate because you cannot add new object stores until the whole
migration process is complete.
2. Export all the on-prem solutions of the development and production
environments.
3. Export the security manifest and audit manifest, if any.
4. Take a backup of the custom widgets.
5. Take a backup of the Content Platform Engine and IBM Content
Navigator
databases. 
Back to top

### 2b. Preparing the cluster

Use the migration planning sheet to gather information. Prepare the cluster for moving
from IBM Case
Manager to
Cloud Pak for Business Automation.

#### About this task

Use the migration planning sheet to gather the on-prem environment configuration data that is
required for migration. After you generate the custom resource, check that all the values listed in
the migration planning sheet are correctly filled in. See Migration planning sheet.

#### Procedure

1. To prepare to install Cloud Pak for Business Automation, follow the instructions
in Installing a CP4BA multi-pattern production
deployment.
2 Log in to the cluster with the cluster administrator that you used in Option 1: Preparing your cluster for an onlinedeployment or a non-administrator user who has access to the project. oc login https://<cluster-ip>:<port> -u <cluster-admin> -p <password> where

```
oc login https://<cluster-ip>:<port> -u <cluster-admin> -p <password>
```

    - <cluster-ip> is the IP address of the cluster
    - <port> is the port number of the cluster
    - <password> is the password for your <cluster-admin> user
3. View the list of projects in your cluster to see the target project before you run the
deployment script: 
oc get projects

Note: If you used the All Namespaces option to install the Cloud Pak operator, then
you must have another project in addition to openshift-operators in the cluster
before you create the deployment. Change the scope to the project that you created for your
deployment.oc project <project\_name>The specified
project is used in all later operations that affect project-scoped content.
4. Optional: If you need to, download the cert-kubernetes repository to an
amd64/x86, a Linux on Z, or a Linux on Power based VM/machine. For more information about
downloading cert-kubernetes, see Preparing a client to connect to the
cluster. 
Back to top

## 3. Generating the CR

After you prepare the cluster, you can generate and run a custom resource (CR) file. The
CR file acts as a template of what you will install, and can be customized according to the
components that the operator supports for installation.

### Procedure

1. In the cert-kubernetes/scripts folder, run the
./case-migrate-cp4a-prerequisites.sh script. Running the prerequisites script
gives you the instructions to follow. 
Usage: case-migrate-cp4a-prerequisites.sh -m [modetype]

Options:
  -h  Display help
  -m  The valid mode type: [property], [generate], or [validate]
      STEP1: Run the script in [property] mode to create the user property files (DB/LDAP property files) with default values (database name/user).
      STEP2: Modify the DB/LDAP/User property files with your values.
      STEP3: Run the script in [generate] mode to generate the DB SQL statement files and YAML template for the secrets, based on the values in the property files.    
      STEP4: Create the databases and secrets manually based on the modified DB SQL statement file and YAML templates for the secret.    
      STEP5: Run the script in [validate] mode to check that the databases and secrets are created before you deploy Business Automation Workflow.
2 Run the script in property mode to generate the properties files: ./case-migrate-cp4a-prerequisites.sh -m property This mode displays thedifferentcapabilities.Select the Cloud Pak for Business Automation capability to install:1) FileNet Content Manager2) Operational Decision Manager3) Automation Decision Services4) Business Automation Application5) Business Automation Workflow (Selected) (a) Workflow Authoring (b) Workflow Runtime (Selected)6) Automation Workstream Services7) IBM Automation Document Processing (a) Development Environment (b) Runtime Environment8) Workflow Process Service AuthoringInfo: Note that Business Automation Workflow Authoring (5a) cannot be installed together with Automation Workstream Services (6). However, Business Automation Workflow Runtime (5b) can be installed together with Automation Workstream Services (6).Info: Business Automation Navigator will be automatically installed in the environment as it is part of the Cloud Pak for Business Automation foundation platform. Tips: After you make your first selection you will be able to make additional selections since you can combine multiple selections.ATTENTION: IBM Automation Document Processing (7a/7b) does NOT support a cluster running a Linux on Z (s390x)/Power architecture.Tips: Press [ENTER] when you are doneEnter a valid option [1 to 4, 5a, 5b, 6, 7a, 7b, 8]:

```
./case-migrate-cp4a-prerequisites.sh -m property
```

```
Select the Cloud Pak for Business Automation capability to install:
1) FileNet Content Manager
2) Operational Decision Manager
3) Automation Decision Services
4) Business Automation Application
5) Business Automation Workflow (Selected)
   (a) Workflow Authoring
   (b) Workflow Runtime (Selected)
6) Automation Workstream Services
7) IBM Automation Document Processing
   (a) Development Environment
   (b) Runtime Environment
8) Workflow Process Service Authoring

Info: Note that Business Automation Workflow Authoring (5a) cannot be installed together with Automation Workstream Services (6). However, Business Automation Workflow Runtime (5b) can be installed together with Automation Workstream Services (6).

Info: Business Automation Navigator will be automatically installed in the environment as it is part of the Cloud Pak for Business Automation foundation platform. 

Tips:  After you make your first selection you will be able to make additional selections since you can combine multiple selections.

ATTENTION: IBM Automation Document Processing (7a/7b) does NOT support a cluster running a Linux on Z (s390x)/Power architecture.

Tips: Press [ENTER] when you are done
Enter a valid option [1 to 4, 5a, 5b, 6, 7a, 7b, 8]:
```

    - If you are moving from the Case Manager development
environment, enter 5a to move to the Business Automation Workflow Authoring
environment.
    - If you are moving from the Case Manager production
environment, enter 5b to move to the Business Automation Workflow Runtime
environment.
3. If you want to use Business Automation Insights, choose the optional components. 
Pattern "(b) Workflow Runtime": Select optional components:
1) Business Automation Insights
2) Exposed Kafka Services
3) Exposed Elasticsearch

Tips: Press [ENTER] if you do not want any optional components or when you are finished selecting your optional components
Enter a valid option [1 to 3 or ENTER]:
4. Select the Lightweight Directory Access Protocol (LDAP) that you use in the on-prem
environment.
5. Enter the storage class name or names you want to use.  For more information,
see Storage considerations.
6. Select the deployment profile: small, medium, or large. For more information,
see System requirements.
7. Select the database type.  
Note: PostgreSQL is not
supported for moving Case Manager.
8. Enter an alias name for the database server.
9. Enter the name of an existing project (namespace) where you want to deploy Cloud Pak for Business Automation.
10. Answer the question asking whether you want to restrict access to the Cloud Pak for Business Automation deployment.
11 View your results. The database and LDAP property files for Cloud Pak for Business Automation are created, followed bythe property file for each database name and user, followed by the Cloud Pak for Business Automation propertyfiles. In cert-kubernetes/scripts/cp4ba-prerequisites/propertyfile ,the following files are created:

- cp4ba\_case\_migration.property
- cp4ba\_db\_name\_user.property
- cp4ba\_db\_server.property
- cp4ba\_LDAP.property
- cp4ba\_user\_profile.property
12. To configure multiple target object stores (TOS), enter a value greater than 1 for the
number of target object stores.
13 Update the property files.

1. Update the cp4ba\_case\_migration.property file with the values
from the on-prem Case Manager server and the
multiple target object store information from the on-prem environment
2. Update the cp4ba\_db\_name\_user.property file with the usernames
and passwords of the GCD database, DOCS database, DOS database, TOS database, IBM Content
Navigator (ICN)
database, IBM Business Automation Studio (BAS)
database (for authoring) or Business Automation Workflow (BAW) database (for
runtime).
3. Update the cp4ba\_db\_server.property file with the same database
details as in the on-prem Case Manager.
4. Update the cp4ba\_LDAP.property file with the same LDAP details as
in the on-prem Case Manager.
5. Update the cp4ba\_user\_profile.property file with the license,
admin user (as in the on-prem Case Manager), and keystore
passwords.
14. Run the ./case-migrate-cp4a-prerequisites.sh file in generate mode
using the following
command: ./case-migrate-cp4a-prerequisites.sh -m generateThis
command generates all the database SQL statements file required by the Cloud Pak for Business Automation deployment based on the
property files.
15 Run the scripts for the required databases only. (The FileNet and Navigator databases arealready available.)

- For authoring: Run the scripts under
cert-kubernetes/scripts/cp4ba-prerequisites/dbscript/bas
- For runtime: Run the scripts under
cert-kubernetes/scripts/cp4ba-prerequisites/dbscript/baw
16. Apply the secrets by running the create\_secret.sh file in the
./cp4ba-prerequisites folder. 
create\_secret.sh
The required secrets for LDAP, FileNet, Navigator, and Workflow are
created.
17. To validate the configuration before you deploy, run the following command: 
./case-migrate-cp4a-prerequistes.sh -m  validate
This command checks that everything has been created: Slow/Medium/Fast/Block
storage classes, required Kubernetes secrets, LDAP connection, and database connections for all
required databases.
18. Generate the CR. From the /scripts folder, run the
./case-migrate-cp4a-deployment.sh command. Answer the on-screen
prompts and check the input as you go.The CR file
cert-kubernetes-master/scripts/generated-cr/ibm\_cp4a\_cr\_final.yaml is
generated.Back to
top

## 4. Deploying the CR

After you successfully generate the custom resource (CR) file, you can deploy Cloud Pak for Business Automation. The CR acts as a
template of what you will install.

### Procedure

1. Validate your CR file before you apply it or save it in the YAML view. It is likely that
you edited the file multiple times, and possibly introduced errors or missed values during your
customizations. For more information, see Validating the YAML in your custom resource file.
2. Apply the upgraded CR to the operator. For more information, see Applying the updated custom resource.

### What to do next

Back
to top

## 5. Performing required post-migration steps

You must perform post-migration steps if you work with file storage target object
stores.

### Procedure

If you use file storage target object stores:

1. Log in to ACCE.
2. For each file storage target object store, update the path in the TOSStorage,
Properties tab of the file storage device to point to the location in the Content Platform Engine physical volume.
 The file storage backup is now copied to the Content Platform Engine physical volume.Back to top

## 6. Optional: Completing post-migration tasks

After migration, you can update the Daeja Viewer log file path, work with custom plug-ins
and extensions, enable case analyzer and case history, configure the case event emitter, and index
case instances.

### Procedure

1. If you use Daeja Viewer, update the log file path and cache directory to the Cloud Pak for Business Automation container path.
 The default log file in the on-premises system before upgrade is
install\_dir/ibm/viewerconfig/logs/daeja.log, where
install\_dir is the directory where Navigator is installed. Update the path to
reflect your container deployment location, for example,
/opt/ibm/viewerconfig/logs/daeja.log.
2. If you have custom plug-ins and custom extensions in the production environment, you must
copy the plug-ins to /<icn pv directory>/<icn-pluginstore>. Add
lines similar to the following example lines in the CR file under case configuration and deploy the
CR file: 
custom\_package\_names: "ICMCustomWidgets.zip" 
custom\_extension\_names: "CustomEditors.zip"
For more details about custom packages and custom extensions, see Configuring custom case widgets for a container environment.
3 Enable the case analyzer and case history stores in the Administrative Console forContent Platform Engine (ACCE).
    1. In the ACCE, go to FileNet P8 domain > Workflow
Subsystem.
    2. Select Case History enabled and Case Analyzer
enabled.
    3. Restart the Content Platform Engine
pod to reflect the changes.
4. Configure the case event emitter. For the case event emitter configuration parameters,
see Case event emitter configuration
parameters.
5. Index case instances. The case management tools provide support for indexing case
instances in the Elasticsearch index. Full re-indexing and live index updates are supported. For
more information, see Indexing case instances. 
Note:  The FileNet® P8
Process Engine
REST APIs that are packaged with Business Automation Workflow
Case Manager
application are not available in Cloud Pak for Business Automation.

Back to top

### What to do next