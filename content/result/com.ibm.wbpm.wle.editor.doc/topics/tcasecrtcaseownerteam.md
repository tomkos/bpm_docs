# Assigning teams to a process

## About this task

To run a process that uses
the FileNet® Connector
Add-On to
manage documents and folders, you must install the FileNet ECM Connector
Add-On feature.

At run time, you can start an instance of your process, and users can view and start the
activities in the activity list in Process Portal. The Expose to start option determines the users who can start the
instance. The instance owner team identifies the users who can work with the process. For example,
for the Manage Dispute process you might create an instance owner team called Customer Service
Representatives.

## Procedure

1. Open the process for which you want to assign teams.
2. Click the Overview page.

To assign the team of users that can start a process instance:

1. Select a team for the Expose to start option. You can also create
a new team here. See Creating a team.

To assign the team of users that can work on the process:

1. Select a team for the Instance owners option. You can also create
a new team here. See Creating a team.
2. Click Save or Finish Editing.

- Process instance owners team

Instance owners team is an authorization role that enables associated users to administer instances of a specific process. An instance owners team is used to manage the task instances or documents of a process instance or the process instance itself.
- Assigning a process activity to a dynamically retrieved team

If you do not want to assign a process activity to a static team, you can define a team retrieval service that dynamically returns a set of users and managers.