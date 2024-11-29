# Configuring authentication to deploy to a production environment

## Procedure

1. Log in to the WebSphere administrative console on the Workflow server.
2. Find the appropriate alias name for the EmbeddedECMTechnicalUser
role.

Click Servers > Deployment Environments > [Deployment Environment Name]
> Related Items > Authentication Aliases. 
Note the alias that is associated with the EmbeddedECMTechnicalUser
role.

1. Find the user associated with the alias.

Click Security > Global security > Java Authentication and Authorization
Service > J2C authentication data. 
Note the user who is associated with the EmbeddedECMTechnicalUser Alias
that are identified in step 2.

1. Ensure the user who is identified in step 3 belongs to the same LDAP group that is configured
for Solution Administrators for Case. Refer to Planning for security in the development environment, Table 3
for more details.

## Related reference

- Connections from Workflow Server to Workflow Center