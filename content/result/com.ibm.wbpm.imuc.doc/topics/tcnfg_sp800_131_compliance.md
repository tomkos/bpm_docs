# Enabling a NIST SP800-131a compliant environment

## Before you begin

## Procedure

1. Generate or import certificates and activate SSL on the directory server. This step
varies depending on the LDAP server that you are using.
2. Add the signer certificate of your LDAP server to the truststore of your application
server.
3. Enable the SP 800-131a standard for IBM Business Automation
Workflow.
For updates to the administrative console, see Transitioning WebSphere Application Server to the SP800-131 security standard. Note: In a
clustered environment, before you run the syncNode.bat or
syncNode.sh command, change to strict mode and update the
ssl.client.props configuration file, which is at
ProcessDesignerInstallation Path/resources/ssl.client.props.
You are prompted to accept the self-signed certificate into the truststore before the changes can be
propagated. For more information, see  Configuring WebSphere Application Server for SP800-131 standard strict
mode.
4. Enable TLS V1.2 for all clients. Specify the Secure Sockets Layer (SSL)
protocol to be used for client applications, such as the wsadmin command or the
Process Designer. For the wsadmin
command, see Transitioning WebSphere Application Server to the SP800-131 security standard. For the
Process Designer, update the ssl.client.props configuration file, which is at
ProcessDesignerInstallation
Path/resources/ssl.client.props.
5. Configure SSL communication for Workflow Center and Workflow Server. See Configuring Secure Sockets Layer (SSL) for IBM Business Automation Workflow.Note: After you convert the certificates to the NIST SP 800-131a
standard in a clustered environment that includes a Workflow Center cluster and a Workflow Server cluster, add the Workflow Server signer to the Workflow Center truststore. Then add
the Workflow Center signer to
the Workflow Server
truststore.
6 Specify that SSL is used for Enterprise JavaBeans (EJB) method calls.
    1. In the administrative console, click Security > Global security > RMI/IIOP Security > CSIv2 inbound communications.
    2. Select SSL-required in the Transport pull-down
menu.
    3. In the administrative console, click Security > Global security > RMI/IIOP Security > CSIv2 outbound communications.
    4. Select SSL-required in the Transport pull-down
menu.
7 Switch the data sources to SSL:

- If you are using Oracle, follow the steps in 7.a.
- If you are using SQLServer, follow the steps in 7.b.
- If you are using Db2, follow the steps in 7.c.
- If you are using PostgreSQL, follow the steps in
7d.

1 If you are using Oracle, follow the instructions:
    1. The following configuration example assumes that SSL client authentication is enabled and the
Public-Key Cryptography Standards 12 (PKCS12) wallet is being used in Oracle. Generate a keystore
and a certificate on the Oracle server. The following keytool command generates a self-signed Java
Keystore (JKS) format
keystore:keytool -genkey -keyalg RSA -alias server\_key\_alias -keystore full\_path\_of\_server\_keystore\_file.jks -dname “CN=machine\_name” -storepass server\_keystore\_password -validity 360 -keysize 2048 -keypass server\_key\_passwordFor
example: keytool -genkey -keyalg RSA -alias dbserverkey -keystore /home/oracle/keystore/serverdbkeystore.jks -dname "CN=myOracleServer.company.com" -storepass Password -validity 3600 -keysize 2048 -keypass Password
The following keytool command exports the keys of the Oracle server into a
certificate:keytool -export -alias server\_key\_alias -storepass server\_keystore\_password -file full\_path\_of\_server\_certificate\_file.cer -keystore lfull\_path\_of\_server\_JKS\_file.jksFor
example:keytool -export -alias dbserverkey -storepass Password -file /home/oracle/keystore/servercertificate.cer -keystore /home/oracle/keystore/serverdbkeystore.jks
    2. Import the signer certificate for the database into the IBM WebSphere® Application
Server Java cacerts truststore by
running the following
command.WAS\_HOME/java/bin/keytool -import -file full\_path\_of\_certificate\_file -keystore WAS\_HOME/java/jre/lib/security/cacerts -alias alias\_of\_certificate\_file -storepass ts\_password
Where WAS\_HOME is the WebSphere Application
Server home directory,
full\_path\_of\_certificate\_file is the full path of the certificate file,
alias\_of\_certificate\_file is the alias of the certificate file, and
ts\_password is the truststore password.
    3 Because the WebSphere ApplicationServer is a client to the Oracle server, the WebSphere ApplicationServer is referred to as client,and Oracle server is referred to as server in the following commands.
        1. Create the Java keystore on WebSphere Application
Server by running the following
command:WAS\_HOME/java/bin/keytool -genkey -keyalg RSA -alias client\_key\_alias -keystore client\_keystore\_file.jks -dname “CN=computer\_name” -storepass client\_keystore\_password -validity 360 -keysize 2048 -keypass client\_key\_password
where WAS\_HOME is the WebSphere Application
Server home directory. For
example:keytool -genkey -keyalg RSA -alias dbclientkey -keystore clientdbkeystore.jks -dname "CN=myserver.company.com" -storepass Password -validity 360 -keysize 2048 -keypass Password
        2. Export the keys of WebSphere Application
Server into a certificate by
running the following
command:keytool -export -alias client\_key\_alias -storepass client\_keystore\_password -file full\_path\_of\_client\_certificate\_file.cer -keystore full\_path\_of\_client\_JKS\_fileFor
example:keytool -export -alias dbclientkey -storepass Password -file /root/keystoreDir/clientcertificate.cer -keystore /root/keystoreDir/clientdbkeystore.jks
4. Copy the certificate of the WebSphere Application
Server to the Oracle server
computer, then import the certificate into Oracle's keystore by running the following
command:keytool -import -v -trustcacerts -alias client\_key\_alias -keypass client\_key\_password -file full\_path\_of\_client\_certificate\_file.cer -keystore full\_path\_of\_server\_JKS\_file -storepass server\_keystore\_passwordFor
example:keytool -import -v -trustcacerts -alias dbclientkey -keypass Password -file D:\serverkeystore\clientcertificate.cer -keystore D:\serverkeystore\serverdbkeystore.jks -storepass Password
5. Copy the certificate of the Oracle server to the WebSphere Application
Server computer, and import the
certificate into the WebSphere Application
Server keystore by running the
following
command:keytool -import -v -trustcacerts -alias server\_key\_alias -keypass server\_key\_password -file full\_path\_of\_server\_certificate -keystore full\_path\_of\_client\_keystore -storepass client\_keystore\_passwordFor
example:keytool -import -v -trustcacerts -alias dbserverkey -keypass Password -file /home/oracle/clientkeysore/servercertificate.cer -keystore /home/oracle/clientKeystore/clientkeystore.jks -storepass Password
    1. On the Oracle server, create an empty wallet from the keystore by using the
orapki
command:orapki wallet create -wallet wallet\_directory -auto\_login -pwd wallet\_passwordFor
example:orapki wallet create -wallet /home/oracle/serverKeystore -auto\_login -pwd walletPassword1!
    2. Convert the JKS file to a wallet file by running the orapki
command:orapki wallet jks\_to\_pkcs12 -wallet wallet\_directory -pwd wallet\_password -keystore full\_path\_of\_server\_keystore -jkspwd server\_keystore\_passwordFor
example:orapki wallet jks\_to\_pkcs12 -wallet /home/oracle/serverKeystore -pwd walletPassword1! -keystore /home/oracle/serverKeystore/serverdbkeystore.jks -jkspwd Password
    3. Ensure that the Oracle wallet has the keys by running the following
command:orapki wallet display -wallet wallet\_directory
    4. Copy the ewallet.p12 file to the WebSphere Application
Server computer, if WebSphere Application
Server and Oracle are installed
on different computers.
- Ensure that the .ora files contain the required contents. On Oracle, the
listener.ora file
contains:LISTENER = (ADDRESS\_LIST= (ADDRESS=(PROTOCOL=tcps)(HOST=servername)(PORT=2484))
) WALLET\_LOCATION=(SOURCE=(METHOD=FILE)(METHOD\_DATA=(DIRECTORY=directory\_of\_the\_wallet)))
SSL\_CLIENT\_AUTHENTICATION=TRUE The SQLNET.ora file
contains:SQLNET.AUTHENTICATION\_SERVICES = (TCPS,NTS)
SSL\_CLIENT\_AUTHENTICATION = TRUE
WALLET\_LOCATION = (SOURCE=  (METHOD=File)  (METHOD\_DATA=   (DIRECTORY=directory\_of\_the\_wallet)))
The tnsname.ora file contains:ORCL =
  (DESCRIPTION =
    (ADDRESS\_LIST =
      (ADDRESS = (PROTOCOL = TCP)(HOST = 0.0.0.0)(PORT = 1521))
          (ADDRESS = (PROTOCOL = TCPS)(HOST = servername)(PORT = 2484))
    )
    (CONNECT\_DATA =
      (SERVICE\_NAME = orcl)
    )
  )Stop and start the listener to apply the changes.
- Add the Oracle certificate to the WebSphere ApplicationServer CellDefaultTrustStore.

1. Log in to the WebSphere Application
Server
Admin Console.
2. Go to Security > SSL certificate and key
management then click Key stores and
certificates > CellDefaultTrustStore and click Signer certificates under Additional
Properties and click the Retrieve from port button.
3. Enter the information for the Oracle server. This information includes hostnames, the configured
SSL port, and an alias, so that you can later identify it in the keystore.
4. Click Retrieve signer information to show the details of the certificate,
and to confirm that the Oracle server is listening on the port.
5. Click OK to save the configuration.
- Set up the data source to use SSL by adding custom properties for the data sources, which youwant to secure with SSL encryption.

1. Log in to the WebSphere Application
Server
Admin Console, and go to
Resources > JDBC > Data
sources.
2. This step uses the BPM Process Server data source, namely TeamWorksDB, but other data sources
follow the same steps. Click BPM Process Server data source under
Additional Properties and click the Custom Properties
link.
3. Click New. Add a property that is named
connectionProperties with a value of
javax.net.ssl.trustStore=wallet\_directory/ewallet.p12;javax.net.ssl.trustStoreType=PKCS12;javax.net.ssl.trustStorePassword=wallet\_password;oracle.net.ssl\_version=1.0
For example, connectionProperties might have a value similar
to:javax.net.ssl.trustStore=/root/keystoreDir/ewallet.p12;javax.net.ssl.trustStoreType=PKCS12;javax.net.ssl.trustStorePassword=walletPassword1!;oracle.net.ssl\_version=1.0
4. Go to the main data source configuration page and scroll to the end of the page where the
connection properties are and update the URL to the SSL value to
jdbc:oracle:thin:@(DESCRIPTION=(ADDRESS=(PROTOCOL=tcps)(HOST=db\_host\_name)(PORT=security\_port\_number))(CONNECT\_DATA=(SERVICE\_NAME=database\_alias)))For
example, the SSL value may look similar to
jdbc:oracle:thin:@(DESCRIPTION=(ADDRESS=(PROTOCOL=TCPS)(HOST=9.110.86.237)(PORT=2484))(CONNECT\_DATA=(SERVICE\_NAME=orcl)))
5. Click OK and then click Save directly to the master
configuration.
6. Click Test connection to test the connection to Oracle server through the
secured port. You might need to click Synchronize before testing the
connection.
7. Repeat for any other data sources you want to secure with SSL encryption.
- If you are using SQLServer, follow the instructions:

1. Configure the SQLServer to use encrypted communications and export the server certificate as
described in Enable Encrypted Connections to the Database Engine.
2. Import the signer certificate for the database into the WebSphere Application
Server Java cacerts truststore,
for example, by running the following
command:WAS\_HOME/java/bin/keytool -import -file full\_path\_of\_certificate\_file -keystore WAS\_HOME/java/jre/lib/security/cacerts -alias alias\_of\_certificate\_file -storepass ts\_password
where WAS\_HOME is the WebSphere Application
Server home directory,
full\_path\_of\_certificate\_file is the full path of the certificate file,
alias\_of\_certificate\_file is the alias of the certificate file, and
ts\_password is the truststore password.
3. Set up the data source to use SSL. Add the following custom properties for each data
source:
Table 1. Data source custom
properties for SQLServer database

Custom property name
Value
Notes

encrypt
true
Specify that the SQL Server uses SSL encryption for communication with the database.

hostNameInCertificate
host\_name\_of\_SQLServer
The hostname used to validate the SSL certificate of the database

trustServerCertificate
false
JDBC Driver to validate the SSL certificate of the database.

trustStore
WAS\_HOME/java/jre/lib/security/cacerts
The fully qualified path to the certificate truststore file

trustStorePassword
ts\_password
The password for the truststore

trustStoreType
JKS
The certificate type of the truststore is Java KeyStore
4. Test the data source connection to the SQLServer.
- If you are using Db2, perform the following actions:

1. To create a keystore with IBM Global Security Kit (GSKit), you need to add a root CA certificate
into your keystore. To do this, see Creating a keystore with GSKit. You can also add self-sign certificates for servers in your
network. See Digital certificates.
2. To configure TLS support for Db2 see TLS configuration of Db2.
3 Import the signer certificate for the database into the WebSphere ApplicationServer truststore. Before the JDBC driver can use SSL tocommunicate with the database, the truststore that it uses requires the database's signercertificate. To get the signer certificate into the appropriate truststores:
    1. Go to Security > SSL certificate and key management and click Key stores and certificates under Related
Items.
    2. Click CellDefaultTrustStore to go to the application server's default
truststore.
    3. Click Signer certificates under Additional
properties.
    4. On the Signer Certificates page, click Retrieve from
port to retrieve the Db2's signer certificate.
    5. On the Retrieve from port page, enter the following values:
Table 2. 

Field
Value
Notes

Host
hostname
Host where Db2 is running.

Port
50443 
Port on which Db2 is listening for SSL communication.

Alias
MyRootCA or myselfsigned;
Keep this value consistent with the certification label used to create a
keystore with GSKit in the first step of switching the data sources to SSL for Db2.
    6. Click Retrieve signer information.
    7. Click Save.
4 Set up the data source to use SSL:

1. Go to Resources > JDBC > Data
sources and click the data source to update to use SSL. For example, the
data source might be jdbc/TeamWorksDB.
2. Under the Additional Properties section, click the Custom
properties link, find the sslConnection property, change the value to
true, and save the changes. If the sslConnection property is not
already in the list of custom properties, add the sslConnection custom property of
type Boolean to the data source and set the value to true. To add this custom property, go to the
data source page and click Custom properties in the Additional
Properties section. On the Custom Properties page, click
New to create the sslConnection property.
3. Go to the data source configuration page and update the port number in the common and required
data source properties sections. This value is the same as the ssl\_svcename value
that was set in the step to configure TLS support for Db2.
4. Repeat steps 1-3 to configure other data sources that you want to secure with SSL
encryption.
5. Synchronize and restart your node agents and application servers.
6. Test the connection. This ensures that your configurations are applied.
- If you are using PostgreSQL , perform the following actions:

1. To configure the PostgreSQL database to use encrypted
communications and export the server certificate, see Using
SSL. If your PostgreSQL database server uses
certificate authentication, make sure that the database server is configured as described in Using Client Certificates. Create the client certificate for the Business Automation Workflow server. The subject
name 'CN' must be the same value as the database username that is used to connect to the Business Automation Workflow databases. In other
words, it must be the same value as the one you specified as user of database authentication alias
in bpmconfig.properties.
For example, if you want to use "workflowadmin"
as the database user to connect Business Automation Workflow databases, run the
commands to create postgresql.key, postgresql.crt for
Business Automation Workflow server and
convert postgresql.key to pk8 format.
To create postgresql.csr
openssl req -new -nodes -text -config /etc/pki/tls/openssl.cnf -out postgresql.csr -keyout postgresql.key -subj "/CN=workflowadmin".
To create postgresql.crt (a client certificate signed by the root
certificate authority)
openssl x509 -req -in postgresql.csr -text -days 365 -CA root.crt -CAkey root.key -CAcreateserial -out postgresql.crt
To convert PEM key to DER
format.
openssl pkcs8 -topk8 -inform PEM -in postgresql.key -outform DER -out postgresql.pk8 -v1 PBE-MD5-DES -nocrypt
2. Import the server certificate for the database into the WebSphere Application
Server Java cacerts truststore,
for example, by running the following commands:
openssl x509 -in server.crt -out server.crt.der -outform der WAS\_HOME/java/bin/keytool -import -file server.crt.der -keystore WAS\_HOME/java/jre/lib/security/cacerts -alias postgresql -storepass ts\_password
If
your PostgreSQL database
server uses certificate authentication, there is one more command to import the certificate to
/jre/lib/security/cacerts
keystore
WAS\_HOME/java/bin/keytool -import -file root.crt -keystore WAS\_HOME\java\jre\lib\security\cacerts -alias psqlsslWhere
WAS\_HOME is the WebSphere Application
Server home directory,
server.crt is the certificate file that is generated from the PostgreSQL database, and
ts\_password is the truststore password.
If your PostgreSQL database server uses
certificate authentication, copy postgresql.crt,
postgresql.pk8 and root.crt into IBM BPM server machine.
3 Set up the data source to use SSL. Change the following custom properties for each datasource:Table 3. Data source custom properties for PostgreSQL database Custom property name Value URL If your PostgreSQL database server uses certificate authentication for all data sources that Business Automation Workflow DE has, then changetheir JDBC URL tojdbc:postgresql://host:port/database?sslmode=verify-full&sslrootcert=C:\root.crt&sslcert=C:\postgresql.crt&sslkey=C:\postgresql.pk8 For more information on this sslmode , see SSLConnection parameters .

| Custom property name    | Value                                                                                                                                                                                           |
|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| URL                     | jdbc:postgresql://host:port/database?sslmode=verify-full or jdbc:postgresql://host:port/database?sslmode=verify-full&sslrootcert=C:\root.crt&sslcert=C:\postgresql.crt&sslkey=C:\postgresql.pk8 |

```
jdbc:postgresql://host:port/database?sslmode=verify-full&sslrootcert=C:\root.crt&sslcert=C:\postgresql.crt&sslkey=C:\postgresql.pk8
```

4. Test the data source connection to PostgreSQL.
- Switch the distribution and consistency services (DCS) transport link to SSL. You caneither configure by using the wsadmin commands or through the UI.

- To configure by using the wsadmin commands, run the following commands,replacing the PCCell1 WebSphere Application Server Deployment Manager (Dmgr) andserver name with your own Dmgr and server name.
    1. To list the distribution and consistency services, run the command:
AdminTask.listChains('(cells/PCCell1/nodes/Dmgr/servers/dmgr|server.xml#TransportChannelService\_1)', '[-acceptorFilter DCSInboundChannel]')
    2. To configure the DCS transport link to SSL, run the
command:AdminConfig.modify('(cells/PCCell1/coregroups/DefaultCoreGroup|coregroup.xml#builtin\_CoreGroup\_1080665362339)', '[[transportType "CHANNEL\_FRAMEWORK"] [numCoordinators "1"] [channelChainName "DCS-Secure"] [description "Default Core Group. The default core group cannot be deleted."] [transportMemorySize "100"]]')
- To configure by using the UI, complete the following steps.

1. In the WebSphere Application
Server
administrative console, click Servers > Core Groups > Core group settings.
2. Click DefaultCoreGroup.
3. Select DCS-Secure from the Channel framework
pull-down menu.
4. Save your changes and restart the server.
- Disable unencrypted ports. You can either configure by using the wsadmin commands or through the UI.

- To configure by using the wsadmin commands, run the following commands,replacing the PCCell1 Dmgr and server name with your own Dmgr and server name.
    1. To see the list of ports, run the
command:AdminTask.listChains('(cells/PCCell1/nodes/Dmgr/servers/dmgr|server.xml#TransportChannelService\_1)', '[-endPointFilter DCS\_UNICAST\_ADDRESS]')
    2. To disable the unencrypted ports, run the
command:AdminConfig.modify('(cells/PCCell1/nodes/Dmgr/servers/dmgr|server.xml#Chain\_3)', '[[name "DCS"] [enable "false"]]')
- To configure by using the UI, complete the following steps.

1. In the WebSphere Application Server administrative console, click System administration > Deployment
manager > Configuration > Ports.
2. Click each instance of View associated transports.
3 Disable each transport chain that shows Enabled in the SSLEnabled column.
    1. Click the name of the transport chain and clear the Enabled
checkbox.
    2. Click OK.
    3. Click System administration > Nodes.
    4. Click each node and select the Local Topology tab.
    5. Expand the node name and expand Servers.
    6. Click the managed node and select the Configuration tab.
    7. Click Ports and click each instance of View associated
transports.
    8. Disable each Transport Chain that shows Enabled in the SSL
Enabled column.
    9. Click Save directly to master configuration.
    10. Stop the nodes, node agents, and deployment manager.
    11. Restart the deployment manager.
    12. Synchronize the configuration changes across each of the federated nodes by clicking
System administration > Nodes. Select all the nodes and then click Full
Resynchronize.
    13. Restart the node agents and nodes.