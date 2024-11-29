# Loading the database with system information
in a network deployment environment

## Procedure

Run the bootstrapProcessServerData command
successfully at least once for each deployment environment before you start using the
environment:

1 If you deferred DB table creation or you work with a SQL Serverdatabase that uses Windows authentication(sqlServerWinAuth =true ), manually run thebootstrapProcessServerData command after the database tables arecreated. Note: When you created the deployment environment either by setting thebpm.de.deferSchemaCreation parameter to false for theBPMConfig command or by enabling Create Tables in theDeployment Environment wizard, the bootstrapProcessServerData command is runautomatically. Note: For Windows, ensure that the command prompt is opened using Run as anAdministrator .
    - For Linux and UNIX, run DMgr
profile\_root/bin/bootstrapProcessServerData.sh -clusterName
cluster\_name, where cluster\_name is the deployment
environment's application cluster for a three-cluster setup and is case sensitive.
    - For Windows, run DMgr profile\_root/bin/bootstrapProcessServerData.bat
-clusterName cluster\_name, where cluster\_name is the
deployment environment's application cluster for a three-cluster setup and is case sensitive.
2. Check the bootstrapProcessServerData log for errors. If there
are issues, correct them and rerun the bootstrapProcessServerData command until
it is successful.
The log file is located at
DMgr
profile\_root/logs/bootstrapProcesServerData.clusterName.log.

## Results

You have successfully loaded the database
with system information for a deployment environment.