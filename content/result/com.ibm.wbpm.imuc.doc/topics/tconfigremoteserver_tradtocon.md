# Configuring an on-premises IBM Business Automation
Workflow to run
and debug on a remote on-container Workflow Server

## Before you begin

Ensure Workflow Server is online. For more
information, see Managing online and offline workflow servers.

Complete the steps in Customizing Workflow Server to connect to Workflow Center on
premise.

## Procedure

1. On IBM Workflow
Center, add the Workflow Server host name to the connect-src, frame-src,
frame-ancestors, and script-src-elem using wsadmin for example:
AdminTask.setBPMProperty(['-name', 'Security.ContentSecurityPolicyHeaderValue',
'-value', "default-src 'self' 'unsafe-inline' 'unsafe-eval'; font-src 'self'
https://fonts.gstatic.com; connect-src 'self' Workflow Server host name:Workflow Server port; img-src 'self' data: blob:;
frame-src 'self' Workflow Server host
name:Workflow Server port;
frame-ancestors 'self' Workflow Server host
name:Workflow Server port;
script-src-elem 'self' 'unsafe-inline' 'unsafe-eval' Workflow Server host name:Workflow Server port"])

AdminConfig.save()
2. Add users to the Debug user group. For more information, see the steps to add members to a
group in Creating and managing groups.
3. Deploy the snapshot you want to debug.