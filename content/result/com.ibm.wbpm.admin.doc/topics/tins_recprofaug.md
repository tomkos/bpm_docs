# Recovering from profile creation or augmentation failure

## Log files

1 The log file profile\_name\_ create\_error.log (where profile\_name isthe name of the profile). Note: Look at this file only if you werecreating a new profile, not augmenting an existing one. Search for the text Configuration action succeeded or Configurationaction failed . Note: There can be multiple occurrencesof Configuration action failed . Investigate andremedy each one. Also review the log files described in the followingoptions, if the profile was created. Note: Additional informationis available in the manageprofiles directoryin the pmt.log, which logs all events that occur when a default profileis created during a complete installation using the Profile ManagementTool.
    - install\_root/logs/manageprofiles/profile\_name\_create\_error.log
    - install\_root\logs\wbi\update\profile\_name\_create\_error.log

Search for the text Configuration action succeeded or Configuration
action failed.

2 Log file profile\_name\_ augment\_error.log (where profile\_name isthe name of the profile).This log file is located in the followingdirectories: Search for the text Configuration action succeeded or Configurationaction failed . Note: There can be multiple occurrencesof Configuration action failed . Investigate andremedy each one. Also review the log files described in the followingoptions, if the profile was created. Note: If you want to knowthe status of a profile you created during installation, run the followingcommands:

- install\_root/logs/manageprofiles/profile\_name\_augment\_error.log
- install\_root\logs\wbi\update\profile\_name\_augment\_error.log

Search for the text Configuration action succeeded or Configuration
action failed.

- install\_root/bin/logProfileErrors.sh
- install\_root\bin\logProfileErrors.bat
3 Individual profile template action log files.If you discoveredfalse values in the log files described in the preceding options,review the log files in the following directories: where profile\_root or user\_data\_root isthe installation location of the profile. These log files donot follow a consistent naming convention, but typically, each isthe name of the Apache Ant script that failed followed by .log .For example, suppose the following entry is in the profile\_name\_ augment.log file: <messages>Result of executingE:\o0536.15\profileTemplates\default.wbicore\actions\saveParamsWbiCore.ant was:false</messages> First look at the surroundingentries in the profile\_name\_ augment.log filein the install\_root /logs/manageprofiles directory.If you cannot determine the cause of the failure from the surroundingentries, look for the corresponding log file for any failing Ant scriptentries. In this case, the log file created by the saveParamsWbiCore.ant scriptis saveParamsWbiCore.ant.log . Look at that fileto investigate why the failure occurred.

- install\_root/logs/manageprofiles/profile\_name on Linux® and UNIX systems
- install\_root\logs\manageprofiles\profile\_name on Windows systems

These log files do
not follow a consistent naming convention, but typically, each is
the name of the Apache Ant script that failed followed by .log.
For example, suppose the following entry is in the profile\_name\_augment.log file:

```
<messages>Result of executing
E:\o0536.15\profileTemplates\default.wbicore\actions\saveParamsWbiCore.ant 
was:false</messages>
```

First look at the surrounding
entries in the profile\_name\_augment.log file
in the install\_root/logs/manageprofiles directory.
If you cannot determine the cause of the failure from the surrounding
entries, look for the corresponding log file for any failing Ant script
entries. In this case, the log file created by the saveParamsWbiCore.ant script
is saveParamsWbiCore.ant.log.  Look at that file
to investigate why the failure occurred.

## Recovery for creation failure

To
determine if the profile exists, run the install\_root/bin/manageprofiles
-listProfiles command. If the profile name you used for
creation does not exist, you can recreate the profile. If the profile
name you used for creation exists, then the profile was created and
you have encountered an augmentation failure. For tips on recovering
from an augmentation failure, see Recovery for augmentation failure.

## Recovery for augmentation failure

- If any of the profile creation was successful and if the create succeeded by a subsequent
augmentation failed then you have to delete the profile using the manageprofiles
command: manageprofiles -delete -profileName

- You must remove the profile directory manually since the deletion will leave file remnants
behind.
- You must remove and recreate the database if the profile creation went far enough to start
working with the database. However if it failed during WAS profile creation it is not necessary to
remove and recreate the database.