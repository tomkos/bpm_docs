<!-- image -->

# Create the business process implementation

## About this task

## Procedure

1. In the assembly editor, double-click the HelloWorldProcess process
component to start work on it. Click Yes in
the Open window and click OK in the Generate
Implementation window. The business process editor opens, as shown
here:
2. Your process is going to invoke a human task, which could
take a long time to respond. As a result, you need the process to
be defined as long running. Click somewhere
in the white space of the editor and go to the Properties view
and select the Details tab. Notice that the
process is identified as a Long-running process,
as shown here:If you want to change the process from a long-running process
to a microflow, click the Refactor to Microflow link.
This ensures that not only the process definition is changed, but
also the process component in the assembly editor. This means that
the process changes and all downstream artifacts impacted by the change
are updated.
3. A business process is made of activities or individual
steps. When a process is initially created for an interface with a
request response operation, it has two activities pre-supplied: a Receive activity
for starting the process through the operation and a Reply activity
for returning the response to the caller. Your own activities will
be inserted between these two activities. On the palette, expand the Structures category
and drag Generalized Flow and drop it between Receive and Reply,
as shown here: Note that some activities like
Generalized Flow are structured, meaning they are intended to contain
other activities. To produce a flow that branches, you must use Parallel
Activities, Generalized Flow, or Collaboration Scope.
4. In the tray on the right side of the canvas, expand the Reference
Partners category and drag HelloWorldTaskPartner into
the GeneralizedFlow structure, then set the
name to InvokeTask, as shown here:This creates a configured
Invoke activity that calls this reference, which is wired to the human
task component back in the assembly editor. This means that at run
time, the activity results in the creation of an instance of your
human task; that is, a to do task is created
and awaits being claimed by one of its potential owners. It is not
fully configured yet, however. You need to define where to get its
input parameter data and store its output results.
5. On the canvas, select the InvokeTask activity
and open the Properties view below the editor.
Select the Details tab. In the Inputs rows
of the table, click none  in the cell of the gender row
and of the last column named Read from Variable.
You see a drop-down list showing all variables currently defined in
this process that have a matching type, which at this point consists
only of the input and output parameters of the process interface.
Select the gender variable, which is the input
parameter to this process. This selection means that you will pass
this variable's text data as input to the human task.
6. Similarly, in the Outputs rows,
click none in the cell of the firstName row
and of the last column named Store into Variable,
but this time select New and create a new variable
named firstname. Do the same for the lastName row
and create a new variable named lastname. Note
that the variables are created with the appropriate type for this
reference partner parameter. Your table should look like this:
7. At run time when the InvokeTask returns,
you will have variables containing the given name and family name
of the user. The Hello World Part 1 sample service that you need to
invoke also requires a title like Mister, which means that you need
to define a variable to hold the value. Beside the Variables category
in the tray, click the plus (+) icon as shown in the following figure:
  The Add a Variable window box opens.
8. In the Name field, type the variable
name fullname and select the type FullName,
which is a business object created in the Hello World Part 1 sample.
Click OK. This is the matching data type of
the variable that the service from the first sample requires as input.
Your variable list should now look like this: The fullname variable has three fields defined
in it, all of type string: title, firstName and lastName.
You will need to set a value for all three fields before you can invoke
the service, as described in the following steps.
9. From the palette, expand the Basic Actions category
and drag the Assign activity to the inside
of the GeneralizedFlow structure on the canvas.
Rename it to AssignM.
10. While AssignM is selected, go to
the Properties view and the Details tab.
In the Assign To column of the table, click Select
To. In the drop-down list, expand fullname and
select title.
11. In the same table, in the Assign From column,
click Select From. Select String
(enter a value) from the drop-down list and type Mr,
as shown here:
12. In the canvas, wire the InvokeTask activity
to the AssignM activity and select Add
a Link.
13. Once again, drag the Assign activity
from the palette to the interior of the GeneralizedFlow structure
and name it AssignF. Configure it to assign Ms to
the title field, as shown here:
14. Wire the InvokeTask activity to
the AssignF activity and select Add
a Link. Your flow should now look like this:
15. It is time to assign values to the remaining two fields
in fullname: namely firstName and lastName.
You will set these from the values that are returned from the human
task. Drag Assign again from the palette to
the inside of the GeneralizedFlow structure
and then rename it to AssignNames. Using the Add button
to add another row to the Assign table, configure it as shown in the
following figure:
16. Wire both the AssignF and AssignM activities
to this new AssignNames activity and select Add
a link when prompted. The GeneralizedFlow should
look like this:
17. You need to condition the two links coming from InvokeTask so
that there is some criteria about when to follow each link. Select
the blue link that goes into AssignF and go
to the Details tab of the Properties view.
In the Expression Language field, select XPath
1.0 and then click the Edit button.
The XPath Expression Builder opens.
18 Set the gender condition to female usingone of the following approaches:
    - Type the expression $gender='female' directly
and click OK.
    - Click Insert Simple XPath and select $gender in
the list of data types, then select the equals sign (=)
as the Operator in the Add an optional
condition area and type female in
the corresponding Value field. Click OK twice.
19. Select the link that goes into AssignM,
and for its properties set the Expression Language to XPath 1.0 and
the Condition to $gender!='female' as shown
here:    Optional: It is possible
to give your links a label by setting the Display Name in
the Description tab of the Properties view,
then showing the label by right-clicking the link and selecting Show
Labels on Links.
20. In the tray, drag HelloWorldPartner to
a position immediately above the Reply activity
and name it InvokeHW1, as shown here:
21. In the Details tab of the Properties
view, for the InvokeHW1 activity, bind the
input and output parameters to the fullname and result variables,
as shown here:
22. From the Basic Actions category in the palette, drag Snippet to
immediately above Reply. In the Details tab
of the Properties view, there is a visual Java snippet editor. Double-click
the Properties tab to go full screen. Click Standard in
the palette. The Add a Standard Visual Snippet window appears. Expand utility and
select print to log and then click OK.
Click in the visual snippet editor canvas. A print to log node
appears.
23. Drag the result variable from the
tray on the right to the visual snippet editor canvas. Wire from the result node
to the print to log node, so that your snippet
looks like this:   Restore
the Properties view to its normal size. You have now
visually authored Java code to emit the contents of the result variable
to SystemOut. Technically, by wiring one node to another, you supply
an input parameter to a method.
24. You are done authoring the process! Save your process.
It should look like this:
25. Switch to the assembly editor and save your changes, then
switch back to the business process editor.
26. Optional:  In your process, you sometimes want to
know which activities use a particular variable. There is a way to
do that. In the tray, select the fullname variable.
From the Window menu, select Show
View > References. The References view opens in the lower
left of the perspective, where you see a graph showing as input to
the variable all those activities that set the variable, as shown
in the following figure:

## Results