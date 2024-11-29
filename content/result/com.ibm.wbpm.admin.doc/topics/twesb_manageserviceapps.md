<!-- image -->

# Administering service applications and service modules

## Before you begin

## About this task

- Resources for service modules

Service modules use resources provided by the service integration technologies of WebSphere® Application Server. Service modules can also make use of a range of resources, including those provided by the Java™ Message Service (JMS) and Common Event Infrastructure. To administer the resources for service modules, you can use the WebSphere administrative console, commands, and scripting tools.
- Versioning in service applications

Service applications support versioning. You can develop and deploy one or more versions of a module and its artifacts into the runtime environment for use by specific clients.
- Administering service modules with the administrative console or widgets

Use the administrative console and administration widgets to view and modify service modules. You can do some tasks, such as viewing modules and their properties, in both administrative interfaces. Other tasks, such as stopping and starting modules or modifying business calendars, are specific to one interface.
- Using wsadmin to administer service applications

You can manage service applications using commands. The commands can be used within scripts.
- Administering the throughput of SCA requests

For each Service Component Architecture (SCA) module deployed, requests being processed are held on queue points and in the data store for messaging engines. You can display the data for SCA requests, and take any appropriate action to manage the throughput of SCA requests.
- Managing service integration in applications

This set of topics provides information about the service integration technologies. Service integration is implemented as a group of messaging engines running in application servers (usually one engine to one server) in a cell.
- Working with imports and exports

You can list the imports and exports of service modules that have been deployed to IBM Business Automation Workflow. You can also display import and export interfaces and change the details of import bindings and selected export bindings.
- Working with modules in the administration widgets

Use the administration widgets to browse deployed modules in a cell, view detailed information about each module, and edit module artifacts.
- Administering services

Use the administration widgets to list services defined in WebSphere Service Registry and Repository (WSRR) and administer the mediation policies associated with the services.