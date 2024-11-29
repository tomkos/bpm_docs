# Copying the migration utilities to the source computer

## About this task

## Procedure

1 On a system that has the new version installed and the same operating system asthe source environment, create a remote migration image by using theBPMCreateRemoteMigrationUtilities command from thetarget\_install\_root /bin directory. This image must be copied to the migration source computer and is used tocreate the snapshot. Use the followingsyntax:BPMCreateRemoteMigrationUtilities.bat remoteMigrationUtilities.zip The location of the remoteMigrationUtilities.zip file is displayed when yourun the BPMCreateRemoteMigrationUtilities command. If you specify only the filename and not the full path name, the remoteMigrationUtilities.zip file is inthe install\_root \util\migration\scripts directory. The BPMCreateRemoteMigrationUtilities command does not write to a log file,but displays the results in a window. Forexample:C:\BPM24.x \bin>BPMCreateRemoteMigrationUtilities.bat C:\MigrationUtility.zip Buildfile: C:\BPM\util\migration\scripts\createMigrationUtilDisk.antcreate\_zip\_image: [zip] Building zip: C:\MigrationUtility.zipBUILD SUCCESSFULTotal time: 41 seconds After you have run the BPMCreateRemoteMigrationUtilities command, check thegenerated remoteMigrationUtilities.zip file and verify that it contains thefollowing folders: The bin folder should contain BPMConfig.bat ,BPMExtractSourceInformation.bat , andBPMManageApplications.bat . For more information, see the BPMCreateRemoteMigrationUtilities command-line utility command.

```
BPMCreateRemoteMigrationUtilities.bat remoteMigrationUtilities.zip
```

The location of the remoteMigrationUtilities.zip file is displayed when you
run the BPMCreateRemoteMigrationUtilities command. If you specify only the file
name and not the full path name, the remoteMigrationUtilities.zip file is in
the install\_root\util\migration\scripts directory.

```
C:\BPM24.x\bin>BPMCreateRemoteMigrationUtilities.bat C:\MigrationUtility.zip 
Buildfile: C:\BPM\util\migration\scripts\createMigrationUtilDisk.ant
create\_zip\_image:
      [zip] Building zip: C:\MigrationUtility.zip

BUILD SUCCESSFUL
Total time: 41 seconds
```

    - bin
    - BPM
    - configuration
    - etc
    - java
    - jdbcdrivers
    - lib
    - plugins
    - properties
    - util

For more information, see the BPMCreateRemoteMigrationUtilities command-line utility command.

2. Use FTP, RCP, or some other mechanism to copy the remote migration
utility image from the target system to the source system. Then, extract the remote migration
utilities into their own unique directory on the source system. 

Note: If the source deployment environment secure socket layer (SSL) setting has
a custom configuration, then you must rename the existing remote\_migration\_utility/util/migration/resources/ssl.client.props file, and
copy the ssl.client.props file from
the dmgr\_profile/properties/ directory into the remote\_migration\_utility/util/migration/resources/ directory.
3 Optional: The following steps are required ifa custom resource that relies on third-party libraries, such as athird-party JMS provider, is configured in the source environment.The dependent third-party libraries are not migrated, so you mustcopy them to the target environment manually to make the custom resourcework correctly in the target environment. For a migrationon the same computer: For a migration to a different computer: No matterwhere the dependent third-party libraries are placed in the sourceenvironment, copy them to the same folder in the target environment.Important: If you are migrating from a Windows system to a Linux® or UNIX system,or from a Linux or UNIX system to a Windows system, besides copying the third-partylibraries to the target environment, you must also modify the configurationof the custom resource so that it refers to the correct location ofthe libraries because of the different file path formats of the operatingsystems.

1. If the dependent third-party libraries are in a folder
under install\_root in the
source environment, copy them to the same folder under install\_root in
the target environment.
2. If the dependent third-party libraries are in a folder
outside install\_root in the source environment,
 make sure that they are in the same location in the target environment
after migration.

For a migration to a different computer:

- Considerations for migrating to a different operating system

To migrate to a computer with a different operating system, you must perform more migration steps.

## Related information

- BPMCreateRemoteMigrationUtilities command-line utility