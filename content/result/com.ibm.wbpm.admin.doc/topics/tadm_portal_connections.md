# Configuring IBM Connections integration for task
notifications (deprecated)

## Before you begin

- IBM Business Automation
Workflow must
be configured to use the same user repository that the IBM Connections server uses.
- If you want your team of Process Portal users
to receive notifications about tasks in IBM Connections,
you must have IBM Connections
V4 or later.
- If you want your team to use IBM Connections
only for business card information, see Enabling IBM Connections integration for Process Portal.

## About this task

- Verify that the IBM Connections
user ID that is specified in the IBM Connections
Server profile in IBM Process
Designer has
authority to post to the IBM Connections
stream, which means that the user is a member of the trustedExternalApplication
security role in the WidgetContainer application that is running on IBM Connections. This authorization
prevents notifications from not being successfully posted to the IBM Connections stream although
the Process Portal and IBM Connections configuration steps
were followed properly.
- Make sure that the IBM Connections access role is
configured properly on the IBM Connections server. In the
configuration, select the Use SSO token option, which ensures that users can
open tasks from the links in the task notifications that are visible in the IBM Connections stream.
- Verify that the correct port is specified in the Process Designer IBM Connections server definition.
If no port is specified, the default port 443 is used.
- Verify that the IBM Connections
server HTTP server is running; otherwise notifications might not be
successfully posted to the IBM Connections
stream although the Process Portal and IBM Connections configuration steps
are followed properly.
- Make sure that single sign-on (SSO) is configured with the same
domain in both Business Automation Workflow and IBM Connections. The Business Automation Workflow domain
that is specified in the 99Local.xml file must
match your IBM Connections server.
- Make sure to use the same security realm name for the Business Automation Workflow server
and the IBM Connections server.
- Perform the
actions that are described in Configuring SSL communication. Tip: Using the same security protocol for both the Business Automation Workflow server
and the IBM Connections server
prevents an issue where Process Portal users
see a blank task completion view in IBM Connections
server. For example, use HTTPS for both the Business Automation Workflow server
and the IBM Connections server,
or use HTTP for both the Business Automation Workflow server
and the IBM Connections server.
- Adding the  IBM Connections
server to the trusted servers list prevents problems with sizing in Process Portal. See Adding servers to the trusted server list.

## Procedure

To configure the integration for task notifications in IBM Connections, complete the following
steps:

1. Configure the Business Automation Workflow server
to use the same LDAP server that the IBM Connections
server uses.
2 Enable SSO for the Business Automation Workflow server.
    1. In the administrative console, select Security > Global Security.
    2. In the Authentication cache settings section, expand Web
and SIP security and select Single sign-on (SSO).
    3. Select Enabled, select Interoperability
Mode, and select Web inbound security attribute.
Make sure to include the correct domain name and change the cookie
names to match your environment. Tip: Add a period before the domain name, for example
.ibm.com
3 Configure cross-cell security for the Business Automation Workflow serverand the IBM Connections server.

1 Configure Secure Sockets Layer (SSL) by exchanging theserver SSL certificates. Extract the root SSL certificatefrom the IBM Connections server.Use the administrative console on the Process Portal serverto complete the following actions: To retrieve the root signer of the Process Portal server,repeat the previous steps on the IBM Connectionsserver.
    1. Select Security > SSL
certificate and key management  > Key stores and
certificates  > DefaultTrustStore  > Signer certificates.
    2. Click Retrieve from port.
    3. Specify the host name and SSL port (for example, the admin host
secure port) of the remote Workflow Center server.
    4. Specify an alias that you want to use for the root signer.
    5. Click Retrieve signer information and verify
that the retrieved signer information is correct.
    6. Save the root signer in the local truststore.

To retrieve the root signer of the Process Portal server,
repeat the previous steps on the IBM Connections
server.

2 Share the LTPA keys by exporting the LTPA key from the IBM Connections server and importingit into the keystore of the Process Portal server. Sharing LTPA keys is required for configuring cross-cell securityfor the Business Automation Workflow serverand the IBM Connections server. Tip: When multiple cells are involved, one set of LTPA keys is shared among them.Therefore, administrators must plan which set of LTPA keys to use in the organization and ensurethat the automatic LTPA key generation is turned off. Otherwise, if a new set is generated, thecells can become unsynchronized.

1. In the administrative console of the remote IBM Connections server, select Security > Global Security.
2. In the Authentication section, click LTPA.
3. In the Cross-cell single sign-on section, type a new password
and a fully qualified key file name.
4. Click Export keys.
5. Transfer the exported key file in binary mode to the file system
of the local Process Portal server
by repeating the previous steps on the administrative console of the Process Portal server
and clicking Import keys.
3 Verify that cross-cell security is configured correctly. If security is configured correctly, you arenot prompted to log in to the Business Automation Workflow server.

1. Log in to your IBM Connections
server.
2. In the same browser session, launch the URL for your Business Automation Workflow server.
4. Optional: If you want to
customize the URLs of links to gadgets, configure the optional scenario
key SERVER\_EMAIL\_GADGET\_LINK, as described in Configuring endpoints to match your topology.
Tip: By default, links to widgets are generated
using the EXTERNAL\_CLIENT scenario key, which points
to the Business Automation Workflow server
or, if you have one, the web server.
5 Enable task notifications in IBM Connectionson the server by editing the 100Custom.xml file. For information about modifying the 100Custom.xml file,see The 100Custom.xml file and configuration .

For information about modifying the 100Custom.xml file,
see The 100Custom.xml file and configuration.

1. Insert the following XML code in the <server> section
of the file: <connections-task-notification merge="mergeChildren">
<!-- Change the value to true in order to enable connections task notification-->
<enable-connections-task-notification merge="replace">true</enable-connections-task-notification>
</connections-task-notification>
2. Restart the deployment manager, nodes, and clusters.

## What to do next

In Process Designer, enable
the IBM Connections integration.

For
notifications, make sure that users' email addresses in the IBM Business Automation
Workflow user
profiles match the email addresses in their IBM Connections user profiles.

So that
process participants receive notifications in IBM Connections, ask them to update their user
preferences as described in Setting preferences in Process Portal.