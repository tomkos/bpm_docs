<!-- image -->

# Creating a new mediation subflow

## About this task

## Procedure

1 Launch the New Mediation Subflow wizard in one of the followingways:
    - In the Business Integration perspective, click File
> New > Mediation subflow.
    - In the Business Integration view, select a module, mediation
module, or library. Right-click and select New > Mediation
subflow.
    - In the Mediation Flow editor, proceed as follows:
        1. Expand the Mediation Subflow folder in
the palette, click the Subflow icon, and drop it onto the canvas.
        2. In the Subflow Selection wizard, click New to
create a new mediation subflow.
2. In the New Mediation Subflow wizard, choose the project
that will contain the subflow, or click New to
create a new project.  A mediation subflow can be created
in a module, mediation module or library. Create your subflow in a
library if you want to share the subflow among modules.
3. Optional: Specify a folder for the new subflow.
4. Provide a name for your subflow.
5. Click Finish. The
Mediation Subflow editor opens showing an in  node
that represents the input terminal of the subflow instance, and an out node
that represents the output terminal of the subflow instance.
6. Drag the mediation primitives from the palette onto the
canvas and lay them out from left to right in processing sequence.
7. Wire the primitives to the in and out terminals and to
each other, and configure the primitives in the properties editor.
8. Optional: Define the message types of the input terminal
of the in node and the output terminal of the out node.
Click the terminal to select it and right click > Change
Message Type.
9. Optional: Promote properties that you want to be able to
change at run time, or if you want to set the value of the property
in the parent mediation flow at development time. For more information,
See Promoting properties in a subflow.
10. Save your changes

## What to do next

## Related concepts

- Mediation subflows
- Mediation subflow limitations

## Related tasks

- Editing a mediation subflow
- Copying part of a mediation flow into a subflow
- Adding a mediation subflow in a mediation flow
- Using Service Invoke in a subflow
- Synchronizing a subflow instance and implementation

## Related information

- Promoting properties in a subflow
- Changing the input or output message type in a subflow