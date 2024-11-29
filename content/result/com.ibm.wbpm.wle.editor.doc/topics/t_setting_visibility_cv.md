# Setting the visibility of views

## About this task

- Same as parent (default value)
- Required
- Editable
- Read only
- None
- Hidden

When you set the visibility to Same as parent, you set the view to
inherit its visibility from the coach or view that contains it. For example, your view is within a
view that has Read only visibility. If your view's visibility is set to
Same as parent, your view inherits the Read only value. For
information about these options and visibility in general, see View visibility properties.

| In a page                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | In a view                                                                                                                                                      |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| For a view that is in the layout of a page, you can set the visibility of the view according to a value, rule, or script.Generally, setting the visibility by value is the simplest but least flexible option while setting the visibility by script is the most complex but most flexible option.  You can also change the visibility according to the screen size if you chose to set visibility by value. For example, you might want to have a view visible in a large screen but hide it for a medium or small screen. To do this, you would set the visibility to Editable when you are editing the large screen layout. You then switch to the medium screen layout and change the visibility to Hidden or None. If you do not specify a value for the small screen layout, it inherits the visibility value from the medium screen layout. For information, see Responsive settings for views. Restriction: You cannot have different rules or scripts for each screen size setting. | For a view that is in the layout of a view, you can set the visibility of the view according only to a value. In the procedure, only the first option applies. |

## Procedure

<!-- image -->

<!-- image -->

1. Determine whether the first rule in the rule set is based on a variable value or on a team
membership and select Variable or Team
accordingly.
2. Set the default value for the rule set by selecting a value in the
Otherwise field.
3 Create the first rule in the rule set. For a variable, the format of the rule isvisibility variable condition value . To create a visibility rule that is based on a variable value, completethe following steps: For a team, the format of the rule is visibility membership team . To create a visibility rule that is based on team membership, complete thefollowing steps: To add more variable values or team memberships to a rule, click . Subsequent clicks add a variable value or team membership for each click. If there aremultiple variables or team memberships in a rule, each of them has an AND relationship with theother. That is, all of them must be true for the rule to apply.
    - For visibility, set the value for the visibility in the Set
to field.
    - For variable, click Select and then select the
variable that is defined in the human service that determines when the visibility value
applies.
    - For condition, select the type of comparison that is used on the variable
value.
    - For value, enter the variable value that triggers the application of the
visibility value.
    - For visibility, set the value for the visibility in the Set
to field.
    - For membership, select the membership type of the user in the team.
    - For team, select the team that the user belongs to.

To add more variable values or team memberships to a rule, click . Subsequent clicks add a variable value or team membership for each click. If there are
multiple variables or team memberships in a rule, each of them has an AND relationship with the
other. That is, all of them must be true for the rule to apply.

4. Create more rules as needed.
5. Click Save or Finish Editing.

1. Click Select.
2. Select one or more local variables that trigger the script to run.
3 Type JavaScript code into the field. Thefollowing parameters are available for your code: Parameter Description context The context parameter contains data fromcontext.bpm.system , context.bpm.team.member , andcontext.bpm.team.manager . The system , member , andmanager objects are identical to objects that have the same name in theview.context object. Remember: If your script checks the teammembership and multiple teams have the same name in the processapplication and its dependent toolkits, themembership in those teams must be the same. If the team membership is not the same, use rulesinstead of a script to set the visibility. event The event parameter contains data from theinitialize or change event. The framework calls the visibilityscript by using the initialize event (type: "initialize" ) duringthe page initialization. The framework calls the visibility script with the change event(type: "change" ) when one of the watched variables changes. Thechange event is similar to the one that is handled by the change() event handler except that it has the following extra properties: local The local parameter contains all the human servicevariables that are available to the page. For example, you can get a variable value by using a calllike local.get("employee").get("phoneNumber").get(0).get("type") In your JavaScript, each returnvalue must be a string with one of the following values: REQUIRED EDITABLE READONLY NONE DEFAULT HIDDEN . When a user changes the value in one of these watched variables, theresulting change event causes the script to run. For example, you might want the user interface todisplay a view when the user selects tea from the MyDrink brand. Users fromthe sales team can edit the view. The service has Drink and Brand variables. You select these variables and then add the following code into thefield:if(local.get("brand") == "MyDrink" && local.get("drink") == "Tea") { if(context.bpm.team.member.indexOf("SalesTeam") != -1) { return "EDITABLE"; } else { return "READONLY"; }} else { return "NONE";}

| Parameter   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| context     | The context parameter contains data from context.bpm.system, context.bpm.team.member, and context.bpm.team.manager. The system, member, and manager objects are identical to objects that have the same name in the view.context object. Remember: If your script checks the team membership and multiple teams have the same name in the process application and its dependent toolkits, the membership in those teams must be the same. If the team membership is not the same, use rules instead of a script to set the visibility.                                                                                     |
| event       | The event parameter contains data from the initialize or change event. The framework calls the visibility script by using the initialize event (type: "initialize") during the page initialization. The framework calls the visibility script with the change event (type: "change") when one of the watched variables changes. The change event is similar to the one that is handled by the change() event handler except that it has the following extra properties: type: "change" or "initialize" path: fully qualified path to the variable that changed. For example, type "local.employee.phoneNumber[2].areaCode" |
| local       | The local parameter contains all the human service variables that are available to the page. For example, you can get a variable value by using a call like local.get("employee").get("phoneNumber").get(0).get("type")                                                                                                                                                                                                                                                                                                                                                                                                    |

In your JavaScript, each return
value must be a string with one of the following values: REQUIRED
EDITABLE
READONLY
NONE
DEFAULT
HIDDEN.

```
if(local.get("brand") == "MyDrink" && local.get("drink") == "Tea") {
	if(context.bpm.team.member.indexOf("SalesTeam") != -1) {
		return "EDITABLE";
	} else {
		return "READONLY";
	}
} else {
	return "NONE";
}
```

4. Click Save or Finish Editing.