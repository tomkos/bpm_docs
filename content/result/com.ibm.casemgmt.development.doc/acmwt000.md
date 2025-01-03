# Creating custom page widgets and actions

## Before you begin

## About this task

## Procedure

To create a custom page widget:

1 Create a web project that contains the following folders for your widget package: Folder Content ProjectName /ProjectName Plugin Contains the files that are used to create the JAR file for the IBM ContentNavigator plug-in. ProjectName /ProjectName Plugin/src/PackageName Contains the files that are used to create the JAR file for the IBM ContentNavigator plug-in. ProjectName /ProjectName Plugin/src/PackageName /WebContent Contains the CSS files, the main JavaScript plug-in file and related files such as images.Note: In the JAR file, update therelative path with the absolute path for the custom widget application that is installed on theworkflow server that corresponds to your custom widget EAR. ProjectName /ICMRegistry Contains the JSON files that are used to register the widget package and thepage widgets.Optionally, this folder can contain folders for: ProjectName /ProjectName Widget Contains the files that are used to define the user interface for a custompage widget. ProjectName /ProjectName Widget.PackageName /pgwidget Contains the files that are used to define the custom page widgets. ProjectName /ProjectName Widget.PackageName /action Contains the files that are used to define the custom actions that are used bythe custom page widgets. For more information, see section 5.2.1, General structure of a plug-in project, in theIBMRedbooks publication Customizing and Extending IBM Content Navigator .

| Folder                                                   | Content                                                                                                                                                                                                                                                                                 |
|----------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ProjectName/ProjectNamePlugin                            | Contains the files that are used to create the JAR file for the IBM Content Navigator plug-in.                                                                                                                                                                                          |
| ProjectName/ProjectNamePlugin/src/PackageName            | Contains the files that are used to create the JAR file for the IBM Content Navigator plug-in.                                                                                                                                                                                          |
| ProjectName/ProjectNamePlugin/src/PackageName/WebContent | Contains the CSS files, the main JavaScript plug-in file and related files such as images.Note: In the JAR file, update the relative path with the absolute path for the custom widget application that is installed on the workflow server that corresponds to your custom widget EAR. |
| ProjectName/ICMRegistry                                  | Contains the JSON files that are used to register the widget package and the page widgets.Optionally, this folder can contain folders for: Images that are used in the widget package, such as icons or thumbnails. Translated resource files                                           |
| ProjectName/ProjectNameWidget                            | Contains the files that are used to define the user interface for a custom page widget.                                                                                                                                                                                                 |
| ProjectName/ProjectNameWidget.PackageName/pgwidget       | Contains the files that are used to define the custom page widgets.                                                                                                                                                                                                                     |
| ProjectName/ProjectNameWidget.PackageName/action         | Contains the files that are used to define the custom actions that are used by the custom page widgets.                                                                                                                                                                                 |

For more information, see section 5.2.1, General structure of a plug-in project, in the
IBM
Redbooks publication Customizing and Extending IBM Content Navigator.

2 Create the registry files and place them in the ICMRegistry folder:

1. Create a file called Catalog.JSON.
This JSON-format file identifies the widget category and the page widgets that the package
contains.
2. For each page widget, create a definition file in JSON format that identifies the properties,
toolbars, menus, and actions that can be configured for the widget.
3. Create a self-contained widget that is based on Dojo to represent the user interface component
of the custom page widget.

Do not include the business logic for the page widget in this file. Instead, use this file to
define the visual representation of the widget that is displayed to users in Case Client. In addition, include a
destroy method to be called to close the widget when the page that contains the
widget is closed.
4 Create a wrapper file that defines a custom class to represent the page widget. You define the wrapper JS file in the Dojo Asynchronous Module Definition (AMD) format by callingthe Dojo.declare() method. The class for the page widget must:

You define the wrapper JS file in the Dojo Asynchronous Module Definition (AMD) format by calling
the Dojo.declare() method.

- Extend the user interface component that you created.
- Mix in the icm.base.BasePageWidget class. This class mixes in the
icm.base.\_EventStub class that includes methods for publishing and broadcasting
events.
- If the page widget contains a toolbar or menu that uses the workflow action framework, mix in
the icm/base/BaseActionContext class.
- If the page widget must interact with other page widgets to perform tasks such as adding or
saving cases, tasks, or work items, participate in coordination.
5. If your page widget uses custom actions, define a class for each action.

A workflow action extends the ecm.model.Action class. To make a standard
IBM Content
Navigator action
work in IBM Business Automation
Workflow, the
com.ibm.ecm.extension.PluginAction implementation must override the
getAdditionalConfiguration method to provide the action definition.
To define the class for a custom action, you extend the icm.action.Action
class. Implement an execute method in the class to define the operation logic for
the action. Optionally, you can implement an isEnabled method and an
isVisible method to check the state.
Tip: You can customize the dialog boxes that are used to display error messages and
confirmation messages for your custom actions. To override the default dialog boxes, use the
showConfirmationDialog method and showErrDialog method that
are defined for the icm.action.Action JavaScript class.
6. Create the IBM Content
Navigator plug-in for the
widget package.
The plug-in contains the web browser logic that enables users to call the page widget. For
more information, see section 5.2.2, Create a plug-in project from the samplePlugin code, in
the IBM
Redbooks publication Customizing and Extending IBM Content
Navigator.
7 Create a widget package that contains the custom page widgets and actions:

1 Create a build.xml script that builds the following components:
    - An EAR file that contains the runtime code that implements the page widgets and actions.
    - The ICMRegistry folder that includes the page widget definitions.
    - A JAR file that contains the IBM Content
Navigator plug-in,
including the bootstrap file and the action definitions.
    - In the JAR file, update the relative path with the absolute path for the custom widget
application that is installed on the workflow server that corresponds to your custom widget
EAR.
2. Create a compressed file that contains the files and folders from the previous step.
8. Create a MANIFEST.MF file that is in the
ProjectNamePlugin/src/META-INF folder that contains the
following reference to the Custom plug-in .js file:

Plugin-Class: Custom plug-in
9. If your custom widget package references Case resources, update the workflow widget package.
For more information, see step 7.b in Upgrading your IBM Case Manager system using an external IBM Content Navigator.
10 Deploy and register your custom widgets by using one of the following options. Important: If you run this task in a cluster environment, you must make sure that theplug-in is loaded on each node of the cluster. Either restart the cluster to force the plug-in to beloaded on all nodes or manually load the plug-in on each node by using the IBM ContentNavigator administrationclient.The Deploy and Register Widgets Package task modifies only those components within theapplication server for IBM ContentNavigator applicationserver. For environments where client requests are routed through an HTTP Server such as IBM HTTP Server , a load balancer, or so on, makesure that the endpoints are configured correctly. In addition, ensure that the HTTP Server plug-insare regenerated to allow clients access to the runtime code with the deployed EARapplication.

- Use the workflow case configuration tool.In the configuration tool, make and run a copy of
the Deploy and Register Widgets Package task to register your widget package and to deploy it in
your design environment.
- Use the workflow administration client if the widget does not need an ear file that is deployed,
or the ear file needs to be manually deployed.Use the administration client to deploy and
register custom widgets, and then, if required, manually deploy the ear file that is associated with
the custom widgets. See EAR file for custom widget package isn't deployed for
details on how to manually deploy the ear file.
- Deploy and register custom widgets in a container environment.For more information on how to
deploy and register custom case widgets for a container environment, see Configuring custom case widgets for a container
environment.

The Deploy and Register Widgets Package task modifies only those components within the
application server for IBM Content
Navigator application
server. For environments where client requests are routed through an HTTP Server such as IBM HTTP Server, a load balancer, or so on, make
sure that the endpoints are configured correctly. In addition, ensure that the HTTP Server plug-ins
are regenerated to allow clients access to the runtime code with the deployed EAR
application.

11. In Case Builder, use Page
Designer to add the custom page widget to a page and configure the properties and actions for the
page widget.
12. Deploy and test the solution.

- Defining registry files for custom actions, properties, page widgets, and events

You can include certain properties in the registry files for your custom action, properties, page widget, or event.