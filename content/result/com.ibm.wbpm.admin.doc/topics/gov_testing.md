# Traditional: Testing a governance process (deprecated)

## About this task

## Procedure

1. Create a snapshot of the governance process that you are
testing and set it to Released.  It is immediately
available for use. You do not need to notify people that it is released.
2. Optional: Create dummy offline workflow servers
to test governance processes that involve installation.  You
can also use a test workflow server to verify your governance processes.
3. In IBM® Process
Center,
create a dummy process application to use for testing.
4. Select the dummy process application. On the Governance page for the process application, click
the Change link next to the current governance process and select the
governance process that you want to test.
5. Test your changed governance process by making installation
requests or status change requests on the dummy process application.
6 If you encounter an installation failure while testing,follow these steps to recover:
    1. Fix the problems with the governance process that you
are testing.
    2. Create a new snapshot, or if you want to use the same
snapshot for testing, reset the governance association to the default
governance process in the dummy test process application. This latter
action should clear the Installation terminated status messages
if there are any.
    3. Repeat the test.
7. Keep the previous governance process until you are sure
it is not needed.

## What to do next

1. Optional: Delete the dummy offline server and dummy test application.
2. Let the process administrator know that the new process is available
for use.
3. Before changing the governance association to a new governance
process, make sure that any existing governance process instances
are either completed or stopped.

If you encounter a difficulty after putting a governance application
into service, the recovery process is straightforward. Stop or complete
the running instances of the governance process. Then replace the
faulty governance process with a proven governance process or with
the default process until you fix the governance process that caused
the problems.

## Related tasks

- Traditional: Applying a governance process to a process application or snapshot (deprecated)
- Traditional: Migrating a governance process from IBM Business Process Manager V8.0.0 (deprecated)
- Traditional: Creating a governance process for installing a process application (deprecated)
- Traditional: Creating a governance process for the status of a snapshot (deprecated)
- Traditional: Creating a governance process that installs a snapshot when the status changes (deprecated)
- Traditional: Changing a governance application (deprecated)
- Traditional: Exporting and importing a process application that uses customized governance (deprecated)
- Traditional: Recovering if a process application under governance fails to install (deprecated)
- Traditional: Removing governance to install a snapshot on Workflow Server (deprecated)

## Related reference

- Traditional: Governance service flows (deprecated)