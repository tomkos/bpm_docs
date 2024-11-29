# Creating user interfaces for process instances

## About this task

- The Default user interface that overrides the provided user interface.
Any user that has permission to see the process instance in Process Portal will see this interface. You can create a client-side human service and specify it as the
user interface. If you do not specify a client-side human service here, the provided user interface
is used.
- The Instance Owners user interface is an optional user interface that you
can create for the team that is specified in the Instance owner team field in
the Overview page. You can create a client-side human service and specify it as
the user interface for the instance owners.
- The Launch UI
Default user interface is seen by members of the team that is assigned to the
Expose to start option in the Overview page.

## Procedure

To create a process instance user interface, first create a client-side human service,
which includes a generated page. You can then create your customized interface by modifying the
generated service and page.

1. Open the process for which you want to create the user
interface.
2. Switch to the Views page.
3. Select the interface that you want to create, for example Default under Details
UI or Launch UI.
4. Click New beside Client-side
human service and enter a name for your user interface.
5. Click Next. In the New
Client-side Human Service page, you see a list of variables that you can pass to and
return from the client-side human service.You do not need to map the variables between the
process and the human service. The process variables are already mapped to the human service
variables with the same name.
6. Click Finish.
7. The client-side human services editor opens. Switch to
the Variables page.  Notice that the input and output variables that are mapped from the process are locked. You
can edit these variables only in the process editor. You can, however, add private variables that
are available only to the human service. If you are creating a launch UI,  a
cancelLaunch variable of type Boolean is generated. The default value is false.
You can only view this variable, you cannot change or delete it. The value of the variable is set by
the launch UI human service. If the value of cancelLaunch is true when a user
completes the human service during the launch, the launch is canceled. If the value is false, the
process is started.
8. Switch to the Diagram  page. 
A basic diagram is generated for you. If
you are creating a details UI, the diagram includes a data change
event handler for managing data changes in the UI at run time. The
event handler is ready to use. You can, however, customize the implementation
by double-clicking the Data Change node. For
more information, see Handling data changes.
9 Complete the human service diagram and customize the pages.
    - For a Details UI , the generated human service has two pages: The human service is generated from a template in the Dashboards toolkit,called Instance Details UI Services Template. For more information, see Instance Details UI Service Template .
        - View Instance Details, which contains the following views: 
Default Instance Details Template
Displays the instance details in Process Portal.
Data section
Displays the values of the variables that are passed into the human service.
        - Show error, which returns an error if the instance is not found.
- For a Launch UI , the generated human service has an EnterData page, with a control for each mapped process variable. When you specify a launchprocess UI, a cancelLaunch variable of type Boolean is generated. The value ofthe variable is set by the launch UI human service. If the value of cancelLaunch is true when a user completes the launch human service, the launch is canceled. If the value ofcancelLaunch value is false, the process is started. The default value is false.The generated Launch UI has one page with two buttons; OK andCancel . If a user clicks Cancel , thecancelLaunch variable is set to true. You can modify your Launch UI so that auser can view or add documents in the process folder that you specified in theFolders page. To do so, use views that are provided in the Content Managementtoolkit for viewing and retrieving documents in the content store. For example, theDocument Explorer control. These controls are available in the ContentManagement toolkit. For more information, see: Note: If the process launch is canceled, the documents and folders located in an externalEnterprise Content Management system that are referenced from the process folder are notdeleted.
    - How to use views to store or view documents
    - Responsive Document Explorer
10. Click Save or Finish Editing.
11 Test the client-side human service.

- For Launch UI, click Run
 to test the
client-side human service and the page.

- For Details UI, do one of the following:
    - If the human service flow is not customized, run the instance UI in Process Portal.
    - If you want to incrementally test and build your custom UI:
        1. Run an instance of the process that is associated with the custom
UI and make a note of the instance ID.
        2. The human service has logic that shows an error if the process
instance ID is null. Remove this logic by wiring the Start node
directly to the Client Side Init Data node.
        3. In the Client Side Init Data script, modify
the first line as follows: tw.local.selectedInstanceId ='6'; where 6 is
the instance ID that you noted in step a.
        4. Run the human service.
        5. After you are satisfied that the service works as expected, revert
the changes that you made in steps b and c. Test again by running
the instance UI in Process Portal.

## What to do next

If your variables change in the future, you can use the Update button
to synchronize the variables and human service. During synchronization,
you can optionally choose to regenerate the human service body. Regenerating
replaces any customization that was done in the human service.

If
you want to make the user interface reusable, you can unlock the variables
of the client-side human service. See Making process instance user interfaces reusable