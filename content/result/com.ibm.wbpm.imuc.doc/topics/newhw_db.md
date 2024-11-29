# Dropping the messaging
engine tables

## Procedure

1 Optional: If you want to move your Business Automation Workflow databases,use your database utility to back up each of your source databasesand restore them to another database instance or schema. Youmust make sure that they match the database information that you specifiedwhen you updated the BPMConfig properties file, including the followingproperties:
    - hostname
    - port
    - database name
    - schema
    - user
    - password
2. Manually
drop the existing messaging engine tables in the
messaging database of your new deployment environment before you start
the deployment environment.  Tip:  The messaging
engine table names use the SIB prefix.