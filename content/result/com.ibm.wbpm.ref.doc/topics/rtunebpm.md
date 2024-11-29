# tuneBPM command-line utility (removed)

The tuneBPM command
is used to apply the properties specified in the performanceTuning.properties file
to the existing deployment environment. It can only be used in an
ND environment and cannot be used in a stand-alone environment.

If
you want to run the tuneBPM command against the
default profile, specify the two required parameters without the optional -profileName parameter
and run the command in the directory install\_root/BPM/scripts.

If
you want to run the tuneBPM command against a different
profile, you can specify the two required parameters without the optional -profileName parameter
and run the command in the profile directory profile\_root/bin.
For example, to run the tuneBPM command against
the deployment manager profile, you can specify the parameters and
run the command in the profile directory Dmgr\_profile\_root/bin.
You can also run the tuneBPM command against any
specific profile by using the optional -profileName parameter.

## Location

The tuneBPM command-line
utility script is in the following directories:

- install\_root/BPM/scripts
- profile\_root/bin

## Syntax

<!-- image -->

```
tuneBPM.bat 
[-profileName dmgr\_profile\_name] 
-de deployment\_environment\_name 
-propertyFile property\_file\_path
```

<!-- image -->

<!-- image -->

```
tuneBPM.sh 
[-profileName dmgr\_profile\_name] 
-de deployment\_environment\_name 
-propertyFile property\_file\_path
```

## Parameters

## Examples

- tuneBPM.bat -de De1 -propertyFile "C:\bpm
85\BPM\samples\config\performanceTuning\performanceTuning.properties"
- tuneBPM.bat -profileName DmgrProfile -de
De1 -propertyFile "C:\bpm 85\BPM\samples\config\performanceTuning\performanceTuning.properties"
- tuneBPM.sh -de De1 -propertyFile
/tmp/samples/config/performanceTuning/performanceTuning.properties
- tuneBPM.sh -profileName DmgrProfile
-de De1 -propertyFile /tmp/samples/config/performanceTuning/performanceTuning.properties

- Sample performanceTuning.properties file (removed)

To assist you with your performance-tuning tasks, a performanceTuning.properties file is provided. You can define and edit the properties in the file and then run the tuneBPM command to apply the properties to your existing deployment environment.