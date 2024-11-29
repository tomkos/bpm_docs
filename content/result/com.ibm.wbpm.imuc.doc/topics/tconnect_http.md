# Re-enabling HTTP access in Business Automation Workflow
temporarily

## About this task

Your environment reverts to the state of IBM Business Process Manager
 V8.5.7 CF2016.12 after you complete these
steps.

Note that many web applications already enforced HTTPS and some web applications were introduced
later. These web applications are not affected by this configuration and will continue to enforce
HTTPS, as these steps provide backwards compatibility only and are not general purpose
security-removal tools. There is no supported way to enable unencrypted HTTP traffic for the
Process Admin Console, Workflow Center (formerly the Process Center Console) or
current implementations of IBM Process
Portal.
However, SSL offloading that uses httpsIndicatorHeader can allow unencrypted traffic from an
intermediary web server to Business Automation Workflow.

## Procedure

Follow these steps assuming the name of your deployment environment is
De1:

1. Shut down all the servers.
2. Go to the <install\_root>/bin directory, and run wsadmin
-conntype none -lang jython -profileName dmgrProfile. For Business Automation Workflow Express, use the stand-alone server's
profile.
3. If secure connections are used, Business Automation Workflow marks the cookies as secure by default. However,
if you re-enabled non-secure http:// access to Business Automation Workflow, you must disable the
Secure flag for Business Automation Workflow
cookies by setting the deployment-level custom property
ProcessServer.MarkCookiesSecureOnSecureConnections to
false. When reverting to secure HTTPS, you should re-enable the
Secure flag and set the property back to true.
To set the property to false, you can use the following command (which
assumes that your deployment environment is named De1):
AdminTask.setBPMProperty(['-de', 'De1', '-name', 'ProcessServer.MarkCookiesSecureOnSecureConnections', '-value', 'false'])
4. Enter the following commands on the wsadmin prompt (where
De1 is the name of your Business Automation Workflow deployment environment):

wsadmin> print AdminTask.configureBPMTransportSecurity( [ '-de', 'De1', '-apps', '201612', '-transportSecurity', 'allowhttp'] )
wsadmin> print AdminTask.configureBPMTransportSecurity( [ '-de', 'De1', '-apps', 'productREST', '-transportSecurity', 'allowhttp'] )
wsadmin> AdminTask.configureSingleSignon('-requiresSSL false')
wsadmin> for server in AdminUtilities.convertToList(AdminTask.listServers('-serverType APPLICATION\_SERVER')):
 
wsadmin> for cookie in AdminUtilities.convertToList(AdminConfig.list('Cookie', server)):
Note: This line must be indented one space.
wsadmin> AdminConfig.modify(cookie, [['secure','false']])
Note: This line must be indented two spaces.
wsadmin>
Note: This line is a required empty line to end the loop. Just press Enter.
wsadmin> AdminConfig.save()
wsadmin> exit
5. Restart all the servers.

## What to do next

## Related information

- IBM Smarter Process Security