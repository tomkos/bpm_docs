# Snapshot support

On the Linux platform, you can use Logical Volume Management (LVM). LVM provides a higher-level
view of the disk storage on a computer system than the traditional view of disks and partitions.
With LVM, the system administrator has more flexibility in allocating storage to applications and
users by demand. The physical volumes of the disk are organized as logical volumes, and the file
system is mounted on logical volumes. This organization allows the flexible and dynamic management
of the disk size of the file system.

1. The snapshot creates a logical copy of the data after the application is frozen for a very short
period.
2. A write request to the original copy of the data results in the system copying the original data
to the snapshot disk area before the original copy is overwritten.
3. A read into the logical copy is redirected to the original copy if the data is not modified. If
the data is modified, the read request is satisfied from the snapshot disk area.

The following topics provide information about taking the snapshot:

1. Preparing the operating system before a snapshot

Before you take a snapshot of the operating system, you create a physical volume and logical volume.
2. Taking an operating system snapshot

As part of your disaster recovery plan, you create a snapshot of the operating system from your primary environment. You then transfer the snapshot to your secondary environment.