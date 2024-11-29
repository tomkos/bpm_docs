<!-- image -->

# Factors affecting the behavior of stand-alone invocation tasks
and their service components

- A one-way operation implies a service execution the completion
of which is not made known to the invoking task. The task service
execution ends with the successful invocation of the associated service.
- A request-response operation implies a service execution the completion
of which is made known to the invoking task. The task execution ends
when the result of the service execution is made available to the
invoking task.

- Synchronous invocation of the task and its associated service
using the callTask method
- Asynchronous invocation of the task and its associated service
using the startTask method