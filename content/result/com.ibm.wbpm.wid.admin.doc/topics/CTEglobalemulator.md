<!-- image -->

# Defining global emulators in the Component Test Explorer

## Before you begin

## About this task

## Procedure

1. In the menu bar of Component Test Explorer, click Component
Emulators. The Component Emulators page opens.
2. In the explorer area, click a component. The Component
view is displayed for the selected component.
3. In the Emulate this Component field,
select Yes. A check mark appears on the component
in the explorer area to denote that the component is being emulated,
as shown in the following figure:
4. If you want to define an emulator for an operation, expand
the component and interface, then select the operation name and click Create.
The details area displays the operation name and a table that contains
the emulator rules as you create them. Each rule has a condition that
describes the conditions under which the rule should be applied and
a response that describes the output from the operation.
5. The Condition section includes the
Groovy statements that are constructed when you click the buttons
in the Request and Operations sections.
You can also enter a Groovy  statement directly. An evaluated Groovy
statement determines whether the response should be returned for the
operation invocation. The Condition section
can contain many Groovy statements, but the last statement must evaluate
to a Boolean string to determine whether the rule will be used. Only
the final statement will be evaluated as the condition. To programmatically
set the Condition expression, click Assist.
The Condition section populates with a Condition expression that you
can modify.
6. For example, if the condition should be If the
request Vacation.id field is not null, then click Getter for
the id field. The resultant Groovy statement will look  like input.get('/vacation/id').
Then click the != Operation button and type null to
get the following final expression: input.get('/vacation/id')!=null.
7. To save the condition, click Finish.
You return to the previous screen with the condition expression completed.
8. In the Response section, specify
static representations of the parameters that will be returned from
the operation when the Groovy statement in the Condition section
evaluates to true. To programmatically set
the response, click Assist.
9. To assign programmatically calculated values to the response,
specify Groovy statements in the Implementation section.
Groovy statements can run when the static response values are set.
You can specify multiple statements in this section.
10. The details section shows the input request as well as
the output response. Click Assist to programmatically
set the implementation. For example, if you want to copy input values
from the request to the response and then set the state to STARTED,
you can use the Code Assist view to do the copying and then use the
static view to set the state.
11 To copy the input to output, complete the following steps:
    1. In the Response section, click Setter and
then click Getter.
    2. Cut the getter string and paste it into the setter string
by replacing the question mark (?). To separate statements with a
new line, press Enter.
    3. To save the implementation and return to the previous
view, click Finish.
    4. In the static section, enter the STARTED state,
as shown in the following figure:
    5. Save the emulator and click Finish.
The condition displays in the Rules table, as shown in the following
figure:
12 Complete one of the following steps to activate, deactivate,or define the component emulators:

- If you want to activate all of the defined component emulators,
click the Start icon .
- If you want to deactivate all of the component emulators,
click the Stop icon .
- If you want to import component emulators, click the Import icon .
- If you want to export component emulators, click the Export icon .

## Results

Note: When you import emulators, all of the existing
emulators will be overwritten. If an emulator is defined for any operation
of a component, then all of the operations for that component will
be emulated.