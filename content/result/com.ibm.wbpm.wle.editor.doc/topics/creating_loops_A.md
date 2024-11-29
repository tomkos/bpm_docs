# Configuring a process activity for simple loops

## Before you begin

## About this task

When you model an activity with simple loops, the required number of instances is dynamically
created, up to the loop maximum value that you specify. A simple-loop activity is run sequentially
until the last instance of the activity is run. When you run an activity configured for simple
loops, a single token is generated and used for each instance of the activity, which, in effect,
recycles the runtime task.

## Procedure

1. Open a process.
2. Select the activity that you want to configure in the process diagram.
3. Click the General option in the properties.
4. Expand Loop and select the Simple Loop
option from the Loop type list.
5. Type a value in the Loop maximum box. This value sets
the maximum number of instances that can be created at run time. If you declare a variable that can
be used for this setting, click the variable icon to select it or type the variable name into the
Loop maximum box.
6. In the Loop condition box, type an optional JavaScript condition
to dictate the runtime loop behavior. A condition is evaluated before any instances are created from
the activity. If the condition is not met, the loop configuration does not occur.
7. Click Save or Finish Editing.

## Results

<!-- image -->