# Activity initiation

You can define the workflow for an activity by using the Step Designer in Case Builder. In the Step Designer, you select the case properties
and activity properties that are used as parameters for each step. The parameters determine what
information the case worker can view and edit for each step. The Step Designer automatically
generates the values to be assigned to the step parameters after the processing of the launch step
completes. Case Client uses these assigned values to
synchronize the case properties and activity properties with the step parameters.

The mapping of case properties or activity properties to workflow fields determines the initial
values of the step parameters when an activity is started. When an activity is started, the step
parameters are initialized with the property values.

When a case worker opens a work item, the Work Details page opens
or displays. Case Client populates
the fields with the property values from the case instance. If a property
value is null, Case Client populates
the field with the appropriate default value. For example, a null
integer property is populated with a 0.

## Activities that start automatically

You can define an activity that starts automatically. Optionally, you can specify that the
activity starts based on a precondition such as when an estimation document is added to an insurance
claim case. If you do not specify a precondition, the activity starts automatically when the case is
created.

In Case Client, an activity that starts automatically
does not open a Work Details page, so the case worker cannot see the work item for the Launch step.
Instead, the default values that were set for the properties are used to start the activity. When
the activity is started, or when a case is added and the automatic activities start, the user will
see the work items in their in-basket.

## Activities that start manually

You can define an activity that a case worker starts manually. You can define preconditions that
must be met to put the activity into Ready state. However, the activity does not start until the
case worker decides to manually start the activity.

In Case Client, the user starts the activity by
selecting the activity in the Case Information widget on the Case Details page and clicking
Start. The default values that were set for the properties are used. The case
worker cannot edit the property values until the activity progresses to a step where the properties
are available.

## Activities that start when they are added to the workflow at runtime

You can define a discretionary activity that starts when a case worker or the system creates an
instance of an activity. As part of defining the workflow for this activity, you specify parameters,
such as policy number and accident details, for the launch step that map to the case properties.

In Case Client, a case worker can add a discretionary
activity to the Case Details page. The launch parameters that you defined for the activity are then
displayed in the Add Activity page for the case worker to edit. The system then
updates the corresponding case properties with the parameter values.

## Custom activities

You can configure a case type to allow a case worker to create a custom activity at run time.

In Case Client, the case worker defines and starts a
custom activity whenever one is needed.