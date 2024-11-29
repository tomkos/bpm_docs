<!-- image -->

# Configuring correlation sets

## About this task

The following procedure creates a correlation
set for a process:

## Procedure

1 Add a Correlation set to your BPEL process as follows:
    1. In the tray, click the add () icon
beside Correlation Sets.
    2. Give the new correlation set an appropriate name.
2 Create a correlation property as follows:

1. Click the add () icon beside Correlation Properties.
2. In the Add Correlation Property window,
assign an appropriate name to the new property in the Name field.
3. Select an XSD simple data type from the list.
4. Click OK.
3 Create a property alias as follows:

1. In the Description tab for the
Correlation Property, select an operation in the interface table,
and click Add. All of the interfaces
that are used by the process are listed here, and multiple property
aliases can be defined for each operation.
2. In the Create Property Alias window,
specify if this variable is an input or an output.
3. Select the correct part or element from the list that
matches the type defined in step 2c, and click OK

## What to do next

The following procedure creates a correlation set reference
for an activity:

1. In the BPEL process editor, click the activity that you want to
associate with a correlation set, and click Correlation in
the properties area.
2 Click Add and configure the set as follows:
    1. In the Direction field, chooseSend if
this set is to be used for outgoing messages, Receive for
those that are incoming, or Both when it can
be used for either.Note: The options available here will depend upon
what kind of activity you are configuring. For some activities like
receive, reply or elements like receive, this field is set for you.
    2 In the Initiation field choose from oneof the following options:
        - Select Yes if this is the first time this
correlation set has been executed, and this is when the messages that
will link this user to this workflow are to be stored.
        - Select No if the correlation set will be
always initialized by another activity.
        - Select Join if multiple activities can
initialize the correlation set. This is especially useful if you are
designing a process with multiple parallel receives, and you are not
sure which one will get executed first. If you specify Join for
both of them, then the first one to run will initiate the correlation
set, and the second will use the existing value.
3. In the Correlation Set field, select the
appropriate pre-existing correlation set from the drop-down menu.