# Configuring a traditional IBM Business Automation
Workflow to run and debug on a
remote on-premises Workflow Server

## Before you begin

Ensure Workflow Server is
online. For more information, see Managing online and offline workflow servers.

Accept the certificates and deploy the snapshot that you want to debug.

## Procedure

If the IBM Business Automation
Workflow Center and the remote Workflow Server are in the same
domain, set up LTPA token security by selecting Global Security > LTPA >  Cross-cell single sign-on. For more information, see How to configure single sign-on (cross-cell
SSO).

1. Use the wsadmin command to update
ContentSecurityPolicyHeaderValue. To determine the previous value, use
AdminTask.getBPMProperty() and add the returned results when you run the
AdminTask.setBPMProperty commands. For more information, see Security hardening properties.

Add the Workflow Server
hostname to the connect-src, frame-src, frame-ancestors, and script-arc-elem on IBM Workflow
Center. For example,
AdminTask.setBPMProperty(['-name', 'Security.ContentSecurityPolicyHeaderValue', '-value',
"default-src 'self' 'unsafe-inline' 'unsafe-eval'; font-src 'self' https://fonts.gstatic.com;
connect-src 'self' https://WS\_host:WS\_port; img-src 'self' data: blob:; frame-src 'self'
https://WS\_host:WS\_port; frame-ancestors 'self' https://WS\_host:WS\_port; script-src-elem 'self'
'unsafe-inline' 'unsafe-eval' https://WS\_host:WS\_port"])

AdminConfig.save()
Add the Workflow Center
hostname to frame-ancestors on Workflow Server. For example,
AdminTask.setBPMProperty(['-name', 'Security.ContentSecurityPolicyHeaderValue', '-value',
"default-src 'self'; frame-ancestors 'self' https://WC\_host:WC\_port; script-src 'self'
'unsafe-inline' 'unsafe-eval'; style-src 'self' 'unsafe-inline'; img-src 'self' data: blob: https:;
font-src 'self' fonts.gstatic.com data:; worker-src 'self' blob:; child-src 'self' blob:; frame-src
'self' https:"])

AdminConfig.save()
2. Use the wsadmin command to update
Security.CsrfProtectionOriginWhitelist on Workflow Server. To determine the
previous value, use AdminTask.getBPMProperty() and add the returned results when
you run the AdminTask.setBPMProperty commands.  For
example,AdminTask.setBPMProperty(['-de', DEname, '-name', 'Security.CsrfProtectionOriginWhitelist', '-value', 'https://WC\_host:WC\_port'])
AdminConfig.save()
3. Use the wsadmin command to update
Security.CsrfProtectionRefererWhitelist on Workflow Server. To determine the
previous value, use AdminTask.getBPMProperty() and add the returned results when
you run the AdminTask.setBPMProperty commands. For
example,AdminTask.setBPMProperty(['-de', DEname, '-name', 'Security.CsrfProtectionRefererWhitelist', '-value', 'WC\_Host:WC\_port'])
AdminConfig.save()
4. To ensure the remote Workflow Server points to the correct
Workflow Center hostname, add
the following lines to the 100Custom.xml file from Workflow Server:

<server>
    <rest>
      <allowed-origins merge="replace">https://WChost:WCport </allowed-origins>
    </rest>
  </server>
5. In the WebSphere administrative console, select Security > Global Security > Custom Properties, and then add the
com.ibm.websphere.security.addSameSiteAttributeToCookie custom property with
value None for Workflow Center and an online Workflow Server.
6. Configure the trust association interceptor (TAI) for Workflow Server. In the WebSphere
administrative console, select Global Security > Trust Association > interceptors > com.ibm.bpm.security.PreemptiveBasicAuthTAI > enabledForDEs and set the value of enabledForDEs to your DE, such as
De1.

Important: To ensure your changes are saved, delete the
userAgentFilter row if you don't have a userAgentFilter value.
7. Add users to the Debug user group for Workflow Server. For more information,
see the steps to add members to a group in Creating and managing groups.
8. Restart the deployment environment.