# Restarting a workflow activity that fails to start

## Symptoms

## Resolving the problem

To restart activities that failed to start, you must first put these activities into a state
where they can be restarted. Then, you can restart the activities.

1. Open Administration Console for Content Platform
Engine, click
Object Stores and select your target object store.
2. Click Search and select New Object Store
Search.
3. In the Class list, select Activity.
4. In the Column list of the Criteria section for row
A, select Activity State.
5. In the Condition list, select Equals To.
6. Enter 6 in the Value column.
7. In the Column list of the Criteria section for row
B, select Last Failure Reason.
8. In the Condition list, select Equals To.
9. Enter CmAcmError Launch Failed in the Value
column.
10. In the Properties list, select * (asterisk).
11. Click the Bulk Actions tab and select Enable, then
scroll down and select Run Script.
12. Enter the following script:
function OnCustomProcess (CEObject) 
          { 
             CEObject.changeState(4194304); 
             CEObject.save(1); 
          }
13. Click Run to run the query and the script.

Now that the activities are in a state where they can be restarted, you can restart the
activities. To restart activities in Business Automation Workflow, you must use the Case
REST API. You restart the activity by issuing a Restart call to the Case REST API in Poster. For
example, issue a Restart call to the Case REST API with the PUT method by using the Poster AddOn for
Mozilla Firefox.

- Container or Compound activity
- Workflow task
- Discretionary activity

- The Content Platform Engine workflow item process completed
(the value of the TaskState property is Completed).
- The Content Platform Engine workflow item process failed to
launch (the value of the TaskState property is Failed and the
value of the LastFailureReason property is CmAcmError Launch
Failed).
- The Content Platform Engine workflow item process failed and
then stopped (the value of the TaskState property is Failed, the
value of the TaskDisabledState property is disabled\_aborted, and
the value of the LastFailureReason property is set to a Content Platform Engine error).
- The Content Platform Engine workflow item process was running
and then stopped (the value of the TaskState property is Failed,
the value of the TaskDisabledState property is disabled\_aborted,
and no value is set for the LastFailureReason property).

Issue a restart call to the Case REST API with the PUT method by using the Poster AddOn for
Mozilla Firefox. Enter the following parameter values in the Request form:

1. Use a tool like the Firebug Console to find a Request URL like the following
example:<PROTOCOL>://<HOST\_NAME>:<PORT\_NUMBER>/CaseManager/CASEREST/v1/case/993D3E31-EB4E-4646-B879-2A56055BA874?tasks?TargetObjectStore=MyExampleObjectStore&Grouping=ROD
2. When you load the Activities tab for a case, extract the TaskId value
from the JSON Response payload for the activity that wants to restart. For example,
Taskid="=7A75A997-0E42-406E-AZC4-EE55D7DER9PF.
3. Use this task ID to build the URL for your restart Request payload. For example,
<PROTOCOL>://<HOST\_NAME>:<PORT\_NUMBER>/CaseManager/CASEREST/v1/task/7A75A997-0E42-406E-AZC4-EE55D7DER9PF?TargetObjectStore=MyExampleObjectStore&Grouping=ROD
4. Enter the URL for your request in the URL field in Poster.

Actions: The Case REST API must be run by using the PUT method.

Content Type: The Content Type of the payload must be
application/json; charset=UTF-8

Content: The Case REST API to restart the activity has a payload like:
{ "Action" : "restart" }