# Event types

You can include the following types of events in your processes.

Start events have the following implementation
options:

| Option      | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|-------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| None        | Enables users to start a process manually from IBM® Process Portal , run the process in the Inspector, or call the process as a linked process from another higher-level process.Exposure of your process affects the Start event option. If exposed and it has a launch process UI, then your process can be started as a task. If exposed but with no launch process UI, then your process can be started though no UI task appears. The process starts immediately. If your process is not exposed, then your process must be started programmatically, or as a linked process, or through an API call. |
| Message     | Starts a process when an incoming message is received (see Using start message events ) or starts an event subprocess (see Modeling event subprocesses). An undercover agent (UCA) receives the incoming message, and then starts the process. You can use an undercover agent to receive messages from another process, or from a web service.                                                                                                                                                                                                                                                            |
| SCA Service | Starts a process when an SCA service message is received.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ECM Content | Starts a process when an Enterprise Content Management (ECM) event is received.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Document    | Starts a process when a new document is created on an Enterprise Content Management (ECM) system.Alternatively, launches a process instance from an existing document on an ECM system. See Document start event.                                                                                                                                                                                                                                                                                                                                                                                          |

| Option               | Description                                                                                                                                                                                                                                                                                                                                                                                                            |
|----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| UCA Message          | Receives a message from an undercover agent or sends a message while a process is running. You can include an event in the process flow or attach an event to an activity. When attached to an activity, the event only receives messages. For more information, see Using intermediate and boundary message events to receive messages and Using intermediate message events and message end events to send messages. |
| Message (receiving)  | Receives a message.                                                                                                                                                                                                                                                                                                                                                                                                    |
| Message (sending)    | Sends a message.                                                                                                                                                                                                                                                                                                                                                                                                       |
| SCA Service Message  | Receives a message from an SCA service while the process is running.                                                                                                                                                                                                                                                                                                                                                   |
| ECM Content          | Receives a message from an undercover agent when an Enterprise Content Manager (ECM) event is received while the process is running. You can include a content event in the process flow or attach an event to an activity.                                                                                                                                                                                            |
| Timer                | Creates a delay to prevent an event or activity from immediately triggering. Use a timer event to model escalation paths or delays in your process. You can specify a time interval before or after an activity is run. You can include a timer event in the process flow or attach it to an activity. For more information, see Modeling delays, escalations, and timeouts.                                           |
| Tracking             | Creates a point in the process at which you want to capture the runtime data for reporting purposes.                                                                                                                                                                                                                                                                                                                   |
| Error boundary event | Catches process execution errors and can trigger further process flow. This event must be attached to an activity.                                                                                                                                                                                                                                                                                                     |

| Option      | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|-------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| None        | Stops the activities on a particular path.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Error       | Use the Error implementation option when you want to throw an error to parent processes or to error event subprocesses. For more information, see Handling errors using error events.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Message     | Sends a message at the end of a particular path. For example, you can send a message at the conclusion of each process instance that is received by a start message event in another process so that the completion of one process starts another process. See Using message end events.                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Terminate   | Closes running tasks that are associated with a process and cancel outstanding timers. You can set these options for the terminate event:  Terminate entire process instance Terminates the entire process instance. If you do not select this option, only the process that contains the event and its subprocesses is terminated. If an entire process instance is terminated, the process shows a status of Terminated in the Inspector.  Delete all terminated instance runtime data Cleans up the run time state for the running instance. All database states for the runtime instance and any generated tracking data is deleted. This setting applies only to top-level process instances, and is ignored otherwise. |
| UCA Message | Sends a message. For example, you can send a message at the conclusion of each process instance that is received by a start message event in another process so that the completion of one process starts another process. See Using message end events.                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |