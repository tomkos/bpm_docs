# Setting variables in pre and post assignments

## About this task

You can set pre and post assignments for activities in a process.

For
example, if you want to send an email message to end users as soon
as an activity is active and can be completed, you can attach a timer
event to the activity and use a post assignment to place the task
ID into a variable so that it can be passed to the follow-on activity
that sends the email message. The task ID is needed so that the email
message sent to end users includes information about the task to complete.
You can achieve this by using a post-assignment.

## Procedure

1. Open a process that includes an activity or event that requires a pre assignment or a post
assignment.
2. Click the activity or event in the process diagram and then select the Pre &
Post option in the properties.
3. To add an assignment, click the Add assignment icon
() in either the Pre Assignments section
or the Post Assignments section.
4. In the field on the left, click the variable icon to choose a variable that you have
declared in the current process that will receive the value.
5. In the field on the right, type the variable name that
will be used as value for the variable in the left field.   Tip: You can type any existing variable name. Use the type-ahead
feature to select your variable, you do not have to limit yourself
to local variables.
When you set a pre or post assignment for an activity, the activity in the diagram includes a
circular indicator on the left side (pre assignment) or on the right side (post assignment).