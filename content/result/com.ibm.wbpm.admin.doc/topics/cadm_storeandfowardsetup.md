<!-- image -->

# Store-and-forward feature set up

The most common application of the store-and-forward qualifier is to detect when a service is
unavailable, but it could be used to detect other problems such as not authorized exceptions by
defining different runtime exceptions for the qualifier.

Store-and-forward asynchronous request processing can be specified on the interfaces of all
import bindings.

- When setting up the store-and-forward qualifier on a component or import, keep the following
tasks in mind:
- You configure the runtime exceptions.By default, the runtime exception is the
ServiceUnavailableException. Note: When this exception is received, the store-and-forward
functionality activates and IBM Business Automation Workflow begins
storing events for future processing. If any other exception except the specified exception is
received, the store-and-forward function will not be activated and events are not stored for future
processing.

<!-- image -->

| Qualifier settings                                                                                                                                                                                                                                | Store-and-forward behavior                                                                                                                                                                        |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| If the qualifier is set on the first operation and the failed event is generated by the invocation of the second operation                                                                                                                        | store-and-forward feature is not activated                                                                                                                                                        |
| If the qualifier is set on the first operation and the first interface and a failed event is generated by the invocation of the second operation                                                                                                  | Only the qualifier and properties specified only the first interface take effect. The qualifier and properties specified on the first operation do not take effect.                               |
| If the qualifier is set on the second operation and a failed event is generated by the invocation of the second operation, but the headers in the event are incorrect and the information for the second operation cannot be found in the headers | store-and-forward feature is not activated and a warning is logged                                                                                                                                |
| If the qualifier is set on the InterfaceSet (for all interfaces)                                                                                                                                                                                  | The qualifier on the interfaceSet takes effect even if the headers in the failed event are not correct                                                                                            |
| If the qualifier is set on the first interface and the first operation and a failed event is generated by the invocation of the first operation                                                                                                   | The qualifier and properties for both the first operation and the first interface take effect. When multiple qualifier properties take effect, then it is an OR operation between the properties. |