# CWMCO

- CWMCO6101E

The object could not be written back: java.lang.UnsupportedOperationException.
- CWMCO0001I

Usage BPMGenerateUpgradeSchemaScripts [options] -propertiesFile <propertiesFile>
- CWMCO0002I

Found component 0 is configured for the 1 database.
- CWMCO0003I

Do you want to generate scripts? Y/N
- CWMCO0004I

Enter the value for 0.
- CWMCO0005I

Scripts have been generated in the 0 directory.
- CWMCO0006I

The logger did not initialize the 0 log file and received the following exception: 1.
- CWMCO0007I

The command BPMGenerateUpgradeSchemaScripts completed successfully.
- CWMCO0008I

Information is being logged to the 0 file.
- CWMCO0201E

The 0 file cannot be found.
- CWMCO0202E

An exception occurred during load the properties 0.
- CWMCO0203E

The required property 0 cannot be found in properties file 1.
- CWMCO0204E

The property 0 is empty.
- CWMCO0205E

The version 0 specified for 1 is invalid. Please specify the correct value of version number in format <w>.<x>.<y>.<z>, E.g. 7.5.1.0.
- CWMCO0206W

Cannot find database configured for component 0,there would be no database upgrade schema generated for the component.
- CWMCO0207E

The BPMGenerateUpgradeSchemaScripts command could not complete successfully.
- CWMCO1001I

Start to take snapshot of the source environment.
- CWMCO1002I

All steps of the snapshot completed successfully.
- CWMCO1003I

Start to migrate snapshot to the target environment.
- CWMCO1004I

All steps of the migration completed successfully.
- CWMCO1005I

Usage 0 [options]
- CWMCO1006E

The input parameter is incorrect.
- CWMCO1007E

Failed to read configuration file:0. Check the path of the configuration file.
- CWMCO1008E

The JMX connection to the server did not initiate. The following exception occurred : 0.
- CWMCO1009E

The snapshot root directory could not be located. The following exception occurred: 0. Check the migration log for details. Log location:1.
- CWMCO1010E

The snapshot directory does not exist. Make sure you specified the correct snapshot folder that you extracted from the source environment.
- CWMCO1011E

An exception occurred while the snapshot of the source environment was being taken. Check the migration log for details. Log location:0.
- CWMCO1012E

An exception occurred during the extraction of database configuration information from the source environment. Check the migration log for details. Log location:0.
- CWMCO1013E

An exception occurred during the loading of properties from the server configuration repository. Check the migration log for details. Log location:0.
- CWMCO1014I

Start to perform configuration synchronization of all custom nodes with the cell repository.
- CWMCO1015I

Configuration synchronization of all custom nodes has completed.
- CWMCO1016E

Custom nodes were not synchronized with the cell repository. The following exception occurred: 0.
- CWMCO1017I

Start to migrate IBM Business Automation Workflow schedulers to the target environment.
- CWMCO1018I

Migration of IBM Business Automation Workflow schedulers has completed. Check the scheduler migration log for details.
- CWMCO1019E

Business Process Manager schedulers were not migrated.  Check the scheduler migration trace for details: 0.
- CWMCO1020I

Start to do pre-check for the source environment.
- CWMCO1021I

Pre-check for the source environment has completed.
- CWMCO1022I

Pre-check of the source environment passed. See the following summary of pre-check results. You can continue other migration steps.
- CWMCO1023I

Pre-check for the source environment failed. See the following summary of pre-check results.
- CWMCO1024E

Failed to do pre-check for the source environment with exception: 0.  Check the migration log for details. Log location:1.
- CWMCO1025I

Start to query deployment configuration for adapters.
- CWMCO1026I

Query deployment configuration for adapters completed successfully.
- CWMCO1027E

Failed to query deployment configuration for adapters with exception: 0.  Check the migration log for details. Log location:1.
- CWMCO1028I

Start to migrate the adapter.
- CWMCO1029I

Migration of the adapter completed successfully.
- CWMCO1030E

Failed to migrate adapter with exception: 0.  Check the migration log for details. Log location:1.
- CWMCO1031I

Log file for scheduler migration will be saved on the host: 0
- CWMCO1032E

Failed to find any active cluster member for the cluster: 0. Make sure the environment is running and try again.
- CWMCO1033W

The JMX connection to the server did not initiate. The following exception occurred :0.
- CWMCO1034W

Custom nodes were not synchronized with the cell repository.
- CWMCO1035E

The backup folder you specified is not empty. The snapshot folder is: 0.
- CWMCO1036I

IBM Business Automation Workflow migration logs are saved under 0.
- CWMCO1037E

Required properties: 0 are not specified in the migration properties file.
- CWMCO1038I

Current source environment is not supported by the migration utility because it is augmented with IBM Business Monitor.
- CWMCO1039E

Failed to detect if current source environment is augmented with IBM Business Monitor with exception: 0  Check the migration log for details. Log location:1.
- CWMCO1040I

Start to extract the custom context root prefix from source environment.
- CWMCO1041I

Extraction of custom context root prefix from source environment completed successfully.
- CWMCO1042E

Failed to extract the custom context root prefix from source environment with exception: 0.  Check the migration log for details. Log location:1.
- CWMCO1043I

Start to apply the custom context root on target environment.
- CWMCO1044I

Apply custom context root prefix on target environment completed successfully.
- CWMCO1045E

Failed to apply the custom context root on target environment with exception: 0.  Check the migration log for details. Log location:1.
- CWMCO1046I

No need to run command 0, as the source environment is 1.
- CWMCO1047E

Mismatched snapshot version is found: the target product version is 0, but the snapshot version is 1.
- CWMCO2001E

Messaging Engine 0 is stopped.
- CWMCO2002E

Make sure that all messaging engines have been started before continuing.
- CWMCO2003I

Start to take snapshot of SIB messages.
- CWMCO2004I

Snapshot of SIB messages completed successfully.
- CWMCO2005E

A snapshot of SIB messages was not created. The following exception occurred: 0.  Check the migration log for details. Log location:1.
- CWMCO2006I

Start to migrate SIB messages to the target environment.
- CWMCO2007I

Migration of SIB messages completed successfully.
- CWMCO2008E

SIB messages were not migrated. The following exception occurred: 0.  Check the migration log for details. Log location:1.
- CWMCO2009I

0 messages were migrated to the destination in the target environment 1.
- CWMCO2010I

0 messages were extracted from the destination in the source environment 1.
- CWMCO2200E

Failed to generate the report for validation rule: 0
- CWMCO2201I

The messaging engine with name 0 is not started.
- CWMCO2202E

Failed to validate applications, please check the log for details.
- CWMCO2203E

Failed to validate data sources, please check the log for details.
- CWMCO2204E

Failed to validate SIB messaging engines, please check the log for details.
- CWMCO2205E

Failed to validate source product, please check the log for details.
- CWMCO2206E

The application 0 has been stopped.
- CWMCO2207E

The status of application 0 cannot be determined.
- CWMCO2208E

Test connection operation for data source 0 returned warning.
- CWMCO2209E

Test connection operation for data source 0 returned error.
- CWMCO2210E

The messaging engine 0 was not started normally.
- CWMCO2211E

The source environment version 0 cannot be migrated.
- CWMCO2212E

Exception occurred when running validation rule: 0
- CWMCO2213E

Failed to validate SIB destination, please check the log for details.
- CWMCO2214E

Failed to validate customized configuration that cannot be migrated, please check the log for details.
- CWMCO2215E

Failed to validate failed events, please check the log for details.
- CWMCO2216E

Exception occurred when running migration prevalidation. Check the log file under 0 for details.
- CWMCO2217E

Failed to validate Lightweight Third-Party Authentication(LTPA) keys, please check the log for details.
- CWMCO2218E

Failed to validate WebSphere Lombardi Edition XML configuration files, please check the log for details.
- CWMCO2219E

The messaging engine 0 has been stopped.
- CWMCO3001I

Start to take snapshot of configuration from the source environment.
- CWMCO3002I

Snapshot of configuration from the source environment completed successfully.
- CWMCO3003E

A snapshot of configuration from the source environment was not created.  The following exception occurred: 0.  Check the migration log for details. Log location:1.
- CWMCO3004E

Failed to create snapshot directory for configuration.
- CWMCO3005I

Start to copy configuration files.
- CWMCO3006I

Configuration files were copied successfully.
- CWMCO3008W

File 0 does not exist under 1.
- CWMCO3009E

An exception occurred when file 0 was being copied to the backup folder.
- CWMCO3013I

Start to export LTPA key from the source environment.
- CWMCO3014I

Export of LTPA key from the source environment completed successfully.
- CWMCO3015E

LTPA key was not exported from the source environment.  The following exception occurred: 0.  Check the migration log for details. Log location:1.
- CWMCO3016I

Start to import LTPA key to the target environment.
- CWMCO3017I

Import of LTPA key completed successfully.
- CWMCO3018E

LTPA key was not imported into the target environment. The following exception occurred: 0.  Check the migration log for details. Log location:1.
- CWMCO3019I

Start to import 100Custom to the target environment.
- CWMCO3020I

Import of 100Custom completed successfully.
- CWMCO3021E

Failed to import 100Custom into the target environment. The following exception occurred: 0.  Check the migration log for details. Log location:1.
- CWMCO3022I

Start to export database information from the source environment.
- CWMCO3023I

Export of database information from the source environment completed successfully.
- CWMCO3024E

Failed to export database information from the source environment. The following exception occurred: 0.  Check the migration log for details. Log location:1.
- CWMCO3025E

Database information was not exported from the source environment because the specified output file 0 already exists.
- CWMCO3026E

Failed to read the JMX object of 0.
- CWMCO3027E

Failed to initialize the configuration service.
- CWMCO3028E

Failed to initialize the XML document object.
- CWMCO3029E

Failed to extract the performance parameters.
- CWMCO3030E

Failed to persist the performance parameters. The following exception occurred : 0 .
- CWMCO3032E

The directory ''0'' does not exist or input for directory property value is empty, check the value which set by bpm.home at the input migration property file.
- CWMCO3033E

Check the specified output parameter: 0. It must be the full path to a file.
- CWMCO3034E

Failed to create folder 0 for the specified output parameter.
- CWMCO3035E

Cluster 0 does not exist.
- CWMCO3036I

Start to generate migration2002to3001.properties file that is required by Business Space data migration.
- CWMCO3037I

Generate migration2002to3001.properties file completed successfully. It was generated under folder 0.
- CWMCO3038E

Failed to generate migration2002to3001.properties file that is required by Business Space data migration. The following exception occurred: 0.  Check the migration log for details. Log location:1.
- CWMCO3039I

Start to merge source user registry file with target user registry file.
- CWMCO3040I

Merge source user registry file with target user registry file completed successfully.
- CWMCO3041E

There was a failure to merge source user registry file with target user registry file. The following exception occurred: 0.  Check the migration log for details. Log location:1.
- CWMCO3042E

An exception occurred during the validation of migration properties file. Check the migration log for details. Log location:0.
- CWMCO3043E

File 0 or 1 cannot be found. You must complete step 2 and 3 before you run step 4.
- CWMCO3044E

Cluster information for the source environment was not found in the migration properties file.
- CWMCO3045E

File 0 cannot be found. You must complete step 1 before you run step 2
- CWMCO3046E

Required property values: 0 are not specified in the migration properties file.
- CWMCO4001I

Source application directory is 0.
- CWMCO4002I

Application backup directory is 0.
- CWMCO4003I

There are 0 applications saved in the snapshot directory.
- CWMCO4004I

Start to take snapshot of applications.
- CWMCO4005I

Snapshot of applications completed successfully.
- CWMCO4006E

A snapshot of applications was not created. The following exception occurred: 0.   Check the migration log for details. Log location:1.
- CWMCO4007I

Start to migrate applications to the target environment.
- CWMCO4008I

Migration of applications completed successfully.
- CWMCO4009E

Applications were not migrated. The following exception occurred: 0.  Check the migration log for details. Log location:1.
- CWMCO4010I

The migration for applications started.
- CWMCO4011I

Node name is 0, server name is 1.
- CWMCO4012I

Will not migrate object 0 of type EAR file. It is already installed.
- CWMCO4013I

No applications found in snapshot directory 0.
- CWMCO4014E

Failed to map to a new cluster.
- CWMCO4015I

Skip copy 0, it already exists.
- CWMCO4016I

The application 0 does not exist.
- CWMCO4017I

There are 0 applications to be migrated.
- CWMCO4018I

Application 0 failed to install.
- CWMCO4019I

Return code after application installation is 0.
- CWMCO4020I

Start to set auto-start properties for all applications and the scheduler daemon.
- CWMCO4021I

Auto-start properties were set for all applications and the scheduler daemon.
- CWMCO4022E

Failed to set auto-start properties for all applications and the scheduler daemon. Check the migration log for details. Log location:0.
- CWMCO4023E

An error occurred while setting the auto-start properties for applications and the scheduler daemon.
- CWMCO4024I

Application installed successfully 0.
- CWMCO4025W

Could not find any application with prefix 0.
- CWMCO4026E

Application failed to installed 0.
- CWMCO4027I

Application migration result: success 0, failed 1.
- CWMCO4028W

Try to manually migrate the failed applications.
- CWMCO4029I

Start to migrate business level applications.
- CWMCO4030I

Business level applications migration completed successfully.
- CWMCO4031I

Failed to migrate business level applications.
- CWMCO4032I

0 exported successfully.
- CWMCO4033I

Asset 0 imported successfully.
- CWMCO4034I

Empty business level application 0 created successfully.
- CWMCO4035I

Add composition unit 0.
- CWMCO4046E

An error occurred while setting the custom context root prefix. Check the BPMConfig command log under 0 to get more error details.
- CWMCO4047I

The installation script for application 0 was generated successfully.
- CWMCO4048I

Application 0 is being installed. The installation process might take a while.
- CWMCO4049I

Installing applications in a batch. The installation process might take a while. You can get details of the application installation in the migration log.
- CWMCO4050E

An error occurred while installing applications in a batch. Check the migration log for details.
- CWMCO4051I

Start to generate installation script for application 0.
- CWMCO5001I

Invoking the AdminTask to migrate IBM Business Automation Workflow schedulers ...
- CWMCO5002I

Verifying scheduler tables and stopping all scheduler daemons.
- CWMCO5003E

The environment could not be made ready for scheduler migration.
- CWMCO5004W

0 is unavailable in the current environment.
- CWMCO5005I

Determining if it should execute: 0
- CWMCO5006I

Executing step: 0
- CWMCO5007I

All scheduler migration steps completed successfully.
- CWMCO5008E

An invalid slice number was specified.
- CWMCO5009I

Slice number is 0
- CWMCO5010E

The message class handlers for BPC scheduler could not be initialized.
- CWMCO5011I

Begin time: 0
- CWMCO5012I

End time: 0
- CWMCO5013I

The size of the scheduler task is 0; it is not necessary to migrate.
- CWMCO5014I

**** Start Batch 0 ****
- CWMCO5015I

1 of 0 tasks migrated successfully.
- CWMCO5016E

Failed to get Application Scheduler task.
- CWMCO5017I

0 / 1 AppScheduler tasks migrated successfully.
- CWMCO5018I

0 / 1 BPCScheduler tasks migrated successfully, 2 tasks ignored, 3 tasks failed.
- CWMCO5019I

0 / 1 PCSharing Scheduler tasks migrated successfully.
- CWMCO5020I

Original task name is : 0.
- CWMCO5021I

Updated task name is : 0.
- CWMCO5022W

Name of task ''0'' cannot be updated because of duplication; re-create the task manually.
- CWMCO5023E

Failed to delete task with id 0.
- CWMCO5024W

Failed to get the task 0.
- CWMCO5025I

Collecting scheduler task information ...
- CWMCO5026W

Deserialized MessageData of task 0 is blank, ignoring this task.
- CWMCO5027W

Message length 1 of task 0 is not valid, ignoring this task.
- CWMCO5028I

Serialized object is of class 0.
- CWMCO5029I

No record file found: 0.
- CWMCO5030I

0 succeed, 1 are ignored, new task id is 3.
- CWMCO5031I

Task ''0'' is a ''1'', ignoring this task.
- CWMCO5032E

Failed to handle task: 0.
- CWMCO5033I

Task 0 is the cleanup service for BPC; it must be created manually after migration.
- CWMCO5034I

Looking up Scheduler Configuration Helper MBean for 0.
- CWMCO5035I

0 : Scheduler tables were verified successfully.
- CWMCO5036E

The configuration of the scheduler could not be verified.
- CWMCO5037W

No scheduler ID was found for scheduler: 0.
- CWMCO5038I

The scheduler daemon for instance 0 has been stopped.
- CWMCO5039I

Loading configuration file for scheduler migration ...
- CWMCO5040E

The configuration file for scheduler migration is invalid.
- CWMCO5041I

No pre-defined handler exists for class 0, using the default one.
- CWMCO5042I

Log directory is 0, log level is 1.
- CWMCO5043E

The data length is 0, but expected size is 4.
- CWMCO5044W

Loading topology information ...
- CWMCO5045I

Starting application 0 ...
- CWMCO5046I

0 started successfully.
- CWMCO5047I

Path of scheduler migration log: 0
- CWMCO5048E

Failed to find Scheduler tasks.
- CWMCO5049E

Invalid parameter is specified, please check it again.
- CWMCO6002I

Found component 0 is configured for the 1 database.
- CWMCO6003I

Do you want to generate scripts? Y/N
- CWMCO6004I

Scripts have been generated in the 0 directory.
- CWMCO6005I

Enter the value for 0.
- CWMCO6006E

The version 0 specified for 1 is invalid. Please specify the correct value of version number in format <w>.<x>.<y>.<z>, E.g. 7.5.1.0.
- CWMCO6007E

The BPMGenerateUpgradeSchemaScripts command could not complete successfully. The following exception occurred : 0 .
- CWMCO6008E

The required property 0 cannot be found in the migration properties file 1.
- CWMCO6009I

The BPMGenerateUpgradeSchemaScripts command completed successfully.
- CWMCO6010I

The BPMGenerateUpgradeSchemaScripts logs are in 0.