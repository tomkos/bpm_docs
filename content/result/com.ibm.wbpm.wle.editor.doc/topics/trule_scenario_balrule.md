# Scenario: Creating a Decision service in a Personalized Notification process (deprecated)

## Before you begin

To perform
this task, you must be in the IBM® Process
Designer desktop
editor, which is deprecated.

## About this task

<!-- image -->

## Procedure

To add a Decision service to the Personalized Notification
process, complete these steps:

1. Open the desktop Process Designer (deprecated).
2. Open a process application that contains a business process
definition (BPD).
3 Create a new Decision service called NotificationRulesService . Youcan find more information about adding a Decision service in the relatedtopic "Adding a Decision service to a process."
    1. In the Library panel on the left side of the Process Designer window,
move the mouse cursor over the Decisions item
in the list of library items for the process application.
    2. Click the plus sign next to Decisions to
add a new Decision service.
    3. In the Create New window, click Decision
Service.
    4. In the New Decision Service window,
enter NotificationRulesService as the Decision
service name, then click Finish.

<!-- image -->

4 Add a BAL Rule component called AlertRules tothe NotificationRulesService Decision service. You can find moreinformation about adding a BAL rule component in the related topic"Adding a BAL Rule component to a service."

1. Make sure that you are editing the NotificationRulesService
Decision service.
2. Click BAL Rule in the component
palette and drag the BAL Rule component icon from the palette to the
service diagram.
3. In the Properties tab, enter AlertRules ad
the name for the new BAL Rule component.
4. Click Save, or use the Ctrl+S keyboard
shortcut to save the Decision service.

<!-- image -->

5 Create a business object called CheckingAccount thatcontains parameters such as CustomerName, Balance and Payments. Youcan find more information about creating a business object in therelated topic "Adding variable types and business objects to a Decisionservice."

1 Add a business object from the Process Designer librarypanel.
    1. Click the indicator next to the process application name in the
library panel to see the categories of library items in the current
process application.
    2. Click the plus sign next to the Data library
item.
    3. In the Create New window, click Business
Object.
    4. In the New Business Object window, enter CheckingAccount as
the name for the business object, then click Finish.
2. In the Behavior section of the
Business Object panel, select Complex Structure Type as
the Definition Type.
3 Add parameters to the CheckingAccount businessobject.

1. In the Parameters section of the Business Object panel, click Add.
2. In the Parameter Properties section, add the CustomerName parameter
with the variable type set to String, the Balance parameter
with the variable type set to Decimal, and
the PastPayment parameter with the variable
type set to Payment.
4. Click Save, or use the Ctrl+S keyboard
shortcut to save the Decision service.

<!-- image -->

6 Define which of the parameters are used as input variablesto the Decision service, such as CustomerName, Balance and PastPayment,and which parameters are output variables from the Decision service,including the notification message. You can find more information about defining Decision servicevariables in the related topic "Adding and modifying Decision servicevariables."

1. Make sure you are editing the NotificationRulesService
Decision service.
2. Click the Variables tab.
3 Click Add Input to add the inputvariables:
    1. In the Details section, enter accountIn as
the name for the input variable.
    2. Click Select next to Variable
type and click CheckingAccount in
the list.
    3. Click the plus sign next to accountIn in
the Variables list to confirm that CustomerName, Balance and PastPayment are
included in the list.
4 Click Add Output to add the outputvariable, notificationOut .

1. In the Details section, enter notificationOut as
the name for the output variable.
2. Click Select next to Variable
type and click Notification in
the list.
3. Click the plus sign next to notificationOut in
the Variables list to confirm that message is
included in the list.
5. Click Save, or use the Ctrl+S keyboard
shortcut to save the Decision service.

<!-- image -->

7 Use the BAL Rule editor to create rules in the AlertRulesBAL Rule component. You can find more information about using the BAL Rule editorin the related topic "Creating a rule using the rule editor."

1. Make sure you are editing the NotificationRulesService
Decision service.
2. Click the Diagram tab, then click to select the AlertRules
BAL Rule component.
3. Click the Decisions tab. By default, the
rule editor opens with an empty BAL rule window. The rule window contains
a basic template for a simple rule, with one condition (if)
and one action (then).
4 Click inside the rule window to begin creating a newrule from the template. The first part of the rule (if ) looks likethis:if the amount of paymentIn is more than the balance of accountIn
    1 Click the condition placeholder, next to if , to use theContent Assist menu to complete the condition. Add the following conditionstatements by double-clicking on each as it appears in the list. Ifthe list closes before you can select a condition statement, press Shift+Spacebar toreopen the Content Assist menu.
        - if the amount of
        - paymentIn
        - is more than
        - the balance of
        - accountIn

```
if the amount of paymentIn is more than the balance of accountIn
```

5 Click the action placeholder next to then andadd the following condition statements. When you double-click to select string , theedit cursor appears between two double quotation marks. Type the notificationmessage, Payment takes account overdrawn betweenthe double quotation marks.The second part of the rule (then )looks like this:then set the message of notificationOut to "Payment takes account overdrawn";

- set the message of
- notificationOut
- to
- string

```
then set the message of notificationOut to 
 "Payment takes account overdrawn";
```

6. Add a second rule editor window. Click the plus sign
in the upper right corner of the BAL rule editor panel. Repeat the
previous sequence of steps to create a second rule that looks like
this: if there is no payment in the past payments of accountIn 
 where the payee of this payment is the payee of paymentIn , 
then 
set the message of notificationOut to the message of notificationOut + "\n" +
 "Payment to new payee: " + the payee of paymentIn ;
7. Click Save, or use the Ctrl+S keyboard
shortcut to save the Decision service.

<!-- image -->

8 Attach the NotificationRulesService Decision service tothe Send Alert decision gateway. You can find more information about decisionsin the implementation of a gateway, and attaching a Decision serviceto a gateway, in the related topic "Attaching a Decision service toa decision gateway."

1. Make sure you are editing the NotificationRulesService
Decision service.
2. In the business process definition diagram, click  the
Send Alert decision gateway icon to select the decision gateway.
3. Click the Properties tab.
4. Click Decision.
5. In the Decision Service section,
click Select. Click to select the
NotificationRulesService Decision service.
6. Click Implementation in the Properties
tab.
7. Under the Decisions heading,
add a variable statement to each decision to control the output of
the decision gateway.

<!-- image -->

9 Test the Decision service and the BAL rules that you createdand attached to the decision gateway.

1. Make sure that you are editing the NotificationRulesService
Decision service and the AlertRules BAL Rule component.
2. In the NotificationRulesService Decision service, click
to select the Send Alert decision gateway.
3. Set a breakpoint for the gateway. Set breakpoints
at specific locations in the process where you want the process flow
to pause during testing so that you can determine the status of the
process, and identify any errors that might have occurred.
4. In the AlertRules BAL Rule component panel, click the Debug  icon in the banner above the rule editor windows.
5. The Business Automation Workflow Debug
Service opens in a new browser window.
6. When Process Designer prompts
you to change to the Inspector interface, click Yes.
The prompt to switch to the Inspector view might be covered up by
the Debug window.
7. Click Step in the Debug window
to run the Decision service one step at a time. The Inspector
clearly identifies any errors in the Execution State panel. The Inspector
also tells you where the error happened, and links directly to the
source of the problem. The Debug service browser window captures error
and exception messages. For more information about using the Debug
service and the Inspector window to identify and fix Decision service
problems, refer to the related topic "Debugging a Decision service."
8. If you make any changes to resolve errors in the Decision
service or the BAL rules, click Save, or use
the Ctrl+S keyboard shortcut to save the Decision
service.

## What to do next