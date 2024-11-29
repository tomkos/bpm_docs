# Building heritage coaches to collect input and display output (deprecated)

## About this task

## Procedure

1. Click the Diagram tab for your service and then drag a heritage coach component from the
palette to the diagram. Place the heritage coach component before the nested service
component.
2. While the heritage coach component is selected in the diagram, click the Step option in the
properties and type a name for your coach in the Name field.
3. Click the Coaches tab.
4. Drag the variable that you declared for your integration service from the palette to the
heritage coach.
An input text field is created with a mapping to the variable, and a label that matches
the variable.
5. In the heritage coach, select the group containing the default
OK button, and then in the properties, click the Presentation
option.
6. In the Buttons section, click OK definition
and type Search in the Label text
box.
7. Click the Preview tab for the heritage coach to see your label change.
8. Click Save in the main toolbar.
9. Click the Diagram tab for your service.
10. Drag another heritage coach from the palette to the diagram and name it View search
results . Place the heritage coach component after the nested service component.
11. Click the Coaches tab.
12. From the palette, drag an Output Text control to the heritage coach.
13. In the properties, select the Output Text option in the
properties and in the Behavior section, click the Select button
to create a binding to the results variable.
14. From the list that opens, find and select the appropriate
output variable.
15. Click the Diagram tab to return to the diagram view of
your service. Select the Sequence Flow tool from the palette and then
connect the components.
16. Click Save in the main toolbar.
17. To test your service, click the Run icon in the upper right corner.
The heritage coach opens in your
browser.