# Example: validating page data in a heritage human service in
Process Designer (deprecated)

## About this task

The example contains a Credit Application page that gathers information
for a credit card application. To simplify the example, the page has only a
Name field, a Salary field, a Credit
Limit field, and a Submit button. The Name
and Salary fields must contain values, and the Credit
Limit maximum is double the Salary field value.

The example uses a server script to validate the page data. It uses a
CreditCardApplication business object that contains the validation information that
is returned to the page as output. This sample uses the addCoachValidationError
API to construct the business object.

For information on how to validate a page in a heritage human service in the desktop Process Designer, see Example: validating coach data in a heritage human service in the desktop Process Designer (deprecated). For more information about validating a page in a client-side human service, see Validating coach data without exiting a coach.

## Procedure

1 Click Data > Business Object and create the CreditCardApplication business object with thefollowing parameters:
    - name(String)
    - salary(Decimal)
    - creditLimit(Decimal)
2. Click User Interface > Heritage Human Service and create the CreateCreditApplication heritage human service.
Label the default page to Credit Application.
3. In the Variables tab of the heritage human service, add
application(CreditCardApplication) as a private variable.
4. In the diagram view, double-click the Credit Application page to open
it.
5. From the Variables section of the palette, drop the
name, salary, and creditLimit parameters onto the
page. Relabel the default OK button to Submit.
6. Select the connection between the Credit Application page and the end
node. Set Fire Validation to Before. 
 The connection has now a green dot at its start, which indicates that validation is enabled
for the Submit button.
 A boundary event  is automatically attached to the page, indicating that you can connect the page to the
validation script.

 The validation construct ensures that at run time, when the user clicks the
Submit button, the flow first goes to the validation script to do the page
data validation. If the data is valid, the flow then goes to the end node. If you leave the default
setting for Fire Validation at Never, data validation
does not occur, and the flow goes directly to the end node.
7 Create the server script to validate the page data:

1. From the palette, under Activity, use the Server
Script activity tool  to add a script node to the human service diagram, and then select the node.
2 In the Script properties of the node, add the following JavaScript codefor the validation. if (tw.local.application.name == ""){ tw.system.addCoachValidationError(tw.system.coachValidation, "tw.local.application.name", "The name cannot be empty.");}if ( tw.local.application.salary <= 0){ tw.system.addCoachValidationError(tw.system.coachValidation, "tw.local.application.salary", "The salary must be above 0.");}if (tw.local.application.creditLimit > 2 * tw.local.application.salary){ tw.system.addCoachValidationError(tw.system.coachValidation, "tw.local.application.creditLimit", "The credit limit cannot be more than double the salary. " + "The maximum credit limit is $" + 2 * tw.local.application.salary + ".");} The tw.system.coachValidation parameter is theCoachValidation business object that contains the validation information. The firststring contains the full variable path to the data element with the problematic data. The secondstring is the message for the user. The message should identify what is wrong with the data or tellthe user how to fix the problem.Important:

```
if (tw.local.application.name == ""){
    tw.system.addCoachValidationError(tw.system.coachValidation, "tw.local.application.name",
    "The name cannot be empty.");
}
if ( tw.local.application.salary <= 0){
    tw.system.addCoachValidationError(tw.system.coachValidation, "tw.local.application.salary",
    "The salary must be above 0.");
}
if (tw.local.application.creditLimit > 2 * tw.local.application.salary){
    tw.system.addCoachValidationError(tw.system.coachValidation, "tw.local.application.creditLimit",
    "The credit limit cannot be more than double the salary. " + "The maximum credit limit is $" + 
    2 * tw.local.application.salary + ".");
}
```

    - A page can use only one validation script to validate its data. However, more than one page can
use the same validation script.
    - If the data element being validated is not bound to a view, there is nowhere to display a
validation error if one occurs.
    - If a view being validated contains rich text, the validation service must remove any formatting
before validating the contents.
3. Wire the script node in the CreateCreditApplication diagram as shown.
Add a stay-on-page node to the diagram and connect the script node to the stay-on-page node.
 The stay-on-page node loops the flow back to the page if the data in the page is not valid.
The system passes error information back to the page and users see an indicator beside the view with
the problematic data. If the validation service provides error messages, users see the appropriate
message when they hover over an indicator. If the data is valid, the system processes the boundary
event to move to the next step.
8. Click Save or Finish Editing.
9. Run the heritage human service by clicking Run
.
10 In the browser that displays the page, test the validation by doing the following:

1. Leave the Name field empty, type a 1 into the
Salary field and into the Credit Limit field. Click
Submit. The browser displays a message that the Name
field cannot be empty.
2. Type a name into the Name field, and replace the
1 in the Salary field with a 0.
Click Submit. The browser displays a message that the salary must be more
than 0.
3. Replace the 0 in the Salary field with a
1. Replace the 1 in the Credit
Limit field with a 3. Click Submit. The
browser displays a message that the credit limit cannot be more than twice the salary.
4. Replace the 3 in the Credit Limit field with a
2. Click Submit. The human service finishes because
all three values are now valid.