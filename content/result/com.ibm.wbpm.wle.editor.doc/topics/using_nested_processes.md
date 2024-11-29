# Working with linked processes

## About this task

Linked processes encapsulate logically related steps within a process while retaining the
high-level view of the parent process. However, linked processes differ from subprocesses because
they can be accessed and instantiated from processes other than a single parent process. In previous
product releases, linked processes were known as nested processes.

## Procedure

1. Open the parent process.
2. In the Definition page, add a linked process to the diagram.
3. Select an existing process for the linked process to call, or create a new process. You
can also dynamically call one of many linked processes at run time, depending on your needs, by
using a variable defined in the parent process. See Calling a linked process dynamically.
4. In the parent process, connect the linked process activity to other elements in the
process flow.
5 Variables in a linked process activity are local to the linked process. If you want topass data into or out of a linked process activity, you must map the inputs and outputs of yourlinked process to the inputs and outputs of the linked process activity in the parent. Complete oneof the following steps in the Data Mapping tab of the Properties view for thelinked process activity:
    - If you declared variables in the parent process that have the same names and data types as
the input and output variables in the linked process, use auto-mapping to have the inputs or outputs
of the linked process automatically mapped to variable defined in the parent process.
    - If the variables declared in the parent process do not match the variables of the linked
process inputs or outputs, you can manually select the variables to map.
6. Click Save or Finish Editing.

- Calling a linked process dynamically

When you use a linked process as the implementation for an activity, you can use an advanced option in the implementation properties to supply a predefined variable to dynamically call one of many linked processes, depending on your needs.