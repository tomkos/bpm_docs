# Preparing the operating system before a snapshot

## About this task

- The /opt and /home directories must be vacant, because
any data in the directory is destroyed when you mount a directory.
- You can mount an extra disk with about 10 GB of vacant space and then create a physical volume
on it.
- After you extend the physical volume to a volume group, you can create the new logical volume in
the volume group.

## Procedure

To prepare the operating system before you take a snapshot, complete the following
steps:

1. List the general information (physical volume, volume group, and logical volume) of the
Linux operating system:  
# pvdisplay
# vgdisplay
# lvdisplay
2. List the disk information:  
# fdisk -l
3. Create a physical volume on the disk partition, as in the following example:  
/dev/sda2:  # pvcreate /dev/sda2 /home
4. Extend the new physical volume to the volume group: 

# vgextend VolGroup00 /dev/sda2
5. Create a logical volume on the volume group:  
# lvcreate -name homebackup -size 10G VolGroup00
6. Make the file system format for the new logical volume:  
# mkfs.ext3 /dev/VolGroup00/homebackup
7. Mount the logical volume to the /home directory: 

# mount /dev/VolGroup00/homebackup/home /home

## What to do next