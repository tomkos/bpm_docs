# Changing the visibility of a heritage coach control (deprecated)

## About this task

## Procedure

1. Open the service that contains the heritage coach to work with.
2. Click the Variables tab and add
the private variables that you need for the custom script. For this
example, add Boolean variables named visible , enabled ,
and required.
3. Click the Coaches tab.
4. Click the heritage coach control for which you want to add visibility control.
5. Click the Visibility option in the
properties.
6. Click the Override Parent Visibility check
box to enable it. Doing so allows you to change the default visibility
properties.
7. From the Default Visibility list,
select the Hidden (no access) for everyone option.
8. Click the Custom Script button.
9. In the Custom Visibility section,
enter the JavaScript rule to control visibility.  The following
example uses a server-side JavaScript function, and so return statements
are required. For custom visibility using server-side JavaScript,
return one of the following values (must be in upper case): 
Table 1. Values returned for custom visibility

Value
Result

"NONE"
Hidden

"READ"
Disabled

"FULL"
Editable

"REQUIRED"
Required

The following script causes the runtime engine to determine
if user input is required:var customVisibility;
if(tw.local.visible) {
        if(tw.local.enabled) {
                 if(tw.local.required) {
                         customVisibility = "REQUIRED";
                 }
          } else {
                 customVisibility = "READ";
             }
            } else {
         customVisibility = "NONE";
  }
  return customVisibility;If user input is not required,
the control can be edited, but it is not required. If the value of tw.local.visible is
false, the control is not displayed to the user.
10. You can set default values for the variables (that you
added in step 2) and then run the service to test the script.