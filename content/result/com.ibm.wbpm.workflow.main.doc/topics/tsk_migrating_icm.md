# Moving from on-premises IBM Case
Manager to IBM Business Automation
Workflow on containers

## About this task

The Case Manager
system is composed of the IBM FileNet Content Platform Engine, IBM Content
Navigator, and
Case Manager. To
move Case Manager
from on-prem to cloud, you must also move the FileNet Content Platform Engine and IBM Content
Navigator to IBM Business Automation
Workflow on containers.

When you move to IBM Business Automation
Workflow on containers, the case production environment is moved to the Workflow Runtime environment.
There is no development environment in IBM Business Automation
Workflow on containers.

Before you move, it is important to understand what you need, what options you have, and your
license entitlements. Complete the following steps in the specified sequence.

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
IBM Business Automation
Workflow on
containers.

### About this task

Before you move IBM Case
Manager to Business Automation Workflow on containers, be
aware of the prerequisites.

- Production environment:
    - It is recommended that you install Case Manager 5.3.3 interim
fix *10* or later. For more information about creating a production deployment, see Configuring IBM Case Manager.
    - When you configure the Case Manager profile, select
the production environment and deploy Case Manager with the default
configuration tasks.
    - The Content Platform Engine and
IBM Content
Navigator
versions in the on-prem environment must be the same version or earlier than what is supported by
Business Automation Workflow on
containers. If the versions of Content Platform Engine and IBM Content
Navigator are later
than the one supported by Business Automation Workflow on containers,
database conflicts might occur.
- Databases and object store:

- The database that has the global configuration database (GCD), IBM Content
Navigator, design
object store (DOS), and target object store (TOS) is the same database that is used after the
migration. Ensure that the database is available after the migration. If you use file storage object
stores, take a backup.
- The same LDAP is used in the on-prem and container environments.
- The DOCS (Documents object store) must be created in the on-prem environment before the
migration. If data persistence is configured in Application Engine, you must create the AEOS
(Application Engine object store) as
well.

- Solutions that use forms do not work as expected in container environments because forms are not
supported.
- Migrated object stores from the on-prem environment are not used after migration. The IBM Content
Navigator URL of the
on-prem environment no longer works.
- The traditional Content Platform Engine cannot be used along with
the container Content Platform Engine
after migration.
- Case widget plug-ins must be refactored before deploying them in Business Automation Workflow on containers. The
Case Manager path
must be an absolute URL, and not a relative URL.

Back to top

## 2. Preparing to move

After you assess your readiness, prepare for the move from IBM Case
Manager to Business Automation Workflow on containers. Make
sure that the required databases are online.

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
any other capabilities of FileNet Content Manager, see  Moving
from on-premises FileNet Content Manager to Cloud Pak for Business Automation.

- 2a. Preparing the case solutions
- 2b. Preparing the cluster

Back to top

### 2a. Preparing the case solutions

Export the case solutions and prepare them for moving from IBM Case
Manager to Business Automation Workflow on
containers.

#### About this task

Use the migration planning sheet to gather the on-prem environment configuration data that is
required for migration. After you generate the custom resource, check that all the values listed in
the migration planning sheet are entered. See Migration planning sheet.

Back to top

#### Procedure

To prepare your case solutions:

1. On the Content Platform Engine server, create and initialiize the required object stores, with the default add-ons. One object
store is used for Documents (DOCS) and the other for Application Engine. If data persistence is
configured in Application Engine, create
the Application Engine object store
(AEOS). It must exist before you migrate because you cannot add new object stores until the whole
migration process is complete.
2. Export all the on-prem solutions of the production environment.
3. Export the security manifest and audit manifest, if any.
4. Take a backup of the custom widgets.
5. Take a backup of the Content Platform Engine and IBM Content
Navigator
databases.
6 Ensure that the following conditions are met for all the Case Manager on-premenvironment case solutions that you might want to work with: Back to top
    1. The solutions are imported to the design object store.
    2. The solutions are deployed to the required target area or areas.
    3. Security manifests are applied to all the target areas where the solutions are deployed.

Back to top

### 2b. Preparing the cluster

Use the migration planning sheet to gather information. Prepare the cluster for moving
from IBM Case
Manager to
Business Automation Workflow on
containers.

#### About this task

Use the migration planning sheet to gather the on-prem environment configuration data that is
required for migration. After you generate the custom resource, check that all the values listed in
the migration planning sheet are correctly filled in. See Migration planning sheet.

#### Procedure

1. To plan for installation, see Business Automation Workflow on containers,
follow the instructions in Containers: Installing, configuring, and upgrading IBM Business Automation Workflow on containers.
2. To prepare the cluster for installation, do all the steps until 4g in Installing a production deployment.

## 3. Generating the CR

After you prepare the cluster, you can generate and run a custom resource (CR) file. The
CR file acts as a template of what you will install, and can be customized according to the
components that the operator supports for installation.

### Procedure

1. In the cert-kubernetes/scripts folder, run the
./case-migrate-baw-prerequisites.sh script. Running the prerequisites script
gives you the instructions to follow. 
Usage: case-migrate-baw-prerequisites.sh -m [modetype]

Options:
  -h  Display help
  -m  The valid mode types are [property], [generate], [validate], or [generate-cr].
      STEP1: Run the script in [property] mode to create the user property files (DB/LDAP property files) with default values (database name/user)."
      STEP2: Modify the DB/LDAP/User property files with your values.
      STEP3: Run the script in [generate] mode to generate the DB SQL statement files and YAML template for the secrets, based on the values in the property files.
      STEP4: Create the databases and secrets manually based on the modified DB SQL statement file and YAML templates for the secret.
      STEP5: Run the script in [validate] mode to check that the databases and secrets are created before you deploy Business Automation Workflow.
      STEP6: Run the script in [generate-cr] mode to generate the Business Automation Workflow custom resource based on the property files.
2. Run the script in property mode to generate the properties files:  
./case-migrate-prerequisites.sh -m property
3. Enter the number for the cloud platform you want to deploy to.
4. For the production license, enter 1.
5. Enter 1 for production or 2 for non-production.
6. Select the correct number for your IBM FileNet Content Manager license.
7. Select the Lightweight Directory Access Protocol (LDAP) type that you use in the on-prem
environment. By default, LDAP SSL is enabled. You can change the
LDAP\_SSL\_ENABLED parameter in the
cert-kubernetes/scripts/baw-prerequisites/propertyfile/baw\_LDAP.property file
later.
8. Select the database type.  By default, database SSL is enabled. You can change
the DATABASE\_SSL\_ENABLED parameter in the
cert-kubernetes/scripts/baw-prerequisites/propertyfile/baw\_db\_server.property
file later.
9. Enter an alias name for the database servers or instances to be used by the Business Automation Workflow
deployment. This name cannot be the host name of the database server and cannot include a
dot (.) character. You can use a comma-separated list, for example, icm533ps1, icm533ps2,
icm533ps3.
10. Enter the storage class name or names you want to use.  For more information,
see Planning.
11. Select whether to enable the Case Event Emitter with this deployment.
12. Select whether to restrict network egress to unknown external destinations for this
deployment. By default, Business Automation Workflow on containers
prevents all network egress to unknown destinations. You can either enable all egress or accept the
new default and create network policies to allow your specific communication targets as documented
in Configuring cluster security.
13. View your results. The database and LDAP property files for Business Automation Workflow on containers are
created, followed by the property file for each database name and user, followed by the Business Automation Workflow property
files.In cert-kubernetes/scripts/baw-prerequisites/propertyfile,
the following files are created:
Table 1. Property files

Name
Description

baw\_case\_migration.property
Properties for target object stores.

baw\_db\_name\_user.property
Properties for the database name and user name required by each component of the Business Automation Workflow on containers
deployment, such as GCD\_DB\_NAME, GCD\_DB\_USER\_NAME, and
GCD\_DB\_USER\_PASSWORD.

baw\_db\_server.property
Properties for the database server used by Business Automation Workflow on containers, such
as DATABASE\_SERVERNAME, DATABASE\_PORT, and
DATABASE\_SSL\_ENABLE.

baw\_LDAP.property
Properties for the LDAP server that is used by Business Automation Workflow on containers,
such as LDAP\_SERVER, LDAP\_PORT, LDAP\_BASE\_DN,
LDAP\_BIND\_DN, and LDAP\_BIND\_DN\_PASSWORD.

baw\_user\_profile.property
Properties for the global values used by the Business Automation Workflow on containers
deployment, such as "sc\_deployment\_license".Properties for the values used by each component of
Business Automation Workflow on containers, such as <APPLOGIN\_USER> and
<APPLOGIN\_PASSWORD>
14. To configure multiple target object stores (TOS), enter a value greater than 1 for the
number of target object stores.
15 Update the property files. Notes:
    - The key names are created by the prerequisites script and you cannot edit them.
    - The values in the property files must be inside double quotation marks.
    1. Update the baw\_case\_migration.property file with the values from
the on-prem Case Manager server and the
multiple target object store information from the on-prem environment.
    2. Update the baw\_db\_name\_user.property file with the usernames and
passwords of the GCD database, DOCS database, DOS database, TOS database, IBM Content
Navigator (ICN)
database, and Business Automation Workflow (BAW) database. Change the <DB\_SERVER\_NAME> prefix to assign which
database is used by the component. The value of <DB\_SERVER\_NAME> must match the
value of <DB\_SERVER\_LIST>, which is defined in the
baw\_db\_server.property file.The username and password values must not include
special characters "=" "." "\" (equals, dot, or backslash).
    3. Update the baw\_db\_server.property file with the same database
details as in the on-prem Case Manager. The
value of <DB\_SERVER\_LIST> is an alias for the database servers. The key supports
comma-separated lists.
    4. Update the baw\_LDAP.property file with the same LDAP details as
in the on-prem Case Manager. The
values in this file must not include special character '"'' (double quotation
mark).
    5. Update the baw\_user\_profile.property file with the license, admin
user (as in the on-prem Case Manager), and keystore
passwords. The username and password values must not include special characters "=" "."
"\" (equals, dot, or backslash).
16. Run the ./case-migrate-baw-prerequisites.sh file in generate mode
using the following
command: ./case-migrate-baw-prerequisites.sh -m generateBased on
the property files, this command generates all the database SQL statements file required by the
deployment: GCD, IBM Business Automation
Navigator,
document object store (BAWDOCS), design object store (BAWDOS), target object store (BAWTOS),
Business Automation Workflow database
instance1, and User Management Services
(UMS).It also creates the required secrets for LDAP, FileNet Content Manager, IBM Business Automation
Navigator, Business Automation Workflow, and
UMS.
17. Run the scripts for the required databases only. (The FileNet and Navigator databases are
already available.) The scripts are under
cert-kubernetes/scripts/cp4ba-prerequisites/dbscript/baw
18. Apply the secrets by running the create\_secret.sh file in the
./baw-prerequisites folder. 
create\_secret.sh
19. To validate the configuration before you deploy, run the following command: 
./case-migrate-baw-prerequistes.sh -m  validate
This command checks that everything has been created: storage classes, required
Kubernetes secrets, LDAP connection, and database connections for all required
databases.
20. Generate the CR. Run the script in generate-cd mode, using the following
command.  ./case-migrate-baw-prerequisites.sh -m generate-crAnswer
the on-screen prompts and check the input as you go.The CR file
cert-kubernetes-master/scripts/baw-prerequisites/generated-cr/ibm\_cp4a\_cr\_production\_FC\_workflow-standalone\_final.yaml
is generated.Back to
top

## 4. Deploying the CR

After you successfully generate the custom resource (CR) file, you can deploy Business Automation Workflow on containers. The
CR acts as a template of what you will install.

### Procedure

1. Validate your CR file before you apply it or save it in the YAML view. It is likely that
you edited the file multiple times, and possibly introduced errors or missed values during your
customizations. For more information, see  Validating the YAML in your custom resource file.
2. To deploy the CR, apply the upgraded CR to the operator. For example, using the OpenShift
CLI:  
oc apply -f ibm\_cp4a\_cr\_production\_FC\_workflow-standalone.yaml
3. To verify that the installation was successful, follow the steps in Verifying the installation. 
Back to top

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

After migration, you can work with custom plug-ins and extensions, enable case analyzer
and case history, configure the case event emitter, and index case instances.

### Procedure

1. If you have custom plug-ins and custom extensions in the production environment, you must
copy the plug-ins to /<icn pv directory>/<icn-pluginstore>. Add
lines similar to the following example lines in the CR file under case configuration and deploy the
CR file: 
custom\_package\_names: "ICMCustomWidgets.zip" 
custom\_extension\_names: "CustomEditors.zip"
For more details about custom packages and custom extensions, see Configuring custom case widgets for a container environment.
2 Enable the case cnalyzer and case history stores in the Administrative Console forContent Platform Engine (ACCE).
    1. In the ACCE, go to FileNet P8 domain > Workflow
Subsystem.
    2. Select Case History enabled and Case Analyzer
enabled.
    3. Restart the Content Platform Engine
pod to reflect the changes.
3. Configure the case event emitter. For the case event emitter configuration parameters,
see Case event emitter configuration parameters.
4. Index case instances. The case management tools provide support for indexing case
instances in the Elasticsearch index. Full re-indexing and live index updates are supported. For
more information, see Indexing case instances. 
Back to top

### What to do next