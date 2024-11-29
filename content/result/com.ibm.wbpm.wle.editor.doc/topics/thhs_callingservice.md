# Calling another service from a heritage human service (deprecated)

## About this task

When you develop your heritage human service, add an activity of Nested Service type to the human
service diagram, and then specify the service that you want the nested service to call. When the
nested service activity is triggered at run time, the nested service is run. After the nested
service is completed, the parent heritage human service resumes execution.

To call another service from a heritage human service:

## Procedure

1. Open the appropriate process application in the Designer view.
2. Create or open a heritage human service that you want to work with.
 See Building a heritage human service.
3. In the Diagram view, click Activity , add a Nested Service  to the diagram, and wire it as required.
4. In the Implementation properties of the nested service node, click
Select next to Called service to specify the service
that you want to call. To create a service to call, click New and complete
the wizard.
5. In the Data Mapping view, set the input and output mapping for the nested
service.
6. Optional: 
In the Pre & Post properties, you can assign pre-execution and
post-execution scripts to the nested service node. The JavaScript code that you add as pre- and
post-execution scripts runs immediately before or after the nested service runs.
7. Click Save or Finish Editing.