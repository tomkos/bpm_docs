# Creating UI for a BPD process instance (deprecated)

## About this task

- The Default user interface that
overrides the user interface that is provided by Business Automation Workflow. Any user
that has permission to see the process instance in Process Portal will
see this interface. You can create a client-side human service and
specify it as the user interface. If you do not specify a client-side
human service here, the user interface that is provided by Business Automation Workflow is used.
- The Instance Owners user interface
is an optional user interface that you can create for the team that
is specified in the Instance owner team field
in the Overview page. You can create a client-side
human service and specify it as the user interface for the instance
owners.

## Procedure

To create a process instance user interface, first create
a client-side human service, then create your customized interface
by modifying the generated service and adding a coach.

1. Open the BPD for which you want to create the user interface.
2. Switch to the Views  page.
3. Under Details UI, select the interface
that you want to create (Default or Instance
Owners).
4 Select a client-side human service, or create a new one. Business Automation Workflow providesa template in the Dashboards toolkit, called Instance Details UI Servicestemplate. You can copy this template and modify it to create yourcustom UI. The template contains the following coaches: For more information, see Instance Details UI Service Template .
    - View Instance Details coach, which contains
the following coach controls:   
Default Instance Details Template
Displays the instance details in Process Portal.
Data section
Displays the values of the variables that are passed into the
client-side human service.
    - Show error, which returns an error if the
instance is not found.
5. Map the process variables to the client-side human service
variables. To automatically map input properties with process variables,
click the auto-map icon .
6. Open the client-side human service, switch to
the Diagram view, and implement the data change
event handler that is provided for managing remote data changes.
The Instance Details UI Services template contains a reference
implementation that you can customize. For example, you might want
to provide an alternative to the server refresh of the instance details
UI by implementing the event handler to refresh the instance details
UI when a user clicks the corresponding button. For more information,
see Handling data changes.
7. Click Run  to
test the client-side human service and the coach. Note: If
you copied the template in step 4, remove the defensive logic that
shows an error when the instance ID is null.
8 To test the interaction between the user interface andthe process: Process Portal opensin your default browser showing the process instance user interface.You can view the user interface, enter data, and interact with theprocess.

1. Open the BPD and click Run Process  in the toolbar.
2. Switch to the Inspector when prompted.
3. In the Inspector, select the process instance and click
the Runs the Details UI for the selected BPD Instance in
the toolbar.