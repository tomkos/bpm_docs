<!-- image -->

# Compensating activities in a long-running process

## About this task

- Compensation is tightly coupled with fault handling. You need
to think about compensation when you are modelling fault handling.
- The steps necessary to deal with it, and return the process to
an equitable state.

## Related concepts

- Key concepts for BPEL business processes
- Working with BPEL extensions
- Choosing between long-running processes and microflows
- Best Practice: When to not use the BPEL extensions

## Related tasks

- Compensating a microflow

## Related reference

- Server tab: BPEL process editor

## Compensation using Compensation Handlers (BPEL)

### About this task

### Procedure

1. To begin, you will have to make this a long-running process.
To do this, click an empty area of the canvas, click the Details tab
in the properties area, and check the BPEL process type setting. If
it is not set to Long-running, click the Refactor to link
to make it Long-Running.
2. Select either one of the following activities onto the
canvas: invoke, scope, collaboration scope or human task. Use
an invoke or human task if you will be creating a compensation handler
for a single activity of this type, or use a scope or collaboration
if you want to compensate the whole structured activity.
3. Click this activity to launch the action bar.
4. In the action bar, click the Add Compensation
Handler icon as shown in this image.  This will create a handler (an empty
box outlined in gray) beside the original activity.
5. Populate this compensation handler with the activities
needed to create the compensation logic.
6 If a compensate activity itself is part of your compensationlogic, you have two choices:
    1. the compensate activity should compensate everything
that is included in your selected activity: (default, do nothing)
    2. the compensate activity should compensate a specific
invoke, scope, collaboration scope or human task activity that is
included in your selected activity, then you must specify that target
activity in the Target Activity field in the Details tab
for this compensate activity.

### Results

- A compensation handler will only run if the activity with which
it is associated has completely successfully.
- You can also define undo actions for individual invoke activities
in long-running processes in the same manner as you would assign a
compensation to invoke activities within a microflow. See Compensating a microflow.

## BPMN-style Compensation

### About this task

- They do not have a Target Activity field
specified in the Details tab for this compensate
activity.
- They are directly enclosed in a generalized flow activity. Thatgeneralized flow activity must either be:
    - Directly enclosed in the Process or a Scope activity.
    - Directly enclosed in a receive case branch of a Receive Choice
activity, that Receive Choice activity, in turn, must also be directly
enclosed by a process or scope.

### Results