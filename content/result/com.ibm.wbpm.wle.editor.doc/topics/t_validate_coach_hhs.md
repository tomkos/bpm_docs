# Validating coaches in heritage human services (deprecated)

## About this task

The
following procedure describes how to validate coach data by using a server script. For an example,
see Example: validating coach data in a heritage human service in the web Process Designer.

For information about using a service
to validate coach data in the desktop Process Designer, see Example: validating coach data in a heritage human service in the desktop Process Designer (deprecated). For information on how to validate data for shared business
objects, see Save services for shared business objects.

## Procedure

1. To validate the coach data before a boundary event occurs, select the connection between the
coach and the end event. In the properties for the connection, set Fire
Validation to Before.
 The connection shows a green dot at its start, which indicates that
validation is enabled. A boundary event  is automatically attached to the coach, indicating that you can connect the coach to a
validation script.
2. Add a server script that contains the logic for data validation to the human service
diagram.
3 Select the script of the validation pattern. In the Script properties, addJavaScript code that identifies problematic data. Use the tw.system.addCoachValidationError(CoachValidation coachValidation, StringerrorBOPath, String errorMessage) API to add the error data to thecoachValidation system variable. For example, you want two fields to have a value. They are bound to var1 and var2 . To ensure that they have a value, use code like the following examplecode:if (tw.local.var1 == ""){ tw.system.addCoachValidationError(tw.system.coachValidation, "tw.local.var1", "Enter a value for field 1");}if (tw.local.var2 == ""){ tw.system.addCoachValidationError(tw.system.coachValidation, "tw.local.var2", "Enter a value for field 2");} Thetw.system.coachValidation parameter is the system variable that contains thevalidation information. The first string contains the full variable path to the data element withthe problematic data. The second string is the message for the user. The message identifies what iswrong with the data and tells the user how to fix the problem. Important:

```
if (tw.local.var1 == ""){
	tw.system.addCoachValidationError(tw.system.coachValidation, "tw.local.var1", "Enter a value for field 1");
}
if (tw.local.var2 == ""){
	tw.system.addCoachValidationError(tw.system.coachValidation, "tw.local.var2", "Enter a value for field 2");
}
```

    - A coach in a heritage human service can use only one validation script to validate its data.
However, more than one coach can use the same validation script.
    - If the data element that is being validated is not bound to a view, there is nowhere to display
a validation error if one occurs.
    - If a view that is being validated contains rich text, code the validation script to remove
formatting before it validates the text contents.
4. Connect the validate icon of the coach to the validation script.
 A green dot at the coach end of the connection shows that validation
is enabled.
5. Add a stay-on-page event to the diagram, and then connect the validation script to the
stay-on-page event.
This construct loops the service flow back to the coach if the data in the coach is not valid.
At run time, the system passes error information back to the coach and users see an indicator beside
the view with the problematic data. If the validation script provides error messages, users see the
appropriate message when they hover over an indicator. If the data is valid, the system processes
the boundary event to move to the next step.
6. Click Save or Finish Editing.