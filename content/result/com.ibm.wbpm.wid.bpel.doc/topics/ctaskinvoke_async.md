<!-- image -->

# Scenario: stand-alone invocation tasks that support the asynchronous
invocations of services

This scenario is applicable to Human Task Manager API clients,
for example, Business Process Choreographer Explorer, that make use
only of asynchronous invocations. It avoids the need for assessing
the execution duration of the service associated with the task when
you model the task.

## Task component settings

| Qualifier type: attribute type                 | Value               |
|------------------------------------------------|---------------------|
| Reference attribute: Multiplicity              | 1:1 (mandatory)     |
| Reference qualifier: DeliverAsyncAt            | commit (mandatory)  |
| Implementation qualifier*: Transaction         | global (mandatory)  |
| Reference qualifier**: SuspendTransaction      | Not applicable      |
| Implementation qualifier***: ActivitySession   | true (mandatory)    |
| Reference qualifier***: SuspendActivitySession | false (default)     |
| Reference qualifier: Reliability               | assured (mandatory) |
| Reference qualifier: RequestExpiration         | any                 |
| Reference qualifier: ResponseExpiration        | any                 |

- *: use global if you use transactions
settings, and local if you use activity session settings.
- **: if the transaction is set to global,
only the transaction settings are used
- ***: if the transaction is set to local,
only the settings for the activity sessions are used

## Service component settings

The
service component can take the following settings. If you use IBM Integration
Designer to
define the task component, valid values for the attribute type are
generated automatically.

| Qualifier type: attribute type                 | Value                   |
|------------------------------------------------|-------------------------|
| Interface attribute: PreferredInteractionStyle | Ignored                 |
| Implementation qualifier*: Transaction         | local (default)  global |
| Interface qualifier**: JoinTransaction         | false (default)  true   |
| Implementation qualifier***: ActivitySession   | any (default)           |
| Interface qualifier***: JoinActivitySession    | false (default)         |

- *: use global if you use transactions
settings, and local if you use activity session settings.
- **: if the transaction is set to global,
only the transaction settings are used
- ***: if the transaction is set to local,
only the settings for the activity sessions are used

- The Transaction qualifier is set to local and
the JoinTransaction is set to false.
With these settings, the task and service invocation run in separate
transactions.
- The Transaction qualifier is set to global and
the JoinTransaction is set to false.
With these settings, the task and service invocation run in separate
transactions.
- The Transaction qualifier is set to global and
the JoinTransaction is set to true.
With these settings, the task and service invocation run in the same
transaction.

## Transactional and fault behavior

| Operation type             | When the SCA runtime exception occurs                                   | Behavior of tasks and services                                                                                                                                                                                                    |
|----------------------------|-------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| One-way operation          | During service invocation but before the start of the service execution | The task receives an SCA runtime exception. The Human Task Manager API method throws a CoreOTaskServiceRuntimeExceptionReceivedException exception. The task transaction is rolled back and the task stays in the inactive state. |
| One-way operation          | During service execution                                                | The invocation task is not notified. The task moves to the finished state. A failed event is generated that can be handled by using the failed event manager.                                                                     |
| Request-response operation | During service invocation but before the start of the service execution | The task receives an SCA runtime exception. The Human Task Manager API method throws a CoreOTaskServiceRuntimeExceptionReceivedException exception. The task transaction is rolled back and the task stays in the inactive state. |
| Request-response operation | During service execution                                                | The task is notified of the SCA runtime exception and stores it in the task context in the database. If a reply handler is available, it is used to notify the client. The task is put into the failed state.                     |

The operation definition can include one or more fault
messages that can be thrown by the service component during execution.

- The fault message is stored in the database in the context of
the task
- The task is put into the failed state
- If the task was invoked synchronously and a reply handler was
specified, the reply handler is invoked to return the fault occurrence
to the client
- If the task was invoked asynchronously, the fault message is returned
to the client as a FaultReplyException exception

Fault handling does not impact transactional behavior.
The transactions are not rolled back.