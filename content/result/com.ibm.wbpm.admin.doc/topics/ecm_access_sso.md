# Accessing an Enterprise Content Management server using single
sign on (SSO)

## About this task

For general information about application security for Business Automation Workflow, see Application security and WS-Security specification.

## Procedure

- Where you set up the Enterprise Content Management server
configuration, there is a check box labelled Always use
connection information specified here, which is selected
by default. If you want to use single sign on, you must clear this
check box. When that check box is not selected, the Business Automation Workflow system
uses individual user IDs for authentication and projects the identity
to the Enterprise Content Management server. For more information
about authentication between Business Automation Workflow and the
Enterprise Content Management server, see Authentication scenarios.
- When a Content Integration step-type is called from a Human Service or Coach, the
outbound JAX-WS call is done using the current user, rather than the user specified in the
configuration settings for the Enterprise Content Management server.