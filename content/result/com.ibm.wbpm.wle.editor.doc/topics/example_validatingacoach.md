# Example: validating page data in a heritage human service in the desktop Process Designer
(deprecated)

The example contains a Credit Application page that gathers information for a credit card
application. To simplify the example, the page has only a Name field, a
Salary field, a Credit Limit field, and a
Submit button. The Name and
Salary fields must contain values, and the Credit
Limit maximum is double the Salary field value.

The example uses a General System Service to validate the page data. Except for Ajax services and
human services, you can use any service type and you are not limited in how the service does the
validation. However, the service must construct a CoachValidation business object
to contain the validation information that it returns to the page as output. This sample uses the
addCoachValidationError API to construct the business object. For the sake of
simplicity, the service in the example uses a script to validate the data.

For information on how to validate a page in a
heritage human service in the Process Designer,
see Example: validating coach data in a heritage human service in the web Process Designer. For more information about validating a
page in a client-side human service, see Validating coach data without exiting a coach.

1 Create the CreditCardApplication business objectwith the following parameters:
    - name(String)
    - salary(Decimal)
    - creditLimit(Decimal)
2. Create the CreateCreditApplication heritage human
service.
3. Add application(CreditCardApplication) as a private
variable.
4. In the diagram, add the Create Application page, and then open the page.
5. From the Variables section of the palette, drop the
name, salary, and creditLimit parameters onto the
page. Relabel the default OK button to Submit.
6. In the diagram, connect the Credit Application page to the start and end nodes.
7. Select the connection between the Credit Application page and the end node. Set Fire Validation
to Before. The connection now has a check mark at its start. The page has an
icon  to indicate that you can now connect the page to the validation service. This change means
that when the user clicks the Submit button, the flow first goes to the
validation service to do the data validation. If the data is valid, the flow then goes to the end
node. If you leave Fire Validation at its default of Never, the data
validation does not occur and the flow goes directly to the end node.
8 Create the service to validate the page data:

1. From the library, create a general system service called
CreditApplicationFormValidation.
2. On the Variables page of the service, add
application(CreditCardApplication) as an input of the service. Important: The name and the type of the service input must match the name and type of the page
variable that contains the data that you want to validate.
Add
validate(CoachValidation) as an output of the service. The service must have one
output only and it is of the CoachValidation type. The presence of this output
indicates that the service is a validation service. In this case, the example uses the input to
provide the data that the service validates.
3. Add a server script to the service diagram and connect the start and end nodes to the
script.
4 In the implementation of the server script, add the following code to construct theCoachValidation businessobject:tw.local.validate = new tw.object.CoachValidation();if (tw.local.application.name == ""){ tw.system.addCoachValidationError(tw.local.validate, "tw.local.application.name", "The name cannot be empty.");}if ( tw.local.application.salary <= 0){ tw.system.addCoachValidationError(tw.local.validate, "tw.local.application.salary", "The salary must be above 0.");}if (tw.local.application.creditLimit > 2 * tw.local.application.salary){ tw.system.addCoachValidationError(tw.local.validate, "tw.local.application.creditLimit", "The credit limit cannot be more than double the salary. " + "The maximum credit limit is $" + 2 * tw.local.application.salary + ".");} Thetw.local.validate parameter is the CoachValidation business objectthat contains the validation information. The first string contains the full variable path to thedata element with the problematic data. The second string is the message for the user. The messageshould identify what is wrong with the data or tell the user how to fix the problem.Important:

```
tw.local.validate = new tw.object.CoachValidation();

if (tw.local.application.name == ""){
    tw.system.addCoachValidationError(tw.local.validate, "tw.local.application.name",
    "The name cannot be empty.");
}
if ( tw.local.application.salary <= 0){
    tw.system.addCoachValidationError(tw.local.validate, "tw.local.application.salary",
    "The salary must be above 0.");
}
if (tw.local.application.creditLimit > 2 * tw.local.application.salary){
    tw.system.addCoachValidationError(tw.local.validate, "tw.local.application.creditLimit",
    "The credit limit cannot be more than double the salary. " + "The maximum credit limit is $" + 
    2 * tw.local.application.salary + ".");
}
```

    - A page can use only one validation service or server script to validate its data. However, more
than one page can use the same validation service or script.
    - If the data element being validated is not bound to a view, there is nowhere to display a
validation error if one occurs.
    - If a view being validated contains rich text, the validation service must remove any formatting
before validating the contents.
9. Add the CreditApplicationFormValidation service
to the CreateCreditApplication heritage human service
diagram.
10. Select the CreditApplicationFormValidation service and open the data mapping
properties. To provide the data to the validation service, add the application
private variable as an input map. To map the output of the validation service to the
CoachValidation object, add the following variable as an output map:
tw.system.coachValidationImportant: The output mapping to the
system variable is mandatory for the page to use the service as a validation service. The
tw.system.coachValidation parameter is the system variable that contains the
validation information.
11. Connect the validate node  of the Credit Application page to the
CreditApplicationFormValidation service.
12. Add a Stay on Page node to the diagram.
13. Connect the CreditApplicationFormValidation service to the Stay On Page node.
This construction loops the flow back to the page if the data in the page is not valid. The system
passes error information back to the page and users see an indicator beside the view with the
problematic data. If the validation service provides error messages, users see the appropriate
message when they hover over an indicator. If the data is valid, the system processes the boundary
event to move to the next step.
14. Save your changes and then run the heritage human service by clicking
the  button.
15 In the browser that displays the page, test the validation by doing the following:

1. Leave the Name field empty, type a 1 into the
Salary field and into the Credit Limit field. Click
Submit. The browser displays a message that the Name field cannot be
empty.
2. Type a name into the Name field, and replace the 1 in the Salary field
with a 0. Click Submit. The browser displays a message
that the salary must be more than 0.
3. Replace the 0 in the Salary field with a 1. Replace the 1 in the Credit
Limit field with a 3. Click Submit. The browser
displays a message that the credit limit cannot be more than twice the salary.
4. Replace the 3 in the Credit Limit field with a 2. Click
Submit. The human service now finishes because all three values are now
valid.

Pay attention to the following behavior when you debug a page and step through each activity in
the flow as the page service is running: If page data validation is required at a step, the validate
boundary event path loops back and goes back to open a new page. Because the validate boundary event
response cannot go back to the originating page during the debugging, you do not see a visual error
during debugging. You can step through a page and see the validation error on the debug page, but
the flow always returns to a new page.

- Run to continue.
- Run to the next break point that is defined in the next step in
a regular boundary event flow. This option moves to the next step
in the regular boundary event flow.