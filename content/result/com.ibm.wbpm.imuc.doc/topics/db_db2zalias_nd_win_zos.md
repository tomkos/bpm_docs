# Configuring the DB2 command
line processor

## Before you begin

Ensure that a properties file,
for example, clp.properties, exists for the DB2 command line processor. If required,
you can create your own properties file by using the sample properties
file that is available in the directory where the command line processor
is installed. For more information, see your DB2 for z/OS documentation.

## Procedure

Complete the following configuration
steps in the z/OS UNIX System Services environment from which
the createDatabase.sh script will be run:

1 Configure the DB2 command line processor for each user ID thatwill work with DB2 for z/OS from the command line. Youcan update the user profiles as follows: You can use the following syntax to add the required entriesto the .profile file of the user ID running thecommand:export CLPHOME=clp\_install\_dir export CLASSPATH=$CLASSPATH:$CLPHOME/lib/clp.jarexport CLPPROPERTIESFILE=clp\_properties\_file\_path alias db2="java -Ddb2.jcc.propertiesFile=/file\_path /DB2JccConfiguration.properties com.ibm.db2.clp.db2" For example:export CLPHOME=/shared/db2910\_baseexport CLASSPATH=$CLASSPATH:$CLPHOME/lib/clp.jarexport CLPPROPERTIESFILE=/wasv85config/clp.propertiesalias db2="java -Ddb2.jcc.propertiesFile=/wasv85config/DB2JccConfiguration.properties com.ibm.db2.clp.db2"
    - Modify the CLASSPATH environment variable to include the clp.jar file.
    - Use the CLPPROPERTIESFILE environment variable to define the fully
qualified name of the properties file for the command line processor.
    - Define the db2 command as an alias for the
command that starts the command line processor.
    - Specify the DB2JccConfiguration.properties file
that defines the JDBC properties to be applied to the command line
processor.

```
export CLPHOME=clp\_install\_dir
export CLASSPATH=$CLASSPATH:$CLPHOME/lib/clp.jar
export CLPPROPERTIESFILE=clp\_properties\_file\_path
alias db2="java -Ddb2.jcc.propertiesFile=/file\_path/DB2JccConfiguration.properties com.ibm.db2.clp.db2"
```

```
export CLPHOME=/shared/db2910\_base
export CLASSPATH=$CLASSPATH:$CLPHOME/lib/clp.jar
export CLPPROPERTIESFILE=/wasv85config/clp.properties
alias db2="java -Ddb2.jcc.propertiesFile=/wasv85config/DB2JccConfiguration.properties com.ibm.db2.clp.db2"
```

2 In the properties file for thecommand line processor, define alias names that can be used to connectto the DB2 for z/OS server. An alias name definitioncan include the following entities: You can add the required alias name entries to the propertiesfile by using the following syntax:DB2ALIASNAME =URL ,user\_ID ,password Forexample:DSNXWBD=localhost:9446/DSNXWBD,SYSADM1,SYSPWRD1 Tip: When you define a DB2ALIASNAME valuein the properties file, ensure that the correct connection detailsare specified to avoid connecting to the wrong database and inadvertentlyoverwriting its contents.

- A URL that specifies the domain name or IP address of the database
server, the port on which the server listens, and the DB2 location name that was defined during installation.
The URL can take the form: server:port/database.
The port is optional, and the DB2 location
name must be specified in uppercase characters.
- A user ID and an associated password that can be used to connect
to the DB2 server. This user
ID should correspond to the user ID that either the DB2 system administrator (with SYSADM authority)
or the WebSphere® administrator
(with DBADM authority) uses to run the createDatabase.sh script.

```
DB2ALIASNAME=URL,user\_ID,password
```

```
DSNXWBD=localhost:9446/DSNXWBD,SYSADM1,SYSPWRD1
```

3. Configure the DB2 DBACRVW subsystem parameter to enable user
IDs with DBADM authority on a database to perform the following tasks
for other user IDs: create views on tables in the database, create
aliases for tables, and create materialized query tables.  You
can use the installation Command List (CLIST) to access the DSNTIPP
ISPF panel and update the DBADM CREATE AUTH field to set DB2 ZPARM DBACRVW=YES.

## What to do next

Create and configure the product
databases.

## Related information

- Creating Db2 for z/OS database objects using the createDatabase.sh script in a network deployment environment on Windows
- Creating Db2 for z/OS database objects using the Db2 command line processor in a network deployment environment on Windows
- createDatabase.sh script