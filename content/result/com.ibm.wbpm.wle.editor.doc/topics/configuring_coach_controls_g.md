# Displaying a control based on the input value of another control in a heritage coach
(deprecated)

## About this task

## Procedure

1. Open the service that contains the heritage coach that you want to work with and then click the
Coaches tab.
2. Drag a List control from the palette onto the design area.
3. In the properties for the control, type Do you
want to contribute? in the Label text box.
4. Click the Presentation option in the properties.
5. Under the Manual Data section, click
the Add button. With the Add button,
create three Value-Display pairs, one for each list item option as
shown in the following table:
Table 1. Entries for the Value and
Display Text fields

Value
Display Text

true
Yes

false
No

defer
Decide at a later date
6. Drag a Text control from the palette onto the design area.
7. In the properties for the control, type 401K Contribution
% in the Label text box.
8. Click the Visibility option in the properties.
9. Select the Override Parent Visibility check
box. Doing so allows you to change the default Visibility properties.
10. From the Default Visibility drop-down list, select the Hidden
(no access) for everyone option.
11. Click the Depends on Control button.
This creates a new override condition.
12. Under the Control Dependent Visibility section,
select the Required (full access) option from
the Visibility drop-down list.
13. From the Control list, specify the
coach control the input value of which is to determine if the selected
control is displayed to participants when the service runs. In this
example, the control is the Do you want to contribute? List
control.
14. From the Operator list, select the ==(equals)
operator.
15. In the Value text box, type true. 
This is the value that you assigned to the Yes list
option in step 5.
16. Drag a Date Selector control from the palette onto the
design area.
17. In the properties for the control, type Date in
the Label text box. Depending on the selection list choice, this can
be the date of contribution or the date until a contribution decision
is deferred.
18. Click Visibility, and repeat the steps above to make the
Date Selector dependent on the control Do you want to contribute?.
19. From the Operator list, select the in operator.
20. In the Value text box, type "{'true','defer'}". 
These are the values that you assigned to the Yes and Decide
at a later date list options in step 5. The Date Selector
will be displayed if either of these options is selected.
21. Save the heritage coach and then run the service to see how the Input and Date Selector
controls are hidden and then shown according to the visibility rules you have specified.