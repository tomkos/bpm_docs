<!-- image -->

# Programming BPEL processes and
tasks

## About this task

These clients can be Enterprise JavaBeans (EJB)
clients, web service clients, or web clients that exploit the Business
Process Choreographer Explorer JavaServer Faces (JSF) components.
Business Process Choreographer provides Enterprise JavaBeans (EJB)
APIs and interfaces for web services for you to develop these clients.
The EJB API can be accessed by any Java™ application,
including another EJB application. The interfaces for web services
can be accessed from either Java environments
or Microsoft .Net environments.

- Comparison of the programming interfaces for interacting with BPEL processes and human tasks

Enterprise JavaBeans (EJB), web service, Java Message Service (JMS), and Representational State Transfer Services (REST) generic programming interfaces are available for building client applications that interact with BPEL processes and human tasks. Each of these interfaces has different characteristics.
- Human Task Manager API authorization and actions

Human Task Manager API authorization is based on actions. Each API method is represented by one or more actions. The role that a user has determines the actions the user is authorized for.
- Queries on BPEL process and task data

Instance data for long-running BPEL processes and human tasks are stored persistently in the database and are accessible by queries. Also, template data for BPEL process templates and human task templates can be accessed using a query interface.
- Developing EJB client applications for BPEL processes and human tasks

The EJB APIs provide a set of generic methods for developing EJB client applications for working with the BPEL processes and human tasks that are installed on a Workflow Server.
- Developing web services API client applications for BPEL processes and human tasks

You can develop client applications that access BPEL process applications and human task applications through the Business Process Choreographer web services APIs. The client application development process consists of a number of mandatory and optional steps, including generating a web service proxy and adding security and transaction policies to the client application.
- (Deprecated) Developing client applications using the Business Process Choreographer JMS API (deprecated)

You can develop client applications that access BPEL process applications asynchronously through the Java Messaging Service (JMS) API.
- Developing web applications for BPEL processes and human tasks by using JSF components

Business Process Choreographer provides several JavaServer Faces (JSF) components. You can extend and integrate these components to add business-process and human-task functionality to web applications.
- Developing JSP pages for task and process messages

The Business Process Choreographer Explorer interface provides default input and output forms for displaying and entering business data. You can use JSP pages to provide customized input and output forms.
- Creating plug-ins to customize human task functionality

Business Process Choreographer provides an event handling infrastructure for events that occur during the processing of human tasks. Plug-in points are also provided so that you can adapt the functionality to your needs. You can use the service provider interfaces (SPIs) to create customized plug-ins for handling events and the post processing of people query results.