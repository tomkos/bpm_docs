# Verifying restored data

## About this task

- System
- Module and application
- Process instance
- Consistency
- SCA
- Monitoring

A failure, loss of data, or inconsistency from the process instance level can be tolerated.
However, an abnormal state from the system level or application level  must be fixed because the
backup is invalid.

Generally, verification is relatively simple for
the system, module, and application levels. Verification of the instance
level can be more difficult because the number of instances might
be large. Use a real runtime scenario for the disaster recovery test,
which takes the backup of the running instances and verifies that
the specific instances are working properly.

## Procedure

To verify that the restored data in the secondary environment
is valid, complete the following steps:

1. Verify that the system-level services such as the Business
Process Choreographer container and the Human Task Manager container
are working properly. Verify that the messaging engines for various
buses can be started successfully. To perform these verifications,
you can use the System Health widget in Business Space.
2. Verify that the modules and applications can be started
successfully. Verify that the process templates can be started normally.
3. Verify that the process instances are in a consistent state.
Some backups might not work properly after restoration. You
must identify and discard those backups and use only the valid ones.Figure 1. Backup to a remote storage system
4. Verify that the process instance state is correct.
5. Verify that synchronous and asynchronous invocation for
Service Component Architecture (SCA) can continue for processing.
6. Verify that you see new instances in your monitor dashboards
when you run new process instances.