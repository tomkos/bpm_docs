# Configuring the NFS clients

## About this task

## Procedure

For each NFS client, complete the following steps:

1. To mount the corresponding directory to the
remote NFS server, use the following commands: # mount	<server\_ip>:/home/machine1 /home/dmgr
# mount	<server\_ip>:/home/machine2 /home/db2
# mount	<server\_ip>:/home/machine3 /home/custom01
2. Make these mounts start automatically with the
system so that you will not have to run these commands every time
that you start your system.
3. Repeat steps 1 and 2 for all other NFS clients.