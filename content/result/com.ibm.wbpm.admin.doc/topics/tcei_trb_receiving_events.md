# Problems when receiving or querying events

- Error when querying events (message CEIDS0060E)

My event consumer encounters an error when trying to query events from the event service, and message CEIDS0060E appears in the WebSphere® log file.
- Events not being stored in the persistent data store

My event source application is successfully submitting events to the emitter, but when an event source queries the events, they are not in the persistent data store.
- Events not being received by consumers (no error message)

My event source application is successfully submitting events to the emitter, but the events are not received by consumers using the JMS interface.
- Events not being received by consumers (NameNotFoundException)

My event source application is successfully submitting events to the emitter, but the events are not published to consumers using the JMS interface, and the log file indicates a NameNotFoundException.
- Error when querying an event group (message CEIES0048E)

My event consumer application encounters an error when trying to query events from an event group. The log file indicates an EventGroupNotDefinedException and shows message CEIES0048E (The event group is not defined in the event group list that the event server instance is using.)