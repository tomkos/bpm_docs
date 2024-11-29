<!-- image -->

# Working with basic activities

## About this task

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

- Receive case element
- Use this element within a receive choice activity to create
a control path and specify the operation that will run it. There is
at least one receive case element path nested within a receive choice
activity. When run, the process halts at the receive choice activity
and listens for a message from its operations. The first message that
comes in determines which path is followed.

- Timeout element
- Use this element within either a receive choice activity
to create a control path that is followed when a specified time has
either been reached or has elapsed. This element is used on a single
path, and is configured to specify either a specific date, or period
of time. When run, this path is chosen when no input is received within
this time period, or by the specified date.

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

To work with a basic activity,
proceed as follows:

## Procedure

1. In the palette, click an activity's icon.
2. Drag the cursor out over the canvas.  You will
notice that the icon beside your cursor has a plus symbol when you
are at a place where you are allowed to drop the activity. When the
cursor becomes a crossed out circle, continue moving the cursor until
it becomes a plus sign again.
3. Click the area of the canvas where you want to drop the
activity.
4. Configure the activity as necessary in the Properties area
of the BPEL process editor.

- Using assign

Use the assign activity to manipulate data within your BPEL process and map data from one location to another.
- Working with XPath in the BPEL process editor

There are several places in the BPEL process editor where you have the option of using the XPath standard.
- Configuring the wait activity

The wait activity stops the process for a period of time that you specify. You configure this activity either by telling it how long it should pause the process, or by specifying a date and time when the process should restart.
- Expiration tab: BPEL process editor

This topic includes a description of each of the fields on the Expiration tab of the Properties view.
- Defining timer-driven behavior in a BPEL process

You can set timer values in a number of places in the business process editor, and for several different activities or elements. Timer values can be configured to trigger processing or expiration after a specific period of time has either elapsed or been reached.
- Setting duration values for your human task

You can set a duration value for your human task to specify how long the task will hold before it is either due, set to expire, or set to be deleted.
- Adding a data map activity

Use the data map activity to transform data between two business objects.

## Related concepts

- Replacement variables and context variables
- Using Java methods in process snippets
- Using custom properties for human tasks
- Using event handlers

## Related tasks

- Modifying the properties of an activity
- Modifying the type of an activity
- Working with structured activities
- Modeling human workflows

## Related reference

- Details tab: BPEL process editor
- Authorization tab: BPEL process editor