# Configuring an activity for multi-instance loops

## Before you begin

## Procedure

To configure an activity for a multi-instance loop, follow these steps.

1. Open a process and select the activity that you want to configure.
2. In the properties, select General.
3. Expand Loop and select Multi-instance loop
from the Loop type list.
4. Set a value for Start quantity. This value sets the
number of instances that are created at run time. To specify a variable that can be used for this
setting, click the variable icon to select it or type the variable name into the Start
quantity box. Note:  For information about how to associate each loop
activity instance with a specific item in a list, see Associating loop activity instances with different items
.
5. From the Ordering list, select one of the following
options: 

Option
Description

Run in sequence
Resulting instances are run sequentially until the last instance of the activity is
complete.

Run parallel
Resulting instances are run at the same time until all instances are finished or until the
condition that you specify is met.
6. For parallel ordering, select one of the following options from the
Flow condition list: 

Option
Description

Wait for all to finish (All)
Looping continues until all resulting instances of the activity are finished.

Conditional wait (Complex)
Looping continues until the condition that you specify in the following step is
met.
7. For complex flow conditions, type the JavaScript to implement that condition in the
Complex flow condition box.

At run time, if a multi-instance loop with complex conditions evaluates to false, it closes the
active instance and does not move to the next activity. This is the default behavior since the BPMN
2.0 specifications (section 13.2.7 Multiple Instances Activity) do not provide guidance for a false
evaluation. To advance the token to the next activity, use an OR Boolean
expression.
8 If you want active instances of the activity to be canceled when the preceding conditionis met, select Cancel remaining instances . The runtime behavior of a multi-instance loop depends on how its task is implemented. Thebehavior is different when the task content contains server scripts only and when it also includesservices. For example, a loop with Ordering selected to Runparallel , with a valid complex flow condition, and Cancel remaininginstance set to true, runs as follows:
    - Loop content contains server scripts only: If you specify only server scripts in the
multi-instance loop task content, the various instances of the loop run sequentially. Therefore, all
instances run in sequence to their end, and at the end of all task instances the exit conditions are
verified sequentially.
    - Loop content contains Human, Decision, or System services: If the loop task content contains a
Human, Decision, or System Service, then the tasks instantiate in parallel within their own thread.
In the example of the System service, if an exit condition is set, upon completion of the System
service task, the result is given back to the multi-instance loop. Then, the condition is evaluated
and the multi-instance loop task completes, which ends all other still running loop instances.
9. Click Save or Finish Editing.