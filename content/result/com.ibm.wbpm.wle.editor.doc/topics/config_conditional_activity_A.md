# Implementing a conditional activity

## Procedure

Complete the following steps to implement a conditional activity.

1. Open a process.
2. Select the activity that you want to make conditional.
3. Under Conditions in the properties section, select the
Conditional option.
Restriction: The conditions tab is disabled for ad hoc activities (unwired
activities). If a wired conditional activity is turned into an ad hoc activity by deleting wires to
and from the activity, the Conditional option becomes disabled. To set
conditions for an ad hoc activity, use preconditions. See Creating an unstructured (ad hoc) activity

The activity in the process diagram includes a diamond-shaped icon to indicate that it is
conditional. The diamond-shaped icon on an ad hoc activity indicates that the activity has a
precondition.
4. Select the conditional activity for execution by using one of the following
options:

Option
Description

JavaScript
Enter JavaScript in the available box. It returns a valid Boolean
(true or false) value. If the runtime return value of the supplied
script is true, the activity is carried out. Note: If a script is present in the
box, it overrides any human decision at run time to carry out or skip the activity.

Set selected conditional activities
If the Conditional option is enabled and no JavaScript is entered in
the box, the activity is carried out only if previously selected. Use the
tw.system.process.selectedConditionalActivities property to set selected
conditional activities. 

Note: Performance Data Warehouse records data that can be used to analyze the conditional activities. When a conditional activity
is skipped, a tracking point is created with SKIP appended to the name of the
skipped activity. A tracking point is created in the TRACKINGPOINT views each time an activity is
skipped. Using this data, you can generate reports to show which activities are skipped and how
often those activities are skipped in a process instance.
5. Click Save or Finish Editing.