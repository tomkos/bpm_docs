# BPMProcessInstancesPurge command

<!-- image -->

## Prerequisites

- Run the command in the connected mode, that is, do not use the
wsadmin -conntype none option.
- To run this command, you must be a user in
the DeAdmin role. In a network deployment environment, you must run
this command on the node that contains the application cluster member
that handles Workflow Server applications.
Do not run this command from the deployment manager profile.
- You cannot use this command to delete BPEL
processes.
- You can run the command from any cluster member in a network deployment
environment. However, you must first establish the wsadmin session
to the SOAP port of the cluster member from where you are running
the command.

## Location

Start the wsadmin scripting client from the install\_root/bin directory.

## Syntax

```
BPMProcessInstancesPurge
-instanceStatus instance\_statuses
[-containerAcronym process\_application\_acronym]
[-containerSnapshotAcronym process\_application\_snapshot\_acronym]
[-endedAfterLocal local\_time\_on\_the\_server]
[-endedBeforeLocal local\_time\_on\_the\_server]
[-instanceID instance\_ID]
[-maximumDuration number\_of\_minutes]
[-outputFile file\_path]
[-transactionSlice number\_of\_instances\_to\_delete\_in\_a\_transaction]
[-force]
```

## Parameters

- COMPLETED - Removes all completed process instances.
- TERMINATED - Removes all terminated process instances.
- FAILED - Removes all failed process instances.
- DID\_NOT\_START - Removes all process instances
that are in the did not start state.
- SUSPENDED - Removes all suspended process instances.
- ACTIVE - Removes all active process instances.
- ALL - Removes all process instances.

## Using the BPMProcessInstancesPurge command

The
following sections provide some illustrative examples of using the
command.

## Example: Deleting instances and associated tasks

```
wsadmin -conntype SOAP -port 8880 -host ProcessServer01.example.com -user admin -password admin -lang jython 

wsadmin>AdminTask.BPMProcessInstancesPurge('[-containerAcronym PA435 -containerSnapshotAcronym V1 -instanceStatus FAILED -outputFile C:\US58626\log1.txt]')

wsadmin>AdminTask.BPMProcessInstancesPurge('[-containerAcronym PA435 -containerSnapshotAcronym [V1 V2] -instanceStatus FAILED -force -outputFile C:\US58626\log1.txt]')
```

## Example: Deleting instances, based on the instance
ID

```
wsadmin -conntype SOAP -port 8880 -host ProcessServer01.example.com -user admin -password admin -lang jython 

wsadmin>AdminTask.BPMProcessInstancesPurge('[-containerAcronym BILLDISP -containerSnapshotAcronym SS2.0.1 -instanceStatus TERMINATED -instanceID [4 5 1001 1002]]')
```

## Example: Deleting instances that completed or terminated
during a specific time period

```
wsadmin -conntype SOAP -port 8880 -host ProcessServer01.example.com -user admin -password admin -lang jython 

wsadmin>AdminTask.BPMProcessInstancesPurge('[-containerAcronym BILLDISP -containerSnapshotAcronym SS2.0.1 
          -instanceStatus ALL -endedAfterLocal 2015-01-01T00:00:00 -endedBeforeLocal 2015-02-31T21:37:06]')
```

## Sample entries in SystemOut.log to confirm that the
command ran

```
wsadmin>AdminTask.BPMProcessInstancesPurge('[-containerAcronym HSS -instanceStatus TERMINATED 
      -endedBeforeLocal 2016-11-02T21:37:06]')'The BPMProcessInstancesPurge command passed.'
```

```
[11/1/16 14:22:45:532 PDT] 000001cc CommandServic I PALAdminCommands otherProcessInstancesPurge Entering
[11/1/16 14:22:45:553 PDT] 000001cc Log           I   PAL: About to delete the process instances matching the filter criteria: 
SnapshotIDs: [Snapshot.f1659d94-2365-4903-8a90-9fa62f3ccc97, Snapshot.95fb38c2-50b4-4ba7-b3e9-24e72254233b]
Statuses: [4]
Ended before: 2016-11-02 21:37:06.0
Maximum duration: 0
Transaction slice: 10

[11/1/16 14:22:45:554 PDT] 000001cc Log           I   PAL: Number of qualifying instances before deletion: 1
[11/1/16 14:22:45:664 PDT] 000001cc Log           I   PAL: A deletion job is running. Progress: Deleted 1 instance(s).
[11/1/16 14:22:45:665 PDT] 000001cc Log           I   PAL: Every instance has been deleted. The deletion job finished.
[11/1/16 14:22:45:676 PDT] 000001cc Log           I   PAL: Successfully deleted the process instances matching the filter criteria: 
SnapshotIDs: [Snapshot.f1659d94-2365-4903-8a90-9fa62f3ccc97, Snapshot.95fb38c2-50b4-4ba7-b3e9-24e72254233b]
Statuses: [4]
Ended before: 2016-11-02 21:37:06.0
Maximum duration: 0
Transaction slice: 10

[11/1/16 14:22:45:677 PDT] 000001cc Log           I   PAL: Number of qualifying instances before deletion: 1
[11/1/16 14:22:45:689 PDT] 000001cc Log           I   PAL: Number of qualifying instances after deletion: 0
[11/1/16 14:22:45:693 PDT] 000001cc CommandServic I PALAdminCommands otherProcessInstancesPurge Exiting
```

## Performance tuning of the instance purge

The default value is 10. It controls the number of threads to run instance purge when
purge-instances-in-multi-threads is set to true. For the traditional
environment in Business Automation Workflow,
instance purge uses the thread pool that DefaultWorkManagerconfigures.

To make sure the thread pool of DefaultWorkManager is configured properly for
the instance purge, open WebSphere Integrated Solutions Console in your browser, expand
Resources > Asynchronous beans
and click Work managers. Then locate the
DefaultWorkManager, which has the same scope as
bpm-em-workmanager, and click the
DefaultWorkManager. Check Growable so that this thread
pool can grow. You can increase this number if enough resources are in the Business Automation Workflow server and database
server to speed up the instance purge.

- When both of these two properties are 0 or a positive number, Business Automation Workflow cleans up only sharedbusiness objects in the database within time range that is specified by these two properties. For example: Then Business Automation Workflow cleansup only the shared business object data between 5 PM to 7 AM the next day.
    - orphan-sbo-cleanup-start-hour = 17
    - orphan-sbo-cleanup-end-hour = 7

Then Business Automation Workflow cleans
up only the shared business object data between 5 PM to 7 AM the next day.

- When any of these two properties are negative number, Business Automation Workflow tries to clean up shared
business object at all times. It might impact Business Automation Workflow performance in Process
Portal or Workplace. To
improve performance, these two properties can be set to run during nonbusiness hours.
- The parameters orphan-sbo-cleanup-daemon-interval or
orphan-sbo-cleanup-daemon-interval-for-idle control the frequency.

```
<server>
     <bpd-engine>
          <sbo-deletion-tuning merge="replace">true</sbo-deletion-tuning>
          <purge-instances-in-multi-threads merge="replace">true</purge-instances-in-multi-threads>
          <num-of-threads-to-purge-instances merge="replace">10</num-of-threads-to-purge-instances>
          <process-instances-cleanup-helper-daemon-interval merge="replace">600</process-instances-cleanup-helper-daemon-interval>
          <delay-update-process-instances-cleaned-on-timestamp merge="replace">true</delay-update-process-instances-cleaned-on-timestamp>
          <orphan-sbo-cleanup-start-hour merge="replace">17</orphan-sbo-cleanup-start-hour>
          <orphan-sbo-cleanup-end-hour merge="replace">7</orphan-sbo-cleanup-end-hour>
          <orphan-sbo-cleanup-daemon-interval merge="replace">15</orphan-sbo-cleanup-daemon-interval>
          <orphan-sbo-cleanup-daemon-interval-for-idle merge="replace">600</orphan-sbo-cleanup-daemon-interval-for-idle>
     </bpd-engine>
</server>
```