# Problems when sending events

- Error when sending event (message CEIDS0060E)

My event source encounters an error when trying to send an event, and message CEIDS0060E appears in the WebSphere® log file.
- Error when sending event (ServiceUnavailableException)

My event source application encounters an error when trying to send an event to the event server. The log file indicates a ServiceUnavailableException with the message A communication failure occurred while attempting to obtain an initial context with the provider URL.
- Error when sending event (NameNotFoundException)

My event source application encounters an error when trying to send an event to the event service. The log file indicates a NameNotFoundException with a message such as First component in name events/configuration/emitter/Default not found.
- Error when sending event (message CEIEM0025E)

My event source application encounters an error when trying to send an event to the event server. The log file indicates a DuplicateGlobalInstanceIdException.
- Error when sending event (message CEIEM0034E)

My event source encounters an error when trying to send an event to the event service. The log file indicates an EmitterException with the message The JNDI lookup of a JMS queue failed because the JNDI name defined in the emitter profile is not bound in the JNDI.
- Event is not valid (message CEIEM0027E)

My event source is trying to send an event, but the emitter does not submit it to the event service and outputs message CEIEM0027E to the log file ("The emitter did not send the event to the event server because the Common Base Event is not valid").
- Synchronization mode not supported (message CEIEM0015E)

My event source is trying to send an event, but the emitter does not submit it to the event service and outputs message CEIEM0015E to the log file (The emitter does not support the specified synchronization mode).
- Transaction mode not supported (message CEIEM0016E)

My event source is trying to send an event, but the emitter does not submit it to the event service and outputs message CEIEM0016E to the log file (The emitter does not support the specified transaction mode).