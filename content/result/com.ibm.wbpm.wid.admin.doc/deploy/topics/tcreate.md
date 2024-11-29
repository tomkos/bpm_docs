<!-- image -->

# Creating test environment servers

If you chose to install the  Workflow Server test
environment profile when you installed IBM® Integration
Designer,
then you will already have a default unit test environment (UTE) server
that was automatically created. However, if you deleted the default
server or if you are working with a standalone installation of  Workflow Server, you
will need to manually create a test environment server for testing
your integration and mediation modules.

## Before you begin

## Procedure

To create a server:

1. In the Business Integration or Debug perspective, click
the Servers tab to open the Servers view.
2. In the Servers view, right-click anywhere in the view and
select New > Server. The New Server wizard
opens to the Define a New Server page.
3. In the Select the server type  list
box, select one IBM Workflow
Server.
4. In the Server's host name field, ensure that the correct host name
is selected for the server that you want to create. By default, the host name
localhost (IP address 127.0.0.1) is automatically selected, which is
the appropriate selection if you chose to install the test environment when you installed IBM Integration
Designer. However, you can
also type or select another fully-qualified DNS name or IP address if you chose to install
standalone Workflow Server on
a different machine than IBM Integration
Designer.
5. Click Next. The Server Settings
page opens.
6. Edit the settings as required. You can obtain help information
for any individual field or control by selecting a field or control
and pressing F1.
7. Click Next again. The Add and Remove
Projects page opens.
8. On the Add and Remove Projects page, select one or more
modules to add to the server. Information about adding modules to
a server is found in the topic "Adding modules to servers."
9. Click Finish. The new server is
now displayed in the Servers view.

## What to do next