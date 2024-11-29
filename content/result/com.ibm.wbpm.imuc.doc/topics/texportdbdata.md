# Using the BPMConfig command to export database information
for performance analysis

## About this task

When you run the BPMConfig command
to export database information, queries are run against the databases
and information is generated for export. If you are using SQL Server,
some of the queries require SQL Server 2008 R2 SP2 (or higher).

## Procedure

To use the BPMConfig command to export
database information for performance analysis:

1. Ensure that your local user account has sufficient privileges
to run the BPMConfig command with the –export parameter.
Information about the BPMConfig command is found
in the topic BPMConfig command-line utility.
2 By default, the database user and password for ProcessServer are used to run queries against various Workflow Server andPDW database system objects. Ensure that the database user has sufficientprivileges to run queries against these databases. Alternatively,you can specify a different database user that has sufficient privilegesby completing the following steps:
    1. In the file system, navigate to the following sample
input file (which will be passed to the BPMConfig command):
install\_root/BPM/samples/config/performanceanalysis/PerformanceAnalysis.properties
    2. Open the PerformanceAnalysis.properties input
file in a text editor. The input file contains properties
that are similar to the ones shown in the following example:processServerDb.user=
processServerDb.password=
pdwDb.user=
pdwDb.password=
    3. For the processServerDb.user and processServerDb.password properties,
specify a user and password for the Workflow Server database.
    4. For the pdwDb.user and pdwDb.password properties,
specify a user and password for the PDW database.
    5. Ensure that you can connect to the databases using the
specified database users and passwords, then save and close the PerformanceAnalysis.properties input
file.
3. Run the following command (where ProfileName is
the name of a deployment manager profile or stand-alone profile and inputFile.properties is
the full path to the optional input file): BPMConfig.bat -export -profile ProfileName [-de deName] -db [inputFile.properties] [-outputDir outputDir]
BPMConfig.sh -export -profile ProfileName -de deName -db [inputFile.properties] [-outputDir outputDir]For
example:
BPMConfig.bat -export -profile DmgrProfile -de De1 -db E:\performanceAnalysis.properties -outputDir E:\output
BPMConfig.sh -export -profile DmgrProfile -de De1 -db /home/user/performanceAnalysis.properties -outputDir /home/user/outputNote: If
there is only one deployment environment in the WebSphere cell, you
can omit the -de option.
When you run the command using this syntax, the output is returned to the deployment manager
machine. If you specify the optional -outputDir option and an output directory
name, the output files are generated under the specified output directory. If you do not specify the
-outputDir parameter, the output files are generated under the default output
directory install\_root/temp/deName.
Note: If you intend to run the command more than once because
you have more than one deployment environment, remember to specify
different output directory names whenever you use the -outputDir parameter.
4. After you run the command, switch to the output directory,
which is either the output directory that you specified with the -outputDir parameter
or the default output directory (if you did not specify the -outputDir parameter).
The output directory contains processServerDb.csv and pdwDb.csv files,
which contain the database information that was exported from the
Workflow Server and PDW databases.
5. Open the two output files and read and analyze the database
information.