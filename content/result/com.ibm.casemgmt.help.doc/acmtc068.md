# Content security policy directive frame-ancestors self errors in the Case Client

## Symptoms

The browser window does not render when you go to the IBM Business Automation
Workflow desktop. The error is seen on
the Network tab in the browser developer tool. For example,

## Causes

The IBM Content
Navigator
server is external and it might be located in a different domain than the workflow server. The
browser does not render the page because strict Content Security Policy settings prevent it.

## Environment

## Resolving the problem

You can configure Content Security Policy settings in two locations:

- IBM Content
Navigator
server;
- IBM Business Automation
Workflow server.

Configuring the IBM Content
Navigator server IBM
Documentation reference: How to configure the Content Security Policy header in IBM Content
Navigator

1. Follow the directions in the configuration scenario to allow embedding external resources. The
relevant part of the CSP string is this section:
frame-ancestors 'self' xxx;
2. The following strings are examples that work:
frame-ancestors 'self' https://[external ICN server]:[port] https://[BAW server]:[port];
    frame-ancestors 'self' http://[external ICN server]:[port] https://[BAW server]:[port];
    frame-ancestors 'self' https: http:;
3 For quick testing, you can edit the ESAPIWafPolicy.xml file in the deployedlocation. Then, you do not have to rebuild and redeploy IBM ContentNavigator . However, ifyou do this, the changes in the ESAPIWafPolicy.xml file are lost the next timethat you rebuild and redeploy IBM ContentNavigator .
    - For example,
ContentNavigator.ear/navigator.war/WEB-INF/ESAPIWafPolicy.xml

For configuring the IBM Business Automation
Workflow server, see  Security-hardening properties

1. The Security.ContentSecurityPolicyHeaderValue property value has the CSP
string.
2. Sample command to get the current CSP string to check its current value: wsadmin>print
AdminTask.getBPMProperty(['-name', 'Security.ContentSecurityPolicyHeaderValue'])
3. Out of the box, the Security.ContentSecurityPolicyHeaderValue property
value is empty.
4. Sample command to set the current CSP string: wsadmin>print
AdminTask.setBPMProperty(['-name', 'Security.ContentSecurityPolicyHeaderValue', '-value',
"frame-ancestors 'self' https://[external ICN server]:[port] https://[BAW
server]:[port];"])
5. Remember to run the save command after running the command above:
wsadmin>AdminConfig.save()
6. Synchronize the nodes and restart servers.
7. The CSP string in the command mentioned in the step 2 and 4 shows the frame-ancestors 'self'
policy. Your environment might require other policies as well.

More Resources

- The MSDN documentation has a clear explanation of how the browser Content
Security Policy works: Content Security Policy (CSP) - CSP: frame-ancestors
- This web page can be used to test browser Content Security Policy settings: https://cspvalidator.org/