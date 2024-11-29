# Administering the technical user for the BPM document store

## Before you begin

The maintainDocumentStoreAuthorization and
updateDocumentStoreApplication commands are used to perform many of the tasks in
this topic. The commands are run using the AdminTask object of the wsadmin scripting client. To run
the commands, the following conditions must be met:

- maintainDocumentStoreAuthorization command:
    - The command must be run on the deployment manager node.
    - One or more application cluster members must be running.
    - Run the command in connected mode. Do not specify the wsadmin -conntype none
option.
    - You must connect to the deployment manager with a user ID that has WebSphere Application Server
operator privileges.
- updateDocumentStoreApplication command:

- The command must be run on the deployment manager node.
- Run the command in either local or connected mode.
- When running the command in connected mode, you must specify a user ID that has WebSphere
Application Server operator and deployer privileges.

For the maintainDocumentStoreAuthorization command, start the wsadmin
scripting client from the profile\_root/bin directory of the
deployment manager profile. For the updateDocumentStoreApplication command, start
the wsadmin scripting client from the
deployment\_manager\_profile/bin directory on either Workflow Server or Workflow Center. The commands do not write to a log file, but
the wsadmin scripting client always writes a
profile\_root/logs/wsadmin.traceout log file where you will
find exception stack traces and other information.

## About this task

For all of these scenarios, the same technical user is used and the credentials are saved in an
authentication alias. The authentication alias that is used is the one that is mapped to the
Business Automation Workflow role type EmbeddedECMTechnicalUser. The
default authentication alias is DeAdminAlias, but the authentication alias may have been customized
during the configuration of the deployment environment. The technical user must have the WebSphere
Application Server administrator role. Information about using the administrative console to manage
authentication aliases is found in the Authentication alias topic.

- Changing the password of the technical user
- Changing the technical user
- Changing the authentication alias for the technical user
- Reconfiguring the user registry
- Security configuration for BPM content store

These tasks are described in the following sections.

## Changing the password of the technical user

## Changing the technical user

```
AdminTask.maintainDocumentStoreAuthorization('[-deName myDEname -add cn=newTechnicalUser,o=defaultWIMFileBasedRealm]')
```

```
AdminTask.maintainDocumentStoreAuthorization('[-deName myDEname -list]')
```

Alternatively, you can authorize groups to access the BPM document store.

1. Log in to the ACCE (https://BAW\_host:BAW\_port/acce).
2. Click BPM domain. Click the Properties tab and
change the values for the System User Name and System User
Password. Click Save.

```
AdminTask.maintainDocumentStoreAuthorization('[-deName myDEname -remove cn=oldTechnicalUser,o=defaultWIMFileBasedRealm]')
```

If you change the technical user, then a change to the application settings of
IBM\_BPM\_DocStoreAdmin is required to allow the new technical user to access the IBM Administrative
Console for Content Platform Engine (ACCE). When the Business Automation Workflow deployment environment is
created, the DE admin user becomes the admin user for the embedded IBM Content
Navigator and Content Platform Engine components. The Business Automation Workflow server uses the DE admin
user to connect to those components.

## Changing the authentication alias

```
AdminTask.updateDocumentStoreApplication('[-deName myDEname]')
```

## Reconfiguring the user registry

Authorization to the BPM document store is based on
unique IDs. If the document store was initialized during initial server startup, only the same user
(with the same unique ID) can manage the document store and access its documents. If you change your
user registry configuration (for example, by removing the file-based repository in order to use only
an LDAP server in federated repositories), a user with the same user ID and password in LDAP will
not have access to the document store. This is also true if you simply delete a user and recreate
one with the same user ID. In this situation, you lose access to the document store and you must
rollback the configuration change.

Duplicate users are not permitted in federated repositories, which means that you cannot connect
to an LDAP server that contains the same users that you have in your file-based repository. You must
remove the file-based and add LDAP. A user in LDAP with the same user ID does not have access to the
document store. As a result, you may choose to authorize all authenticated users to work with the
document store for the duration of reconfiguration (while access has been shut down through the HTTP
server).

```
AdminTask.maintainDocumentStoreAuthorization('[-deName De1 -add #AUTHENTICATED-USERS]')
```

After this configuration has been completed, you can safely re-configure your user registry
without losing access to the document store. After the configuration change is
complete and the cell is restarted, you can authorize a new user and remove the #AUTHENTICATED-USERS
entry.

For information about configuring the user registry, see Configuring the user registry.

## Security configuration for BPM content store

The BPM content store is used for document
attachments and case management applications. You can only develop case management applications with
IBM Business Process Manager
Advanced. When you add or remove an
administrator, many objects and metadata need to be updated. For better efficiency, you should
create a Lightweight Directory Access Protocol (LDAP) group as an administrator. Then you can use
the LDAP and directory tools to add and remove administrators as needed; that is, by managing the
LDAP group membership.