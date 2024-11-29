# Configuring a remote Decision service (deprecated)

## Before you begin

- Export the rules to an Eclipse rule project file.
- Using IBM ODM Rules Designer, import theproject .zip file to create a new Rule Studio project.
    1. Click File > Import > General > Existing Projects into Workspace.
    2. Click Select archive file. Click Browse to
navigate to the location where you saved the exported rule project file and select the file.
    3. Select an existing project where the rules will be imported, or create a new Rule Studio
project, then click Finish.
    4. Deploy the imported rules to the Rule Execution Server. For more information, see the related
topic "Deploying from Rule Designer." A related link is provided.

## About this task

## Procedure

1. Make sure that you are working in the Decision service where you want to add the Rule Decision
Service.
2. Remove the BAL Rule component that contains the rules you
exported.
3. Drag a Rule Decision Service component from the palette to the service diagram, and place it in
the same location as the deleted BAL Rule component.
Reconnect any sequence lines to other activities or services.
4. Select the new Rule Decision Service component, then click
Implementation in the Properties tab.
5. In the Discovery section, enter
the following information to connect to the Rule Execution Server
that contains the rules that you want to use. 
Table 1. Input
required to connect to the Rule Execution Server

Field
Action

Server
Select the server that you want from the list of IBM ODM Server variables. See the related topic "Setting
environment variables" for more information.

SOAP Port
Specify a port for the SOAP connection if the Rule Execution Server instance
is running on WebSphere® Application
Server.

User name
Enter a user name if the IBM ODM server requires a secure connection.

Password
Enter the password if the IBM ODM server requires a secure connection.

The SOAP port, user name, and
password fields accept embedded JavaScript expressions, so variables
can be used to provide those values.
6. Click Connect.
7. In the Rule section, select the RuleApp that you want from the menu,
then select the version that you want to use.
If a secure connection to the Rule Execution Server has not been established, the menu is not
populated. In this case, manually enter the name and version of the RuleApp and ruleset that you
want to use. The names must be accurate for the next step to work.
8. Click Generate Types.
9. In the Generating Types window, make sure that the Generate
request/response wrapper types option is not selected.
Click Next.
10. Click Finish when type generation
is complete.
11. In the Properties section, click Data
Mapping.
12. Click the auto-map icon in upper right corner of the Input Mapping section.
The "Create variables for auto-mapping" window opens, listing the
private variables needed for input parameters from the selected RuleApp.
13. Click to select each variable that you want to create in
your Decision service and then click OK.
14. Click the auto-map icon in upper right corner of the Output Mapping section.
The Create variables for auto-mapping window opens, listing the private variables needed
for output parameters from the selected RuleApp.
15. Click to select each variable that you want to create in
your Decision service and then click OK.
16. Save the updated Decision service.