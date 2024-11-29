<!-- image -->

# Registering API event handler and notification event handler
plug-ins with task templates, task models, and tasks

## About this task

You can register a plug-in in one of the following
ways.

## Procedure

- For task templates modeled in IBM® Integration
Designer,
specify the plug-in in the task model.
- For ad hoc tasks or ad hoc task models, specify the plug-in
when you create the task or task model. Use the setEventHandlerName method
of the TTask class to register the name of the
event handler.
- Change the event handler for a task instance at run time.
Use the update(Task task) method to use
a different event handler for a task instance at run time. The caller
must have task administrator authority to update this property.