# Adding variable types and business objects to a Decision service  (deprecated)

## Before you begin

To perform
this task, you must be in the IBM Process
Designer desktop
editor, which is deprecated.

## Procedure

To add a business object (variable type) to a Decision
service, complete these steps:

1. Open the desktop Process Designer (deprecated).
2. Open a process application that contains the Decision service.
3 You can add a variable type from the library panel, orfrom the Variables tab while you are working in the Rule service.
    - To add a business object from the library panel:
        1. Click the plus sign next to the Data library
item.
        2. In the Create New window, click Business
Object.
        3. In the New Business Object window, type
a name for the variable type, then click Finish.
        4. Follow the procedure steps to define the new business object (variable
type).
- To add a variable type while working in the Decision service:
    1. Make sure you are working in the Decision service where you want
to add the new variable type.
    2. Click the Variables tab.
    3. Create a new variable, or select the variable where you want to
add the new variable type. For more information about adding variables,
refer to the related topic "Adding and modifying Decision service
variables."
    4. In the Details section, click New next
to the Variable Type field.
    5. In the New Business Object window, type
a name for the variable type, then click Finish.
    6. Follow the procedure steps to define the new business object (variable
type).
4 In the Behavior section, selecta Definition Type from the list.

- Select Simple Type to create a new
variable type using an existing type such as String, Decimal, or Integer.
For more information about creating simple variable types, refer to
the related topic "Creating custom variable types."
- Select Complex Structure Type to create
a new complex variable type. You can create a custom variable type
by adding parameters and parameter properties to the business object.
For more information about creating complex variable types, refer
to the related topic "Adding process variables to a BPD."As you
are adding parameters for a complex structure type, you can see the
resulting changes to the XML schema for the variable type. To see
how the variable parameters are declared in the XML schema, open the Advanced
Properties section and click View XML Schema.
5. When you have entered all the necessary parameters and
settings for the variable type, click Save in
the main toolbar.
6. Return to the Decision service editing panel, then click Select next
to the Variable Type field. The
variable type that you added is listed as an available type.

## What to do next