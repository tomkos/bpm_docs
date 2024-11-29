# Running the process in the Process Designer Inspector view

## About this task

## Procedure

1. In Process Designer, click the
Run icon ().
The Inspector opens and displays the Process Instances view, as shown in the following figure:
The Process Instances view display the status of the process and its tasks. In the
process diagram, the process flows from task to task.
2. In the Process Instances view, expand the Tasks section. The
Submit job requisition task is displayed, which is a task for the hiring
manager.
3. Next to the Submit job requisition task, click the
Start icon (). The Job Requisition Data page opens in a browser window and presents the requisition data
for the hiring manager.
4. In the Education, Skills, and
Experience tabs, select one or more entries.
5. Review the data and then click Next. The Confirm Position Request page
opens.
6. Click Submit. The page closes and the browser window displays the
message The service has finished.
7. Close the browser window that displays the message The service has finished.
8. In the Process Instances view, click the Refresh icon (). In the Data section of the Process Instances view, the specified
values are displayed for the parameters. And in the Tasks section, the
Submit job requisition task for the hiring manager is now closed and a new
Approve / reject requisition task is displayed for the general manager
(GM).
9. Next to the Approve / reject requisition task, click the
Start icon. The New Position Approval page opens.
10. In the page, change the approval status to Approved.
11. Click Submit. The page closes and the browser window displays the
message The service has finished.
12. Close the browser window that displays the message The service has
finished.
13. In the Process Instances view, click the Refresh icon. In the
Tasks section, the Approve / reject requisition task
for the GM is now closed. The next task in the process is the
FindCandidatesList task for Human Resources (HR), but this task started
automatically and is now closed, as shown in the Tasks section.

The FindCandidatesList task triggers an advanced integration service (AIS)
that is integrated through Service Component Architecture (SCA). The service is implemented by
calling a number of (simulated) back-end systems orchestrated in a BPEL process. This advanced
integration service was developed in IBM Integration
Designer
and, for simplicity, it was implemented within the process application. The advantage of
implementing an advanced integration service in a process application or toolkit is that source
control, deployment, and versioning is managed from the Workflow Center. A disadvantage is that the process application
or toolkit may need to be redeployed to the Workflow Center server before each playback. An alternative is
to implement the advanced integration service in a separate SCA module, but that is beyond the scope
of this sample. For more information, see Implementing an Advanced Integration service.
14. In the Tasks section, find the new Select candidate for
interview task for the hiring manager, then click the Start icon.
The Present Candidates List page opens.
15. As the hiring manager, review the information about the candidates and then select the radio
button next to one of the candidates.
16. Click Select Candidate. The page closes and the browser window displays
the message The service has finished.
17. Close the browser window that displays the message The service has
finished.
18. In the Process Instances view, click the Refresh icon. In the
Tasks section, the Select candidate for interview task
for the hiring manager is closed and the process has now completed, as shown in the following
figure:

## Results

## Related concepts

- Overview of the Advanced Hiring tutorial
- Examine the Advanced HR Open New Position process

## Related tasks

- Managing access to the Hiring Sample Advanced process application
- Verifying access to the Hiring Sample Advanced process application
- Activating the Hiring Sample Advanced process application
- Opening the Hiring Sample Advanced process application