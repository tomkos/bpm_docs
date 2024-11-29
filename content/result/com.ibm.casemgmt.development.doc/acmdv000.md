# Programming case solutions

For situations where solution requirements go beyond what is provided out of the box, use
application programming interfaces (APIs) and extension points that allow the custom code to be
blended with standard features in ways that seamlessly extend the solutions that you create.

These APIs and extension points can be grouped in the following key areas. Refer to the subtopics
in each section for more details.

## Server

## User interface

- Developing case management applications with JavaScript API

You can use a JavaScript application programming interface (API) to customize your case management client application. For example, you can use this API to create cases, gather information about solutions, and start manual activities.
- Developing case management applications with Java API

You can use a Java application programming interface (API) to create custom applications. For example, you can create applications that create cases, gather information about solutions, and start manual activities.
- Developing case management applications with REST protocols

You can use the REST protocols to incorporate workflow features in your custom application. You use the IBM® Business Automation Workflow REST protocol to access case-specific objects. You use the Content Platform Engine REST Service to access workflow-related aspects of tasks.
- Managing case folders and documents by using IBM CMIS for FileNet Content Manager

You use the IBM CMIS for FileNet Content Manager in your case management application to create and access the case content that is stored in an object store.
- Configuring a solution to create a case when a document is added to the object store

You can configure your solution to create cases programmatically when a document is added to the target object store. You use the initiating document setting when you create the case type in Case Builder, and then configure the addition of the document to the object store in one of several ways.
- Setting values to case content object properties for Add Case, Split Case, and Case Details

You can set values to case content object properties by using JavaScript at authoring time.
- Getting case data from an external data source

Case data is stored in Content Platform Engine. However, you can use an external data service with a solution to access data from a different repository or other data source. This data is then incorporated into the case and stored with the rest of the case data in Content Platform Engine.
- Content Platform Engine add-on extensions

The Content Platform Engine add-on extensions are modules that contain custom metadata and data that is stored in the design and target object stores and are used by Case Builder and Case Client. The custom metadata includes classes that are derived from base Content Platform Engine classes. These add-on extensions provide the core object model, history, and analytics support.
- Using external properties

External properties are ad-hoc properties that are not defined within the properties of a case or task, but that can be rendered within their associated workflow views, for example, the Properties widget. External properties are defined, retrieved, and persisted by using an external data source such as a JAVA servlet, JSON file, or data service. The binding of external properties is handled by the Properties area in the model layer.
- Creating custom property editors and controllers

You can create custom editors and controls to use with properties views. For example, you might create a custom editor and controller to display a record from an external data source such as a customer relationship management system.
- Creating custom inline messages and prompts

When a text-box field, such as a Number Text Box Editor, is empty, Case Client displays a prompt message as a popup tooltip. After the user enters data in the field, the tooltip goes away. In addition, Case Client displays default messages if the user enters a value that is invalid or outside the range for the property.
- Creating custom page widgets and actions

You can create custom page widgets to use with or in place of the workflow page widgets. For example, you might create a custom widget to display a record from an external data source such as a customer relationship management system. You might create a widget that replaces the workflow Search widget with a user interface that customizes the display of search properties for your users.
- Tips for sizing workflow widgets

Some size settings for workflow widgets can cause unexpected behavior at run time.
- Widget toolbar

You can add an event action or a script action to a widget toolbar or menu. For more information, see the following topics: