# Building process applications

You can either create process applications in Workflow Center or export and import
process applications into Workflow Center. After a process
application is created or imported, it is stored and listed in the Workflow Center repository. You open
process applications in Process Designer where you can create
and edit the business processes within those process applications.

- For designing processes, see Chapter 5: Design considerations and patterns in Business Process Management Design Guide: Using IBM Business Process Manager.
- For best practices, see Chapter 2: Architecture best practices and Chapter 3: Development best
practices in IBM Business Process Manager V8.5 Performance Tuning and Best Practices.
- For an overview of critical performance-related information, see IBM Business
Process Manager V8.5 Performance Tuning.

The following high-level diagram illustrates the basic tasks and activities that are typically
associated with building a process application.

<!-- image -->

- IBM Process Designer

The Process Designer is the primary modeling and designing tool in IBM Business Automation Workflow. It is an editor that you access in a browser to model, implement, and inspect business processes.
- Creating process applications

When you create a process application (process app), you provide a name, acronym, and optional description of the process application.
- Creating a process

A process is a set of related activities, along with supporting information such as data and content. The activities can be part of a structured flow, or ad hoc activities that are not part of a structured flow.
- Validating process applications and toolkits (projects)

Use validation functions to fix errors and refine process applications and toolkits (projects) as you build them.
- Running and debugging processes and services in the Inspector

Authoring processes is an iterative process that can involve several playback sessions. You can run, test, and debug your processes and services in the designer's Inspector.
- Creating a team

A team is a group of users that perform similar tasks, and consists of a set of members and a team of managers. Teams are used to manage the tasks that users can perform in Process Portal . Because any team can be added as the manager of another team, you can flexibly define your organization's management structure.
- Integrating services in the designer

Services provide functions for a business process, which itself is a sequence of services. You can discover and use external services in the designer.
- Creating relationships between process instances

You can create relationships between process instances so that all authorized Process Portal users can view all the information for their cases or processes, such as all the cases for a particular client or similar cases in a particular region. You can also create dependencies between process instances so that a process instance cannot complete until all the instances that it depends on are completed.
- Business objects and variables

Variables capture the business data that is used by activities in a process, service flow or human service.
- Creating user interfaces

Human services provide the logic and user interface through which users can view and interact with process and case instances and their data.
- Enabling document support

You can use a document management system to store and interact with documents that you use in your process. You can create, query, view, update and delete documents.
- Enabling processes for tracking and reporting

IBM Business Automation Workflow provides ways to collect and consume process performance information. To take advantage of this information, you enable to design your processes to make them trackable.
- Designing process interactions for business users

A business user might interact with a process in a number of ways. The user might be the one to launch the process, or the user might be assigned tasked generated from individual activities in the process.
- Exposing items

Exposure settings enable you to see which authorized users can start certain processes, services, client-side human services, and heritage human services.
- Globalization

To ensure that applications can be used in multiple geographical locations and cultures, globalization support is built in through appropriate design and implementation of systems, software, and procedures. IBM Business Automation Workflow provides globalization support for single- and multi-byte character sets and for bidirectional transformation including contextual support, support for text layout transformation, and calendar support for Hebrew and Hijri.
- Modeling business process definitions (deprecated)

 Traditional: 
A business process definition (BPD) is a major unit of logic in a business application. You can create BPDs in the desktop Process Designer (deprecated).