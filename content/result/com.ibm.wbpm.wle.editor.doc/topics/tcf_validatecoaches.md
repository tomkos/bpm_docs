# Validating data without exiting the coach

## About this task

For a typical coach validation, you can use a client-side JavaScript that you specify in the
coach to be validated. To avoid perceived performance issues with the coach, it is a best practice
to use a fast-executing script.

For information on how to perform coach data validation after exiting the
coach, see Validating coach data after exiting a coach.

## Procedure

To validate the coach data in your client-side human service without exiting the
coach:

1. Open the client-side human service that contains the coach to be validated.
2. Select the coach to be validated and switch to Data Change.
3 In the Script properties, add the JavaScript code that identifies the problematic data in the coach. Use the tw.system.coachValidation.addValidationError (StringvariableName, String errorMessage) JavaScript API to identify the view that has theproblematic data and provide a message that helps the user to correct theproblem. Forexample:if (tw.local.startDate.getTime() > tw.local.endDate.getTime()) tw.system.coachValidation.addValidationError("tw.local.startDate", "The start date must precede the end date. Set the start date before the end date, and try again."); Note:

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
4. Click Save or Finish Editing.
5 Test that the coach validation works correctly by clicking Run . At run time, when data is changed in one of the views, the following validation actions occur: For an example, see Example: validating a coach in a client-side human service .

<!-- image -->

- If the data is valid, the coach execution completes successfully.
- If the data in the coach is not valid, a validation error occurs, and the control indicates the
problem.
- If the next change fixes the data, the data is validated again, and the error is removed.