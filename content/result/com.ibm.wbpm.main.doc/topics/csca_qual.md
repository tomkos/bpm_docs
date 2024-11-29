<!-- image -->

# Qualifiers

There are several different categories of qualifiers available
in SCA. These categories of qualifiers are transaction, activity session,
security, and asynchronous reliability.

| Type                  | Qualifier              | Scope                         | Description                                                                                                                                                                                                                                                                                                                    |
|-----------------------|------------------------|-------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Transaction           | transaction            | Implementation                | global - A global transaction must be present to run the component local - A global transaction must not exist to run the component  any - Component is unaffected by transactional state local application - Component processing occurs within a WebSphere® local transaction containment that is managed by the application |
| Transaction           | joinTransaction        | Interface                     | true - Hosting container joins client transaction false (default) - Hosting container does not join client transaction                                                                                                                                                                                                         |
| Transaction           | suspendTransaction     | Reference                     | true - Synchronous invocations of target component do not run within client global transaction. false - Synchronous invocations of target component run within client global transaction                                                                                                                                       |
| Transaction           | deliverAsyncAt         | Reference                     | call - Asynchronous invocations of a target service occur immediately commit - Asynchronous invocations of a target service occur as part of a global transaction                                                                                                                                                              |
| Asynchronous Response | reliability            | Reference                     | Specifies the quality of service level for asynchronous message delivery. Reliability can be one of the following values: bestEffort or assured                                                                                                                                                                                |
| Asynchronous Response | requestExpiration      | Reference                     | Specifies the length of time (milliseconds) after which an asynchronous request is to be discarded if not delivered                                                                                                                                                                                                            |
| Asynchronous Response | responseExpiration     | Reference                     | Specifies the duration (milliseconds) between the time a request is sent and the time a response or callback is received                                                                                                                                                                                                       |
| Security              | securityIdentity       | Implementation                | The permission specifies a logical name for the identity under which the implementation executes at run time.                                                                                                                                                                                                                  |
| Security              | securityPermission     | Interfaces, Interface, Method | The caller identity must have the role specified from this qualifier in order to have permission to run the interface or method                                                                                                                                                                                                |
| Activity Session      | activitySession        | Implementation                | true - There must be an ActivitySession established in order to run this component false - The component runs under no Activity Session  any - The component does not depend on the presence or absence of an ActivitySession                                                                                                  |
| Activity Session      | joinActivitySession    | Interface                     | true - Hosting container joins client ActivitySession false - Hosting container does not join client ActivitySession                                                                                                                                                                                                           |
| Activity Session      | suspendActivitySession | Reference                     | true - Methods on target component does NOT run as part of any client ActivitySession false - Methods on target component run as part of any client ActivitySession                                                                                                                                                            |

## Transaction qualifiers

## Asynchronous response qualifiers

## Security qualifiers

For both the securityPermission and the securityIndentity,
the underlying implementation for these qualifiers is based on existing Java™ EE concepts.

## Activity session qualifiers