# Creating a custom event handler for the IBM Business Automation
Workflow
Box Event Listener

## Before you begin

| File                            | Description                                                                                                                                                                                                                                                                                                                                 |
|---------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ICNTasks.jar                    | This file contains the com.ibm.ecm.icm.boxeventhandlers.BaseHandler  that you must extend to create a custom event handler.You can find this file in Installation\_directory\configure\explodedformat\taskManager\taskManagerWeb\WEB-INF\dropins, where Installation\_directory is the directory in which IBM Content Navigator is installed. |
| acmapi.jar                      | This file contains the IBM Business Automation Workflow Java API.You can find this file in Installation\_directory\CaseAPI\lib, where Installation\_directory is the directory in which IBM Business Automation Workflow is installed.                                                                                                        |
| Box-java-sdk-1.0.0.jar          | This file contains the Box API.You can find this file in Installation\_directory\configure\explodedformat\taskManager\taskManagerWeb\WEB-INF\lib, where Installation\_directory is the directory in which IBM Content Navigator is installed.                                                                                                 |
| Minimal-json-0.9.2-SNAPSHOT.jar | This file contains the minimal JSON parser and writer that the Box API uses.You can find this file in Installation\_directory\configure\explodedformat\taskManager\taskManagerWeb\WEB-INF\lib, where Installation\_directory is the directory in which IBM Content Navigator is installed.                                                    |

## About this task

You can find sample custom event handler plug-ins in the following location: https://github.com/ibm-ecm/ibm-casemanager-samples

## Procedure

1. Create a Java class that extends the com.ibm.ecm.icm.boxeventhandlers.BaseHandler class that is provided by the IBM Business Automation
Workflow
Box Event Listener.

This new class must implement the following methods:
processBoxEvent
This method is called by the event listener to process an event. The
processBoxEventmethod takes the following parameters:
boxEvent
A Box object that contains detailed information about the
event.
caseID
A string that contains the identifier of the case in which the event occurred.

eventSupported
This method is called by the event listener to determine whether the event handler supports a
specific event. If the event is supported, the method returns true.The
eventSupportedmethod takes the following parameter:
boxEvent
A Box object that contains detailed information about the
event.
2. If your custom class requires any input or configuration from the user, create a Dojo
JavaScript class that inherits from the
boxeventlistener/eventhandler/configuration/BaseConfigurationPane class that is
provided by the event listener.

The new class must implement the following methods:
getInput
This method returns a JSON object that contains the configuration information that the user
enters.
setInput
This method populates and initializes the user interface that is used to collect the user
input.The setInput method takes the following parameter:

inputParam
A JSON object that contains the information that is used to populate the user interface.
3. Create an IBM Content
Navigator plug-in that includes your compiled
Java event handler class and, if applicable, your JavaScript configuration class in the plug-in JAR
file.
For more information, see Creating plug-ins to IBM Content Navigator,
4. Deploy your plug-in JAR file into the Task Manager Web-INF/Dropins
directory.
The location of this directory depends on your application server settings. For example, if
you use WebSphere® Application
Server, the directory location might be
C:\IBM\WebSphere\AppServer\profiles\AppSrv02\installedApps\oclv0288Node02Cell\navigator.ear\taskManagerWeb.war\WEB-INF
\ dropins.
5. In the IBM Content
Navigator administration desktop, add the new
plug-in to the IBM Case Manager administration desktop.
6 Register your custom event handler with the IBM Business AutomationWorkflow Box Event Listener plug-in.
    1. On the Configuration tab for the event listener, click
Register.
    2. Complete the Custom Event Handler Registration dialog box, and click
OK.
7. In task manager, configure the IBM Business Automation
Workflow
Box Event Listener and select your custom event handler.