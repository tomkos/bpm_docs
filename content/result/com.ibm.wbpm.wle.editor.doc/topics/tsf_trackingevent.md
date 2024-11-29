# Enabling runtime data tracking

## About this task

When you build your service, determine the point in the service flow at which you want runtime
data to be captured, and then insert an intermediate tracking node in the diagram at that point. A
tracking event is emitted when the service execution passes through the intermediate tracking event
node. The intermediate tracking event emits an EVENT\_THROWN monitoring event. The event reports that
a message was sent, or an exception error or tracking data was created.

To track service flow or heritage human service variables for
performance monitoring, associate the variables with a tracking group, which holds the variable data
that you want to track. In the properties of the tracking event, bind a service variable to each
tracked field that you want to use. For more information about tracking groups, see Tracking groups of process variables.

## Procedure

To model tracking logic into your service for data capture at run time, complete the
following steps:

1. Open the designer.
2. From the library, create or open the service flow or heritage human service that you want to
work with, and click its Diagram tab.
 To create the service, see Creating a service flow or Building a heritage human service.
3. From the palette, under Error, use the Tracking
 tool to add an intermediate tracking event node to the service diagram. Wire the node in
the diagram, and then select the node.
4 In the Implementation tab, under IntermediateEvent Type , ensure that the event type is set to Tracking .Under Event Properties , specify the propertiesfor tracking data at run time:
    1. Click Select next to Tracking group to specify the
tracking group that you want to use. To create a tracking group, click New.
See Creating a tracking group.
The
external unique ID of the tracking point in the Performance Data Warehouse database that is recorded
by this tracking event is displayed next to Performance warehouse ID. The
tracking fields that are defined in the tracking group are listed underneath.
    2. Optional: Under Associate tracked fields with other
task, you can specify the ID of the task with which you
want to associate the tracked fields in the selected tracking group.
You can also use the variable picker () to choose an existing variable from the library.
    3 Optional: Under Sort tracked fields by , bind a service variable to eachof the listed tracked fields. Use the variable picker ( ) to select a variable from the variables list for the service flow. The variable must be asimple type. You can also assign expressions and literal values to tracking group fields.If you have multiple tracked fields, you can sort them by selecting a sort order fromthe Sort tracked fields by list. Choose one of the following options:

<!-- image -->

        - Default Order: The tracked fields are sorted as they appear in the
tracking group definition.
        - Alphabetical (A-Z): The tracked fields are sorted in an alphabetical
list.
        - Alphabetical (Z-A): The tracked fields are sorted in a reverse
alphabetical list.
5. Optional: In the Pre & Post tab,
you can assign pre-execution and post-execution scripts to the tracking
event node. The JavaScript code that you add as pre- and post-execution
scripts runs immediately before or after the event runs.
6. Click Save or Finish Editing.