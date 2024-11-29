# Granting access to the Workflow Center repository

## About this task

- Business Automation Workflow internal
groups created in the Process Admin console.
- The user repository that was configured for the Business Automation Workflow environment.

The best way
to manage access to the Workflow Center and
its repository is by using groups. For example, the easiest way to
manage access to the Workflow Center repository
is to add preexisting groups of users from your external user repository
to tw\_authors, which is an Business Automation Workflow group
whose members have access to the repository by default. Then, when
changes are required, you can add or remove individual users from
the groups that exist in your external user repository. This practice
ensures that the security maintenance that you complete in your external
user repository does not require more work in Business Automation Workflow.

## Procedure

To grant access to the Workflow Center repository:

1. In Workflow Center,
click the Admin option.
2. Select the Manage Users option,
and then click Add Users or Add
Groups.
3. In the window, enter the name of the user or group that
you want to add in the Search for Name field.
You can enter part of the name and all accounts that match are displayed.
For information about recognizing new groups added to the external
user repository, see the topic Synchronizing external users and groups.
4. Click the check box next to the users and groups that you
want to add, and click Add Selected.

## Results

- Ability to view the online and offline servers in Workflow Center
- Ability to connect to Workflow Center from Process Designer

Adding users to the tw\_author group grants
them write permission, which gives them the ability to import or create
new process applications and toolkits. By default, users have administrative
rights to the application or toolkit they create or import.