<!-- image -->

# Compensating a microflow

## About this task

## Procedure

1. To begin, you will have to make this a microflow. To do
this, click an empty area of the canvas, click the Details tab in the properties area, and clear the Process is
long-running check box.
2. Configure the Compensation Sphere setting. You have the following two options:

Option
Description

Supports
Use this setting when this microflow can run without a compensation
service.

Required
Use this setting when this microflow needs a compensation
service.
3 For each invoke activity in this microflow, proceed asfollows: In the event that the microflow has to be compensated,it will look at these values, and restore them to the activity.
    1. Click the Compensation tab in
the properties area.
    2. Browse to a reference partner, and select an appropriate
operation to store the original condition of the activity.
    3. Browse to an input variable to store the original value
of the activity.

## Results

## Related concepts

- Key concepts for BPEL business processes
- Working with BPEL extensions
- Choosing between long-running processes and microflows
- Best Practice: When to not use the BPEL extensions

## Related tasks

- Compensating activities in a long-running process

## Related reference

- Server tab: BPEL process editor