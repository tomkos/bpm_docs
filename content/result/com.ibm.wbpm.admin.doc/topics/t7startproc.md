<!-- image -->

# Starting a new process instance

## About this task

All of the installed and started process templates are
shown in the list of process templates in Business Process Choreographer
Explorer. To start a new process instance, complete the following
steps.

## Procedure

1. Display the process templates that you are authorized to
use. Click All Versions under
Process Templates in the Views tab navigation
pane.
2. Select the check box next to the process template and click Start
Instance. This action displays the Process
Input Message page. 
If the process has more than one operation,
this action displays a page that contains all of the available operations.
Select the operation that is to start the process instance.
3. Provide the input data to start the process instance.
If the process is a long-running process, you can type in
a process instance name. If you do not specify a name, a system-generated
name is assigned to the new process instance.
Complete the input
for the process input message.
4. To start the process, click Submit.

## Results

If the process instance is a microflow, a process
output message is displayed automatically in the web browser. For
long-running processes that are not automatically deleted after the
process completes, a process output message is available in the process
instance view. To see the output message, select the instance in a
process list in Business Process Choreographer Explorer, and open
the process instance view. Not all processes have output messages,
for example, if the process implements a one-way operation, an output
message is not available.

<!-- image -->