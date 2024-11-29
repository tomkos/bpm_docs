<!-- image -->

# Business Process Choreographer overview

Business Process Choreographer is an enterprise workflow engine
that supports both BPEL processes and human tasks in a WebSphere® Application
Server environment.
These constructs can be used to orchestrate services as well as integrate
activities that involve people in business processes. Business Process
Choreographer manages the lifecycle of BPEL processes and human tasks,
navigates through the associated model, and invokes the appropriate
services.

- Support for BPEL processes and human tasks. Allows you to model your business process using the
Web Services Business Process Execution Language (WS-BPEL, abbreviated to BPEL). With human tasks,
you can use the Task Execution Language (TEL) to model activities that involve people. Both BPEL
processes and human tasks are exposed as services in a service-oriented architecture (SOA) or
Service Component Architecture (SCA); they also support simple data objects and business
objects.
- Application programming interfaces for developing customized applications for interacting with
BPEL processes and human tasks.
- Human workflow widgets as part of Business Space. These widgets allow you to manage work, create
tasks for other people, and initiate services and processes.
- Business Process Choreographer Explorer. This web application allows you to administer BPEL
processes and human tasks.
- Business Process Archive Manager. When configured, this provides a separate database, to which
completed process instances and human tasks can be moved by running an administrative script. This
can help to maintain the performance of your Business Process Choreographer database. An API is also
available so that you can create your own client that can work with archived instances. The
Business Process Archive Explorer is a web application that allows users to browse or delete
instances that have been moved to the archive database. For more information, see BPEL process archive overview.
- By default, new Business Process Choreographer configurations benefit from the performance
improvements resulting from using shared work items.