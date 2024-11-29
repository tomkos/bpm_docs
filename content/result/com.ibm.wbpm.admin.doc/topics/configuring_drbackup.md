# Configuring a disaster recovery backup system

## About this task

Take a snapshot of the configuration data every time it changes so that following a disaster you
can recover with the correct environment.

These instructions help you to set up all of your installation images on a single replication
volume.

When you have your installation images on a single volume, you can duplicate the original data
center configuration in your disaster recovery data center. If a disaster occurs while you are
rolling out a configuration change to your environment, you can continue rolling out the
configuration change when you restart your environment in the disaster recovery data center.

## Procedure

1. Set up a disk replication system.
2. Add the profile directory, profile\_root.
3. Add the following files from subdirectories of the installation directory,
install\_root: properties/profileRegistry.xml,
properties/fsdb/*, and properties/Profiles.menu.
4. Add files from the logs directory that might contain errors that are related to profile
actions. Those files might be useful in the disaster recovery data center.
5. If the original data center uses a storage area network (SAN), create an identical
directory for mounting the SAN in the disaster recovery data center. Create the profiles in a
subdirectory of that mounted directory, /opt/ibm/WebSphere/profiles.
6 Develop scripts for the recovery system. Actions that create a profile, deletea profile, add a node, or remove a node must also trigger a snapshot to the installation data. Youneed a snapshot of the installation data for these configuration changes because some of the filesthat are altered for these changes are contained in the installation data (see step 3).
    1. Develop scripts or procedures for mounting the disk.
    2. Develop scripts to start the administrative processes of your disaster recovery
center.
    3. Develop scripts to start your disaster recovery center resources.
7. Load in the disaster site recovery scripts or procedures for the configuration
replication volume.

## What to do next

When you
set up the snapshot mechanism, do not schedule snapshots of the volume. The snapshot schedule can
take a snapshot while the configuration is in the process of being changed, which would leave you
with an unusable snapshot.

To ensure you have a reliable snapshot, take the snapshots
immediately after a configuration change has been saved.