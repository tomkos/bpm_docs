# Updating the Content Platform Engine client
connector files

## Before you begin

Check with the FileNet® P8
Platform
administrator to determine the update level of the Content Platform Engine. If no software updates are
applied, skip this task.

## Procedure

To update the Content Platform Engine client
connector files:

1. Run updateBPMexternalECM command. Refer to updateBPMExternalECM command for details.
2. After running updateBPMexternalECM command, if it updates the JAR
files, it lists the updated files for you. Copy the files from the deployment manager to the same
installation directory on each custom node in your deployment environment.
3. Restart the workflow deployment manager and clusters.