<!-- image -->

# Changing toolkit dependencies

## About this task

To change the toolkit snapshot that is referenced by a
process application, complete the following steps:

## Procedure

1. Right-click Dependent Toolkits in
the Business Integration view. Select Change
Toolkit Dependencies.
2. Select the snapshot of the toolkit you want to reference
from the window. Only one snapshot will be selectable from any toolkit.
3. After your selection, the dependent toolkit snapshots are
listed under Dependent Toolkits. If
you select two or more dependencies that contain the same project
name, a message tells you that a project name cannot be used more
than once in a process application or its dependencies. Clear the
selection or selections that you do not need.

## Results

When you change the toolkit snapshot, this action affects
the service you have created since the process application and modules
may have referenced elements that are not in the new toolkit snapshot.
In such cases you need to add these elements to the new toolkit snapshot,
or modify your service.