# Nesting the Integration service and mapping its variables (deprecated)

## Procedure

1. Create a heritage human service as described in Building a heritage human service and name it according to what
the service performs.
2. Open the diagram for the new human service and drag the
integration service from the library to the diagram. When
you have an existing service that you want to nest in another service,
you can drag the existing service directly from the library to the
diagram of the parent service. This creates the Nested Service component
with the service attached in a single step.
3. If not already selected, click the nested service in the
diagram to view its properties.
4. Because you already created the input and output variables
for the nested service, the Data Mapping tab
for the parent service includes those variables.
5. From the Input Mapping section, click the auto-map icon.
The Create variables for auto-mapping dialog box opens,
indicating that a matching private variable was not found in the parent
service, and should be created.
6. Select the suggested variable item and then click OK.
A private variable of that name is created for the parent
Service and automatically mapped to the input variable of the nested
service, making it available to all components in the parent service.
7. From the Output Mapping section,
perform the automapping step to create the matching private variable
to capture the output from the nested service. You can
see the private variables added for the parent service.
8. Click Save in the main toolbar.