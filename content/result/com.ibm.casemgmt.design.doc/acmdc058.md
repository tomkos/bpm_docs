# Exporting the audit configuration

## About this task

If you configured auditing for a solution, export the audit configuration package file when you
migrate the solution package. When you configure the target environment after you deploy the
solution, import the audit configuration package file so that the settings can be applied to the
deployed solution.

## Procedure

To export the audit configuration from the bawadmin desktop, you need
to follow different steps because the workflow case solution does not directly show up in the
authoring environment.

1. Start the Case administration client.
 Enter the following URL in a
browser:
http://server:port/navigator/?desktop=bawadmin
where
server is the IBM® Content
Navigator IP address or
fully qualified server name, and 
port is the
IBM Content
Navigator port
number.
2. Select View all in case solution.
3. Select the Overflow menu of the solution and select
Advanced.
4. From the Solutions list, select the solution to be exported that is
associated with the audit configuration.
5. Right click and select Export > Audit
Configuration.
6. Complete the wizard steps and download the audit configuration package file.