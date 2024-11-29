# Validating user input (deprecated)

## About this task

## Procedure

1. Open the service that contains the heritage coach that you want to work with and then click the
Coaches tab.
2. In the design area, click to select the control for which
you want to add a validation script.
3. Click the Presentation option in the properties.
4. If multiple buttons are included in the control, under
Buttons, click the button that needs the validation script.
5. In the text box under the Validation Script section,
type the JavaScript to validate that the required controls have been
set and contain values as expected.  To do this, use the control ID of each required control. The following example is client-side
JavaScript that uses the default controls included when you add a new heritage coach to a service.
The following validation script checks to ensure that the check box is enabled (set to true). If
not, the user is prompted to check it before proceeding by clicking OK.
if ( document.getElementById("checkbox0\_checkbox").checked == true ){
  return true;
} else {
  alert( "Check the checkbox");
  return false;
}
6. Save the heritage coach and then run the service to test the script.

## What to do next