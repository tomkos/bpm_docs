# Configuring secure access to DB2 databases in federated environments

## Before you begin

- SSL is enabled for Process Federation Server.
- SSL is enabled for the DB2 server and an SSL certified authority
(CA) certificate is available.
- In the properties.db2.jcc file on Process Federation Server,
ensure that the sslConnection option is set to true.

## Procedure

1. Import the DB2 database server SSL CA certificate into
the Process Federation Server truststore
with the keytool utility. On Process Federation Server,
run the following command:keytool.exe -trustcacerts -alias custom\_alias -file path\_to\_db2\_cert -keystore path\_to\_keystore

Enter keystore password:
Owner: OU=Org\_Unit, O=Org, C=Country
Issuer: OU=Org\_Unit, O=Org, C=Country

   ...

Trust this certificate? [no]:  yes
Certificate was added to keystore
2. Verify that the certificate is available on the server
by running the following command: keytool.exe -list -v -keystore path\_to\_keystore; -storepass keystore\_password
3 Enable SSL communication between Process Federation Server andthe DB2 database server by adding the DB2 SSL port number that isspecified in the properties.db2.jcc file forthe DB2 JDBC driver to the server.xml file:
    1. Open the server.xml configuration file for
editing.
By default, the configuration file is in the
pfs\_install\_root/usr/servers/server\_name directory on
Process Federation Server.
    2. Update the portNumber property
in the dataSource element for the DB2 JDBC driver
to point to the DB2 SSL port. The following code snippet
is an example of a configured portNumber property
for a DB2 JDBC driver:<dataSource
   ...
   ... 
   <properties.db2.jcc serverName="localhost" databaseName="BPMDB" 
      user="db2admin" password="password" 
      portNumber="DB2\_SSL\_port" sslConnection="true"
    </properties.db2.jcc>
</dataSource>

## Results