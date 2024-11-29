<!-- image -->

# Troubleshooting store-and-forward processing

| Problem                                                                                                                                                              | Refer to the following                                                                                                                                          |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| I am having problems setting the store-and-forward qualifier                                                                                                         | Store-and-forward qualifier processing only works on asynchronous interfaces                                                                                    |
| Qualifying runtime exceptions are occurring, but events are not getting stored                                                                                       | Store is not activated by qualifying runtime exceptions                                                                                                         |
| Messages are still being processed even though the Store and Forward widget shows the state is set to Store (Network deployment environment)                         | In a network deployment environment, messages are being processed even though the store-and-forward state is set to Store                                       |
| The Store and Forward widget shows the state is set to Forward, but messages are not being processed by all members of the cluster. (Network deployment environment) | In a network deployment environment, messages are not getting processed by all members of the cluster even though the store-and-forward state is set to Forward |

## Store-and-forward qualifier processing only works on asynchronous interfaces

The store-and-forward qualifier must be specified on an asynchronous interface. The store cannot
be activated if the interface is called synchronously.

- Examine your short-running business process and what import it invokes. For
example, JMS is an asynchronous import. Therefore, it is called asynchronously by a short-running
process. HTTP is a synchronous import. Therefore, it is called synchronously.
- Long-running processes invoke imports based on the preferred interaction style
set on the import's interface. Look at the interaction style set on the import's interface to see
whether it is synchronous or asynchronous.Note: You can find this setting on the interface's detail
tab.
- POJO components invoke components based on the code that is written in the component. Look at
the code written in the component to see whether it is synchronous or asynchronous.

- Store-and-forward qualifier cannot be set on long-running processes.
- Store-and-forward cannot be set on exports (except SCA export).

## Store is not activated by qualifying runtime exceptions

- The exception specification in the store-and-forward qualifier matches the exception that occurs
at run time. If the exception specification does not match, storing does not activate.
- The user code in the path is not catching the exception and wrapping it. Or, it is converting it
into a different exception. The exception received by the store-and-forward function can be viewed
in the exception details for the failed event.
- The destination component for a failed event has a store-and-forward qualifier set on it.
Storing is activated once a failed event is generated. If a failed event is generated for a
component that is upstream from the component that has a store-and-forward qualifier set on it, then
the store-and-forward component is being invoked synchronously and not asynchronously. If a failed
event is generated for a component that is downstream from the store-and-forward qualifier
component, rather than the component with the store-and-forward qualifier set on it, then there is
an asynchronous invocation closer to the failure and the store-and-forward qualifier should be moved
to that component.

## In a network deployment environment, messages are being processed even though the
store-and-forward state is set to Store

Messages might continue to be processed by some members of a cluster, despite the state being set
to Store, if the state is not set to Store for each member of the cluster. To fix this problem,
confirm that the state is set to Store for each member of the cluster in the Store and Forward
widget. If any members of the cluster are set to Forward, change them to Store.

## In a network deployment environment, messages are not getting processed by all members of the
cluster even though the store-and-forward state is set to Forward

Messages might continue to be stored by some members of a cluster, despite the state being set to
Forward, if the store-and-forward state is not set to Forward for each member of the cluster. To fix
this problem, confirm that the state is set to Forward for the module in the Store and Forward
widget. If any members of the cluster are set to Store, change them to Forward.