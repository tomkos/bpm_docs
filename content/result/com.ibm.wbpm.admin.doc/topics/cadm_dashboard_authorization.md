# Process Portal dashboards:
Authorization overview

## Access to Process Portal dashboards

Access to the Team Performance and Process Performance dashboards is determined by the teams who
are assigned to the dashboards in the Heritage Process Portal application. These teams and the default security groups that are assigned to them are defined in
the System toolkit. You can change the default security groups or members of the team in the Process
Admin Console.

| Dashboard           | Team          | Security groups in the team                                                                                                                                                                                                                                                                                                                                  |
|---------------------|---------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Process Performance | Process Owner | tw\_process\_owners  tw\_allusers Attention: All users typically need access to the dashboard so that they can navigate to the details for a process instance. If you want to restrict access to process owners only, use the Process Admin Console to remove the tw\_allusers group from the Heritage Process Portal snapshot (Installed Apps > Team Bindings). |
| Team Performance    | Managers      | tw\_managers   Attention: The tw\_managers group includes the tw\_allusers group by default. If you want to restrict access to a set of manager users only, use the Process Admin Console to remove the tw\_allusers group from the  Heritage Process Portal snapshot and include the set of managers (Server Admin > User Management > Group Management).       |

## Actions in the Process Performance dashboard

To
manage a process and its instances, users require authorization to
access the individual process and they must be authorized for actions
on the process and its instances.

| Action                                                                                     | Authorization                                                                                                                                                                                                                                                                                              |
|--------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Access the dashboard for a specific process and its instances                              | A member of the team that is assigned to the Expose Performance Metrics setting for the business process in Process Designer.                                                                                                                                                                              |
| Act on a process instance, for example, change the projected path or the instance due date | A member of the security group that is assigned to the following Process Portal action policies: ACTION\_VIEW\_PROCESS\_DIAGRAM  ACTION\_VIEW\_CRITICAL\_PATH ACTION\_CHANGE\_CRITICAL\_PATH ACTION\_CHANGE\_INSTANCE\_DUEDATE  For more information, see Configuration properties for Process Portal action policies. |

## Actions in the Team Performance dashboard

To
manage the work for a team, users must be a member of a team of managers
and they must be authorized for some actions on tasks.

| Action                                                   | Authorization                                                                                                                                                                                                                                   |
|----------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Access the dashboard for a specific team and its members | A member of a team of managers that is defined in Process Designer. For more information, see Defining team managers.                                                                                                                           |
| Change the due date or the priority of a task            | A member of the security group that is assigned to the following Process Portal action policies: ACTION\_CHANGE\_TASK\_DUEDATE ACTION\_CHANGE\_TASK\_PRIORITY  For more information, see Configuration properties for Process Portal action policies. |

The tw\_allusers\_managers group is the security
group for the Managers of All Users team. This security group includes
the tw\_admins group by default. Members of the tw\_admins group can
therefore see the All Users team and the sample teams in the Team
Performance dashboard. To remove the tw\_admins group or add members
to the tw\_allusers\_managers group, use the Process Admin Console.