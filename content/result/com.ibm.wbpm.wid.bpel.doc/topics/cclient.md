<!-- image -->

# Before you begin: Client types and prerequisites

| Client type                             | Description                                                                                                                                                                                                                                                                                                                                                     | Prerequisite                                                                                                                                                             |
|-----------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Process Portal                          | Displays the task details when a human task is opened in Process Portal. The task can be completed from this user interface.                                                                                                                                                                                                                                    | Process Portal must be configured for a federated environment. For more information, see Configuring Process Portal for a federated environment.                         |
| Heritage Process Portal (deprecated)    | Heritage Process Portal spaces contain widgets that you can use to participate in business processes in the runtime environment.                                                                                                                                                                                                                                | You can create an HTML file to be used as the form using IBM® Integration Designer. It can be deployed to, and used in IBM Integration Designer, or IBM Workflow Server. |
| WebSphere® Portal portlet               | Select the page on which the portlet is to be placed in the page hierarchy of IBM WebSphere Portal by setting properties in the User interface settings tab. Alternatively, you can generate a portlet using the portlet generator.                                                                                                                             | To generate portlets, you need the Portal Toolkit. When you install IBM Integration Designer, you have the option to install the Portal Toolkit.                         |
| JavaServer Faces (JSF) client           | The client generator for human tasks generates a JSF-based web client that is useful for quickly prototyping human task processes or as a starting point for creating a custom client. The JSF client is generated based on data described in the interface that the human task implements, and does not need any input defined in the User interface settings. | The JSF client generator is included in IBM Integration Designer.                                                                                                        |
| Business Process Choreographer Explorer | With this client, the task is delivered to the staff member via an HTML-based web page. The style of this web page is determined by the JSP values that are specified in the User interface settings tab. You can modify these values as needed.                                                                                                                | No prerequisites. The client is included in IBM Integration Designer.                                                                                                    |

## Related concepts

- Versioning business state machines
- Ad hoc collaboration

## Related tasks

- Supporting other languages
- Defining user interfaces for a human task
- Generating HTML-Dojo pages for Heritage Process Portal spaces (deprecated)
- Integrating JavaScript in HTML-Dojo pages
- Preparing to extend generated JSF code
- Customizing clients
- Deploying a generated client to an external runtime environment

## Related reference

- Details tab: business state machine editor
- Design considerations for user interface generation