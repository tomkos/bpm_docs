# Changing the network shared directory

## Procedure

To change the network shared directory:

1. Copy all folders and files from the previous network shared directory to the new network shared
directory.
2. Run the BPMConfig command with the -update
option.

BPMConfig -update -profile DmgrProfile [-de deName] -networkDirectory new\_directory\_path -component CaseManager

Note: When you run the BPMConfig.sh -update -profile Dmgr01 -de De1
-networkDirectory command to switch to a new path, you should use a different path rather
than the Business Automation Workflow default path. If you mount it to an external file system that
uses the default network shared directory
BAW\_INSTALL\_ROOT/CaseManagement/properties/, it might result in loss of the
original files.
3. Restart your IBM Business Automation
Workflow
environment.
4. Rerun all enabled tasks in the Case configuration tool.