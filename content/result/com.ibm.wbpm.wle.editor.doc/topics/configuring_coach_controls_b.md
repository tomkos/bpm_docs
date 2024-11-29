# Populating a list with dynamic data in a heritage coach (deprecated)

## Before you begin

| To learn how to...                                                                         | See...                                                                       |
|--------------------------------------------------------------------------------------------|------------------------------------------------------------------------------|
| Create variables for a process                                                             | Declaring and passing variables                                              |
| How to map those process variables to heritage coach controls                              | The following procedure and Building a heritage human service for an example |
| Map variables to a nested service and then bind those variables to heritage coach controls | Building an Integration service for an example                               |

## About this task

## Procedure

1. Open the service that contains the heritage coach that you want to work with and then click the
Coaches tab.
Open or create a service for which you have declared a variable that is a complex
structure.
2. Drag a Combo Box control from the palette onto the design
area.
3. While the Combo Box control is still selected, click the
Presentation option in the properties.
4. Under Manual Data, click Add to
include static instructions at the top of the drop-down list. For
this example, the static text is: -- Select Dept -
5. Under Dynamic Data, for the Based On option, click List
Variable.
6. For the Dynamic Binding option, click Select to
choose the preexisting variable from the library. For this
example, the control must be bound to a complex structure that is
a list.
7. Click the Preview tab to see how
the list works when the service runs. A service inputs
data at run time which is used to populate the values of the drop-down
list. Because these values are only known at run time, the values
do not appear when you select the Preview tab
at development time. These values do appear in the user interface
at run time.