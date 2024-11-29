# Enabling Sametime Connect integration for Process Portal (deprecated)

## Before you begin

- To perform
this task, you must be in the IBM Process
Designer desktop
editor, which is deprecated.
- Ensure that your administrator has configured your Process Portal environment
for Sametime
Connect integration.
You will need the Sametime
Connect server
location information in order to complete this task.
- If the Secure Sockets Layer (SSL) is enabled for your Business Automation Workflow server,
make sure that it is also for the Sametime server, otherwise the Sametime
scripts do not load, as explained in step 5.
- To make changes to the Process Portal environment,
you must be logged into Process Designer with
a user ID with administrative rights.

## Procedure

1. Open the desktop Process Designer (deprecated).
2. Open the process application in the Designer view.
3. Click the Servers tab, and then Add to
add a new server.
4. In the Type field, select IBM
Sametime Server.
5. Enter the information about
your Sametime server.   Important: If the Business Automation Workflow server
is SSL-enabled and you configure the Sametime server without enabling
SSL, Sametime scripts cannot load to Process Portal and
an error message similar to the following one is displayed.portal-components\_en.min.js:601 Mixed Content: 
The page at 'https://9.123.103.217:9444/ProcessPortal/dashboards/SYSRP/RESPONSIVE\_WORK' was loaded over HTTPS, 
but requested an insecure script 'http://sametime11.cn.ibm.com:9081/stbaseapi/baseComps.js'. 
This request has been blocked; the content must be served over HTTPS.
Such
exception is thrown by most browsers, such as Mozilla, Chrome, Internet
Explorer 9 and later, against mixed-content requests. A request is
said to be mixed content when a nonsecured active HTTP
request (for example, downloading a JavaScript file) is made within
a site that has been secured by an HTTPS configuration. For more information,
see the Mixed content Mozilla page.
6. Click Save or Finish Editing.
7. Test the connection to the Sametime
Connect server.
Point your browser to the following URL.https://sthost:secureport/stwebclient/popup.jspWhere: 
sthost
The name of your Sametime
Connect server.
secureport
The port for the Sametime
Connect server.

If your setup is configured correctly,
you will see the Lotus Sametime login window.
8. Create a snapshot of the application, and install the snapshot
on the process server.

## Results