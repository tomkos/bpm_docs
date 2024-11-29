# Configuring administrative security

## About this task

When you create an IBM Business Automation Workflow profile and keep Enable administrative security selected,
you are prompted for a user name. This identity is used as a default
for all underlying components. Configure these identities after you
create profiles to further enhance your security

Several components
of IBM Business Automation Workflow use
authentication aliases. These aliases are used to authenticate the
runtime component for access to databases and messaging engines. You
can modify these aliases on the Business Integration Security page of the administrative console.

- Starting and stopping the server

Administrative security is enabled in IBM Business Automation Workflow, which means that you must provide the appropriate user name and password to stop the server. The server will start without authentication, but authentication is required to access the administrative console.
- Administrative security roles

Several administrative security roles are provided as part of the IBM Business Automation Workflow installation.