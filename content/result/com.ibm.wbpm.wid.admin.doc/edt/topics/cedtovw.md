<!-- image -->

# Custom event definitions

The Common Base Event specification defines the content
of those events that conform to the specification. Event definitions
are files that enable you to define the structure of emitted events
that are based on the Common Base Event specification. Custom event
definitions are event definitions that have been created from
scratch in the event definition editor rather than having been generated
from existing events by the event definition generator.

An event definition file has a .cbe file extension and it can contain
one or more event definitions. If an event definition file contains
multiple event definitions, all of the event definitions in the file
will be listed in the Business Integration view of the Business Integration
perspective (and in the Project Explorer view of the Business Monitoring
perspective if the IBM® Business Monitor
development toolkit is installed). If an event definition file only contains a single
event definition, it will usually have the same name as the event
definition that it contains. For this reason, you can generally consider
event definition files and event definitions to be synonymous when
reading the event definition editor documentation.

It is generally considered a best practice to have only one event
definition in each event definition file. For this reason, the event
definition editor lets you create or edit only one event definition
in each file by default. If you need to edit an event definition file
that contains multiple event definitions, or if you need to add or
delete event definitions in a file, you can set a preference that
will enable you to display and work with all of the event definitions
in the file simultaneously in the event definition editor.

## Content of event definitions

## The event definition editor in context

Using
the event definition editor, you can create or edit custom event definitions.
However, to work with the event definitions in a meaningful way, you
need the IBM Business Monitor
development toolkit. The toolkit enables you to import your event definitions into a
monitor model in the monitor model editor and then add business metrics
to the event definitions. It also enables you to deploy the monitor
model and event definitions to an IBM Business
Monitor server and then monitor the emitted events using the IBM Business
Monitor dashboard.

Creating and editing custom event definitions is
merely one task in an end-to-end chain of event monitoring tasks that
you can perform using the tools of IBM Integration
Designer and the IBM Business Monitor
development toolkit. The following figure shows how the creation of custom event definitions
relates to the other event monitoring tasks:

<!-- image -->

In the figure, the following tasks
are illustrated:

|    Task |  Description                              |
|---------|-------------------------------------------|
|       1 | Select predefined events                  |
|       2 | Add custom event emitters                 |
|       3 | Generate event definitions                |
|       4 | Edit event definitions                    |
|       5 | Test event definitions                    |
|       6 | Generate monitor model                    |
|       7 | Add business metrics to event definitions |
|       8 | Deploy the modules to the server          |
|       9 | Monitor the emitted events                |

These tasks are briefly described in the following sections.

## Selecting predefined events

In IBM Integration
Designer, each kind of component consists of a number of elements that have predefined events. For example, a business process consists of
activities and each type of activity has one or more events predefined
for it. If you want your component elements to emit events at run
time, you must first select the predefined events for the elements
in the event monitor. Once you have selected the predefined events,
you can also choose to generate event definitions for them using the
event definition generator. Information about selecting predefined
events is found in the event monitor topics "Specifying event properties
for component elements" and "Specifying event properties for components."

## Adding custom event emitters

If you want
to emit custom events from a mediation flow or visual snippet, you
can add custom event emitters to the mediation flow or visual snippet
in their   editors. After you have added a custom event emitter to
a mediation flow, you can choose to generate event definitions for
it. Information about adding custom event emitter primitives to mediation
flows is found in the mediation flow editor topic "Emitting common
base events." Before you can add a custom event emitter to a visual
snippet, you must first create a custom event definition for the emitter
in the event definition editor. Information about adding custom event
emitter activities to visual snippets is found in the visual snippet
editor topic "Configuring a custom event in a visual snippet."

## Generating event definitions

In the context
of IBM Integration
Designer, there are two kinds of events. Predefined events are events that have been defined in advance for IBM Integration
Designer components and their elements, such as business processes and their
activities. Custom events, by comparison, are user-defined
events that you can emit from custom event emitters in certain components,
such as mediation flows and visual snippets.

After you have
added custom event emitters to a mediation flow or you have selected
predefined events for a component in the event monitor, you can select
the mediation flow or component in the Business Integration view and
then generate or regenerate event definitions for it. Note, however,
that you cannot generate event definitions for custom events in visual
snippets and you cannot regenerate event definitions that were created
from scratch in the event definition editor.

Generated event
definitions are automatically stored in the same module that contains
your component and they are visible in the Physical Resources view.
If you have installed the IBM Business Monitor
development toolkit, they are also visible in the Project Explorer view of the Business
Monitoring perspective. Information about how to generate event definitions
is found in the event definition generator topic "Generating event
definitions."

## Editing event definitions

The event definition
editor enables you to create custom event definitions from scratch
and store them in either a module or a library that is referenced
by the module. If you have generated event definitions for predefined
or custom events using the event definition generator, you can optionally
edit the event definitions in the event definition editor. However,
any changes that you make to the event definitions in the editor will
be overwritten when you next regenerate the event definitions. For
this reason, it is assumed that you will be deploying any edited event
definitions before you regenerate them. Generally, editing generated
event definitions is unnecessary and it is only recommended for advanced
users. Information about recommended practices for editing generated
event definitions is found in the event definition generator topic
"Event definitions."

## Testing event definitions

After you have
created event definitions using the event definition editor, you can
test the event definitions in the integration test client. The test
client enables you to select an event definition and then emit an
event to ensure that the event definition is defining the structure
of the emitted event correctly. Information about testing event definitions
in the test client is found in the test client topic "Testing event
definitions."

## Generating monitor models

If you have installed
the IBM Business Monitor
development toolkit, you can generate event definitions and a monitor model
to contain them. The event definitions are automatically stored in
the same module that contains the component for which you generated
the event definitions. The monitor model is automatically stored in
the business monitoring project. Information about generating monitor
models is found in the IBM Business Monitor
development toolkit documentation.

## Adding business metrics

If you have installed
the IBM Business Monitor
development toolkit, you can import your event definitions into a monitor
model in the monitor model editor and then add business metrics to
the event definitions. Information about using the monitor model editor
is found in the IBM Business Monitor
development toolkit documentation.

## Deploying the modules

Event definitions
define events that are intended for monitoring by the IBM Business
Monitor tools. For this reason, modules that contain event definitions must
be deployed to an IBM Business
Monitor server. When you deploy your module, any associated business monitoring
projects, monitor models, and event definitions are automatically
deployed as well.

Generally, deploying modules to an IBM Business
Monitor server is similar in many respects to deploying modules to IBM Business Automation
Workflow. Specific information on deploying modules to an IBM Business
Monitor server is found in the IBM Business Monitor
development toolkit documentation. General information on deploying modules to servers
is found in the IBM Integration
Designer topic "Deploying modules."

## Monitoring the emitted events

After you deploy your module to a running IBM Business
Monitor server, you can right-click the server and select the WBM Web Dashboard menu item. This opens the IBM Business
Monitor web dashboard to enable you to monitor the emitted events. Information
about using the dashboard to monitor emitted events is found in the IBM Business
Monitor documentation.