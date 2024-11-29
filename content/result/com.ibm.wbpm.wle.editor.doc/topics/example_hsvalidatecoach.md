# Example: validating a coach in a client-side human service

## About this task

The following example demonstrates how to validate the data that a user enters in the coach so
that an error message shows up in the coach when the data is not valid. The example also
demonstrates how to prevent the user from proceeding to the next step when the data is not
valid.

## Procedure

1. Create the client-side human service that contains the coach to be validated. See Building a client-side human service.
2. In the Variables coach of the human service, create two private
variables, startDate and endDate, and set the type of each
variable to Date.
3. In the client-side human service diagram, rename the coach to Prompt for Start and
End Dates.
4. In the coach, use the top insertion point of the OK button to add two
Date Time Picker views (stacked vertically), rename the views to startDate
and endDate, and ensure that they are bound to the
startDate and endDatevariables, respectively. Leave the
default OK button unchanged.
5. Save the coach configuration.
6 In the diagram view for the coach, under Data Change > Script , enter the following JavaScriptconstruct: if (tw.local.startDate.getTime() > tw.local.endDate.getTime()) tw.system.coachValidation.addValidationError("tw.local.startDate", "The start date must precede the end date. Set the start date before the end date, and try again."); Inthe coachValidation object, the first string contains the full variable path to theelements whose data is to be validated. The second string is the message for the user, whichspecifies what is wrong with the data and tells the user how to fix the problem.Note:

```
if (tw.local.startDate.getTime() > tw.local.endDate.getTime())
	tw.system.coachValidation.addValidationError("tw.local.startDate", "The start date must precede the end date. Set the start date before the end date, and try again.");
```

    - If the data element that is being validated is not bound to a view, there is nowhere to display
a validation error if one occurs.
    - If a view that is being validated contains rich text, the validation script must remove the
formatting before validating the contents.
    - If you are validating a list and you want the error to refer to the entire list, the
variableName parameter must include [] as a suffix. This
matches view binding where [] indicates that the object is a list. For example, if
a view is bound to tw.local.var3[], which is a list, you need code like the
following example:
tw.system.coachValidation.addValidationError("tw.local.var3[]", "Var3 has validation error");
7 Optional: To prevent the user from proceeding to the next step when the data is not valid, complete thefollowing steps:

1. In the Variables coach for the human service, add another private variable
named readyToSubmit, and set its type to Boolean.
2. In the Data Change > Script properties of the coach, append the following JavaScript code to the existing script:

tw.local.readyToSubmit = tw.system.coachValidation.validationErrors.length==0;
3. In the coach, configure the OK button to be read-only when not ready, as
shown:
8. Click Save or Finish Editing.
9. Click Run
 to run the human service.
10 In the browser that displays the coach, test the validation by completing the followingsteps:

1. Set the End date to a date that precedes the start date. Click
OK.
The browser highlights the Start date field and displays a
warning icon. If you hover over the warning icon, you see a message that the start date must precede
the end date.
2. Set the end date to a date that succeeds the start date. Click OK.
The human service completes successfully because both dates are valid.