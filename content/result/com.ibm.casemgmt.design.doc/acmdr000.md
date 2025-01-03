# Resetting the test environment

## Before you begin

After the reset actions
complete, the system administrator can reset the timeout values and heap sizes to the previous
values.

## About this task

Over time, you might need to reset the development environment
to provide a clean environment for further development and testing.
Resetting the test environment returns the project area in the case
management object store to the same state as just after you completed
the configuration tasks. The target object store and the connection
point that is associated with the project area are reinitialized,
and all process configuration information is removed.

Since different people in the development environment on multiple projects, you can define
project areas to limit the effects of resetting the test environment. For example, you can group
users that are working on related solutions in the same project area. Therefore, when you reset the
test environment, only the solutions and artifacts in one project area are removed. The entire
design object store is not affected, and other Case Builder users can continue working
without interruption.

- FileNet® P8 assets that you
copied from your production environment
- Any assets that you defined outside of Case Builder to extend the solution design,
such as reused class definitions or property templates. If your environment reuses existing FileNet P8 assets to provision the
development environment, and the development environment is prepared as described then, you can use
the reset test environment operation to restore some assets automatically.

You might need to reset the environment in the following situations where modifications can be
applied only to a fresh development target object store:

- Some changes are not allowed as part of solution redeployment.
- Artifacts from deployed solutions cannot be deleted by using Case Builder. For example, any documents
that were defined in the object store must be removed by using other
tools.
- The development environment target object store might exceed the
underlying database table limitations.

## Procedure

To reset the test environment:

1. Make sure that other applications, such as Case Client or Administration Console for Content Platform
Engine, are not making
changes to the target object store or querying the project area.

Attention: Skipping this step can cause the reset operation to fail.
2. Save user-defined assets from the target object store.
You might have to ask a system administrator to save the assets.
3. In Classic Case Builder,
click the three vertical dots > Reset Test
Environment on the Manage Solutions page.
4. If you are using Case Analyzer,
use the Reset database option of the Case Analyzer Process Task Manager to
initialize the Case Analyzer
database.

As an administrator, you can also use the Case administration
client to reset the test environment by the following steps:

1 Go to DesignObjectstore and do the following steps: Note: The case process integration data is not removed from the processserver. For the manual steps to delete the BAI indexes after reset test Environment https://supportcontent.ibm.com/support/pages/node/7060778
    1. In the project area, select the project area.
    2. Right click on the project area and select Reset test
environment
    3. Click Finish after completing the steps 1 and
2.

- Saving user-defined assets before you reset the test environment

You can use IBM FileNet Deployment Manager to save assets from the target object store before you reset the IBM Business Automation Workflow development environment project area.