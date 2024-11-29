<!-- image -->

# Invocation style compatibility with prior releases

## Request-response operation

- Async with deferred response
- Async with callback
- As target

Using the new Async invocation styles, the type of Async invocation is selected, without
the need to consider the invocation style used to invoke the mediation flow, and without the need to
specify additional properties.

The As target invocation style is the new default style. It provides a similar capability
to that of the previous Default style, with some modifications. The modifications simplify
the determination of the style used, and remove the potential for a deadlock, due to transaction
context settings. The previous Default style is renamed Default (Compatibility).

| Preferred interaction style of the target   | How the mediation flow component is called   | Invocation style                                                                                                                                                                      | Invocation style        |
|---------------------------------------------|----------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------|
| Preferred interaction style of the target   | How the mediation flow component is called   | Default (Compatibility)                                                                                                                                                               | As target               |
| Sync                                        | Sync                                         | Sync                                                                                                                                                                                  | Sync                    |
| Sync                                        | Async one way                                | Sync                                                                                                                                                                                  | Sync                    |
| Sync                                        | Async with deferred response                 | Sync                                                                                                                                                                                  | Sync                    |
| Sync                                        | Async with callback                          | Sync                                                                                                                                                                                  | Sync                    |
| Async                                       | Sync                                         | Async with deferred response                                                                                                                                                          | Sync [1]                |
| Async                                       | Async one way                                | Async with deferred response                                                                                                                                                          | Async with callback [2] |
| Async                                       | Async with deferred response                 | Async with deferred response                                                                                                                                                          | Async with callback [2] |
| Async                                       | Async with callback                          | Async with callback (or deferred response if the Require mediation flow to wait for service response when the flow component is called asynchronously with callback. property is set) | Async with callback [2] |
| Any                                         | Sync                                         | Sync                                                                                                                                                                                  | Sync                    |
| Any                                         | Async one way                                | Sync                                                                                                                                                                                  | Async with callback [2] |
| Any                                         | Async with deferred response                 | Sync                                                                                                                                                                                  | Async with callback [2] |
| Any                                         | Async with callback                          | Async with callback (or deferred response if the Require mediation flow to wait for service response when the flow component is called asynchronously with callback. property is set) | Async with callback [2] |

[1] Although the preferred interaction style of the target is Async, the use of
Sync by the mediation flow component avoids the potential deadlock that might occur if
Async with deferred response is used.

[2] Async with callback is not available in a subflow, error flow, or aggregation block. A
runtime error occurs if this invocation style is required, as determined by the table.

The property Require mediation flow to wait for service response when the flow
component is called asynchronously with callback. does not apply to the new invocation
styles.

## One way operation

The invocation style used for a one way operation has not changed in the current release of
IBM Business Automation Workflow.

| Preferred interaction style of the target   | Invocation style   | Invocation style   | Invocation style   |
|---------------------------------------------|--------------------|--------------------|--------------------|
| Preferred interaction style of the target   | Sync               | Async one way      | As target          |
| Sync                                        | Sync               | Async one way      | Sync               |
| Async or any                                | Sync               | Async one way      | Async one way      |

## Event sequencing

Event sequencing enables IBM Workflow
Server
components to process events from asynchronous invocations, in the order in which they are
delivered. Event order is maintained throughout the entire business integration scenario.

Certain types of components and invocations offer limited support for event sequencing.

- To effectively use event sequencing with a mediation flow component that has asynchronous
invocations, it is recommended that you use the request-response method signature. The event
sequencing runtime interprets a response as a signal that the work is complete and releases the
lock.Note: If you cannot declare a method as a request-response operation, you might need to specify
event sequencing on downstream components, making sure you use the same event sequencing key for all
methods.

Event sequencing is not supported when you are using synchronous invocations to components with
asynchronous invocations.