# Enabling IBM Connections integration for Process Portal (deprecated)

## Before you begin

```
<proxy:policy url="<IBM Connections endpoint>" acf="none" basic-auth-support="true">
		<proxy:actions>
			<proxy:method>GET</proxy:method>
		</proxy:actions>
		<proxy:cookies>
		   <proxy:cookie>LtpaToken</proxy:cookie>
		   <proxy:cookie>LtpaToken2</proxy:cookie>
		   <proxy:cookie>JSESSIONID</proxy:cookie>
		</proxy:cookies>
	</proxy:policy>
```

For information about updating
the proxy configuration, see Configuring the Business Space Ajax proxy and Adding proxy policies to the Business Space Ajax proxy.

## Procedure

1. Log in to IBM Process
Designer with
a user ID with administrative rights.
2. Open the Process Portal application
by clicking the Servers tab, and then click Add to
add the IBM Connections server.
3. In the Type field, select IBM
Connections Server.
4. Complete the server locations information, including the
host name.
5. Provide a user ID and password. Tip: For IBM Connections notifications, the
user ID and password to IBM Connections
are required to enable the IBM Connections
server. On the administrative console for the IBM Connections server, make sure that the user
is a member of the trustedExternalApplication security
role in the WidgetContainer application. If your participants use
only the business card capabilities, a user ID and password are not
required.
6. Specify whether the IBM Connections
server uses Secure Sockets Layer (SSL). If Heritage Process Portal is
accessed through HTTPS, select this setting. If Heritage Process Portal is
accessed through HTTP, do not select this setting.Tip: SSL
is enabled by default in Business Automation Workflow, so unless
your administrator disabled SSL, select Use SSL for IBM
Connections.
7. Click Save or Finish Editing.
8. Click Test Connection.  This
test checks whether the user ID and password successfully connect
to the IBM Connections server. Tip: The test does not include SSL certification. On the administrative
consoles for your production systems, verify that the administrator
exchanged SSL certificates between the IBM Connections server and Business Automation Workflow as described
in Configuring IBM Connections integration for task notifications.

If your setup is configured correctly, a message appears.
9. Create a snapshot of the application, and install the snapshot
on the workflow server.

## Results

For Workflow Server profiles,
the portal snapshot is installed on the workflow server.

The
user avatar that is defined in the IBM Connections
server is displayed instead of the avatar from the user preferences.

When IBM Connections is set up for Business Automation Workflow, the
fields for the user's telephone number, email address, title, and
avatar become noneditable in the user profile dialog box.

## What to do next

For notifications, make sure that users' email addresses
in the IBM Business Automation
Workflow user
profiles match the email addresses in their IBM Connections user profiles. So that process
participants receive notifications in IBM Connections,
ask them to update their user preferences as described in Setting preferences in Process Portal.