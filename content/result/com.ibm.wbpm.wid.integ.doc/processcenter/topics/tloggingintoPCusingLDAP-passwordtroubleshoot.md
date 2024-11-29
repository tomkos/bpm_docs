# Preventing an LDAP account from being locked when you start Integration Designer

## About this task

## Procedure

To prevent the LDAP accunt from being locked, complete these steps:

1. In Integration Designer, open the preferences by
selecting Business Integration > Process Center
2. Clear the password field and click Apply.
The process apps in the workspace are marked as disconnected.Note: If you don't clear the passwords
before changing the password in LDAP, the LDAP account locks when you start Integration Designer because Integration Designer starts to communicate with Workflow Center immediately if process applications or
toolkits are in the workspace. If the LDAP account locks, open the storage file in a text editor.
You can find in the Windows user folder, such as C:\Users\Administrator\ >
\.eclipse\org.eclipse.equinox.security.security\secure\_storage. Then remove all the
entries that start with /OneBPM\_PC/ and contain the Workflow Center the password was changed for, for example
 /OneBPM\_PC/http\:\\2f\\2fnitmah6.canlab.ibm.com\:9080\\2fProcessCenter/OneBPM\_PC\_pwd=org.eclipse.equinox.security.windowspasswordprovider\tvtd7OSAbjRo\=,J55rHVyOO+YpKPpsCYkvvg\=\=
3. Close Integration Designer.
Now when you start Integration Designer, you are
prompted for login information for that server.
4. Enter the login information.

## What to do next

1. Open the storage file in a text editor. You can find the storage file in the Windows user
folder, such as C:\Users\Administrator\ >
\.eclipse\org.eclipse.equinox.security.security\secure\_storage.
2. Remove all the entries that start with /OneBPM\_PC/ and contain the
Workflow Center the password was changed
for.
3. Start Integration Designer.
4. Enter the login information.
5. Restart Integration Designer to connect.