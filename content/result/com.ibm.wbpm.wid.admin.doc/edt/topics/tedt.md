<!-- image -->

# Creating custom event definitions

Using the event definition editor, you can create custom event definitions
to define the structure of your emitted events. However, you must have the IBM® Business Monitor
development toolkit installed to work with the event
definitions. The toolkit enables you to import your event definitions into a monitor model in the
monitor model editor and then add business metrics to the event definitions. You can then deploy the
monitor model to an IBM Business
Monitor server and
monitor the emitted events with the IBM Business
Monitor dashboard.

## About this task

- Custom event definitions

The Common Base Event specification defines the content of those events that conform to the specification. Event definitions are files that enable you to define the structure of emitted events that are based on the Common Base Event specification. Custom event definitions are event definitions that have been created from scratch in the event definition editor rather than having been generated from existing events by the event definition generator.
- Event definition editor

In IBM Integration Designer, the event definition editor is the designated tool for creating and editing custom event definitions. The event definition editor features a simple user interface that enables you to easily add and manage event definitions.
- Setting preferences for the event definition editor

By default, the user-definable preferences for the event definition editor are already optimized for working with event definitions. However, in the course of your event definition tasks, you may find that you want to change some preferences.
- Creating new event definitions

Using the New Event Definition wizard, you can create a new event definition in a module, library, or business monitoring project and then edit the event definition in the event definition editor. Event definitions that have been created in the event definition editor can be used to create custom event emitter activities in the visual snippet editor.
- Opening existing event definitions

In the event definition editor, you can open any existing event definition that was created using the New Event Definition wizard or that was generated using the event definition generator. However, if you open an event definition that was generated, a window will warn you that your updates will be overwritten the next time that the event definition is regenerated.
- Adding additional event definitions to an event definition file

By default, the event definition editor enables you to create one event definition for each event definition file. Although it is generally considered a best practice to have only one event definition for each file, you can nonetheless set a preference that will enable you to add additional event definitions to a file in the event definition editor.
- Editing event definitions

In the event definition editor, you can edit an event definition and customize its properties and extended data elements.
- Deleting event definitions

By default, the event definition editor displays one event definition for each event definition file. However, if you are working with an event definition file that contains multiple event definitions and you want to delete one or more of the event definitions, you can set a preference that will enable you to delete the event definitions in the event definition editor.
- Limitations for the event definition editor

From time to time, you may encounter some limitations in using the event definition editor. In most situations, you can successfully work around these limitations.