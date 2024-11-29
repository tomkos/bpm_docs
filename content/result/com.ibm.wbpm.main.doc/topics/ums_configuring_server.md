# Creating a User Management Service server
instance

1 Create a Liberty server for theUser Management Service :
    1. Change to the bin subdirectory of your Liberty installation directory, for example:
C:\ums\wlp\bin.
    2. To create a server that is based on the server template for the
ibmUserManagement product extension, run the following
command:server create server\_name --template=ibmUserManagement:ibmUserManagementWhere
server\_name is the name you want to give your server. If you do not specify a
server name, defaultServer is used.
2. After the server is created, verify that an additional directory exists that is named after the
server and contains the configuration for that server. For example,
C:\ums\wlp\usr\servers\serverName.
3. Create the SSL keystore for the User Management Service. Run the
following command with your custom password in the bin subdirectory of your
Liberty installation
directory:securityUtility createSSLCertificate --server=server\_name  --password=passwordWhere
server\_name is the name of your server and password is the
password that you want to use for the keystore. The command prints out the
server.xml file entry, for
example:<keyStore id="defaultKeyStore" password="{xor}Lz7sLChaLTs=" />You
do not need to update server.xml, but you need to remember the password (either
in clear text or as encrypted text "{xor}....") for later configuration steps.

Next, perform Specifying basic User Management Service configuration settings.