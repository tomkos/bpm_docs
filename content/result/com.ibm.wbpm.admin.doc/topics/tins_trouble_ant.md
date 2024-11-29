# Diagnosing a failing Ant configuration script

## Before you begin

## About this task

To diagnose failed Ant configuration scripts,
perform the following steps.

## Procedure

- Diagnose the failed 90SConfigWBIMigrationScript.ant configurationscript. This script changes the permissions of the followingscript to 755: installation\_root /bin/BPMMigrate .This script also replaces the following tokens in the installation\_root /bin/BPMMigrate script: From: To the value that you selected during installation: ${JAVAROOT} installation\_root /java/jre/bin/java ${MIGRATIONJAR} installation\_root /bin/migration/migrationGUI/migrationGUI.jar ${WASROOT} installation\_root ${PRODUCTID} ${WS\_CMT\_PRODUCT\_TYPE}

| From:           | To the value that you selected during installation:           |
|-----------------|---------------------------------------------------------------|
| ${JAVAROOT}     | installation\_root/java/jre/bin/java                           |
| ${MIGRATIONJAR} | installation\_root/bin/migration/migrationGUI/migrationGUI.jar |
| ${WASROOT}      | installation\_root                                             |
| ${PRODUCTID}    | ${WS\_CMT\_PRODUCT\_TYPE}                                        |

    1 Investigative action: Verify that the permissions are755 for the following directories:
        - installation\_root/bin/BPMMigrate.sh
        - installation\_root\bin\BPMMigrate.bat
2 Recovery action: Issue the following command:
    - chmod 755 installation\_root/bin/BPMMigrate.sh
    - chmod 755 installation\_root\bin\BPMMigrate.bat
3 Investigative action: Open the following file in aneditor and verify that real values exist instead of the followingvalues: ${JAVAROOT} , ${MIGRATIONJAR} , ${WASROOT} ,and ${PRODUCTID} .

- installation\_root/bin/BPMMigrate.sh
- installation\_root\bin\BPMMigrate.bat
4. Recovery action:  Change the following tokens to
values in the BPMMigrate script: ${JAVAROOT}, ${MIGRATIONJAR},  ${WASROOT},
and ${PRODUCTID}.
- Diagnose the failed 85SConfigNoProfileFirstStepsWBI.ant . This script copies all files from the installation\_root /properties/version/install.wbi/firststeps.wbi directoryto the installation\_root /firststeps/wbi/html/noprofile directory.This script also replaces the following tokens in the following files: From: To the value that you selected during installation: ${JAVAROOT} installation\_root /java/jre/bin/java ${PROFILEROOT} installation\_root ${HTMLSHELLJAR} installation\_root /lib/htmlshellwbi.jar ${CELLNAME} ${WS\_CMT\_CELL\_NAME}

- installation\_root/firststeps/wbi/firststeps.sh
- installation\_root\firststeps\wbi\firststeps.bat

| From:           | To the value that you selected during installation:   |
|-----------------|-------------------------------------------------------|
| ${JAVAROOT}     | installation\_root/java/jre/bin/java                   |
| ${PROFILEROOT}  | installation\_root                                     |
| ${HTMLSHELLJAR} | installation\_root/lib/htmlshellwbi.jar                |
| ${CELLNAME}     | ${WS\_CMT\_CELL\_NAME}                                   |

1. Investigative action: Verify that all files are copied
from the installation\_root/properties/version/install.wbi/firststeps.wbi directory
to the installation\_root/firststeps/wbi/html/noprofile directory.
2. Recovery action:  Copy all of the files from the installation\_root/properties/version/install.wbi/firststeps.wbi directory
to the installation\_root/firststeps/wbi/html/noprofile directory.
3. Investigative action: Open the installation\_root/firststeps/wbi/firststeps script
in an editor. Verify that real values exist instead of the following
values: ${JAVAROOT}, ${PROFILEROOT}, ${HTMLSHELLJAR},
and ${CELLNAME}.
4. Recovery action: Change the following tokens to values
in the installation\_root/firststeps/wbi/firststeps script. ${JAVAROOT}, ${PROFILEROOT}, ${HTMLSHELLJAR},
and  ${CELLNAME}.

## Results

## What to do next