<!-- image -->

# Adding an activity to a BPEL process

## About this task

After you have created a new process, create the activities
that will run the task to be performed by that process. To add an
activity, proceed as follows:

## Procedure

1. In the palette, click the icon for the activity.
2. Drag the cursor out over the canvas.  You will
notice that the icon beside your cursor has a plus symbol when you
are at a place where you are allowed to drop the activity. If the
cursor becomes a crossed out circle, continue moving the cursor until
it becomes a plus sign again.
3. Click the area of the canvas where you want to drop the
activity.
4. Configure the activity as necessary in the Properties area
of the BPEL process editor.

## Results

- Disable the Use Data Type Variables check
box in the activity.
- Create two Interface-typed variables for the input and
output. These variables are actually WSDL-message-typed, but in the
BPEL process editor you select an Interface and Operation and direction
(input or output) and the editor will determine which WSDL message
to use.
- Add Assign activities before or after the Invoke to
copy the data into these variables.

- Modifying the properties of an activity

Instructions on how to modify the details of any of your activities.
- Modifying the type of an activity

As you construct your BPEL process you may decide that a specific activity should be of a different type than you initially assigned.
- Working with basic activities

A basic activity implements a singular aspect or task within a BPEL process. Unlike structured activities, basic activities do not embed other activities within them.
- Details tab: BPEL process editor

This topic includes a description of each of the fields on the Details tab of the Properties view.
- Authorization tab: BPEL process editor

This topic includes a description of each of the fields on the Authorization tab of the Properties view.
- Replacement variables and context variables

While working with templates, you might want to refer to a variable that will not be resolved until the instance has been started in the runtime environment. This variable is known as a context variable, because its value is dependent upon the task context in which it is exists (or the process context for inline tasks). If you want to refer to such a context variable in a template, you must use a replacement variable.
- Using Java methods in process snippets

You can use Java™ methods in process snippets to perform a variety of functions.
- Using custom properties for human tasks

Custom properties are used to categorize a task, and can be useful for querying, sorting, and filtering tasks.
- Using event handlers

Event handlers are constructs that respond to external stimuli with an appropriate defined action.
- Working with structured activities

A structured activity contains one or more other activities that are arranged on one or more separate paths. Here are some tips on how to work with these activities in the editor.
- Modeling human workflows

Human workflow activities can be added to your business flows from the Human Workflow palette.