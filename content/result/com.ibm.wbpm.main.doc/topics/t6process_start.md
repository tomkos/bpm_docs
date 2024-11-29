<!-- image -->

# Starting BPEL processes

## About this task

Examples are provided that show how you might develop applications
for typical scenarios for starting microflows and long-running processes.

- Running a microflow that contains a unique starting service

A microflow can be started by a receive activity or a pick activity. The starting service is unique if the microflow starts with a receive activity or when the pick activity has only one onMessage definition.
- Running a microflow that contains a non-unique starting service

A microflow can be started by a receive activity or a pick activity. The starting service is not unique if the microflow starts with a pick activity that has multiple onMessage definitions.
- Starting a long-running process that contains a unique starting service

If the starting service is unique, you can use the initiate method and pass the process template name as a parameter. This is the case when the long-running process starts with either a single receive or pick activity and when the single pick activity has only one onMessage definition.
- Starting a long-running process that contains a non-unique starting service

A long-running process can be started through multiple initiating receive or pick activities. You can use the initiate method to start the process. If the starting service is not unique, for example, the process starts with multiple receive or pick activities, or a pick activity that has multiple onMessage definitions, then you must identify the service to be called.