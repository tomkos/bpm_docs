# Preparing customized versions of JDBC drivers for Business Automation Workflow on
containers

## Procedure

1. Prepare your JDBC files and organize them into the following folder structure.

Add JDBC drivers for Business Automation Workflow and all of the other
patterns in your deployment that need them. For more information about compatible JDBC drivers, see
Db2 JDBC information, Oracle JDBC information, SQL Server JDBC information, and PostgreSQL JDBC information. 
The following .jar files are examples.

/jdbc/db2/db2jcc4.jar
/jdbc/db2/db2jcc\_license\_cu.jar
/jdbc/oracle/ojdbc8.jar
/jdbc/sqlserver/mssql-jdbc-8.2.2.jre11.jar
/jdbc/postgresql/postgresql-42.6.0.jar 
The Db2 license file is included in all Db2 server editions and you must take the license file
from the Db2 Activation CD or download it from Passport Advantage. For more information, see Db2 license files.
2. Compress them into a file (.zip, .tar, .tar.gz, .tar.bz2, .tar.xz) by running the
following command.  
zip -r $localpath\_to\_zip/jdbc.zip jdbc 
The command generates the path and file name:
$localpath\_to\_zip/jdbc.zip.
3. Use the HTTPd docker image to start a container with the name
http. 
docker run -dit --name http -p 8888:80 httpd
4. Open the container by using the URL http://hostname:8888.
 The hostname is where you run the HTTPd docker image. It displays the following message:
"it works!"
5. Copy the compressed file to the docker container by running the following command. 
docker cp $localpath\_to\_zip/jdbc.zip http:/usr/local/apache2/htdocs
6. The operator downloads the compressed file when you set the value of the
sc\_drivers\_url parameter in the custom resource (CR) to the URL of the file in
the HTTPd container: http://hostname:8888/jdbc.zip. 
You set the values of the CR when you create an instance of the production deployment.

shared\_configuration:
  sc\_drivers\_url: http://hostname:8888/jdbc.zip