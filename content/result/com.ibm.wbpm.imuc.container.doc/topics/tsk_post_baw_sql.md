# Configuring custom Liberty data sources for Business Automation Workflow on
containers

## Procedure

1. Add the required files, such as the JDBC driver, to the Workflow server pod, by using the
filestore persistent volume claim (PVC) that is mounted at /opt/ibm/bawfile.
For more information, see Accessing files for applications and
configurations.
 For example, run the following command to copy your JDBC driver to the Workflow server
location /opt/ibm/bawfile, where jdbcdriver.file is the
file you want to copy and workflow-server-pod is the name of one of your Workflow
pods.oc cp jdbcdriver.file workflow-server-pod:/opt/ibm/bawfile/The files are
stored in the persistent volume (PV) related to the PVC and are kept between restarts.
2. Create a valid XML snippet with the Liberty datasource settings that you want, starting
from the <server> element.  The file path in the configuration
must match the appropriate container path. For more information, see Configuring relational database connectivity in Liberty and
Administering Liberty manually. This example
uses a PostgreSQL database.

      <server>
        <dataSource id="PostgresSQLDataSource" jndiName="jdbc/postgres">
          <jdbcDriver libraryRef="PostgresLib" />
          <properties.postgresql databaseName="customdb" serverName="dbserver.mydomain.com"
          portNumber="5432" user="username" password="password"/>
        </dataSource>

        <library id="PostgresLib">
          <file name="/opt/ibm/bawfile/postgresql-42.6.2.jar"/>
        </library>
      </server>
3. To customize Liberty with your XML snippet, follow the instructions in
Customizing Business Automation Workflow properties.