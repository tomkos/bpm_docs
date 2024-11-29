# Reassigning a task to a new group

## About this task

When a group or team is updated, the associated manager team is also updated. If you assign a
task to a team, the team must exist in the version or snapshot scope that is currently associated
with the task.

If you are considering reassigning a task to a group, it is generally recommended that you
reassign the task to a team from the task's current version or snapshot context.

If a task is reassigned to a group that is associated with a different version or snapshot than
the task, it can cause problems for the version or snapshot deletion. The instructions in this help
topic can be used to replace an ad hoc group that might be blocking the deletion.

If a task is reassigned to a group that does not have a manager team, the task's manager team
will be cleared. In releases earlier than 20.x, the assigned manager team is only changed when the
task is reassigned to a group that has a manager team.

## Procedure

To reassign a task to a new team:

1 Select one of the following approaches:
    - If you want to reassign a task to a new team by using REST APIs, build a client applicationor use the REST API test tool to perform the required operations. For information about using theREST API test tool, see Testing the IBM BPM REST APIs . You can review the teams for aversion or snapshot by using the Designer or the Install Apps tab of theProcess Admin Console . The steps thatyou would follow to reassign a task to a new team by using REST APIs differs depending on theproduct version:
        - In IBM® Business Automation
Workflow 20.0.0.2
and later, use the Task Instance resource PUT (assign task) method to assign the task to the new
team. You should pass the name using the toTeam parameter. For
example:PUT /rest/bpm/wle/v1/task/1234?action=assign&toTeam=HiringManagers&parts=allFor
more information, see REST interface for BPD-related resources - Task Instance Resource -
PUT (assign task) Method.
        - In IBM Business AutomationWorkflow V20.0.0.1and earlier, complete the following steps:
            1. To obtain detailed information about a task, such as its current version or snapshot context,
use the Task Instance resource GET method that is described in the topic  REST interface for BPD-related resources - Task Instance Resource -
GET Method.
            2. Obtain the internal team name by running the following SQL query (where
'team\_name' is the name of the team that you want to use and
'snapshot\_id' is the snapshot ID from the current task
context):Select g.group\_name from LSW\_USR\_GRP\_XREF g, LSW\_PARTICIPANT\_GROUP t Where g.group\_id = t.group\_id AND g.display\_name = 'team\_name' AND t.snapshot\_id = 'snapshot\_id'The
snapshot ID is the GUID that follows '2064.' in the task details.
            3. Use the Task Instance resource PUT (assign task) method to assign the task to the new team. You
should pass the name using the toGroup parameter. For
example:PUT /rest/bpm/wle/v1/task/1234?action=assign&toGroup=HiringManagers\_S\_cd97937f-06ab-43cc-8067-17dea489fdb3.481abfd8-9868-4638-ace0-7932d46958d5&parts=allFor
more information, see REST interface for BPD-related resources - Task Instance Resource -
PUT (assign task) Method.
- If you want to reassign a task to a new team by using JavaScript APIs, build a service that
is able to run the required JavaScript API methods. The following example shows how task
1234 is reassigned to the team
MyNewTeam:var task = tw.system.findTaskByID(1234);
task.reassignTo(task.processInstance.snapshot.findParticipantGroupByName("MyNewTeam").associatedRole);For
detailed information about the JavaScript APIs, see JavaScript API in processes and service flows.
2. Confirm that the task is now reassigned to the specified team.