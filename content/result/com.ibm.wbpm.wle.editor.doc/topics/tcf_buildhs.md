# Modeling client-side human services

## About this task

The following diagram illustrates at a high level the main tasks and activities that are
associated with building a client-side human service.

<!-- image -->

- Tools available for modeling client-side human services

Learn about the tools that are available when you model client-side human services.
- Building a client-side human service

To create a user interface for a new case instance or process instance, create a client-side human service. When you build the client-side human service in the designer, define the logic for the client-side human service, which consists of a series of interconnected steps. You can then test and run the client-side human service in the web browser.
- Validating data in client-side human services

Data in client-side human services must be secured using appropriate validation practices to ensure that the data is not compromised.
- Reusing client-side human services

To break down a client-side human service into meaningful subflows that can be separately managed and reused in different contexts, you can define the reusable subflows as nested client-side human services.
- Declaring variables for client-side human services

For each client-side human service that you create, declare variables to capture the data that steps or activities in that human service use.
- Calling another service from a client-side human service

You can call a service from your client-side human service by adding an activity to the diagram. This activity calls another service or service flow that you can specify. The called service cannot be another client-side human service or a heritage human service.
- Implementing exclusive gateways

An exclusive gateway controls the divergence of a sequence flow by determining the branching of the paths that the flow can take at run time. When you add an exclusive gateway to your human service or service flow, you model a point in the execution of the service flow where only one of several paths can be followed, depending on a condition.
- Adding notes to client-side human services

To provide additional textual information to your client-side human service, you can add notes to the diagram by using the Note tool.
- Saving the state of a client-side human service during execution

To allow runtime users to save the state of a partially completed task, you can enable the execution context to be saved. By enabling the execution context to be saved, you enable a user who starts working on a task that includes multiple steps to close the browser and resume work later without losing work.
- Validating pages in client-side human services

To ensure that a page that is in your client-side human service passes valid data in the flow, use the page validation pattern to check its data.
- Handling errors in client-side human services

You can handle errors in a client-side human service by using a stand-alone error event handler or you can catch errors at a particular step by attaching a boundary error event to an individual service. To throw specific errors and end the processing of the service at a specified step, you can use error end events.
- Handling data changes in client-side human services

In instance details and task UIs, data can be changed both locally by the user or remotely by another user or service. The remote changes must be propagated to the user's browser to keep the data in the UI current. However, the user might have unsaved changes that need to be reconciled with incoming server updates. Use a data change event handler to react to and handle remote data changes.
- Assigning pre- and post-execution scripts

To specify attributes and conditions for the execution of an activity or event in a client-side human service or service flow, you can assign pre-execution and post-execution scripts to a specified activity or event node. The JavaScript code that you add as pre- and post-execution scripts runs immediately before or after the activity or event runs.
- Adding HTML meta tags to client-side human services

To optimize your HTML pages for being viewed on a mobile device, you can define HTML meta tags in the underlying client-side human service. The HTML meta tags are added to the HTML header when the client-side human service runs.
- Enabling work to be postponed and resumed at run time

If you want to enable Process Portal users to postpone and resume work at run time, you can add a postpone event to your client-side human service  or heritage human service diagram. The postpone event takes effect when it is used in a human service that is implemented as a task in a process.
- Enabling tasks to be reassigned at run time

As the author of a client-side human service, you can add implementation logic to your service to enable Process Portal users to reassign tasks at run time.
- Navigation options for after service completion

To help the user go to a specific page after the client-side human service completes, you can configure the end event of the service to provide an alternative destination.
- Running and debugging client-side human services in the Inspector

Run your client-side human service to see whether it performs as expected. If errors occur, you can use the debugger to examine each step in the client-side human service.
- Troubleshooting errors from running client-side human services

Errors that occur when client-side human services run on the client side are logged to the browser console. The browser console provides the error type, the location of the error, and the line number.