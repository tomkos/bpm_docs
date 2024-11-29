<!-- image -->

# Editing and validating exports used with IBM Business Automation
Workflow activities

## About this task

A binding edit function lets you change these values when
services are moved. A validate function ensures that the IBM® Business Automation
Workflow case
and the web service are able to communicate at run time, by ensuring
that endpoint, input and output values and security settings are synchronized
between the business process management service and IBM Business Automation
Workflow.

## Procedure

1. Launch the assembly editor and right-click the export. 
The Edit Binding and Validate functions are listed on the menu.
2. Click Edit Binding. 
The Select the Input and Output Parameters page opens. The current
input and output parameters for the activity are shown.
3. Change the parameters if needed and click Next. The Specify the Deployment Target page opens.
4. Change the target server, host name, port number and security
options if needed. Click Finish. 
The generated business objects and interface are updated
according to your changes.
5. Click Validate from the menu to
validate the current configuration.  Validation is useful
if an error occurs and you suspect that the problem is in the integration
of the case activity and the web service. If the integration is incorrect,
a page displaying the errors appears.

## Related concepts

- Design considerations for web services used with IBM Business Automation Workflow tasks

## Related tasks

- Creating a web service to implement a IBM Business Automation Workflow task

## Related reference

- Deleting a web service export used with a IBM Business Automation Workflow task