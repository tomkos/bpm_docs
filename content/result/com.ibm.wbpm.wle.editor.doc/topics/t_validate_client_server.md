# Validating coach data after exiting a coach

## About this task

- The validation must access private or confidential data that should not be made available to the
client. Server-side validation is the more secure approach.
- The validation must access server-based data or large amounts of data to do the validation. For
example, you have an Order coach in which users can order parts and you want to validate that a part
is in stock. It is not practical to use a coach data validation without exiting the coach in this
situation. Loading large amounts of data impacts the performance of the client.
- You are migrating heritage human services (deprecated) to client-side human services
and you want to reuse some or all of the validation scripts you had in the heritage human service.
The client-side human services call the validation service that you previously used. However,
examine the script logic to move appropriate validation code to the client to minimize server
calls.

## Procedure

To validate the coach data after exiting the coach:

1 In the designer, create the service that validates the coach data. The service cannot be a human service but it can be a service flow. See Creating a service flow . The example code uses a service flow called Save Ticket Service.
    1. In the Variables view, create an input variable that contains the data
from the coach.
    2. Create the validationResults(CoachValidation) private variable that contains
any validation messages.
    3. Create the hasValidationErrors(Boolean) private variable to indicate when
there is data that fails the validation tests.
    4 In Diagram view, add the following elements:
        - A server script to validate the data.
        - A decision gateway to route the flow according to whether the data is valid.
        - A service task that saves the coach data or an end event to complete the service.
        - An error end event.
5. Connect the Start node to the script and connect the script to the decision. Connect the
gateway to the flow that handles valid data such as a service that saves coach data. Select the flow
line and rename it to Yes. Connect the gateway to the error end event. Select
the flow line and rename it to No.
The resulting diagram looks something like this example:
6. Add JavaScript code to the script to validate the
coach data.
The script code must create a CoachValidation object that contains an
addCoachValidationError instance for every problem with the coach data. If there is
a problem with the coach data, the script must also set isValid to
false.
For example, if the help ticket must contain information in the Summary field, add code
like the following example:// Create the CoachValidation object
tw.local.validationResults = new tw.object.CoachValidation();
tw.local.hasValidationErrors = false; 	// Set to false unless the data fails a validation test
if (tw.local.ticket != null) {
	// If there is nothing in the summary, add the error to the Coach Validation object
	if (tw.local.ticket.summary == null || tw.local.ticket.summary.length == 0) {
    	tw.local.hasValidationErrors = true;
		tw.system.addCoachValidationError(tw.local.validationResults, 
			"tw.local.ticket.summary", "The problem summary is required.");
	}
}
7. In the Implementation properties of the decision, add the following code
to the No branch:

tw.local.hasValidationErrors == true
8. In the Implementation properties of the error end event, set
Error code to coachValidation and set Error
mapping to the tw.local.validationResults variable.
These properties are the mechanism by which the client-side human service receives the
validation messages.
2. Open your client-side human service.
3. In your client-side human service, add a service to your diagram and wire your coach to
the service.
4. In the Implementation properties of the service node, select to call a
service and then select the server-side validation service that you created in step 1.
5. In the Data Mapping properties, map the variable that contains the coach
data to the appropriate business object.
6. Add an intermediate event to the service. Because it is attached to a service,
the intermediate event is an error boundary event.
7. In Implementation properties of the error boundary event, set it to catch
specific errors and map the error data to the tw.system.coachValidation
variable.
8. Connect the error boundary event to a stay on page node.
9. Alternatively, you can add a client-side script node after the coach, followed by a
decision gateway, and specify the coach validation logic in the script:
10. Click Save or Finish Editing.