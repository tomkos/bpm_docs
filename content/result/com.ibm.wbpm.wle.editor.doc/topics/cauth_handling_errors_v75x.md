# Error events in models from V7.5.x and earlier

- Error intermediate events at the boundary of a step in services
or at the boundary of an activity in a business process definition
(BPD), subprocess, or event subprocess catch all errors. As of V8.0,
you model this behavior using the Catch All Errors option,
which is available on the Properties tab for a catching error event.
In addition, you can refine your error handling by catching specific
errors using the Catch Specific Errors option.
- Error intermediate events in the flow of a BPD, subprocess, or
event subprocess were allowed but had no effect on runtime behavior.
You can delete these events.
- Error end events in services, BPDs, subprocesses, or event subprocesses
retain the same error throwing behavior: they can be caught only as
part of an event that catches all errors. To use the extended error-handling
capabilities, delete the old event and add a new event.

To use the latest error-handling capabilities, you can move the
models to V8.0. Open your application, look at the referenced system
toolkits, click a toolkit, and select the menu option to upgrade it.