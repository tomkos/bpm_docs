<!-- image -->

# Assigning users to roles

## Before you begin

## About this task

Applications implement interfaces that have methods. You can secure an interface or a method with
the Service Component Architecture (SCA) qualifier securityPermission. When you
invoke this qualifier, you specify a role (for example, supervisors) that has
permission to invoke the secured method. When you deploy the application you have the opportunity to
assign users to the specified role.

The securityIdentity qualifier is equivalent
to the RunAs role used for delegations in WebSphere® Application
Server. The value
associated with this qualifier is a role. During deployment, the role
is mapped to an identity. Invocation of a component secured with securityIdentity takes
the specified identity, regardless of the identity of the user who
is invoking the application.

## Procedure

1. Follow the instructions for deploying an application into IBM Business Automation Workflow.
See Deploying a module or mediation module.
2 Associate the correct users with the roles. Security qualifier Action to take Security Permission Assign a user or users to the role specified. There are fourchoices: The most flexible choice is Mapped Groups, because users canbe added to the group and thus gain access to the application withoutrestarting the server. Security Identity Provide a valid user name and password for the identity towhich the role is mapped.

| Security qualifier   | Action to take                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|----------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Security Permission  | Assign a user or users to the role specified. There are four choices: Everyone - equivalent to no security. All authenticated - every authenticated user is a member of the role. Mapped User - Individual users are added to the role. Mapped Groups - Groups of users are added to the role.  The most flexible choice is Mapped Groups, because users can be added to the group and thus gain access to the application without restarting the server. |
| Security Identity    | Provide a valid user name and password for the identity to which the role is mapped.                                                                                                                                                                                                                                                                                                                                                                      |