<!-- image -->

# Deploying secure applications

## Before you begin

Before you perform this task, verify that you have designed,
developed, and assembled an application with all the relevant security
configurations. For more information about these tasks, see the Integration Designer information
center.

## About this task

One of the required steps to deploy secured applications is to assign users and groups to the
roles that were defined when the application was constructed. This task is completed as part of the
Map security roles to users or groups step. If an assembly tool was employed, this assignment
might have been completed in advance. In that case, you can confirm the mapping by completing this
step. You can add new users and groups and modify existing information during this step.

If a RunAs role has been
defined in the application, the application will invoke methods using
an identity setup during deployment. Use the RunAs role
to specify the identity under which the downstream invocations are
made. For example, if the RunAs role is assigned
user bob, and the client, alice, is invoking a servlet
(with delegation set) that calls the enterprise beans, the method
on the enterprise beans is invoked with bob as the identity.

As
part of the deployment process, one of the steps is to assign or modify
users to the RunAs roles. This step is entitled, Map
RunAs roles to users. Use this step to assign new users or modify
existing users to RunAs roles when the delegation
policy is set to SpecifiedIdentity.

The steps
described in the Procedure section are common for both deploying an
application and modifying an existing application. If the application
contains roles, you see the Map security roles to users
or groups link during application deployment and also
during managing applications, as a link in the Additional properties
section.

## Procedure

1. Go to the installed application that requires users to
be mapped to the roles. Complete the steps that are required for installing applications before the Map security roles
to users or groups step.
2. Assign users and groups to roles.
3. Map users to RunAs roles if RunAs roles
exist in the application.
4. Click Correct use of System Identity to
specify RunAs roles, if needed.  Complete
this action if the application has delegation set to use system identity,
which is applicable to enterprise beans only. System identity uses
the IBM® Business Automation Workflow security
server ID to invoke downstream methods. Use this ID with caution because
this ID has more privileges than other identities in accessing IBM Business Automation Workflow internal
methods. This task is provided to make sure that the deployer is aware
that the methods listed in the page have system identity
set up for delegation and to correct them if necessary. If no changes
are necessary, skip this task.
5. Complete the remaining non-security related steps to finish
installing and deploying the application.

## What to do next

- Assigning users to roles

A secured application uses one or both of the security qualifiers securityPermission and securityIdentity. When these qualifiers are present, there are additional steps that must be taken at deployment time in order that the application and its security features work correctly.