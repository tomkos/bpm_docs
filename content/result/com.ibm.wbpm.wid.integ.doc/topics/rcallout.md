<!-- image -->

# Callout

<!-- image -->

## Use dynamic endpoint if set in the message header

Dynamic
routing is enabled by default. This means that the callout will invoke
the endpoint that is set in the target element of the SMOHeader in
the message. If no endpoint exists in this location, the callout will
invoke the endpoint defined in the import's binding. For more information,
see Calling a service by selecting an endpoint dynamically at run time

## Invocation style

Determines whether the
service is invoked synchronously or asynchronously. When the synchronous
style is used, the service is performed under the same processing
thread as the mediation flow. When the asynchronous style is used,
a new processing thread is used when invoking the service. The asynchronous
style allows the mediation flow to continue before a response is received
from the service. The invocation style can affect the transactional
scope that applies to the service invocation, and whether a timeout
might occur if the service fails to respond.

Request-response
operations

- Sync
- Async with deferred response
- Async with callback
- As target
- Async (Compatibility)
- Default (Compatibility)

If set to Sync, the service invocation
is performed synchronously. This setting can allow the service to
be included in the transaction scope of the mediation flow when the
service or binding supports this function.

Setting the property
to Async with deferred response means that
the service invocation is performed asynchronously, where the service
requester calls an operation on the service provider, and then continues
processing. At a later time, the service requester calls the service
provider for a response. The service is outside the scope of the mediation
flow transaction. The Async with deferred response setting
can also allow an Async timeout timeout to
be set for a deferred response.

Setting the property to Async
with callback means that the service invocation is performed
asynchronously, where the service requester calls an operation on
the service provider and specifies a callback handler. The service
requester continues processing. When the response is available, the
SCA runtime returns the response to the requester by calling the callback
handler. The service is outside the scope of the mediation flow transaction.

| Property                     | Mediation flow component inbound request                         | Preferred interaction style of the target    | Invocation style used for Callout   |
|------------------------------|------------------------------------------------------------------|----------------------------------------------|-------------------------------------|
| Sync                         |                                                                  |                                              | Sync                                |
| Async with deferred response |                                                                  |                                              | Async with deferred response        |
| Async with callback          |                                                                  |                                              | Async with callback                 |
| As target                    | Sync                                                             |                                              | Sync                                |
| As target                    | Async one way, Async with deferred response, Async with callback | SYNC                                         | Sync                                |
| As target                    | Async one way, Async with deferred response, Async with callback | ASYNC or ANY                                 | Async with callback                 |

Compatibility options for request-response operations

| Property                | Mediation flow component inbound request             | Preferred interaction style of the target    | Force Sync (More information)   | Invocation style used for Callout   |
|-------------------------|------------------------------------------------------|----------------------------------------------|---------------------------------|-------------------------------------|
| Async (Compatibility)   | Sync                                                 |                                              |                                 | Sync                                |
| Async (Compatibility)   | Async with deferred response or Async one way        |                                              |                                 | Async with deferred response        |
| Async (Compatibility)   | Async with callback                                  |                                              | True                            | Async with deferred response        |
| Async (Compatibility)   | Async with callback                                  |                                              | False                           | Async with callback                 |
| Default (Compatibility) | Sync, Async with deferred response  or Async one way | SYNC or ANY                                  |                                 | Sync                                |
| Default (Compatibility) | Sync, Async with deferred response  or Async one way | ASYNC                                        |                                 | Async with deferred response        |
| Default (Compatibility) | Async with callback                                  | SYNC or ANY                                  |                                 | Sync                                |
| Default (Compatibility) | Async with callback                                  | ASYNC                                        | True                            | Async with deferred response        |
| Default (Compatibility) | Async with callback                                  | ASYNC                                        | False                           | Async with callback                 |

One way operations

- Sync
- Async one way
- As target

If set to Sync, the service invocation
is performed synchronously. This setting can allow the service to
be included in the transaction scope of the mediation flow when the
service or binding supports this function.

For one way operations,
the invocation style Async one way is the same
as the Async style in releases before version
8.0.

Setting the property to As target means
that the invocation style is determined by the preferred interaction
style of the target, or the invocation style used by the import that
is invoked by the mediation flow. As target is
the default invocation style.

| Property      | Mediation flow component inbound request                                 | Preferred interaction style of the target    | Invocation style used for Callout   |
|---------------|--------------------------------------------------------------------------|----------------------------------------------|-------------------------------------|
| Sync          |                                                                          |                                              | Sync                                |
| Async one way |                                                                          |                                              | Async one way                       |
| As target     | Sync or Async one way, Async with deferred response, Async with callback | SYNC                                         | Sync                                |
| As target     | Sync or Async one way, Async with deferred response, Async with callback | ASYNC or ANY                                 | Async one way                       |

## Require mediation flow to wait for
service response when the flow component is invoked asynchronously
with callback

This option is only
available with the Async (Compatibility) and Default
(Compatibility) invocation style options, which are provided
are for compatibility with earlier versions before to version 8.0

## Retry

The callout can be set to retry service
invocations depending on the type of fault received.

Retry
On

To enable retry, you must set the value of the Retry
On property to: Any fault, Unmodeled fault or Modeled fault.

Modeled
faults are those that are explicitly listed in a WSDL file, any other
fault is an unmodeled fault. This property is only applicable to request-response
operations.

Retry Count

How many times a service
call should be retried before an output terminal is fired. The output
terminal that is fired can be of the following types: modeled fault,
timeout or fail. The value can be zero or a positive integer.

Retry
Delay

The delay (in seconds) between retry attempts. The
value can be zero or a positive integer.

Try Alternate
Endpoints

Determines if any alternate endpoints in the
SMO should be used on retries. Set to true, (select the check box),
to try alternate endpoints.  This functionality is only available
if the Use Dynamic Endpoint is also specified. If any fault is returned
by the initial service request, and the retry count is greater than
zero, the first endpoint from the alternate endpoint list is used
for the retry. If the retry returns a fault, and the next retry would
not exceed the retry count, the next alternate endpoint is used. After
the last endpoint in the alternate endpoints list is used, the initial
endpoint is used again.

For example, suppose that the first
endpoint is ServiceA, and the alternate endpoints are ServiceB and
ServiceC. If the retry count is 5, the sequence of service calls is
as follows: ServiceA, ServiceB, ServiceC, ServiceA, ServiceB, ServiceC.

| Property                                                                                                            | Description                                                                                                   | Possible Values                                                                                                                                                                                                                                                                                                                                                   |
|---------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Reference Name                                                                                                      | The reference of the service that is called by the callout                                                    |                                                                                                                                                                                                                                                                                                                                                                   |
| Operation Name                                                                                                      | The name of the operation called by the callout                                                               |                                                                                                                                                                                                                                                                                                                                                                   |
| Use dynamic endpoint if set in the message header                                                                   | Determines if the TargetAddress header should be used to override the endpoint if present.                    | If set to True and if the TargetAddress header is populated, message is forwarded. Otherwise the message proceeds normally. Default: true                                                                                                                                                                                                                         |
| Async Timeout                                                                                                       | Specifies time to wait for a responses when performing an asynchronous deferred response invocation.          | -1 - infinite wait 0 - expects an immediate response 1+ - waits specified number of seconds for a response  If timeout occurs, the fail terminal is fired. This is treated as an unmodeled fault with regard to retry conditions. Default: 5 Note:  Async Timeout is only effective when the invocation style used for a Callout is Async with deferred response. |
| Require mediation flow to wait for service response when the flow component is invoked asynchronously with callback | Determines if the call should be forced to act in a synchronous manner.                                       | Boolean: true or false  Default: false  Note: This option is only available with Async (Compatibility) and Default (Compatibility) invocation styles.                                                                                                                                                                                                             |
| Invocation Style                                                                                                    | Determines whether the service is invoked synchronously or asynchronously.                                    | Sync, Async (deferred), Async (callback), Async one way, Default (Compatibility), Async (Compatibility), As target Default: As target                                                                                                                                                                                                                             |
| Retry On                                                                                                            | Determines whether and how fault responses affect retry.                                                      | Never - operation call is never retried, no matter the type of fault Any fault - operation call is retried on both modeled and unmodeled faults Modeled fault - operation call is retried only when a modeled fault is received Unmodeled fault - operation call is retried only when an unmodeled fault is received   Default: Never                             |
| Retry Count                                                                                                         | Number of retry attempts following initial failure before a modeled fault, timeout or fail terminal is fired. | The number must be an integer greater than or equal to 0. Default: 0                                                                                                                                                                                                                                                                                              |
| Retry Delay                                                                                                         | Sets the delay between retry attempts, in seconds.                                                            | Must be an integer greater than or equal to 0. If 0, there will be no delay between attempts meaning they will run as fast as the server can handle them.  Default: 0                                                                                                                                                                                             |
| Try Alternate Endpoints                                                                                             | Determines if any alternate endpoints should be used on retries.                                              | True - alternate endpoints found in the SMO headers will be used   Otherwise they are not tried    This function is only available if 'Use dynamic endpoint' is also True. Default: True                                                                                                                                                                          |