# Creating a team

A team is a group of users that perform similar tasks, and consists of a set of members
and a team of managers. Teams are used to manage the tasks that users can perform in Process Portal
. Because any team can be added as the manager of another team, you can flexibly
define your organization's management structure.

- Assign a team to an activity or a lane in a business process. The users in that team can work
with the tasks that are created for the activities in Process Portal
.
- Provide a team with the authority to view performance data and the
performance dashboards in Process Portal.

## Procedure

To create a team and add members, complete the following steps:

1. In the library, click the plus sign to next to the Teams
category.
2. In the New Team window, enter a name for the team and click
Finish.
3 Select the team members in one of the following ways: Tip: To prevent problems that occur when there is a large number of users in the system,the tw\_allusers user group is ignored for task reassignment. For taskreassignments, add individual users or other groups instead of usingtw\_allusers .
    - Select users or groups that are defined in the user registry.
    - Use a service to dynamically retrieve a team at run time. You can select an existing
service, or you can create a new one. See Setting up a team retrieval service.
4. Select the team of managers that can manage the team's tasks in the Team Performance
dashboard.
5 If you want to simulate a process, set the simulation properties forthe teams that are assigned to the swimlanes in the process model. These settings represent theperformance expectations for the team.

1. Open the Process Designer desktop
editor.
2. Open the team, and enter the simulation properties.
6. Click Save or Finish Editing.

## Results

- Using team services to define dynamic teams

You can use team retrieval services and team filter services to dynamically determine who is eligible to perform activities by using service flows.
- Setting up a team retrieval service

You can define a team retrieval service that dynamically returns a set of users and managers at run time.
- Setting up a team filter service

You can use a team filter service to dynamically prevent certain users from being assigned to an activity. The filtering can be based on any criteria and can use input parameters from relevant process variables to determine which users to filter out.
- Defining team managers

To define who the managers of a team are, you must select a team of managers. In this way, with teams managed by teams, you can define the management structure of your organization.