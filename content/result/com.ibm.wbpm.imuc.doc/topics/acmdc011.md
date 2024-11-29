# Configuring queues to allow users to process work items

## Procedure

Note: Security for running work items that are associated with task objects in the
content store are configured with service groups along with security on queues and rosters.
To
configure queue permissions:

1. In Administration Console for Content Platform
Engine,
select the object store to which the solution was deployed, and click Administrative > Workflow System.
2. On the Workflow System tab, click Actions > Configure Workflow Settings.
3. From the Workflow Systems list,
select the connection point for the project area where the solution
application resides.
In the Action menu,
click Connect to log on to the workflow system.
4. Navigate to the work queue in the left pane, and highlight
the work queue you want to configure.
5. Right click the work queue and click Properties.
6. Click the Security tab, and select Groups.
7. Select the group for which you want to assign permissions,
and move the group to the Selected Users window.
8. Set the Default rights, and click OK.

## Example

| Group               | Permissions                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|---------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Case viewers        | None. In most situations, a member of the case viewer user group does not need to view work items, but instead might search for and view cases. Therefore, those users will have the right to view only the case objects in Content Platform Engine. If a member of the case viewer user group needs to see work items in a queue without opening or processing them, then those users must have Query permissions. If a user with only Query permission tries to open a work item, an error occurs. |
| Case initiators     | Query and Process, but only if case creators must also view and process work items.                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Case workers        | Query and Process Each role is associated with an LDAP group or groups. Any users who must process work items in that role must be in a group given Query and Create rights to the role queue. For example: Users in the Clerks role are added to the Clerks group. The Clerks group is given Query and Process rights to the Clerks queue. Users in the Supervisors role are added to the Supervisors group, which is given Query and Process rights to the Clerks queue.                           |
| Case administrators | Query and Process A case administrator requires Query rights, but might also require Process rights if they must troubleshoot work items.                                                                                                                                                                                                                                                                                                                                                            |

- Queue permissions

Queue permissions determine what actions a user can take on a queue. Typically, case workers need both Query and Process permissions on the role Queue.