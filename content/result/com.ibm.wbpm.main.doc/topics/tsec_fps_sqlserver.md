# Configuring secure access to SQL Server databases in federated environments

## Before you begin

- SSL is enabled on Process Federation Server.
- SSL is enabled on the SQL Server database and an SSL certificate
is available.
- Ensure that in the properties.microsoft.sqlserver file
on Process Federation Server,
the Force Encryption option is set to yes,
and that the file contains the settings for the SSL certificate and
the truststore for the SQL Server database.

## Procedure

1. Import the SQL Server SSL certificate into the Process Federation Server truststore.
On Process Federation Server,
run the following command:keytool -import -keystore path\_to\_keystore 
        -storepass your\_password -keypass your\_password 
        -alias custom\_alias -file certificate.cer

Enter keystore password:
Owner: OU=Org\_Unit, O=Org, C=Country
Issuer: OU=Org\_Unit, O=Org, C=Country

   ...

Trust this certificate? [no]:  yes
Certificate was added to keystore
2. Verify that the certificate is available on the server
by running the following command: keytool -list -v -keystore path\_to\_keystore; -storepass keystore\_password
3 Enable SSL communication between Process Federation Server andSQL Server databases. Add the SQL Server SSL port number,certificate, truststore, and encryption settings that are specifiedin the properties.microsoft.sqlserver file forthe SQL Server driver to the server.xml file:

Add the SQL Server SSL port number,
certificate, truststore, and encryption settings that are specified
in the properties.microsoft.sqlserver file for
the SQL Server driver to the server.xml file:

    1. Open the server.xml configuration file for
editing.
By default, the configuration file is in the
pfs\_install\_root/usr/servers/server\_name directory on
Process Federation Server.
    2. Update the attributes for the properties.microsoft.sqlserver property
with the information from the properties.microsoft.sqlserver file.
The following code snippet is an example of a configured properties.microsoft.sqlserver property
for an SQL Server JDBC driver. The attributes that are relevant for
SSL configuration are highlighted:<dataSource
   ...
   ... 
   <properties.microsoft.sqlserver serverName="localhost" encrypt="true"
       databaseName="BPMDB" instanceName="MSSQLSERVER"
       password="password" trustStorePassword="password" 
       hostNameInCertificate="mssql.mycompany.com" 
       trustStore="pfs\_install\_root/usr/servers/server\_name/resources/security/sqltrust.p12"
       portNumber="SQL\_SSL\_port" 
       ...
       ... 
    </properties.microsoft.sqlserver>
</dataSource>

## Results