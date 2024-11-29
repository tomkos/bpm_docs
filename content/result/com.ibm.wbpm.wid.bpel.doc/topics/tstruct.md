<!-- image -->

# Working with structured activities

## About this task

<!-- image -->

- Case element
- Used within a choice activity, this element is used to
create a control path and define the conditions that will cause this
path to run. When run, the process will evaluate the conditions in
each of the case elements, and follow the first one that evaluates
to true.

- Otherwise element
- Use this element within a choice activity to create a
control path that will run when none of the other cases evaluate to true. Use this element on only one of the paths within a choice
activity. When run, the process will evaluate the conditions in each
of the case elements, and should none of them evaluate to true, it
will run the activities in this path.

<!-- image -->

- Link
- Use the link within a Generalized flow activity to connect
nested activities and form individual control paths. The link is used
to express a synchronization dependency. In other words, it runs under
a constraint because the link creates a dependency of one activity
and the variables it uses on another activity. You can specify a transition
condition on the link in the properties area of the BPEL process editor.

<!-- image -->

<!-- image -->

- Link
- Use the link within a parallel activity to connect nested
activities and form individual control paths. The link is used to
express a synchronization dependency. In other words, it runs under
a constraint because the link creates a dependency of one activity
and the variables it uses on another activity. You can specify a transition
condition on the link in the properties area of the BPEL process editor.

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

To work with a structured activity, proceed as follows:

## Procedure

1 Choose a structured activity from palette, and drop itto the canvas. The activity will appear with a distinctrectangular workspace. Note:
    - If this is a choice or a receive choice activity, it will contain
a default element representing a single control path.
    - With the exception of the parallel and generalized flow activities,
all structured activities differentiate the activities that they contain
into separate control paths. In parallel or generalized flow activities,
you create the control path yourself with links.
2. Populate the workspace with activities from the palette.
If this is the first activity that you're dropping to the workspace,
it will automatically appear in the first path. If there are already
activities on the path, then a black line will appear as you hover
over the path showing where you can drop the new activity.
3. To create a new path in the structured activity (only some
structured activities support multiple paths), hover over the activity's
icon until the action bar appears, and select an element from it.
4 You can expand or collapse this structured activity ineither one of the two following ways:

1. Click the plus () or minus () icons
as appropriate.
2. Double-click the structured activity.

- Linking activities within parallel and generalized flow activities

Links direct the sequence in which the execution of activities occurs within parallel and generalized flow activities.
- Working with parallel activities

A parallel process (or flow) is a collection of other process activities that are all nested within a parallel activity. The nested activities run sequentially in an order that is dictated by links and transition conditions (when no links are present, all activities will be executed concurrently). When activities are arranged on separate control paths, the paths will run concurrently.
- Working with generalized flow activities

The generalized flow activity is very similar to a parallel activity in that you can nest other process activities within it, and then control the execution order of those activities through links. The generalized flow activity differs however in its ability to use conditional links to loop back to previous activities in the sequence.
- Enhanced dynamic behavior in a process

You can configure a scope activity so that users interacting with a runtime instance of the process will have administrative authority over the activities that are nested within the scope activity. You can achieve enhanced dynamic behavior more directly using a collaboration scope in which the associated administration task is automatically generated when the collaboration scope is added to the BPEL process.
- Modifying the join behavior of an activity

Instructions on how to change the behavior of an activity's input link.

## Related concepts

- Replacement variables and context variables
- Using Java methods in process snippets
- Using custom properties for human tasks
- Using event handlers

## Related tasks

- Modifying the properties of an activity
- Modifying the type of an activity
- Working with basic activities
- Modeling human workflows
- Linking activities within parallel and generalized flow activities
- Working with parallel activities