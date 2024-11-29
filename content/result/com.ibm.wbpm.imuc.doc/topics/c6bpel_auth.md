<!-- image -->

# Authorization roles for BPEL
processes

- Java EE roles for BPEL processes

Java EE roles are set up when Business Process Choreographer is configured. For Java EE role-based authorization, you must have a user registry configured and application security enabled.
- Instance-based authorization roles for BPEL processes and activities

A set of predefined authorization roles is provided for BPEL processes and activities. You can assign these roles when you model the process. The association of users to instance-based roles is determined at run time using people resolution.
- Authorization for creating and starting BPEL processes

The set of users that are allowed to create and start a BPEL process is determined by the invocation task that is associated with the receive or pick (receive choice) activity that is used to create and start a new process instance, and also by the administration task that is associated with the process. The process inherits the roles that you assign to these tasks.
- Authorization for interacting with a BPEL process

A long-running BPEL process can have multiple receive activities, pick (receive choice) activities, and event handlers. These are served by submitting a request to the appropriate operation of the corresponding process instance. The process instance is identified implicitly by providing a unique correlation set instance in the request according to the correlation set defined in the process model.
- Authorization for administering BPEL processes

You can use administration tasks to authorize a user, or group of users, to perform administrative actions on BPEL processes and their associated activities

<!-- image -->

## Related information

- Authorization roles for human tasks