# Process Portal
dashboards

The following ready-to-use dashboards are included in Process Portal and available to you
if you have the appropriate authorization. For more information about the different types of
authorization, see Dashboards in Process Portal. For dashboards to work correctly, Process Portal indexing must be
enabled. For more information, see Configuring the Process Portal index.

For a list of action policies, see Configuration properties for action policies.

| Dashboard           | Usage                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Required authorization                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|---------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Work                | Shows your claimed tasks and all the unclaimed tasks that are assigned to your team. You can filter tasks lists and create saved searches.                                                                                                                                                                                                                                                                                                                                                                 | You must be a member of the team who can claim tasks that belong to the process instance. Rights on saved searches can be restricted to some users or groups of users. For more information on searches in the Work dashboard, see Searches and saved searches.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Next Task           | The Next Task dashboard is a variant of the Work dashboard. Use it to display your tasks one by one. Each time you complete a task, only the subsequent one is displayed next, based on the default saved search or on the saved search that you specify. By default, the Next Task dashboard is hidden. If you choose to display it, this dashboard replaces the Work dashboard, which is no longer accessible to the user.  To learn how to configure this dashboard, see Configuring custom properties. | You must be a member of the groups that are authorized to use this dasboard.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Processes           | Shows lists of active and completed process  instances. You can use search filters to reduce the number of instances in the list. To see more information about a process instance, click the instance name.                                                                                                                                                                                                                                                                                               | You can see a specific instance if you are in one of the following situations: Be a member of the instance owner team. Own a task in the instance, be a member of the team who can claim tasks that belong to the instance, or be the manager of this team. Note: If you have defined a team filter service or additional options (for example, "last user"), you see process instances if you are a member of a group that is defined for task assignment in the process model.  Be a member of the team that is assigned to the Expose Performance Metrics setting for the business process definition.   Traditional:  To see the Gantt Chart icon, you must belong to a security group that is assigned to the ACTION\_VIEW\_PROCESS\_DIAGRAM Process Portal action policy. |
| Process Performance | Shows the status of the active instances of particular processes in your organization. You can act on individual process instances to resolve issues, such as bottlenecks.See The Process Performance dashboard.                                                                                                                                                                                                                                                                                           | To see the Process Performance dashboard, you must be a member of the Process Owner team. To see a specific process, you must be a member of the team that is assigned to the Expose Performance Metrics setting for the business process definition.  Other users can view the process instance that is associated with the task that they are working on.                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Team Performance    | Shows the status of the tasks for teams for which you are the designated team manager. You can manage the work load for the team and for individuals. See The Team Performance dashboard.                                                                                                                                                                                                                                                                                                                  | To see the Team Performance dashboard, you must be a member of the Managers team. To manage a team's tasks, you must be a member of a team of managers.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |

| Dashboard                                                                                        | Usage                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Required authorization                                                                                                                                                                                                                                           |
|--------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| My Performance                                                                                   | Shows the status of your tasks for either a specific group or all the groups that you are a member of. You can also choose a specific business process to analyze or view data for all the processes that you participate in. This dashboard includes the following data: A pie chart that shows the percentage of tasks on target, at risk, or overdue A bar chart that shows when upcoming tasks will become overdue A task list that shows the status for each of your assigned tasks | To see the dashboard, you must be a member of the team that the equivalent scoreboard is exposed to. To view data in this dashboard, you must have open or completed tasks.                                                                                      |
| My SLA Overview                                                                                  | If service level agreements (SLAs) are defined and exposed, this dashboard displays a table that lists the name, description, and status of the SLAs. To display a trend chart that shows the violations for selected SLAs, you select one or more of the SLAs.                                                                                                                                                                                                                          | To see the dashboard, you must be a member of the team that the equivalent scoreboard is exposed to.                                                                                                                                                             |
| Deprecated: My Team Performance                                                                  | Shows the status of the tasks assigned to the groups for which you are the designated manager in the Process Admin console. The dashboard includes the following data: A pie chart that shows the percentage of tasks on target, at risk, or overdue A bar chart that shows when upcoming tasks will become overdue A task list that shows the status for each of the team's assigned tasks                                                                                              | To see the dashboard, you must be a member of the team that the equivalent scoreboard is exposed to. To access this dashboard, you must be a manager of a team.                                                                                                  |
| Deprecated: My Process Performance dashboard that is based on the Process Performance scoreboard | Shows the status of the active instances of particular processes in your organization. The dashboard includes the following data:  A pie chart that shows the percentage of tasks on target, at risk, or overdue for the active instances A trend chart of the number of active instances over the last week                                                                                                                                                                             | To see the dashboard, you must be a member of the team that the equivalent scoreboard is exposed to. To see a specific process, you must be a member of the team that is assigned to the Expose Performance Metrics setting for the business process definition. |

- The Process Performance dashboard

 You can use the Process Performance dashboard in Process Portal to get an overview of the processes that you are responsible for. You can identify processes that need attention, go to individual instances, and act to bring them back on track.
- The Team Performance dashboard

 You can use the pages in the Team Performance dashboard to manage the work of the team members that you are responsible for. From the dashboard, you can see whether your team is catching up or falling behind on its work.