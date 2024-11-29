# Configuring the NFS server

## About this task

## Procedure

1. Create the directories that you want to mount to the NFS
client directories (for example, /home/machine1, /home/machine2,
and /home/machine3). Important: Make sure that these directories have write authority.
2. Configure the /etc/exports file: 
  /home/machine1 *(rw, sync)
/home/machine2 *(rw, sync, no\_wdelay, nohide)
/home/machine3 *(rw, sync, no\_root\_squash)
/home/machine4 *(rw, sync, no\_root\_squash) In this example, the /home/machine3 and /home/machine4
directories will be mounted to the remote managed-node profile directory.
3. Before the NFS service starts, the portmap service must
be running. To check its status, use the following command:  
# service portmap status
4. If the portmap service has stopped, use the following command
to start it: # service portmap start
5. To start or restart the NFS service, use one of the following
commands: # service nfs start 
# service nfs restart
6. To make the NFS service start automatically with the system,
use the following command:  # chkconfig --level 35 nfs on
7. To check the NFS export directories, use the following
command.  # showmount -e <server\_ip>
You can use this command on both the NFS server and the NFS
client.

## What to do next