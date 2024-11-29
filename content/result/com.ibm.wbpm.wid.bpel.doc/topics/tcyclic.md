<!-- image -->

# Working with generalized flow activities

## About this task

| Type of activity          | Supports parallelism?   | Cycles?   | Fault links   |
|---------------------------|-------------------------|-----------|---------------|
| Parallel activity         | Yes                     | No        | No            |
| Generalized flow activity | Yes                     | Yes       | Yes           |

You can create a generalized flow activity as follows:

## Procedure

1. Drop a generalized flow activity onto the canvas.
2 Populate the generalized flow activity with the necessaryactivities. It is important that a generalized flow has:
    - exactly one start activity (an activity with outgoing links
but no incoming links)
    - one or more end activities (an end activity is an activity with
incoming links and no outgoing links).
3 Link the activities together as follows:

1. For each element (action or structure) that forms part
of the generalized flow, click the element to select it, right-click
to launch a menu of choices and select Add a link.
Move the mouse so that the free end of the new link is positioned
on the target element and click. A link is created
from the first element to the second.Note: On the same menu as the Add
a link option you will also see Add a fault
link which is tool for creating simple fault handling
behavior in your generalized flow.
2. Create the necessary links between each of the nested
activities. When you are done, there should be a clear control path
through the activities. Note: Crossing links (links where
the source activity and the target activity reside in different structured
activities) are not supported within a generalized flow activity.
4. Optional: Create fault links where appropriate.
When faults occur in your business process, fault handlers
are typically engaged to deal with the fault. The generalized flow
activity offers a simplified fault handling procedure. From any scope
or basic activity (excluding the Throw and Rethrow activities) you
can add one or more fault links. A fault link in an activity
is followed if the specified fault occurs while the activity is running.
You can define catch fault links for various conditions, or
you can create a catch all fault link, which will be followed
should any fault occur that is not covered by a catch fault link.
If multiple fault links are modeled for the same activity, best match
decides which fault link will be followed. The fault catching rules
are the same as for fault handlers.Note: No more than one fault link
can catch an occurred fault.

You can terminate the fault
link at any activity within the generalized flow - for example you
may choose to direct the fault link to a terminate activity to have
the business process stop if a fault occurs, or you may want the business
process to skip the rest of the steps in the generalized flow and
exit to the next activity in which case you would terminate the fault
link at the last activity in the generalized flow. You can also use
a fault link to create a cycle and loop back to a previous activity.
To
create a fault link, right-click the activity and select Add
a fault link. Drag the cursor out over the canvas. A black
line is now attached to the cursor, and when you hover over a valid
incoming link icon or valid gateway, the crossed out circle disappears,
and the link snaps into place. Click the activity or gateway that
you want to link to. The fault link becomes a striped red line and
connects the two activities.
5 Specify the diverging gateway type. A diverginggateway is made available for an activity when two or more links (excludingfault links) start at this activity. You can specify one of threetypes of diverging gateway.

- Split - exclusive
pathway. When the activity runs successfully, the first link that
evaluates to true is followed, at least one of the links must
evaluate to true. None of the other links are followed. Since
the default condition for a link is true, it may then be necessary
to adjust the execution order to make sure that the appropriate link
is fired. Links starting at this gateway type can loop back to a previous
activity in the flow, so these links can create a cycle.
- Fork - parallel pathways.
When the activity runs successfully, all links are followed. Link
conditions cannot be specified. If this activity is skipped, all links
are followed with a false flag, which influences the behavior
at the converging gateway.

- Inclusive OR - parallel
pathways with conditions. When the activity runs successfully, all
links that evaluate to true are followed with a true flag,
at least one of the links must evaluate to true. All links
that evaluate to false are followed with a false flag.
When the activity is skipped all links are followed with a false flag.
6 Specify the converging gateway type. A converginggateway is made available for an activity when two or more links (includingfault links) end at this activity. You can specify one of three typesof converging gateway.

- Merge - exclusive
pathway. When the first link is followed with a true flag,
the gateway is evaluated and the activity commences. No synchronization
happens with the remaining incoming links.
- Join - parallel pathways.
All incoming links are synchronized, the gateway is evaluated when
all links are followed. When all links are followed with a true flag
the activity commences. When all links are followed with a false flag
the activity is skipped. When some links are followed with a true flag
but some with a false flag the runtime throws an exception. Note: In
cases where this exception can happen, a warning is displayed while
modeling the process or when deploying the process.
- Inclusive OR - exclusive
or parallel pathways. This gateway can be used to merge exclusive
paths, or to join parallel paths, or both. When merging exclusive
paths, the gateway is evaluated and the activity commences when the
first link is followed with a true flag. When joining parallel
paths, all incoming links are synchronized, the gateway is evaluated
when all links are followed. When one or more links are followed with
a true flag the activity commences. When all links are followed
with a false flag the activity is skipped. When exclusive and
parallel paths converge at this gateway, it is evaluated in the reverse
order of the opposite converging gateways. See troubleshooting for
more information.
7 Create any necessary conditions as follows:

1. Click a link to highlight it. Links commencing
at a fork gateway cannot have a condition applied.
2. In the Details page of the properties
area, click Create a new condition.
3. Configure the condition. You can use a Simple expression
language (True, False, or Otherwise) or program the condition using
either Java or XPath.
If you choose Java™, you can
use the snippet editor to visually compose the code, or enter it directly
into the Java editor yourself.
4. If necessary, adjust the link evaluation order by selecting
the Split gateway with multiple outgoing links, and clicking the Link
Evaluation Order tab in the Properties area.
8 Create conditions for you fault links as follows:

1. Click a fault link to highlight it.
2 In the Details page of the propertiesarea, choose Catch or Catch All . For a catch fault link you can specify the fault name tobe caught. This can either be a built-in or a user-defined fault.Additionally you can select a fault variable. The fault variable mustbe declared on one of the parent scopes or the process scope. Defaultvariable scoping rules apply. For a catch fault link either the faultname, the fault variable or both must be specified. A catch all faultlink will be followed if a fault occurs and no catch fault link isapplicable. If you specify only catch fault links and do not coverevery eventuality with your conditions you may end up in a situationwhere a fault occurs but the process cannot follow any of the faultlinks. In this case the fault will be thrown to the next scope orto the process scope where normal fault handling continues. Ifmore than one catch fault link is specified for an activity, the followingrules determine which fault link is navigated (these rules are thesame as for a fault handler):

For a catch fault link you can specify the fault name to
be caught. This can either be a built-in or a user-defined fault.
Additionally you can select a fault variable. The fault variable must
be declared on one of the parent scopes or the process scope. Default
variable scoping rules apply. For a catch fault link either the fault
name, the fault variable or both must be specified. A catch all fault
link will be followed if a fault occurs and no catch fault link is
applicable. If you specify only catch fault links and do not cover
every eventuality with your conditions you may end up in a situation
where a fault occurs but the process cannot follow any of the fault
links. In this case the fault will be thrown to the next scope or
to the process scope where normal fault handling continues.

    - If the fault has no associated fault data, a catch fault link
with matching fault name will be selected (providing the catch fault
link has no variable assigned to it). Otherwise, a catch all fault
link is chosen when modeled.
    - If the fault does have fault data associated with it, then a catch
fault link with matching fault name and variable data type will be
selected. If there is no fault name specified, then a catch fault
link with a matching data type will be selected. Otherwise, a catch
all fault link is chosen when modeled.

## Example

<!-- image -->

In this example, the order of a color copy comes in through
the Receive copy order activity. A human task is then assigned
to an employee in the Set up print activity who sets up the
source file for printing. Part of this set up process includes adjusting
the colors so that they are a close match to the original. When this
set up process is complete, the flow continues to the Print activity
which produces the copy. The output is then directed to another human
task, the Color inspection activity. This employee has the
responsibility to decide if the colors are a close match to the original.
If they are not, then the evaluation is set to false, and the
flow is returned to the Set up print activity. This loop will
continue until such time that the employee at the Color inspection activity
decides that the color is acceptable, and the process is allowed to
process to the Ship copy activity.

- Resolving modeling errors in generalized flow activities

When modeling generalized flows there are some common mistakes that can occur. Simple steps to deal with these problems are described.

## Related reference

- Link Evaluation Order tab: BPEL process editor