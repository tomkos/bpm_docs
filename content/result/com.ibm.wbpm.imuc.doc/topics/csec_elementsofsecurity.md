# Application security

The following topics provide more information for application security
in IBM Business Automation Workflow:

- Authentication of users

Clients must be authenticated as a user from the user registry when administrative security is enabled. If a client tries to access a secured application without being authenticated, an exception is generated.
- Characters that are valid for user IDs and passwords

Understanding character limitations for user IDs and passwords is important because they are used throughout IBM Business Automation Workflow to provide access and secure content. The character limitations provided here apply to the IBM Business Automation Workflow administrator, the database administrator, the LDAP server administrator, and user IDs. Database and LDAP servers can have more restrictive limitations than provided here. Therefore, check the database and LDAP server product documentation for restrictions. Failure to define user IDs and passwords correctly during the installation process can result in installation failure. In addition, your specific installation might have more restrictive user ID and password requirements that you must also follow.
- Access control

When authenticating a user for IBM Business Automation Workflow, it is important for security purposes that access to all operations is not automatically granted to that user. Allowing some users to perform certain operations, while denying access to those same operations for other users, is termed access control.
- Data integrity and privacy

The privacy and integrity of data when IBM Business Automation Workflow processes are invoked is critical to maintaining security.