# Configuring the User Management Service

- Creating a User Management Service server instance

 Traditional: 
 Create a IBM® WebSphere® Application Server Liberty server for the User Management Service from the command line.
- Specifying basic User Management Service configuration settings

 Traditional: 
 Before you can start a User Management Service server, you must specify some basic configuration settings.
- Connecting a user registry

 Traditional: 
 To provide single sign-on capabilities for one or more IBM Business Automation Workflow systems, the User Management Service must have access to user and group information for authenticating and asserting users to connected systems.
- Creating User Management Service server clones

 Traditional: 
 For production environments, you must configure multiple User Management Service servers to provide high-availability and load-balancing.
- Configuring a web server

 Traditional: 
 In a highly available, load balanced environment with multiple server clones, clients (such as end users with browsers) still connect to the User Management Service by using a single URL that is provided by a web server, which routes requests to available User Management Service (backend) servers for processing.
- Configuring a single sign-on database

 Traditional: 
When running multiple server clones in a fail-over enabled load-balancing environment, all servers must have access to a shared database to ensure that each server can validate tokens that are issued by the other servers.
- Securing the User Management Service

 Traditional: 
 Certain actions are require to make the User Management Service secure.
- Configuring single sign-on

 Traditional: 
 To connect an OpenID Connect Relying Party (OIDC RP) system, such as IBM Business Automation Workflow, Federated Process Portal, or IBM Process Federation Server to use your User Management Service you must have consistently matching configuration data for your relying party system and the User Management Service, which acts as the OpenID Connect Offering Party (OIDC OP).
- Configuring access to user and group information (SCIM)

 Traditional: 
 User Management Service (UMS) version 1.0.1 and later support the IBM WebSphere Application Server Liberty scim-1.0 feature. This feature allows a user who is in the administrator role of the User Management Service to invoke System for Cross-domain Identity Management (SCIM) operations in Liberty. For example, you can use SCIM REST APIs to search for users and groups and to retrieve user details.