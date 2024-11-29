# User ID or schema name privileges

## Scenario for a single user ID or schema name privileges

If
you chose a default installation for your databases, IBM Business Automation Workflow requires
a minimum of one user ID or schema name that can create tables and
to select, insert, update, and delete rows in those tables. You can
use the Profile Management Tool or the installer to create your databases.

| Database tables                | Default database name with DB2   | User ID or schema name                                                       |
|--------------------------------|----------------------------------|------------------------------------------------------------------------------|
| Common database tables         | CMNDB                            | IBM Business Automation Workflow provides a user ID during installation.     |
| Business Process Choreographer | BPEDB                            | IBM Business Automation Workflow provides a user ID during installation.     |
| Messaging tables               | MEDB                             | IBM Business Automation Workflow provides a schema name during installation. |

If your database design has different properties, you
might need multiple user ID and schema name privileges. The following
scenarios show you how to apply the configuration to achieve your
design. Even if your particular design is not in the provided scenarios,
you can adapt some of the ideas to implement your particular design.

## Scenario 1 for multiple user ID or schema name privileges

- Schema name: dog
- Schema name for SCA.SYSTEM ME : dogSYS
- Schema name for SCA.APP ME: dogAPP
- Schema name for Event ME: dogEvent
- Schema name for BPC ME: dogBPC
- User ID to create schemas: dog
- User ID to select, insert, update, and delete schemas: dog

| Database tables                       | Database name with DB2                                                                                                                                                          | Schema name                                                                                          | User ID to create tables                                                                       | User ID to select, insert, update, and delete rows                                                                                                                              |
|---------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Common database tables                | You supply this value in the  Installation wizard Profile Management Tool Silent install Silent profile creation                                                                | This schema name is the same as the user ID that is used to select, insert, update, and delete rows. | This value is the same as the user ID that is used to select, insert, update, and delete rows. | You supply this value in the  Installation wizard Profile Management Tool Silent install Silent profile creation                                                                |
| Business Process Choreographer tables | You supply this value twice: In table creation scripts  While configuring a deployment target using one of the following tools: Deployment environment wizard BPMConfig command | This schema name is the same as the user ID that is used to select, insert, update, and delete rows. | This value is the same as the user ID that is used to select, insert, update, and delete rows. | You supply this value twice: In table creation scripts  While configuring a deployment target using one of the following tools: Deployment environment wizard BPMConfig command |

## Scenario 2 for multiple user ID or schema name privileges

- Schema name: snow
- Schema name for SCA.SYSTEM ME: snowSYS
- Schema name for SCA.APP ME: snowAPP
- Schema name for Event ME: snowEvent
- Schema name for BPC ME: snowBPC
- User ID to create the schemas: rock
- User ID to select, insert, update, and delete schemas: snow

| Database tables                       | Database name with DB2                                                                                                                                                                                                                                                                                                                                                                                                                 | Schema name                                                                                               | User ID to create tables                                                                    | User ID to select, insert, update, and delete rows                                                                                                                     |
|---------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Common database tables                | You supply this value twice: In table creation scripts During the IBM Business Automation Workflow  configuration with one of the following tools: Administrative console Installation wizard Profile Management Tool Silent install Silent profile creation     Restriction: If you run the installer first, then you supply the value once because the generated scripts already contain the correct schema name and user ID values. | The table creation scripts need to be modified with the schema name that allows reading and writing rows. | The table creation script needs to be modified with the user ID that allows table creation. | You supply the user ID during profile creation through one of the following tools:  Installation wizard Profile Management Tool Silent install Silent profile creation |
| Business Process Choreographer tables | You supply this value twice: In table creation scripts  While configuring a deployment target using one of the following tools: Deployment environment wizard BPMConfig command                                                                                                                                                                                                                                                        | The table creation scripts need to be modified with the schema name that allows reading and writing rows. | The table creation script needs to be modified with the user ID that allows table creation. | You supply the user ID during profile creation through one of the following tools:  Installation wizard Profile Management Tool Silent install Silent profile creation |

## Scenario 3 for multiple user ID or schema name privileges

- Schema name: waterCom
- Schema name for common tables: waterCom
- Schema name for SCA.SYSTEM ME: waterSYSME
- Schema name for SCA.APP ME: waterAPPME
- Schema name for Event ME: waterEventME
- Schema name for BPC ME: waterBPCME
- Schema name for BPC and HTM tables: waterBPC
- Schema name for ESBMessaging tables: waterESB
- User ID to create schemas: milk
- User ID to select, insert, update, and delete schemas: 
Schema name
User ID to select, insert, update, and delete schemas

waterCom 
waterCom 

waterSYSME
waterSYSME

waterAPPME 
waterAPPME 

waterEventME
waterEventME

waterBPCME
waterBPCME

waterBPC 
waterBPC 

waterESB 
waterESB

| Database tables                       | Database name with DB2                                                                                                                                                          | Schema name                                                                                                                | User ID to create tables                                                                       | User ID to select, insert, update, and delete rows                                                                                                                              |
|---------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Common database tables                | You supply this value in the  Installation wizard Profile Management Tool Silent install Silent profile creation                                                                | This schema name is the same as the user ID that is used to select, insert, update, and delete rows.                       | This value is the same as the user ID that is used to select, insert, update, and delete rows. | You supply the user ID during profile creation through one of the following tools:  Installation wizard Profile Management Tool Silent install Silent profile creation          |
| Business Process Choreographer tables | You supply this value twice: In table creation scripts  While configuring a deployment target using one of the following tools: Deployment environment wizard BPMConfig command | The table creation scripts need to be modified with a schema name that is used to select, insert, update, and delete rows. | This value is the same as the user ID that is used to select, insert, update, and delete rows. | You supply this value twice: In table creation scripts  While configuring a deployment target using one of the following tools: Deployment environment wizard BPMConfig command |
| Messaging tables                      | You supply this value with the definition of each messaging engine.                                                                                                             | The table creation scripts must include the schema name that is used to select, insert, update, and delete rows.           | This value is the same as the user ID that is used to select, insert, update, and delete rows. | You supply this value during the creation of the messaging engine. Select the Create Table option during the messaging engine configuration.                                    |