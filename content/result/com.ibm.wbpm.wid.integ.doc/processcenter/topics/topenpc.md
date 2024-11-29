<!-- image -->

# Accessing the Workflow Center repository

## Before you begin

## Procedure

To access the Workflow Center repository,
complete the following steps:

1. In the upper-right corner of the development environment,
click Workflow Center.
2 Complete one of the following steps:
    - If you have connected to a Workflow Center repository
previously or if you installed Integration Designer from
the Workflow Center,
then the Workflow Center view
will open.
    - If you have not connected to a Workflow Center repository
previously, enter the following information on the subsequent page.
3. In the  repository window, enter a URI to connect to the IBM® Workflow
Center repository,
in the following format: http://<server name>:<port
number>/ProcessCenter; for example, http://myserver.toronto.com:9080/ProcessCenter.
Enter your user ID and password. Click Connect.
4. The Workflow Center repository
view opens. Tip: When you enter a URI, it is
recorded in the Preferences page. To see the
current URI, select Window > Preferences > Business Integration > Workflow Center.

## What to do next

If your connection to the Workflow Center fails,
you should check that the port is accessible. One reason the port
may not be accessible is that it is behind a firewall.

If Integration Designer cannot
add the Workflow Center as
a server, you should check that the BOOTSTRAP\_ADDRESS port (default
is 2809) of the Workflow Center is
accessible. One reason the port may not be accessible is that the Workflow Center is
behind a firewall and Integration Designer is
outside the firewall.

- Importing an SSL security certificate into Integration Designer

To connect to an HTTPS enabled server, you must import the SSL security certificate (X509Certificate) for the server.
- Preventing an LDAP account from being locked when you start Integration Designer

When you try to change your password in an LDAP user repository, you can prevent the LDAP account from being locked when using IBM Integration Designer. If the LDAP account is already locked, you can fix it.