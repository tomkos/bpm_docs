# Declaring variables for client-side human services

## About this task

You can add the following variables to your client-side human service.

| Variable               | Description                                                                                           |
|------------------------|-------------------------------------------------------------------------------------------------------|
| Input                  | Variables that represent input data passed to the current client-side human service                   |
| Output                 | Variables that represent output data that the current client-side human service returns to its caller |
| Private                | Local variables that are used only within the client-side human service                               |
| Exposed Process Values | Exposed process values (EPVs) can be linked to and used from a client-side human service              |
| Environment Variables  | Environment variables can be linked to and used from a client-side human service                      |

- When the client-side human service is implemented as a task, and the process instance specifies
variable values for the task through input mapping, the specified values take effect at run time. If
a mapped variable from the process is not initialized, its mapped null value is
used. If no variable values are specified (no mapping), the default values take effect at run time.
See also Creating versus starting a client-side human service task in a process.
- When a client-side human service is implemented as a startable service or a URL, for example, if
there are input variable values that are specified as URL parameters, the specified values take
effect at run time. Otherwise, the default values take effect.
- When a nested client-side human service is called from a parent client-side human service and
the parent specifies variable values through input mapping, the specified values take effect at run
time. If there is no mapping, the nested service uses the default values. If there is a mapping, the
nested input uses the parent variable value, even if it is uninitialized.
- When variables are declared inside an event handler of either error or data change type, the
default values take effect the first time the event handler runs in the current instance of the
nested service that contains the event handler. If you exit the client-side human service that
contains the event handler and enter it again, all the variables, including the event handler
variables, are reset.

- tw.epv.[epv\_name].[epv\_variable\_name]
- tw.env.[env\_variable\_name]

- If a variable with the same name exists in the parent process
application, the value from theprocess application is used,
regardless of its structure or properties.
- If a variable with the same name exists in the dependent toolkit but does not exist in the
process applicationprocess application, the toolkit value is used.

- If want to use the process application value, use the variable's short name in your scripts, for example,
tw.epv.[epv\_name] or
tw.env.
- If you want to use the toolkit value, regardless of overlapping names, use the
tw.epv.toolkit or tw.env.toolkit format in your scripts.

- When the task is created, data is retrieved from the process instance at creation time.
- At a later time, when a user starts the task, data is retrieved from the runtime process
instance, which might be different from the data when the task was created.

## Procedure

To add an input, output, private, or EPV variable to the client-side human
service:

1. Open your client-side human service.
2. Switch to Variables, then click the plus sign next to
Input to add a new input variable.
3 In the Details section:
    1. Specify the variable name.
 Variable names are case-sensitive and must start with a lowercase letter, with subsequent
words capitalized, for example: myVar. Do not use underscores or spaces in
variable names.
    2. Click Select next to Variable Type to select the
type of the variable from the Select Library Item list. 
Custom business objects that you created are also listed. To create a new business object,
click New and complete the wizard steps. 
Client-side human services do not support business object instances that reference themselves.
For example, the following JavaScript generates an error when used inside a client-side human
service:tw.local.myVariable= {};
tw.local.myVariable.pointer= tw.local.myVariable;
Tip:  For more information on how to use the standard JavaScript syntax to instantiate
objects in the client-side script, see Re-creating heritage human services as client-side human services.
    3. Optional: 
Specify a variable description under Documentation.
    4. Optional: If you want your variable to be an array, select Is
List.
4. To specify a default value for the input or private variable that you
are adding, select Has default under Default Value,
and then type in the default value.

Note: For complex business objects, the default value script must declare a variable and return it
by specifying the last line as the variable name. For example,
:var autoObject = <new\_instance>; 
...
autoObject
5. Save the configuration.
6. Iterate through steps 2 to 4 to add an output, private, EPV, or environment variable to
the client-side human service.
7. Click Save or Finish Editing.

## What to do next

- JavaScript API for client-side human service development

Use the following reference information to learn more about the client-side JavaScript system variables that are available in designer for client-side human service development.