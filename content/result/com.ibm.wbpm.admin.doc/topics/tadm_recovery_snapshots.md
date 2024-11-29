# Taking an operating system snapshot

## Before you begin

## About this task

## Procedure

To take an operating system snapshot, complete the following steps:

1. Take a snapshot of the /home directory. The snapshot is also a new
logical volume:  
# lvcreate -L1G -s -n homesnapshot /dev/VolGroup00/homebackup

Tip: You can also use the GUI tool in the operating system, which, for Red Hat Linux, is
Logical Volume Management.
2. To use the logical volume, create a directory under /mnt to store
the snapshot files:  
# mkdir /mnt/homesnapshot
3. Mount the snapshot logical volume to the new directory:  
# mount /dev/VolGroup00/homesnapshot /mnt/homesnapshot
If you no longer need a snapshot, unmount it and remove it to save disk
space:# lvremove /dev/VolGroup00/homesnapshot

## What to do next