# Configuring the application space to enable setting role membership

## About this task

## Procedure

To configure the application space to enable setting
role membership:

1. In Administration Console for Content Platform
Engine,
select the object store to which the solution was deployed, and click Administrative > Workflow System.
2. On the Workflow System tab, click Actions > Configure Workflow Settings.
3. Navigate to the Application Spaces in the left pane, and
highlight the application space that you want to configure.
4. Right click the application space and click Properties.
5. On the Security tab, select Groups.
6. Select the group for which you want to assign permissions,
and move the group to the Selected Users window.
7. Click OK.  Important: Defining role membership does not give users the
rights to process work items in a queue. You must set up the rights
on the queue separately. When setting up your groups, make sure that
all case workers who might be assigned to a role have been granted
Process rights on the role queue.

## Changing role assignments in the application space

- Legal Reviewers: Bob, Srini, Gai
- Legal Reviewers Backup: Sally

The queue for these tasks is called Legal Reviewers. In
this queue, the Legal Reviewers group and the Legal Reviewers Backup
group have Query and Process Rights.

Normally, only the Legal
Reviewers group is assigned to the Legal Reviewers role. However,
during times of heavy workload, the supervisor can add the Legal Reviewers
Backup group to this role. Sally can then help with the Legal Review
tasks when needed.