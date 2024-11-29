# Building a heritage human service with heritage coaches (deprecated)

## Before you begin

To perform
this task, you must be in the IBM® Process
Designer desktop
editor, which is deprecated.

## About this task

If you add an activity to a non-system
lane in a BPD, the activity is initially implemented using the default
human service. You can double-click an activity in a non-system lane
to open the default human service. By examining the service components
and running the default service in the Inspector, you can get an idea
of how human services work and how coaches are used to display and
collect data from process participants.

The following steps
describe how to build a sample heritage human service using example
values. The service in the sample enables employees to enter expenses
for the Expense Reimbursement BPD. This BPD contains an activity called Enter
Expenses and a private variable called request.
The request variable is an EmployeeReimbursement business
object, which has id(String), type(String), amount(Decimal),
and status(String) parameters. See Creating business objects for information. For your
own implementation, you might not use the same steps or names.

## Procedure

1. Starting with the Expense Reimbursement BPD, right-click
the Enter Expenses activity and select Activity Wizard from
the list of options.
2. In Activity Wizard - Setup Activity,
make the following selections: 
Table 1. Recommended
selections in Activity Wizard - Setup Activity

Option
Selection

Activity Type
User Task

Service Selection
Enable the radio button for the Create a New
Service or Process option
3. Type a name for the new service in the Name field.
(The name for this sample service is Enter Expense.)
4. In Activity Wizard - Setup Activity,
click the Next button.
5 In Activity Wizard - Parameters ,choose the existing process variables to use as input and output forthis new service.
    1. You can see the private variable named request.
For this sample, set Input to false and
leave Output set to true.
This enables you to collect the data for the expense using this new
service and then output those values for the subsequent process steps
to act upon.
    2. Click the Finish button. The
new service is created and attached to the activity. The new service
includes a single Coach.
6. Double-click the activity for which you created the new
heritage human service using the Activity Wizard. 
The new service opens in the Designer.
7. Click the Coaches tab and then click
the listed coach component. Because you used the Activity
Wizard, the coach includes a form element for each of the
parameters in the request structure.The
coach designer is where you customize the coach layout and create
or edit the bindings between inputs and outputs. Notice that when
the coach designer is open, the palette shows all the elements (sections
and controls) that you can use in a coach. (Hover over a control to
view a brief description. See Building heritage coaches for
more information about the coach designer.)The items in the palette
are described in the links at the bottom of this page.
8. In the coach designer, right-click the Status control
and select Delete from the list of options.
The status of a request is not data that we need to collect from employees,
but is a value set later after a request is further processed and
so it can be removed.
9. Click the Id control. In
the properties, the Id: field label matches the parameter
in the request variable. Change the label to Employee
ID: so that employees know exactly which ID to provide.
10. Click the Type control. In
the properties, the Type: field label matches the
parameter in the request variable. Change the label
to Employee type:.
11 To enable employees to select from an existing list ofemployee types, in the properties for Employee type ,click the drop-down list for Control Type andchoose Single Select .

1. Select Presentation in the properties.
Under Widget Style, select Drop
Down List for Widget Type.
2. Under Manual Data, click Add to
add a value and associated display text for each option that you want
in the drop-down list.
12 To add a Cancel button to the coach,select the control that contains OK in thecoach designer.

1. In the Presentation properties,
go to the Buttons section and click Add.
2. In the Button Details, enter Cancel for
the label and click Is Cancel.
13. Click Save in the main toolbar.
14. Click the Preview tab at the bottom
of the coach designer to view the coach. The Preview tab
shows how the coach will appear to users when the BPD runs.
15. Click Run Service in the upper right
corner to view the coach in a web browser.