# Downloading the CASE files

## About this task

## Procedure

1. Connect your host to the internet and disconnect it from the local air-gapped network.
2 Download the Business Automation Workflow images to yourhost.
    1. From IBM Catalog Management plug-in (ibm-pak) v1.6 and later, you can download the CASE files
from cp.icr.io/cpopen. You can view the current config of the plug-in by running
the following command:
oc ibm-pak config
The output lists all the configured repositories. The default repository from where the CASE
files are downloaded has an asterisk mark (*) against the Name field.
    2. You can then run the following command to configure a repository that downloads the CASE files
from the cp.icr.io registry (an OCI-compliant registry) before you run the
oc ibm-pak get command.
oc ibm-pak config repo 'IBM Cloud-Pak OCI registry' -r oci:cp.icr.io/cpopen --enable
The command sets 'IBM Cloud-Pak OCI registry' as the default repository.
    3. You can list all the available CASE files to download by running the following command:
oc ibm-pak list
To get more help about the list command, run the following command:
oc ibm-pak list --help
    4. save below file as baw-case-to-be-mirrored\_24.0.0.0.yaml
name: ibm-cs-bawautomation
version:2.7.x
description: Generated from CASE ibm-cs-bawautomation
cases:
- name:ibm-cs-bawautomation
  version: 2.7.x
  launch: true
Note: The value for 'x' is '0' for 24.0.0. For fix pack, like 24.0.0-IF001, the value of 'x' is
'1'.
    5. When you are ready to start the download of the CASE files, run the following command:
oc ibm-pak get -c file://<absolute path to file>/baw-case-to-be-mirrored\_24.0.0.0.yaml
The <absolute path to file> needs to be a path that starts with
"/". For example, "/opt".
By default, the root directory that is used by the ibm-pak plug-in is
~/.ibm-pak. Therefore, by default, the Business Automation Workflow CASE is downloaded
to ~/.ibm-pak/data/cases/$CASE\_NAME/$CASE\_VERSION.
Tip: You can configure the root directory by setting the
IBMPAK\_HOME environment variable.
    6. To list the versions of all the downloaded CASE files, you can run the following command:
oc ibm-pak list --downloaded
If IBMPAK\_HOME is set, the downloaded CASE is located in
$IBMPAK\_HOME/.ibm-pak/data/cases/$CASE\_NAME/$CASE\_VERSION. The logs files can
be found in $IBMPAK\_HOME/.ibm-pak/logs/oc-ibm\_pak.log.

## Results

## What to do next