<!-- image -->

# Data exchange between BPEL processes and services

## A BPEL process consumes a service

The consumption
of a service in a business process is implemented using an invoke activity in the process model. The data that
is passed to the SCA service is retrieved from one or more BPEL variables.
Usually, the data is passed by value, which means that the invoked service
works with a copy of the data.

Under certain circumstances, data can
be passed by reference. Passing data by reference can help to improve the
performance of BPEL processes.

- The invocation of the service is synchronous.
- The BPEL process and the invoked service are in the same module.
- The data is exchanged using data-typed variables.

If the invoked service modifies the data, these changes are applied
to the corresponding BPEL variables. However, the invoked service
should not update the data because any changes that are made to the data are
not persistent. For long-running processes the changes are discarded when
the current transaction commits, and for microflows the changes are discarded
when the process ends. In addition, an event is not generated when the variable
is updated by the invoked service.

## A BPEL process is consumed by a service

A BPEL
process that is consumed by other services contains receive activities, pick
activities, or event handlers in the process model. The data that is passed
to the process is written to one, or more BPEL variables. Usually, the data
is passed by value.

- The invocation of the BPEL process is synchronous.
- The service and the invoked BPEL process are in the same module.
- The data is exchanged using data-typed variables.

If the invoked process modifies the BPEL variables, the input
data from the calling service is also modified.