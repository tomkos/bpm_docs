<!-- image -->

# Creating an escalation for your human task

## About this task

- The state that the task is in when the escalation period begins
(this is also known as the activation state).
- The state that you want the task to be in when the escalation
period ends (it is when the task is NOT in this expected state at
the end of the period that the actual escalation is thrown).
- The escalation period, or how long you want the system to wait
for the expected state to be reached before notification occurs.
- The manner in which the notification takes place.

## Procedure

1. Launch your human task in the editor.
2. Under Escalation settings, choose
the activation state from the following three options:

Option
Description

Ready 
When a task is in the ready state, it is waiting to be claimed.
Configure the escalation settings to notify an authorized staff member
should nobody claim it within the specified period of time.

Claimed 
When a task is in the claimed state, a staff member has accepted
the work and should currently be working on it. Configure the escalation
settings to notify an authorized employee should the staff member
fail to complete the work within the specified period of time.

Subtask 
A task is in the subtask state when the owner of the parent
task must delegate part of the task to other staff members. Configure
an escalation for a subtask to make sure that it can be completed
in time enough for the parent task to be finished as well. If the
subtask cannot be completed within the required amount of time, the
parent task is escalated and indicates that it is still waiting on
the subtask.
3. Click the Escalation icon  to
create a new escalation for the chosen activation state. A
new escalation appears below the selected activation state.
4 To add additional escalations to this activation state,proceed in one of the following two ways:
    1. To create a chained escalation, select an existing
escalation and click the Escalation icon. 
A new escalation appears below the existing escalation.
    2. To create a parallel escalation, select an the
activation state, and click the Escalation icon. 
A new escalation appears beside the existing escalation.
5 In the Details page of the propertiesarea, configure the implementation as follows: Option Description Expected task state Use this field to specify the state in which the task should be when the escalation times out. If the task is not in the state specified, then an escalation is thrown.You will have the three following options: Escalate after Use these fields to specify the period of time that will elapse before this task is escalated. You can enter the values using the spin boxes provided, or click the secondary radio button and enter a value that makes sense to the type of calendar (simple, WebSphere® CRON, user-defined) that is specified in the task's Duration properties page. Notification type Use this list to tell the system how to deal with this escalation. You will have three options: email message Use this field to select the email message that will be delivered to the designated staff member in the event of the escalation. You can create a new message, or select an appropriate message from the list and click Edit to make any necessary changes to it. Repeat notification every Use these fields to specify the period of time that will elapse before the notification associated with this escalation is repeated. You can enter the values using the spin boxes provided, or click the secondary radio button and enter a value that makes sense to the type of calendar (simple, WebSphere CRON, user-defined) that is specified in the task's Duration properties page. Increase task priority Use this list to determine if and how this escalation's priority will change with each iteration of it.You will have three options:

| Option                    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|---------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Expected task state       | Use this field to specify the state in which the task should be when the escalation times out. If the task is not in the state specified, then an escalation is thrown.  You will have the three following options:  Ended Choose this as the expected end state when you want an escalation initiated if the task is not complete by the end of the escalation period.   Claimed Choose this when you want an escalation initiated if, at the end of the escalation period, the task has not yet been claimed by a user.   All subtasks ended Choose this as the expected end state when you want an escalation initiated if the subtasks associated with this task have not been completed by the end of the escalation period.                                                         |
| Escalate after            | Use these fields to specify the period of time that will elapse before this task is escalated.   You can enter the values using the spin boxes provided, or click the secondary radio button and enter a value that makes sense to the type of calendar (simple, WebSphere® CRON, user-defined) that is specified in the task's Duration properties page.                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Notification type         | Use this list to tell the system how to deal with this escalation.   You will have three options:  Work item Choose Work item to have the task delivered directly to a designated staff member's "to do" list. Since a work item is always created in an escalation, this setting creates a work item, and nothing else.   email Choose email to have an email message that announces the escalation delivered to a staff member. Once you select this option, a separate field will appear from which you can choose an appropriate email message.   Event Choose Event if you want to trigger an event handler in the runtime environment. If you select this option, you then have to specify the event handler in the Event handler name field in the task's Details properties page. |
| email message             | Use this field to select the email message that will be delivered to the designated staff member in the event of the escalation. You can create a new message, or select an appropriate message from the list and click Edit to make any necessary changes to it.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Repeat notification every | Use these fields to specify the period of time that will elapse before the notification associated with this escalation is repeated.   You can enter the values using the spin boxes provided, or click the secondary radio button and enter a value that makes sense to the type of calendar (simple, WebSphere CRON, user-defined) that is specified in the task's Duration properties page.                                                                                                                                                                                                                                                                                                                                                                                            |
| Increase task priority    | Use this list to determine if and how this escalation's priority will change with each iteration of it.  You will have three options:  No Choose No to leave the priority unchanged.   Increase this time only Choose this if you only want it to boost the priority with one iteration.   Increase per repetition Select this if you want the priority augmented each time this escalation is repeated.                                                                                                                                                                                                                                                                                                                                                                                  |

6. In the Assign People page of the
properties area, you can define the staff group (criteria) and in
so doing, specify the group of people that are notified should this
escalation be executed.

- Assigning people to escalations

Use the Assign People tab of the properties area to specify the group of people that is notified should this escalation be executed.
- Customizing an escalation email notification

You can use an email message to notify a staff member that they have a work item in the form of an escalation.
- Notifying an event handler of an escalation

You can use customized notification event handlers within your application environment to deal with escalations in your human task model.

## Related tasks

- Selecting a calendar type for your escalation
- Setting duration values for your human task
- Defining timer-driven behavior in a BPEL process
- Using business calendars within human tasks
- Notifying an event handler of an escalation

## Related reference

- Details tab: business state machine editor
- Duration tab: Human Task editor