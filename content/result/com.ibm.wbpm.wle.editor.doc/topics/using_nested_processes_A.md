# Calling a linked process dynamically

## About this task

To use the dynamic option for a linked process, complete the following tasks first:

- Create a variable of type String in the parent process to hold the name of the
linked process that you want to run. Your parent process must also include the logic to determine
the value of this variable at run time. For example, the parent process can include logic to set the
value of this variable based on user input.
- Establish the input and output variables for each potential linked process so that the parent
process runs as expected regardless of which linked process is called. To meet this requirement, the
variables in all potential linked processes must be the same. To map variables from the parent
process to the linked process, follow the steps described in Working with linked processes.
- Dependencies might exist between process applications and toolkits, as well as between toolkits
and other toolkits. For example, process app  PA1 might depend on toolkit TK1, which in turn might depend on toolkit TK2. This
creates a dependency chain: PA1 -> TK1 -> TK2. In order for the search to be started at the
beginning of the dependency chain (in PA1), the name of the invoked process must be prefixed with a
double slash (//). If a process in TK1 invokes another process dynamically without
the double slash prefix, it will find only the processes down the dependency chain (that is, in TK1
and TK2, but not in PA1).

To configure an activity to dynamically call one of many potential linked processes, complete the
following steps:

## Procedure

1. Open the parent process.
2. In the Definition page, add a linked process to the diagram.
3. Select a predefined linked process from the library.

You must initially select one of the predefined linked process for the dynamic configuration to
function properly.
4. Click the Data Mapping tab in the properties. 
Because you already created the input and output variables for the linked process, the
Data Mapping tab for the activity in the parent process includes those
variables.
5. Under Input Mapping, click the auto-map icon in the upper-right
corner, and then click the auto-map icon in the upper-right corner of the Output
Mapping section.
6. Click the General tab in the properties.
7. In the Dynamic process field, choose the previously defined
variable that provides the name of the selected process. 
Note: At run time, the value of this variable cannot be null and it must exactly match the name of
an existing process.
8. Click Save or Finish Editing.