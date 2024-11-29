<!-- image -->

# Details tab: BPEL process editor

- Assign activity
- Case element, link, repeat until loop and while loop
- Catch element
- Compensate activity
- Empty action
- For Each activity
- Human task activity
- Invoke activity, onEvent and receive case elements
- Process level
- Receive activity
- Receive Choice activity
- Scope activity
- Snippet activity
- Throw activity
- Variables
- Wait activity and Timeout element

## Assign activity

Use the fields
on this page to assign a value from one process element to another.
For more information on how to configure this window, refer to Using assign.

## Case element, link, repeat until loop and
while loop

When you first click the Details tab
for the case element, link, repeat until loop or while loop, you will
see a properties view for the selected element. When you choose No
Expression as the Expression language,
you can click Create a New Condition to launch
the expression builder and compose a condition yourself. The other
choices in the drop down menu are very similar to those options described
in the Expiration tab: BPEL process editor topic.

- in a case, the activities inside this case
element will be commenced if the condition evaluates to true.
- in a while loop, the condition specifies
that the activities inside the while loop are performed repeatedly
while the condition is true. (The true value continues the loop. The
false value breaks the loop.)
- in a repeat until loop, the condition specifies
that the activities inside the repeat until loop are performed repeatedly
until the condition evaluates to true, but at least once. (The false
value continues the loop. The true value breaks the loop.)
- on a link, the condition specifies whether
the link should be taken or not. If it evaluates to false, the subsequent
activity/activities might be skipped.

## Catch element

Use the fields
on this page to specify the fault that this catch element will intercept.
You can catch a built-in fault type, or define one yourself. If you
define it yourself, you will be able to give it a name and associate
it with either a data type or interface variable.

## Compensate activity

## Empty action

Use the fields on
this page to change the empty action into a different activity. You
can choose a different category of activities from the drop down list,
or hover over one of the icons to see a description of its associated
activity. Once you have made your choice, simply click the appropriate
icon and the empty action will change accordingly in your business
process.

## For Each activity

- Sequential
- Choose this to have the iterations run one after the other.

- Parallel
- Choose this to have the iterations run simultaneously. In other
words, the scope that is enclosed in this For Each will get n copies
(where n is the number of iterations), and each scope will get access
to the variables that were there in the beginning.

An example of when to use sequential and parallel would be
in a document review process. In some instances you will want to have
certain people review the document before others, for example, you
may want your technical reviewer to complete their review before the
request goes out to the approver. This example calls for sequential
execution. In other cases you may just need a group of people to review,
for example this is a first draft of a document and the order of their
reviews is not important. This situation calls for parallel execution.

- Array (dynamic bounds)
- This is a simple and dynamic way to define the values for start
and end. When selecting an array the value for Start will
be set to one, and the value for End will be
evaluated in the runtime environment, and will be set to the size
of the selected array.
- If you use XPath in a snippet within the For Each activity (getItemAtIndex()),
keep in mind that XPath indexing is 1-based, so you will have to subtract
1 when accessing the same array using a Java™ snippet
since the index in Java is 0
based.

- Integer (static bounds)
- When you select Integer, two text fields
will appear into which you enter the Start and End values
of the iteration.

- Expression
- Choose this to launch a separate inline visual snippet editor
for the Start and End expressions,
and graphically compose the Java or
XPath code for those expressions yourself.
- In the runtime environment, the expression is only evaluated
once: on the first hit of the For Each activity.

- Integer
- Use Integer, to enter the number of iterations
that will be performed no matter what End value
was entered in the Iteration area.

- Expression
- Choose this to launch a separate inline visual snippet editor,
and graphically compose the Java or
XPath code for those expressions yourself.
- The expression must yield an unsigned integer value, that, when
reached, will terminate the loop.

- None
- Choose this to let the loop iterate as configured.

An example of when to use the early exit condition would be
the document approval process. Using parallel execution the document
was sent out to ten reviewers, but the document author needs only
three completed reviews before sending out the next draft. The user
sets the early exit criterion to be an Integer with
a value of 3.

Again using the document approval process,
we may have given the reviewers the option to respond that they cannot
review at this time. Hence we would select the Count successful
iterations only in conjunction with the early exit criterion
to ensure that the subsequent review is sent out only when three completed
(successful) reviews have been received.

## Human task activity

The fields
on this page show the human task that the business process' human
task activity will implement.

If there is no existing human
task associated, click New to launch the human task editor
to configure one. If there is a human task associated, then click Open to
launch the human task editor to make any needed modifications to it,
or click Remove to clear the association.

If you want
to use data type variables, select one from the list, or clear the
check box and browse to the appropriate request and response variables.

## Invoke activity, onEvent and receive case
elements

Use the fields on this page to configure the implementation
of this activity or element. You can choose a reference partner, and
then choose an appropriate operation from the interface that is displayed.
The table below the Use data type variables mapping check
box displays all of the inputs and outputs of the selected operation.
If you want to use data type variables, select one from the list,
or clear the check box and browse to the appropriate request and response
variables.

## Process level

- Yes
- Choose this to delete the data associated with this instance
of the process once it has completed. This setting will remove the
process instance, whether or not the process completed successfully.

- On successful completion
- In this case, the data will remain in the database when the process
fails so that the problem can be traced and the process may be restarted
by the process administrator, if required.

- No
- Choose this to not delete the data associated with this process
once it has completed.

- If this process should fail when the auto-delete option is enabled,
it will not appear as a failed event in the BPEL process Choreographer
Explorer. To make sure that it does appear should it fail, chose
the No option.
- Setting the value to No means that the process instance will not be
removed. Disabling this flag requires that an administrative strategy for removing finished
processes from the runtime environment is in place, see Deleting process instances using the Business Process Choreographer EJB API.

- Supports
- Use this setting when a compensation service has been configured
for this microflow, but it can run without one.

- Required
- Use this setting when a compensation service has been configured
and the microflow cannot run without it.

- Peer
- The invoked process is considered to be a peer of the primary
process. In this case, both processes run concurrently and happen
to have a point where they intersect.

- Child
- The invoked process is considered to be a child, and the primary
process its parent. As such, the child is tied to the lifecycle and
compensation sphere of the parent.

## Receive activity

## Reply activity

When configuring a Reply
activity, you can implement a normal or fault reply. When you configure
a fault reply, your process is indicating the reply is returning a
fault. A fault indicates an error has occurred. This option displays
in the properties view only when the reply is to contain one or more
faults. To configure a fault reply, enable Fault next
to Reply Type. The table below the Use
data type variables mapping check box displays all of
the inputs of the selected operation. If you want to use data type
variables, select one from the list, or clear the check box and browse
to the appropriate request and response variable. See Raising faults for more detail.

## Receive Choice activity

## Scope activity

## Snippet activity

## Throw activity

Use the fields
on this page to assign a name to the fault that this activity will
throw, as well as browse to an appropriate fault variable to store
the data.

## Variables

Use
the fields to set an initial value for a variable as soon as it is
created. Select Initialize this variable to
define an initial value, and use Initial value to
specify an appropriate value or expression for this type of variable.
You can initialize the variable using the value of another variable,
but the latter variable must be defined in advance. Only previously
initialized variables will be listed.

For variables that are
not simple-type, the XML Literal Builder is a very convenient choice.
Select XML Literal for the Initial
value field, this brings up the XML Literal Builder. Select Value
Editor to use the simple interface to assign values to
your complex variables. If you are comfortable with XML you can use
the XML Editor to review or modify the generated
XML code.

Another useful choice is the XPath expression, see
related topics for more information.

## Wait activity and Timeout element

When
you first click the Details tab for the wait
activity and timeout element, you will see a properties page for these
elements. The configuration options are identical to the Expiration tab: BPEL process editor.

## Related concepts

- Versioning business state machines

## Related tasks

- Working with basic activities

## Related reference

- Description tab: business state machine editor
- Authorization tab: BPEL process editor

## Related information

- Customizing behavior with visual snippets