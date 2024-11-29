# Upgrading solutions in Case Builder

## About this task

## Procedure

To upgrade a solution:

1. Start Case Builder.
2. When you are prompted to confirm whether you want to upgrade a previously imported
solution to a newer level, click the Upgrade button. The solution is upgraded
in the background. After the upgrade process completes, a completion message is displayed in the
status bar and the solution is opened in edit mode.
3. Close the upgraded solution or continue with customizing the solution. To customize the
solution, you can edit the solution now or click Edit at another time to edit
the solution later.
4. After you edit the solution, click Commit to commit all of your
changes.
5. Deploy the upgraded solution.
6. Test the solution in the default IBM® Business Automation
Workflow web
application.

## What to do next

In IBM Business Automation
Workflow, changes
that you make to case property values are synchronized in the in-basket. You might experience
performance issues if all property updates are set to synchronize automatically. To improve
performance, you might want to disable automatic synchronization for properties that are not
frequently updated.

After you upgrade a solution, you can use Process Designer in Case Builder to disable the
synchronization of case properties that you do not want to automatically synchronize. For details,
see Configuring the in-basket property synchronization settings.