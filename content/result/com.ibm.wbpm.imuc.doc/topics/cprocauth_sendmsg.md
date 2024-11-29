<!-- image -->

# Authorization for interacting with a BPEL process

A receive or pick activity can be used to create a process instance.
So, interacting with an existing process instance by submitting a
request to a process is similar to starting a new process instance.

The set of users that are authorized to submit a request to a process
instance is determined by the invocation task that is associated with
the receive or pick activity, or the event handlers, and by the administration
task that is associated with the process.

- Assign an inline invocation task to the receive activity, pick
activity, or event handler.The potential starters that are defined
for the inline invocation task submit a request to the corresponding
operation of the process. The invocation task is optional. If an invocation
task is not defined, everyone is authorized to submit a request.
- You can also use a stand-alone human task to secure inbound operations
of a process. The same rules and restrictions apply as
for stand-alone invocation tasks for process-creating operations.
- Assign an administration task to the process.The administrator
role of the administration task is inherited by the process. A process
administrator can interact with a process using its operations.
If
an administration task is not specified for the process, the starter
of the process becomes the process administrator. In this case, the
process starter is allowed to submit requests to operations of the
process instance.

If a process uses the same operation in different receive, pick
(receive choice) activities, or event handlers, and the receiving
process instance is currently not expecting a request, because the
corresponding receive or pick (receive choice) activity is not yet
waiting or the event handler is not yet active, then the user sending
the request must be authorized to send a request to all of these activities
and event handlers, otherwise the request will be rejected.