# Configuring secure access to Oracle databases in federated environments

## Before you begin

- SSL is enabled for Process Federation Server.
- SSL is enabled for the Oracle server and an SSL certificate is
available.

## Procedure

1. Import the Oracle database server SSL certificate into
the Process Federation Server truststore.
On Process Federation Server,
run the following command:keytool -import -keystore path\_to\_keystore 
        -storepass your\_password -keypass your\_password 
        -alias custom\_alias -file certificate.crt

Enter keystore password:
Owner: OU=Org\_Unit, O=Org, C=Country
Issuer: OU=Org\_Unit, O=Org, C=Country

   ...

Trust this certificate? [no]:  yes
Certificate was added to keystore
2. Verify that the certificate is available on the server
by running the following command: keytool -list -v -keystore path\_to\_keystore; -storepass keystore\_password
3 Enable SSL communication between Process Federation Server andthe Oracle database server by adding the Oracle SSL port number thatis specified in the properties.oracle file forthe Oracle JDBC driver to the server.xml file:
    1. Open the server.xml configuration file for
editing.
By default, the configuration file is in the
pfs\_install\_root/usr/servers/server\_name directory on
Process Federation Server.
    2. Update the portNumber property
in the dataSource element for the Oracle JDBC driver
to point to the Oracle SSL port. The following code
snippet is an example of a configured portNumber property
for an Oracle JDBC driver:<dataSource 
   ...
   ... 
   <properties.oracle serverName="localhost" databaseName="BPMDB" 
      user="oracle\_admin" password="password" 
      portNumber="Oracle\_SSL\_port" serviceName="service\_name"
    </properties.oracle>
</dataSource>

## Results