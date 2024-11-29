# Declaring variables for a process or a service

## About this task

You can add the following variables to your process or service
flow:

| Variable                       | Description                                                                                                    |
|--------------------------------|----------------------------------------------------------------------------------------------------------------|
| Private                        | Local variables that are used only within the process.                                                         |
| Input                          | Variable that represents input data passed to the current process or service.                                  |
| Output                         | Variable that represents output data that the current process or service returns to its caller.                |
| Exposed process variable (EPV) | Special type of variables that you can create to set or alter values while instances of a process are running. |

## Procedure

If you want to add an exposed process variable, click Exposed Process
Variables, and then select the EPV from the list. If you want to add a private, input,
or output variable, complete the following steps:

1. Open your process or service diagram.
2. In the Variables tab, click Add
Private, Add Input, or Add
Output to create the corresponding variable. Note: If an input variable is a complex
type and you are passing it from a process to a service, it will be
passed as a value. If you want the updated value to be returned, also
declare it as an output variable. If the complex type is a shared
business object, you do not need to return it as an output because
the updates that are made in a service will become visible to everyone
who uses the shared business object.
3 In the Details section:
    1. Type a variable name in the Name field.
Note: Variable names start with a lowercase letter, with subsequent
words capitalized, for example: myVar. Do not use
underscores or spaces in variable names. Variable names are case-sensitive.
    2. Click Select next to the Variable
Type field to select the type of the variable. Custom
business objects that you created are also listed.
    3. Optional: Type a description of the variable
in the Documentation field.
    4. Optional: If you want your variable to be
an array, select Is List.
4. Optional: 
To set a default value for the variable, in the Default Value section,
select Has default and enter the value in the corresponding field.

Note: For complex business objects, the default value script must declare a variable and return it
by specifying the last line as the variable name. For
example:var autoObject = <new\_instance>; 
...
autoObject
5. Optional: To include a process variable in the business data that users can
view and search in Process Portal, select Expose in work environments, and type an alias in
the Alias field.

Tip: The search alias must be unique to the variable type throughout the workflow server
on which the process runs. If a variable is used in parent and nested processes, use the same search
alias if you want search results to include all related processes.
6. Optional: To include the  variable values in
the data that is collected and used to create reports, in the Performance
Tracking section, select Track this variable.
7. To declare a variable as a secondary process identifier, select  Process Instance
Identifier. While it is possible to mark any variable as process instance
identifier, it is advisable to use a variable for this purpose that is not too complex.Important: The value that is written to the variable must be unique for each instance of the
process. Because variables that are selected as process instance identifiers can be written to only
once, be careful during initialization, data mapping, pre-assignments, and post-assignments to avoid
it ever being written to twice for an instance. Writing any value to such a variable more than once
causes an error.
Tip: If you clear the selection for a variable that is already
used for correlation, the variable is marked with an error icon on the Data
Mapping tab.
Variables that are marked as process instance
identifiers can be selected to be used for correlation, and are indicated in variable selection
dialogs by the text [Identifier].
8. Click Save or Finish Editing.

## What to do next