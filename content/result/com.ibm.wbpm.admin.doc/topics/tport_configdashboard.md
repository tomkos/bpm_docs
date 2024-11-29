# Configuring the My Team Performance dashboard for Process Portal (deprecated)

## Before you begin

These configuration settings apply only to the deprecated My Team Performance dashboard (known as
the My Team Performance scoreboard in releases earlier than IBM® BPM V8.0). This dashboard is deprecated in IBM BPM V8.5 and later, and in IBM Business Automation
Workflow. It is not enabled by default.

- Workflow Center server
- IBM Workflow
Server

## About this task

To configure the dashboard settings, update the PROFILE\_HOME\config\cells\cell\_name\nodes\node\_name\servers\server\_name\process-server\config\100Custom.xml configuration
file.

To include tasks that are assigned directly to
users in the manager's groups, even if the tasks were not initially
assigned to the group, set the value of the element for user-assigned
tasks to true.

To include tasks that
are assigned to related groups, set the value of the element for related
groups to true. A related group is a group
that any user in a manager's group also belongs to.

## Procedure

1. Open the 99Local.xml and 100Custom.xml files
in a text editor. Important: Do not edit the 99Local.xml file.
Change only the 100Custom.xml file.
2. Copy the appropriate section from the 99Local.xml file
to the 100Custom.xml file. <properties>
		<server merge="mergeChildren">
			<portal merge="mergeChildren">
				<my-team-performance-task-visibility-for-user-assigned-tasks merge="replace">false</my-team-performance-task-visibility-for-user-assigned-tasks> 
				<my-team-performance-task-visibility-for-related-groups merge="replace">false</my-team-performance-task-visibility-for-related-groups>
				<my-team-performance-max-task-list-size merge="replace">1000</my-team-performance-max-task-list-size>
			</portal>
		</server>
</properties>
3. Save your changes.
4. Start Workflow Center server
or Workflow Server.