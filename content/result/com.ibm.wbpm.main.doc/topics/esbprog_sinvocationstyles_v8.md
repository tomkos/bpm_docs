<!-- image -->

# Invocation Style property for request-response operations

- As target
- Sync
- Async with deferred response
- Async with callback
- Async (Compatibility) - For more information, see Request-response operation
- Default (Compatibility) - For more information, see Request-response operation

The Async (Compatibility) and Default (Compatibility) invocation style options are compatible
with earlier versions. These options provide a check box for an additional property which influences
invocation style: Require mediation flow to wait for service response when the flow component is
invoked asynchronously with callback. It is recommended that you use the non-compatibility
invocation style options.

## As target

The As target invocation style takes account of the Preferred Interaction
Style that is specified on the target component, or import that is invoked by the
mediation flow.

When the mediation flow component is invoked as Sync, it is not possible to asynchronously return
a response to its caller. As a result, the mediation flow uses the Sync invocation style when it is
invoked Sync, even if the Preferred Interaction Style of the target is set to
Async.

| Property   | How the mediation flow component is called   | Preferred interaction style of the target    | Invocation style    |
|------------|----------------------------------------------|----------------------------------------------|---------------------|
| As target  | Sync                                         |                                              | Sync                |
| As target  | Async one way                                | Sync                                         | Sync                |
| As target  | Async with deferred response                 | Async or any                                 | Async with callback |
| As target  | Async with callback                          | Async or any                                 | Async with callback |

## Sync

The Callout node or Service Invoke mediation primitive invokes the service using the synchronous
invocation style (Synchronous invocation).

## Async with callback

## Async with deferred response

The Callout node or Service Invoke mediation primitive invokes the service using the asynchronous
invocation style. It can continue and complete processing of the mediation flow. At a later time,
the service requester calls the service provider for a response.