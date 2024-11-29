# Deleting unnamed snapshots in bulk from a Workflow Center server

## Before you begin

You must be a development environment administrator with access to the local configuration files
on the server to do this task.

## About this task

- Automatic deletion never removes named snapshots.
- Performing a cleanup also deletes the associated instances.
- Because automatic deletion randomly chooses which process applications
and toolkits to work on, specify a duration that is long enough to
process all the active projects in your Workflow Center.
- Automatic deletion removes unnamed snapshots in chunks of 100 to limit database contention. If
the duration time expires before all the unnamed snapshots are removed, automatic deletion might not
remove all the unnamed snapshots between two named snapshots.
- Automatic deletion runs only when the server is up. If the server is down when the configured
start time occurs, automatic deletion will not run until the next time the deletion feature is
configured to start.
- Delete unnamed snapshots when there are no operations on the Workflow Center and
no connections between the Process Designer and
the Workflow Center.

The feature to automatically delete unnamed snapshots
is controlled by a set of configuration options in the <server>
section of the 100Custom.xml file. The section
begins with the heading <unnamed-snapshots-cleanup-config>.

## Procedure

1. To turn on the automated deletion feature, set <enabled> to true.  The
default setting is false.
2. To set the time of day when you want the automated snapshot
deletion to run, provide a value for <cleanup-start-time>. The time that is used is the local computer time. The
default time is midnight: 23:59:59. The automatic
snapshot deletion process makes intensive use of the database; therefore,
run the process when other demands on the system are low. Running
it during times of heavy use slows the response time for people using
the system.
3. Set <cleanup-duration-minutes> to the
number of minutes that you want the process to run.  The default duration is 5 minutes.
4 To define which snapshots you want to delete, set <clean-after-number-named-snapshots> . Note: For example, imagine that you have a branch with five named snapshots (from V1 to V5). One of therecent snapshots is archived and three unnamed snapshots (going from 1 to 15) were made between eachnamed snapshot and the currenttip:unnamed snapshot 15unnamed snapshot 14unnamed snapshot 13V5.0unnamed snapshot 12unnamed snapshot 11unnamed snapshot 10V4.0 (Archived)unnamed snapshot 9unnamed snapshot 8unnamed snapshot 7V3.0unnamed snapshot 6unnamed snapshot 5unnamed snapshot 4V2.0unnamed snapshot 3unnamed snapshot 2unnamed snapshot 1V1.0 If the snapshot cleanup was run on the example snapshot list withclean-after-number-named-snapshots set to 3, only the unnamed snapshots afterthe third latest named snapshot (skipping archived snapshots) are deleted. Therefore, only the threeunnamed snapshots older than V2.0 are cleaned up, which would be unnamed snapshots 1, 2, and 3.
    - Deleting unnamed snapshots removes some of the change history for your project.
    - Archived snapshots are ignored when calculating the range of snapshots to be deleted.
    - The <clean-after-number-named-snapshots> setting applies at the branch
level. Therefore, you must have at least the set number of named snapshots in one branch that are
not archived for anything to be cleaned up for that branch.

```
unnamed snapshot 15
unnamed snapshot 14
unnamed snapshot 13
V5.0
unnamed snapshot 12
unnamed snapshot 11
unnamed snapshot 10
V4.0 (Archived)
unnamed snapshot 9
unnamed snapshot 8
unnamed snapshot 7
V3.0
unnamed snapshot 6
unnamed snapshot 5
unnamed snapshot 4
V2.0
unnamed snapshot 3
unnamed snapshot 2
unnamed snapshot 1
V1.0
```

If the snapshot cleanup was run on the example snapshot list with
clean-after-number-named-snapshots set to 3, only the unnamed snapshots after
the third latest named snapshot (skipping archived snapshots) are deleted. Therefore, only the three
unnamed snapshots older than V2.0 are cleaned up, which would be unnamed snapshots 1, 2, and 3.

## Example

The relevant section in the 100Custom.xml file looks like this example, which uses default settings:

```
<server>
  <unnamed-snapshots-cleanup-config merge="replace">
   <enabled>true</enabled>
   <cleanup-start-time>23:59:59</cleanup-start-time>
   <cleanup-duration-minutes>5</cleanup-duration-minutes>
   <clean-after-number-named-snapshots>4</clean-after-number-named-snapshots>
  </unnamed-snapshots-cleanup-config>
</server>
```

For more information about changing configuration properties, see the topic Creating a 100Custom.xml configuration file.

## What to do next

The easy way to manage the accumulation of unnamed snapshots
on your Workflow Center server is to enable automated deletion. However, you can
also delete specific unnamed snapshots or archived snapshots. See Deleting unnamed and archived snapshots, manual for details.