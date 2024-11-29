# Recommended: Preparing databases and LDAP by running a script

## About this task

You can use the script to generate the database SQL statement files (scripts) and YAML template
files for the secrets. This process is easier than going through many steps to create the necessary
databases and Kubernetes secrets for the capabilities in your Business Automation Workflow deployment.

The baw-prerequisites.sh script has four modes.

- The first mode is "property", which creates the user property files
(baw\_user\_profile.property, baw\_db\_name\_user.property,
baw\_db\_server.property, and baw\_LDAP.property). You must
review and modify these files to match your infrastructure. You must add values for the licenses,
storage class, user information, database server name, database names, database schema, LDAP server
name, and LDAP attributes. The "property" mode supports the generation of
property files for multiple database servers. The script uses a
"DB\_SERVER\_LIST" parameter in the baw\_db\_server.property
file to list the number of instances.
- The second mode is "generate", which uses the modified property files to
generate the DB SQL statement file and the YAML template for the secret.
- The third mode is "validate", which checks whether the generated databases and
the secrets are correct and ready to use in a Business Automation Workflow deployment.
- The fourth mode is "generate-cr", which generates the Business Automation Workflow custom resource
based on the property files.

In the cert-kubernetes directory, go to the scripts
folder. The script can be run from this location and has the following options:

```
Usage: baw-prerequisites.sh -m [modetype]
Options: -h  Display help
  -m  The valid mode types are [property], [generate], [validate], or [generate-cr].
      STEP1: Run the script in [property] mode to create the user property files (DB/LDAP property files) with default values (database name/user)."
      STEP2: Modify the DB/LDAP/User property files with your values.
      STEP3: Run the script in [generate] mode to generate the DB SQL statement files and YAML template for the secrets, based on the values in the property files.
      STEP4: Create the databases and secrets manually based on the modified DB SQL statement file and YAML templates for the secret.
      STEP5: Run the script in [validate] mode to check that the databases and secrets are created before you deploy Business Automation Workflow.
      STEP6: Run the script in [generate-cr] mode to generate the Business Automation Workflow custom resource based on the property files.
```

## Procedure

1. Log in to the target cluster as the <cluster-admin> user.

Using the OpenShift CLI:
oc login https://<cluster-ip>:<port> -u <cluster-admin> -p <password>
On ROKS, if you are not already logged in:
oc login --token=<token> --server=https://<cluster-ip>:<port>
2 Run the script in the "property " mode. ./baw-prerequisites.sh -m property Follow the prompts in the command window to enter the required information. When the script is finished, the following message appears: [INFO] Please input <required> values in the property files under /root/git/<version>/cert-kubernetes/scripts/baw-prerequisites/propertyfile The /propertyfile directory has the following structure: ├── cert│ ├── db│ └── ldap├── baw\_db\_name\_user.property├── baw\_db\_server.property│── baw\_LDAP.property├── baw\_user\_profile.property

```
./baw-prerequisites.sh -m property
```

Follow the prompts in the command window to enter the required information.

    1. Choose the cloud platform that you want to deploy. The script shows the following
message.Select the cloud platform to deploy: 
1) Openshift Container Platform (OCP) - Private Cloud 
2) Other ( Certified Kubernetes Cloud Platform / CNCF) 
Enter a valid option [1 to 2]: 1 

[✔] Selected platform: OCP
    2. Choose the product for which you have purchased the production license. The possible values are
BAW, CP4A. The script shows the following
message.Which production license have you purchased? (1: BAW, 2: CP4A):

1) BAW
2) CP4A
Enter a valid option [1 to 2]: 1
[✔] Selected purchased license: BAW
    3. Choose the deployment license that you want to use for the Business Automation Workflow deployment. The
script shows the following
message.Which deployment license for IBM Business Automation Workflow do you want to install? (1: non-production, 2: production):

1) non-production
2) production
Enter a valid option [1 to 2]: 1

[✔] Selected deployment license for IBM Business Automation Workflow: non-production
If you chose CP4A, choose the license you want to install. The script shows the
following message.
Which deployment license for IBM Cloud Pak for Business Automation do you want to install? (1: user, 2: non-production, 3: production):

1) user
2) non-production
3) production
Enter a valid option [1 to 3]: 3

[✔] Selected deployment license for IBM Business Automation Workflow: production
    4. Choose the deployment license for the FileNet® Content
Manager you want to
install. The possible values are user, non-production, and production. The script shows the
following
message.Which deployment license for IBM FileNet Content Manager do you want to install? (1: user, 2: non-production, 3: production):

1) user
2) non-production
3) production
Enter a valid option [1 to 3]: 1

[✔] Selected deployment license for IBM FileNet Content Manager: user
    5. Choose the deployment license for the IBM® Cloud Pak for Business
Automation you want to install.
The possible values are non-production and production. The script shows the following
message.Which deployment license for IBM Cloud Pak for Business Automation do you want to install? (1: non-production, 2: production):

1) non-production
2) production
Enter a valid option [1 to 2]: 2

[✔] Selected deployment license for IBM Cloud Pak for Business Automation:production
    6. Choose the LDAP type that you want to use for the Business Automation Workflow deployment.By
default, the LDAP is SSL enabled. You can disable SSL for the LDAP when you edit the LDAP property
file. The script shows the following
message.
[*] You could set parameter "LDAP\_SSL\_ENABLED" in property file "/propertyfile/baw\_LDAP.property" later. "LDAP\_SSL\_ENABLED" is "TRUE" by default.
    7. Choose the database type that you want to use for the Business Automation Workflow deployment.By
default, the database is SSL enabled. You can disable SSL for the database when you edit the
database property file. The script shows the following
message.
[*] You could set parameter "DATABASE\_SSL\_ENABLE" in property file "/propertyfile/baw\_db\_server.property" later.
    8. Enter the alias names for all of the database servers or instances to be used by the Business Automation Workflow deployment. For
example, dbserver1,dbserver2 sets two database servers. The first server is named
dbserver1 and the second server is named dbserver2.Note: The
database server names cannot contain a dot "." character.
    9. Enter the dynamic storage class for slow, medium and fast storage(RWX). The script shows the
following
message.To provision the persistent volumes and volume claims
please enter the file storage classname for slow storage(RWX): sc-for-slow
please enter the file storage classname for medium storage(RWX): sc-for-medium
please enter the file storage classname for fast storage(RWX): sc-for-fast

[✔] Collected file storage classname(RWX)
* Slow: sc-for-slow
* Medium: sc-for-medium
* Fast: sc-for-fast
    10. Choose the egress access to external systems for this deployment. The default is set to
no to restrict accessing external systems. If you choose yes, it
restricts all BAW pods access to external systems. You can customize your network policy or use
specific policies with 'matchLabels' to set exceptions. For more information, see Configuring cluster security. The script shows the following
message.
Do you want to enable egress access to external systems for this BAW deployment? (Notes: BAW 23.2.0 prevents all network egress to unknown destinations by default. You can either (1) enable all egress or (2) accept the new default and create network policies to allow your specific communication targets as documented in the knowledge center.) (Yes/No, default: No): yes

When the script is finished, the following message appears:

```
[INFO] Please input <required> values in the property files under /root/git/<version>/cert-kubernetes/scripts/baw-prerequisites/propertyfile
```

The /propertyfile directory has the following structure:

```
├── cert
│   ├── db
│   └── ldap
├── baw\_db\_name\_user.property
├── baw\_db\_server.property
│── baw\_LDAP.property
├── baw\_user\_profile.property
```

3. You must then edit the new property files (baw\_user\_profile.property,
baw\_db\_name\_user.property, baw\_db\_server.property, and
baw\_LDAP.propertywith the values in your environment. 
Edit the <DB\_SERVER\_NAME> property prefixes in the
baw\_db\_name\_user.property file to assign each component to a database server
name defined in the baw\_db\_server.property file. The value of a
<DB\_SERVER\_NAME> must match a value that is defined in the
DB\_SERVER\_LIST parameter.
4. After you update the user property files, run the
baw-prerequisites.sh script in the "generate" mode.  
./baw-prerequisites.sh -m generate
Note: If the script detects that the property files do not have custom values, the script stops and
displays messages to help identify the missing
values:Please change the prefix "<DB\_SERVER\_NAME>" in /propertyfile/baw\_db\_name\_user.property to assign a database server instance to each component.
Found empty value(s) in "propertyfile/baw\_LDAP.property". Please edit the file and add your values.
The following messages are displayed after the script runs:
[INFO] The DB SQL statement files were created under directory /root/git/<version>/cert-kubernetes/scripts/baw-prerequisites/dbscript,
you could modify or use default setting to create database.
....
Please input <required> value in YAML template for secret under /root/git/<version>/cert-kubernetes/scripts/baw-prerequisites/secret\_template
The /baw-prerequisites directory has the following structure and varies
depending on the capabilities that you selected when you ran the script:
├── baw-prerequisites/dbscript
|
├── ban
│   └── db2
│       └── dbserver1
│           └── createICNDB.sql
├── baw-std
│   └── db2
│       └── dbserver1
│           └──create\_baw\_db.sql
├── fncm
│   └── db2
│       └── dbserver1
│           ├── createBAWDOCS.sql
│           ├── createBAWDOS.sql
│           ├── createBAWTOS.sql
│           └──createGCDDB.sql    
|── ums
     └── db2
         └── dbserver1
            └── create\_ums\_db.sql
   

      
├──baw-prerequisites/dbscript 
    ├── ban
    │   └── ibm-ban-secret.yaml
    ├── baw
    │   └── ibm-baw-db-secret.yaml
    ├── cp4ba\_db\_ssl\_secret
    │   └── dbserver1 
    │       └── ibm-cp4ba-db-ssl-cert-secret-for-dbserver1.sh
    ├── cp4ba\_ldap\_ssl\_secret
    │   └── ibm-cp4ba-ldap-ssl-cert-secret.sh
    ├── fncm
    │   └── ibm-fncm-secret.yaml
    ├── ibm-ldap-bind-secret.yaml
    └── ums
        └── ibm-ums-db-secret.yaml
5. After you generate all the necessary files for your Business Automation Workflow deployment, make
sure that the scripts, and the YAML files have the correct values before you apply them.
6. When you are ready, you can then run the DB scripts against your database server and use
the YAML files to create the necessary secrets in your OpenShift® Container
Platform cluster.  
For example, to run a database .sql script on your database server, run the
sqlplus command and provide your user's credentials:
sqlplus @create\_baw\_db.sql
To create the secret with the edited YAML, run the following
command:oc create -f ibm-baw-db-secret.yaml
7. Optional: When all of the required databases and secrets are created, you can
run the baw-prerequisites.sh script again in the "validate"
mode.  
./baw-prerequisites.sh -m validate
The command checks that all of the required secrets are found and submits a validation query to
the LDAP server and the list of remote database servers. If the operation succeeds within the
timeout threshold, the validation is marked as PASSED! No queries are run and no data is changed and
the script just reports that the connection succeeded.
If a connection is not successful, then a message informs you which connection failed. To resolve
the issue, check the values in your property files so that you can correct them and try again.
8 Run the script in the "generate-cr " mode to generate the Business Automation Workflow custom resourcebased on the property files. ./baw-prerequisites.sh -m generate-cr Follow the prompts in the command windows to enter the required information: The following messages are displayed at the end of theexecution:Please confirm final custom resource under /root/git/<version>/cert-kubernetes/scripts/baw-prerequisites/generated-cr You can review the final custom resource and check the values to make sure they are the valuesthat you want to deploy.

```
./baw-prerequisites.sh -m generate-cr
```

Follow the prompts in the command windows to enter the required information:

1. Select the deployment profile. Possible values are: small, medium, and large.
2. Enter the deployment hostname suffix.

```
Please confirm final custom resource under /root/git/<version>/cert-kubernetes/scripts/baw-prerequisites/generated-cr
```

You can review the final custom resource and check the values to make sure they are the values
that you want to deploy.

9. Deploy the Business Automation Workflow by applying the
custom resource. 
oc apply -f generated-cr/ibm\_cp4a\_cr\_production\_FC\_workflow-standalone\_final.yaml