# Preparing a PostgreSQL database for the User Management Services datasource

## Procedure

1. Using psql create a database and grant your database user privileges to
create resources:
CREATE DATABASE umsdb OWNER db\_user ENCODING UTF8;
GRANT ALL PRIVILEGES ON DATABASE umsdb to db\_user;
Where
umsdb is the name of the database and db\_user
is the database user.
2. Make a note of your values for the following configuration parameters that you will need later
to add to the datasource\_configuration section of the custom resource:

  datasource\_configuration:
    dc\_ums\_datasource: # credentials are read from ums\_configuration.admin\_secret\_name
      # oauth database config
      dc\_ums\_oauth\_type: postgresql
      dc\_ums\_oauth\_host: host\_name
      dc\_ums\_oauth\_port: 5432
      dc\_ums\_oauth\_name: umsdb
      dc\_ums\_oauth\_driverfiles: postgresql-42.2.14.jar
      # teamserver database config
      dc\_ums\_teamserver\_type: postgresql
      dc\_ums\_teamserver\_host: host\_name
      dc\_ums\_teamserver\_port: 5432
      dc\_ums\_teamserver\_name: umsdb
      dc\_ums\_teamserver\_driverfiles: postgresql-42.2.14.jar

Important: If you configured PostgreSQL for high availability following the Patroni
architecture with an HAproxy for load balancing, make sure that you specify the host name and port
number of the HAproxy as the values for dc\_ums\_oauth\_host and
dc\_ums\_teamserver\_host and dc\_ums\_oauth\_port and
dc\_ums\_teamserver\_port.