<!-- image -->

# Create the human task implementation

## About this task

To create the human
task implementation:

## Procedure

1. In the assembly editor, double-click the HelloWorldTask component.
Click Yes on the Open window indicating you
do want to create the implementation. Click OK on
the Generate Implementation window indicating you want to create the
implementation file in the project's root folder. The human task
editor opens, as shown here:
2. Strictly speaking, there is nothing more you need to do
here, but you want to learn! So click in the white space of the human
task editor canvas near the bottom. Then select the Properties view
below the editor and click the Details tab.
3. In the Properties view, select the check box Bind
the lifecycle to the invoking component, as shown here:   This action ensures
that outstanding instances of this task (to-dos) will be cleaned up
when the process that invoked the task is cleaned up.
4. Select the Duration tab in the Properties
view. Set the Duration until task expires 
to 6 minutes, as shown here: This way, it
will clean itself up if you forget to claim and complete it in a reasonable
amount of time.
5. In the editor canvas, note the People Assignment
(Receiver) section, as shown here:    By default, anyone can create
instances of this human task (in other words, create to-dos) and anyone
can claim those instances and work on them. However, you can restrict
this capability. Select the Everybody cell
in the Potential Owners row and focus the Properties
view. There is only the Assign People tab.
In the People assignment criteria field, select User
Records by user ID, as shown here:   
In the Assign People page, scroll
down to the table and set the value of userID to
the user ID that was specified for the server at install time. If
you did not change the user ID, then specify the default user ID admin,
as shown in the following figure: 
In the People Assignment  section
near the top of the editor, you see that the table has changed, as
shown in the following figure:
6. Optional: Note the Escalations section,
as shown here:     In addition
to specifying a duration for how long users must process a task before
it expires, you can also specify a series of escalation actions in
case the task is not claimed in a certain amount of time after it
is created (Ready state), or in case it is not completed in a certain
amount of time after it is claimed (Claimed state).
Actions
include creating a new to-do task for someone else or sending an email
notification. This is where you set these escalations up, using the
green "plus" button when one of the state icons is selected.
For both durations and escalations, you can specify elapsed
time not only with absolute hours, minutes or days, but you can also
specify it with a business calendar. By creating and specifying
a business calendar, you can identify noncontiguous time. For example,
you can specify that escalation should only occur after two business
days have elapsed.
7. Save and close the human task editor and then save your
work in the assembly editor.