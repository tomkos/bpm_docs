# Rolling upgrade

## Before you begin

## Procedure

Complete the following steps:

1. Upgrade your staging server environment. Test your applications in the new environment
and make sure that they work as expected.
2. Upgrade your development server environment. Test your applications in the new
environment and make sure that they work as expected.
3. Upgrade your production server environment.
4. Upgrade Workflow Center. 
Note: A Workflow Center
environment must be upgraded only after server environment that is associated with
it.
The Workflow Center maintains a full
version history of all the process applications, and new function capability cannot be introduced
before the entire topology is upgraded. After you upgrade the Workflow Center, reconnect any servers
that are online. Make sure that everything works as expected.

- Rolling upgrade for case projects and legacy case solutions in the production environment

 As of 24.0.0.0, it is not required that you upgrade the development environment and the project versions before you deploy a project.

## Related concepts

- Development and deployment version levels

## Related information

- Publishing modules to test environment servers
- Deploying service modules
- Working with process application servers
- Merging workspace and Process Center repository changes