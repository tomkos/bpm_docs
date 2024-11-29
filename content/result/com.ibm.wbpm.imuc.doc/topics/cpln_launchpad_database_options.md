# Database server setup options

## Using an existing database or installing a new database

You can choose to have the installation process include automatically installing an instance of
Db2®. Choose this option if you do
not have an existing or planned supported database server you intend to use to store content from
Workflow Center or Workflow Server. If you are installing a test or
proof-of-concept environment, you would likely choose to have a new Db2 installed automatically, unless one
already exists on the system. You must be installing as an administrator to have Db2 installed automatically.

## Applying Windows authentication

Enable this option if you want to use an existing Windows user ID and password for SQL Server authentication rather than providing a user ID and password in the database options. 
For more information, see the SQL Server documentation: http://technet.microsoft.com/en-us/library/ms144284.aspx.

## Specifying the Oracle instance name

If you are using an Oracle database server, provide the name of the Oracle instance to be
configured. You can use a single instance of Oracle for configuring Business Automation Workflow. The Oracle instance must exist and be available
for access. Consult the Oracle documentation to create an Oracle instance. If you use a single
Oracle instance, make sure that you use different user IDs for the three different Business Automation Workflow databases.