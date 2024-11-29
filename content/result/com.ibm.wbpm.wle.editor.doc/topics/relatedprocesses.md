# Process instance relationships

<!-- image -->

A dependent instance cannot complete
until all the instances that it depends on are completed or terminated. If a dependent instance is
terminated forcefully, all its dependencies are also terminated, all the way down the dependency
tree. To terminate a dependent instance (and, therefore, its dependencies), you must be authorized
to terminate all the instances. To keep the dependency instances running, remove the dependency
relationship before you terminate the dependent instance. If you still need a relationship between
the processes, add an independent relationship instead. For information about terminating processes
in the Process Inspector, see Actions in the Process Inspector.

The
following image shows process instance A, which depends on process instances B and C.

<!-- image -->

- A process instance (A) can have multiple dependency process instances (B, C).
- A dependency process instance (B or C) can have only one dependent process instance (A).
- Process instance A cannot complete until process instance B and process instance C are both
completed or terminated.
- If process instance A is terminated, process instance B and process instance C are also
terminated.
- Terminating an instance also terminates its relationships except for completed instances. They
stay in the completed state.

You can create, delete, update, and query relationships programmatically
by using JavaScript API or REST APIs.