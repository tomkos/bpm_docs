# Scenario: Exporting rules to Rule Execution Server 
(deprecated)

## About this task

## Procedure

To export rules for use in Rule Designer and Rule Execution server, complete these
steps:

1 Export the BAL rules from your Decision service. You can find more information about exporting rules in the related topic about exportingrules for use in Rule Designer.
    1. Make sure that you are editing the NotificationRulesService Decision service and the AlertRules
BAL Rule component.
    2. In the AlertRules component pane, click the Decisions tab to open the
rule editor.
    3. In the menu bar above the rule editor window, click the Export
 icon.
    4. In the Save As window, navigate to the location where you want to save
the exported rule file.
    5. Enter a name for the export file, then click Save to specify the
location.
2 Import the rules into Rule Designer. You can find more information about importing rules in the related topic about configuringa remote decision service.

1. Using IBM Rule Designer, import the project
.zip file to create a new Rule Designer project.
2. Click File > Import > General > Existing Projects into Workspace.
3. Click Select archive file. Click Browse to
navigate to the location where you saved the exported rule project file and select the file.
4. Select an existing project where the rules will be imported, or create a new Rule Designer
project, then click Finish.
3 Deploy the rules to Rule Execution Server. For more information, see the related topic about deploying from Rule Designer in theIBM Operational DecisionManager documentation.

1. In Rule Designer, select the RuleApp that contains the AlertRules and click
Deploy a RuleApp to one or more Rule Execution Servers.
2. Select an existing Rule Execution Service and deploy the RuleApp to the server.
4 Add a JRules Decision Service component to the Decision service and connect it to RuleExecution Server. You can find more information about adding a JRules Decision Service component in therelated topic about configuring a remote Decision service.

1. Configure your Decision service to include a JRules Decision Service component.
When you specify the correct rule execution server and port settings, the JRules Decision
component establishes a connection between Process Designer and the Rule Execution Server instance that
contains the imported rule project.
2. Make sure that you are editing the NotificationRulesService Decision service.
3. Remove the AlertRules BAL Rule component that contains the rules you exported.
4. Replace the BAL Rule component with a JRules Decision Service component. Drag a JRules Decision
Service component from the palette to the service diagram, and place it in the same location as the
deleted BAL Rule component. Reconnect any sequence lines to other activities or services.
5. Select the new JRules Decision Service component, then click
Implementation in the Properties tab.
6 In the Discovery section, enter the following information to connect tothe Rule Execution Server instance that contains the rules that you want to use.
    - Server: Select Rule Execution Server.
    - SOAP Port: Specify a port for the SOAP connection if Rule Execution Server is running on
WebSphere® Application
Server.
    - User name: Enter a user name if the server requires a secure connection.
    - Password: Enter the password if the server requires a secure connection.
7. Click Connect.
8. In the Rule section, select the RuleApp that you want from the menu,
then select the version that you want to use.
9. Click Generate Types.
5 Map the variables to make sure that the variables that are used in the rules on Rule ExecutionServer correspond to variables defined in Process Designer .

1. Click the Properties tab in the JRules Decision
Service pane.
2. In the Properties section, click Data
Mapping.
3. Click the auto-map icon in upper right corner of the Input Mapping
section.
4. In the Create variables for auto-mapping window, click to select each
variable that you want to create in your Decision service and then click
OK.
5. Click the auto-map icon in upper right corner of the Output Mapping
section.
6. In the Create variables for auto-mapping window, click to select each
variable that you want to create in your Decision service and then click
OK.
6. Save the updated Decision service.

## What to do next