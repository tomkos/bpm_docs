# Creating a service flow

A service flow is a sequence of services, gateways, and events. The Service Flow editor
palette provides you with the tools to develop a simple or complex service flow that you can then
use in your processes.

## About this task

Services in earlier releases were created with the desktop Process Designer. These heritage
services can be converted into service flows, which you can edit in the Process Designer and run in the
same way you ran heritage services. For more information about the conversion of heritage services,
see Converting heritage services.

## Procedure

1 From the library, click Services > Service Flow and complete the wizard: For more information, see Using services to define dynamic teams .
    1. Specify a suitable name for your service flow.
    2. If
you want the service flow to be used as a team service for team retrieval
or team filtering, select Use as a team service and
specify the service type. A template that corresponds to the selected
service type is specified by default. If you want to replace the default
template, you can point to a service that has additional input parameters
and the same output variable, without any additional output variables.
    3. Click Finish.
2. In the Diagram view, create your
service flow by dragging artifacts in the palette like services, gateways,
and events to the canvas and wiring them. See Service Flow editor palette.
3. Optional: To
assign a pre-execution and post-execution script to an activity in
the service flow, select the activity node in the service flow diagram,
click Pre & Post in the properties view,
and then enter or paste the appropriate JavaScript code in the Pre-Execution
Script section or the Post-Execution Script section.
 The JavaScript code that you add runs immediately before or
after the activity runs. For more information, see Assigning pre- and post-execution scripts.
4. Optional: To invoke
a REST service, a Java application, or an external implementation,
add a service task to the diagram and wire it. In the Implementation tab,
select the corresponding external service, and select the operation
that you want to invoke. Map the inputs and outputs in the Data
Mapping tab. See Calling an external service.
5. Optional: 
To integrate with an Enterprise Content Management (ECM) server,
add a Content Integration Task  to the diagram
and wire it. Enter the properties for the ECM server that you want
to connect to. See Building a service that integrates with an ECM system or a BPM store.
6 To protect theREST services, coach views, or external implementations that callthis service flow, specify the access level that is required for thecall:

- Select Do not allow Ajax calls if the
service flow has access to private or confidential information that
cannot be exposed through any Ajax calls.
- Select Allow calls from trusted callers to
allow only trusted callers, such as known coach views or external
implementations, to call the service flow. The users who trigger the
call must be authorized for the calling context. For example, if the
service flow is called in the context of a specified task, the user
must be authorized for that task. This is the default selection for
service flows.
- Select Allow calls from all users to
allow any user that is authenticated with Business Automation Workflow to call
the service flow.
7. Optional: To call another
service flow or heritage service from your service call, add a linked
service flow node to your diagram, and specify the service that you
want the linked service flow to call. See Calling another service from a service flow.
8. Optional: If
you need to branch the path that your service flow takes at run time,
add an exclusive gateway to the service flow diagram, and define JavaScript
conditions in the implementation properties of the gateway to determine
the path that the flow follows. For more information, see Implementing exclusive gateways.
9. Optional: 
If you want to send a message
to an undercover agent (UCA) while the service flow is running, use
the Message (sending) tool () to add an
outgoing intermediate message event to the diagram. In the Implementation tab
of the selected message event, under Event Properties,
select the UCA that you want to attach to the message event, and then
use Target current snapshot to set the target
for the message event. For more information, see Sending messages to undercover agents.
10. Optional: 
To capture runtime data about the status and progress of a service
flow execution, add a monitoring event to the service flow model.
Use the Tracking tool () to add a tracking
event node to the service flow diagram. Insert the tracking event
in the diagram at the point where you want Business Automation Workflow to capture
the runtime data. For more information, see Enabling runtime data tracking .
11 Optional: To improve performance, under Additional Properties , selectEnable caching of service flow results to display the cache configurationfields, and enable caching of service flow results for each combination of input parameter values.By default, caching is disabled and the duration options are not displayed. When caching is enabled, for every combination of input parameter values, a distinct serviceflow result is automatically added to the cache. When the service flow is started, the cache is checked: By default, the service flow results are stored in the cache for 12 hours. Tochange the caching period, use the Days , Hours ,Minutes , and Seconds fields to select the appropriateduration. If the service flow is called and the number of cached results exceeds the defined cachesize, the least recently used result is removed so that there is space for the new result.Restriction: Service result caching is available for top-level service flows, but does notwork for linked service flows.

- If a matching result is found, the cached result is used directly without invoking the service
flow.
- If a matching result is not found in the cache or the cached result has expired, the service
flow is invoked and the cache is refreshed.
12 Optional: Under Additional Properties , specify whether you want to enable theautomatic synchronization of shared business objects: For more information, see Shared business objects .

- If you selected Do not allow Ajax calls earlier (step 6), you can select Automatically sync shared
business objects to enable the synchronization of shared business objects. To disable
the synchronization, keep Automatically sync shared business objects clear
(default option). For example, when you have a service flow that runs custom logic and then
explicitly saves the shared business objects, clear the automatic synchronization option.
- If you selected Allow calls from trusted callers or Allow
calls from all users, you can select Automatically sync shared business
objects to enable the automatic synchronization of shared business objects. However,
enabling synchronization when the service flow is invoked through Ajax will not take effect. In this
case, a warning message indicates that no automatic synchronization of shared business objects
occurs.
13. Optional: Under Additional Properties, specify whether
you want to execute the service flow within a single transaction. When you execute a service flow in
a single transaction, the activities which trigger data updates are rolled back when an application
error occurs. 
Restriction: Not all activities which are available in the activity palette support the
transaction propagation in the same way.
14. Click Save or Finish
Editing.

- Service Flow editor palette

The Service Flow editor is an easy-to-use graphical development environment for developing service flows. By dragging objects from the palette to the canvas, you compose the structure of your service flow.
- Using transient variables in service flows

You can prevent large variables and sensitive or secret information from being written to the database by marking service flow variables as transient.
- Adding a service from the library

To insert a service flow, REST service, web service, or Java service into your service flow you can drag it from the library and drop it onto your service flow diagram.
- Adding a decision task to a service flow
- Calling another service

You can use a linked service flow to call another service flow or heritage service from the service flow that you are building.
- Using IBM ODM business rules

You can define an IBM® Operational Decision Manager business rule, deploy it as a decision service, and use it as an external service in a service flow. If you have exported a set of rules from a decision task, you can import them to use them in IBM ODM.
- Setting up a team filter service

You can use a team filter service to dynamically prevent certain users from being assigned to an activity. The filtering can be based on any criteria and can use input parameters from relevant process variables to determine which users to filter out.
- Handling errors in service flows

When you design a process or service that includes a service flow, you must provide logic to recover from possible errors that might be generated in the runtime application.
- Using scriptlets in script tasks

Use a scriptlet instead of JavaScript to generate a large amount of text, with variable parts that are computed by using embedded JavaScript. Unlike the general script, a scriptlet can produce a value only for a single variable.
- Assigning pre- and post-execution scripts

To specify attributes and conditions for the execution of an activity or event in a client-side human service or service flow, you can assign pre-execution and post-execution scripts to a specified activity or event node. The JavaScript code that you add as pre- and post-execution scripts runs immediately before or after the activity or event runs.
- Globalizing service flows

Globalizing your service flows enables them to produce entities, such as business objects, for users in different language locales. To enable translation, you must create localization resources for the service flows, and modify the scripts included in them to use these localization resources.
- Implementing exclusive gateways

An exclusive gateway controls the divergence of a sequence flow by determining the branching of the paths that the flow can take at run time. When you add an exclusive gateway to your human service or service flow, you model a point in the execution of the service flow where only one of several paths can be followed, depending on a condition.
- Sending messages to undercover agents

To send a message to an undercover agent (UCA) during the execution of a service flow or heritage human service, you can add an intermediate message event to the service flow diagram.
- Enabling runtime data tracking

To capture runtime information about the progress of a service flow or heritage human service execution for tracking or reporting purposes, you can model your service to emit a tracking event.
- Calling services from views

You can invoke Ajax services or service flows from views. The coach framework calls the services by using workflow REST APIs in taskless mode.
- Modeling secure services

To ensure that the service flows that you model are secure, you must add authorization checks to the service implementation.
- Running and debugging service flows

You can develop your service flow as an iterative process that includes several playback sessions. If errors occur, you can debug the service flow in the Inspector.
- Enabling transactional service flows

To run a transactional service flow, you can enable the feature to execute the service flow within a single transaction.