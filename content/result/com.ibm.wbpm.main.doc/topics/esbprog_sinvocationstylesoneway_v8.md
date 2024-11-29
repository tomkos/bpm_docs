<!-- image -->

# Invocation Style property for one way operations

- As target
- Sync
- Async one way

## As target

The As target invocation style takes account of the Preferred Interaction
Style that is specified on the target component, or import that is invoked by the
mediation flow.

When the mediation flow component is invoked as Sync, it is not possible to asynchronously return
a response to its caller. As a result, the mediation flow uses Sync invocation style when it is
invoked Sync, even if the Preferred Interaction Style of the target is set to
Async.

| Property   | How the mediation flow component is called   | Preferred interaction style of the target    | Invocation style   |
|------------|----------------------------------------------|----------------------------------------------|--------------------|
| As target  | Sync                                         | Sync                                         | Sync               |
| As target  | Async one way                                | Async or Any                                 | Async one way      |
| As target  | Async with deferred response                 | Async or Any                                 | Async one way      |
| As target  | Async with callback                          | Async or Any                                 | Async one way      |

## Sync

The Callout node or Service Invoke mediation primitive invokes the service using the synchronous
invocation style (Synchronous invocation).

## Async one way

The Callout node or Service Invoke mediation primitive invokes the service using the asynchronous
invocation style. The processing by the invoked service is separate from further processing by the
mediation flow (Asynchronous invocation).

## Compatibility

The invocation style used for a one-way operation is unchanged in the current release. For more
information, see One way operation.