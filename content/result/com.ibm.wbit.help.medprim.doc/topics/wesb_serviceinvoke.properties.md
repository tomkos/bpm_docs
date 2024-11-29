# Service Invoke mediation primitive properties

## Reference name referenceName

The name of the service reference to be
called. The reference name is associated with a WSDL interface. Initially, the reference name is set
through an IBM Integration
Designer
window, and cannot be changed afterward. You have to create a new Service Invoke mediation primitive
to change the reference name.

| Field detail   | Value and notes   |
|----------------|-------------------|
| Required       | Yes               |
| Valid values   | StringNote:       |

## Operation name operationName

The name of the service operation to be
called. The operation name is associated with a WSDL operation. Initially, the Operation
Name is set through an IBM Integration
Designer window; and cannot be
changed afterward. You have to create a new Service Invoke mediation primitive to change the
operation name.

| Field detail   | Value and notes   |
|----------------|-------------------|
| Required       | Yes               |
| Valid values   | StringNote:       |

## Use dynamic endpoint if set in the
message header useDynamicEndpoint

Determines whether the SMO header field
Target, if present, should be used to override the service endpoint specified by
the reference operation. You can use the Endpoint Lookup mediation primitive to set the
Target field, or you can set the field yourself.

| Field detail   | Value and notes   |
|----------------|-------------------|
| Required       | Yes               |
| Valid values   | BooleanNote:      |
| Default        | true              |

## Async timeout (seconds) asyncTimeout

The time to wait for a response, when a call is
asynchronous with a deferred response. The Async Timeout property is not used for
calls that are asynchronous with callback.

| Field detail   | Value and notes                                                                                                                                                                                                                                                    |
|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Required       | Yes                                                                                                                                                                                                                                                                |
| Valid values   | IntegerNote: If the Async Timeout is 0, there is no wait and the response is immediate. If the Async Timeout is -1, the wait is indefinite. When a timeout occurs the timeout terminal is fired. A timeout is treated as an unmodeled fault, with regard to retry. |
| Default        | 5                                                                                                                                                                                                                                                                  |

## Require mediation flow to wait for
service response when the flow component is invoked asynchronously
with callback. forceSync

This property is only effective for
request-response operations, where the invocation style property is either Async (Compatibility) or
Default (Compatibility). Set the property to true,
(select the check box), to force a service call to act in a synchronous
manner. If true, an asynchronous call causes a deferred response, rather than
a callback. Set this property to true if the whole mediation flow is to run
in a single transaction (in this case, the reference qualifier Asynchronous must also be set
to Call, since the default qualifier setting Commit would result in a deadlock.) If
you set this property to false and the mediation primitive is involved in a
FanOut/FanIn operation or is contained in a subflow, the runtime environment will override
your setting and force the service call to act in a synchronous manner.

| Field detail   | Value and notes   |
|----------------|-------------------|
| Required       | Yes               |
| Valid values   | BooleanNote:      |
| Default        | false             |

## Invocation style invocationStyle

When the synchronous style is used, the
service is performed under the same processing thread as the mediation flow. When the asynchronous
style is used, a new processing thread is used when invoking the service. The asynchronous style
allows the mediation flow to continue before a response is received from the service. The invocation
style can affect the transactional scope that applies to the service invocation, and whether a
timeout might occur if the service fails to respond. The following tables can be used to identify
which invocation style to use.

| Request-response             |
|------------------------------|
| As target                    |
| Sync                         |
| Async with deferred response |
| Async with callback          |
| Async (Compatibility)        |
| Default (Compatibility)      |

| One way       |
|---------------|
| As target     |
| Sync          |
| Async one way |

| Property                     | How the mediation flow component is called   | Preferred interaction style of the target   | Invocation Style             |
|------------------------------|----------------------------------------------|---------------------------------------------|------------------------------|
| As target                    | Sync                                         |                                             | Sync                         |
| As target                    | Async one way                                | Sync                                        | Sync                         |
| As target                    | Async with deferred response                 | Async or any                                | Async with callback          |
| As target                    | Async With Callback                          | Async or any                                | Async with callback          |
| Sync                         |                                              |                                             | Sync                         |
| Async with deferred response |                                              |                                             | Async with deferred response |
| Async with callback          |                                              |                                             | Async with callback          |

| Property      | How the mediation flow component is called   | Preferred interaction style of the target   | Invocation Style   |
|---------------|----------------------------------------------|---------------------------------------------|--------------------|
| As target     | Sync                                         | Sync                                        | Sync               |
| As target     | Async one way                                | Async or any                                | Async one way      |
| As target     | Async with deferred response                 | Async or any                                | Async one way      |
| As target     | Async with callback                          | Async or any                                | Async one way      |
| Sync          |                                              |                                             | Sync               |
| Async one way |                                              |                                             | Async one way      |

| Property                | How the mediation flow component is called          | Preferred interaction style of the target    | Require mediation flow to wait for service response when the flow component is invoked asynchronously with callback.   | Invocation Style             |
|-------------------------|-----------------------------------------------------|----------------------------------------------|------------------------------------------------------------------------------------------------------------------------|------------------------------|
| Async (Compatibility)   | Sync                                                |                                              |                                                                                                                        | Sync                         |
| Async (Compatibility)   | Async with deferred response or async one way       |                                              |                                                                                                                        | Async with deferred response |
| Async (Compatibility)   | Async with callback                                 |                                              | True                                                                                                                   | Async with deferred response |
| Async (Compatibility)   | Async with callback                                 |                                              | False                                                                                                                  | Async with callback          |
| Default (Compatibility) | Sync, async with deferred response or async one way | Sync or Any                                  |                                                                                                                        | Sync                         |
| Default (Compatibility) | Sync, async with deferred response or async one way | Async                                        |                                                                                                                        | Async with deferred response |
| Default (Compatibility) | Async with callback                                 | Sync                                         |                                                                                                                        | Sync                         |
| Default (Compatibility) | Async with callback                                 | Async or Any                                 | True                                                                                                                   | Async with deferred response |
| Default (Compatibility) | Async with callback                                 | Async or Any                                 | False                                                                                                                  | Async with callback          |

| Field detail   | Value and notes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Required       | Yes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Valid values   | Default 0 Setting the property to default means that the invocation style is determined by other factors such as the preferred interaction style of the target, or the invocation style used by the mediation module's export.  Sync 1 If set to sync, the service invocation is performed synchronously. This setting can allow the service to be included in the transaction scope of the mediation flow when the service or binding supports this function. Async 2 Setting the property to async means that the service invocation is performed asynchronously, and the service is outside the scope of the mediation flow transaction. For a one way operation, a reference qualifier can be used to control whether the asynchronous service request is sent immediately, or when the mediation flow transaction commits. The async setting can also allow an async timeout to be set for a deferred response.  Note: |
| Default        | Default                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |

## Parameter mappings parameterMappings

The Parameter
mappings table is enabled only when working in Message Enrichment mode. You can use the
Parameter mappings table to specify XPath expressions that identify elements
to be transformed within the input message, and also to specify XPath expressions that define where
the elements of the response message must be placed.

| Field detail                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Value and notes   |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|
| Parameter parameterType A preconfigured read-only value identifying whether the element to be transformed or updated forms part of the input, output, or fault message. The valid type is String. Name name A preconfigured read-only name for the input, output, or fault parameter type. The valid type is String. Type type The type of the element value in the message. The valid type is String. Value value Specifies an XPath 1.0 expression that identifies the message element to be transformed or updated. Use the XPath Expression Builder to build a custom XPath expression. |                   |

## Propagate request headers to service
being invoked propagateRequestHeader

The Propagate request
headers to service being invoked check box is enabled only when working in Message
Enrichment mode. Select this check box if you want the request message, which is sent to the
service, to be populated with the header of the input message that is received at the
in terminal. When this check box is clear, the header is excluded from the
request message.

| Field detail   | Value and notes   |
|----------------|-------------------|
| Required       | Yes               |
| Valid values   | BooleanNote:      |
| Default        | false             |

## Propagate response headers from service
being invoked propagateResponseHeader

The Propagate response
headers from service being invoked check box is enabled only when working in Message
Enrichment mode. Select this check box if you want the output message to be populated with the
response message header from the service being invoked. When this check box is clear, the header of
the input message that was passed into the mediation primitive is used.

| Field detail   | Value and notes   |
|----------------|-------------------|
| Required       | Yes               |
| Valid values   | BooleanNote:      |
| Default        | false             |

## enrichmentMode

Use this property to enable Message
Enrichment mode, whereby a section of the input message, which is received at the
in terminal of the Service Invoke mediation primitive, is used for the
service invocation.

| Field detail   | Value and notes   |
|----------------|-------------------|
| Required       | Yes               |
| Valid values   | BooleanNote:      |
| Default        | false             |

## Retry on retryOn

Determines whether, and how, fault responses cause a
retry. This property is applicable only to request-response operations.

| Field detail   | Value and notes                                                                                                                                                                                                                                                                               |
|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Required       | Yes                                                                                                                                                                                                                                                                                           |
| Valid values   | Never 0  Any fault 1  Modeled fault 2  Unmodeled fault 3   Note: To enable retry, you must set the value of the Retry On property to: Any fault, Unmodeled fault or Modeled fault. Modeled faults are those that are explicitly listed in a WSDL file; any other fault is an unmodeled fault. |
| Default        | Never                                                                                                                                                                                                                                                                                         |

## Retry count retryCount

How many times a service call should be retried
before an output terminal is fired. The output terminal that is fired can be of the following types:
modeled fault, timeout or fail.

| Field detail   | Value and notes                                           |
|----------------|-----------------------------------------------------------|
| Required       | Yes                                                       |
| Valid values   | IntegerNote: The value can be zero or a positive integer. |
| Default        | 0                                                         |

## Retry delay (seconds) retryDelay

The delay (in seconds) between retry attempts.

| Field detail   | Value and notes                                           |
|----------------|-----------------------------------------------------------|
| Required       | Yes                                                       |
| Valid values   | IntegerNote: The value can be zero or a positive integer. |
| Default        | 0                                                         |

## Try alternate endpoints tryAlternateEndpoints

Determines if any alternate endpoints
in the SMO should be used on retries. Set to true,
(select the check box), to try alternate endpoints.

This functionality is available only if the Use Dynamic Endpoint is also
specified. If any fault is returned by the initial service request, and the retry count is greater
than zero, the first endpoint from the alternate endpoint list is used for the retry. If the retry
returns a fault, and the next retry would not exceed the retry count, the next alternate endpoint is
used. After the last endpoint in the alternate endpoints list is used, the initial endpoint is used
again.

For example, suppose that the first endpoint is ServiceA, and the alternate
endpoints are ServiceB and ServiceC. If the retry count is
5, the sequence of service calls is as follows: ServiceA,
ServiceB, ServiceC, ServiceA,
ServiceB, ServiceC.

| Field detail   | Value and notes   |
|----------------|-------------------|
| Required       | Yes               |
| Valid values   | BooleanNote:      |
| Default        | true              |

## Considerations

- Setting the Async timeout property to -1, (an
indefinite wait), can have a performance impact. If the service call
is asynchronous with a deferred response, server resources are consumed
until a reply is received.
- When using parallel processing, by making service calls asynchronously
with a callback, you should consider the impact on event sequencing.
- The Invocation style property overrides other default properties
that have been specified throughout the module.

## Sample XML code

```
<node name="ServiceInvoke" type="ServiceInvoke">
  <property name="referenceName" value="myInterfacePartner"/>
  <property name="operationName" value="emit"/>
  <inputTerminal type="myInterface:myRequestMsg"/>
  <outputTerminal name="timeout" type="myInterface:myRequestMsg">
    <wire targetNode="MessageLogger1"/>
  </outputTerminal>
  <failTerminal/>
</node>
```