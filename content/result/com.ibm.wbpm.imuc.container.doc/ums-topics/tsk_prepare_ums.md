# Preparing to install User Management Services

## Before you begin

Make sure that you performed Configuring LDAP for
Business Automation Workflow on containers. In addition, if you want all communications
between UMS and your LDAP server to be encrypted, perform Configuring SSL-enabled LDAP.

## Procedure

To prepare to install User Management Services,
perform the following actions:

1. Perform Preparing the database for the User Management Services.
2. Perform Configuring the User Management Services dedicated pods option.
3. Perform Creating the UMS database admin secret.
4. Perform Securing communications with the UMS database.
5. Perform Securing communications routes with User Management Services (UMS).

- Preparing the database for the User Management Services

 Containers: 
Create the database for UMS single sign-on and teams options.
- Configuring the User Management Services dedicated pods option

 Containers: 
User Management Services provides different capabilities. The default is to run each capability in a dedicated pod so that each capability can scale horizontally as required. It is also possible to have a single pod that contains all UMS capabilities.
- Creating the UMS database admin secret

 Containers: 
To avoid passing sensitive information in configuration files, you must create a secret manually before you deploy User Management Services (UMS). The secret contains a UMS database admin user, database users, and passwords.
- Securing communications with the UMS database

 Containers: 
To protect communications with the database, you must create a secret that contains the certificate for the User Management Services (UMS) database.
- Securing communications routes with User Management Services (UMS)

To protect external routes that client communications use with UMS in a production environment, you can use an external TLS certificate that is trusted by your clients. For a test environment without an external TLS certificate, you can let UMS generate certificates using shared\_configuration.root\_ca\_secret.