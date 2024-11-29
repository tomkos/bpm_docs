# Changing the type of a property that is used in in-baskets, in-basket filters, or activities

## Before you begin

For information about the effects of changing a property data type, see Redeployment restrictions for modifying a solution.

## About this task

- Role In-basket General
- Role In-basket Filters
- Personal In-basket General
- Personal In-basket Filters

## Procedure

To apply property type changes in Role In-basket General and In-basket Filters tabs and
case type activities:

1. Open the solution in Case Builder.
2. Click the In-baskets tab
3 Delete the property for each role and personal in-basket.
    1. Select an in-basket.
    2. Click the In-basket Filters tab.
    3. Click the Remove icon next to the property name that is changing to
delete the reference from the list.
    4. Click the In-basket General tab.
    5. Click the Remove icon next to the property name that is changing to
delete the reference from the list.
4. Click OK.
5. Click Save.
6 Change the data type of the property.

1. Click the Properties tab, and then click the name of the property whose
data type you want to change.
2. Select a new type for the property.
3. In the Confirmation window, click Yes.
4. Click OK.
7 Repeat these steps for each case type in the solution:

1. Click the Case Types tab, click the Case Type
name, and then click Activities.
2 If the activity precondition uses the changed property, edit the precondition.
    1. Click the activity name.
    2. Click the Preconditions tab.
    3. Select the property, update the operator value, and then click OK.
3. Click the Edit Steps icon for the activity.
4. Repeat steps 7b - 7c for all the activities that use the property in the precondition or in the
step properties parameters.
8. For each activity that does not use the property in the step properties, open the activity in
Step Editor, and then click Apply, click Validate, and
click Close.
9. Add the changed property to the role in-basket and filter and personal in-basket and filters as
needed.
10 Repeat these steps for each case type in the solution:

1. Click the Case Types tab.
2. Click the Case Type name.
3. Click Activities, then click the Edit Steps icon
for the activity.
4. Click Apply, click Validate, and click
Close.
11. Click Validate, click Save, and then click
Close.