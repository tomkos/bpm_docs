<!-- image -->

# Use case: recovering data from failed events

The solution consists of multiple modules as recommended through
module best practices.

The first module mediates the request and delegates work to an
Account Creation process.  In the Figure 1 we have implemented
the solution as separate modules where the request is passed between
the mediation module (AccountRouting) and the processing module (AccountCreation)
via an SCA import/export. See the following screen capture for an
illustration of the two modules.

Figure 1. Assembly diagram of account routing process

<!-- image -->

From the assembly diagram shown in Figure 1, you
can begin to see at what locations in the flow that failures might
occur. Any of the invocation points in the assembly diagram can propagate
or involve a transaction.  There are a few areas in the flow where
data will collect as a result of application or system failures.

In general, transaction boundaries are created and managed by the
interaction (synchronous and asynchronous) between components and
import/export bindings and their associated qualifiers.  Business
data  accumulates in specific recovery locations most often due to
transaction failure, deadlock or rollback.

Transaction capabilities within WebSphere® Application
Server help IBM® Business Automation Workflow enlist
transactions with service providers.  These enlisted interactions
are particularly important to understand with respect to import and
export bindings.  Understanding how imports and exports are used within
your specific business cases is important in determining where events
in need of recovery accumulate.

An error handling strategy should define interaction patterns,
transactions used, and import and export usage before developing the
application. The solution architect should identify the preferences
to use, and the guidelines that are then used as the application is
created. For example, the architect needs to understand when to use
synchronous compared to asynchronous calls, when to use BPEL fault
handling and so forth. The architect must know whether or not all
services can participate in transactions, and for those services that
cannot participate, how to handle compensation if problems are encountered.

Additionally, the application shown in the assembly diagram in Figure 1 uses
connectivity groups and module development best practices.  By leveraging
this pattern we now have the ability to stop the inbound flow of new
events by stopping the AccountRouting  module.

The following sections address the location of business data in
the case of failure and recovery.

## Business Flow Manager or Human Task Manager

In
our business case, we use a BPEL process for AccountCreation process.

1. What type of process is being run (short running or long running,
business state machine, human task) ?Short running processes are
known as microflows.
2. Is the process developed properly and using fault handling to
promote data integrity?
3. How are the invocation patterns and unit of work properties configured
to predict and control transaction boundaries?

Knowing the answers to these questions will affect your
recovery strategy for invocations 7 and 8 shown in the assembly diagram,
as highlighted in Figure 2.

Figure 2. Assembly diagram of account routing - invocations
7 and 8

<!-- image -->

Stateful components, such as long-running BPEL processes
and business state machines, involve many database transactions where
process activity changes and state changes are committed to the database.
The work progresses by updating the database and placing a message
on an internal queue that describes what is to be done next.

If there are problems
processing messages that are internal to the Business Flow Manager,
these messages are moved to a Retention Queue. The system attempts
to continue to process messages.  If a subsequent message is successfully
processed, the messages on the retention queue are resubmitted for
processing. If the same message is placed on the retention queue five
times, it is then placed on the hold queue.

Additional information
about viewing the number of messages and replaying messages can be
found in Replaying Messages from the Retention Queue / Hold Queue.

## Failed event manager

The failed event manager
is used to replay events or service invocation requests that are made
asynchronously between most component types.

Failed events
are created if the AccountRouting component makes
an asynchronous call to the SCA Import binding AccountCreationSCAImport and
a ServiceRuntimeException is returned.

Failed
events are not generated in most cases where a long running BPEL process
is the client in the service interaction. This means that the invocation
for 7 and 8 (as shown in Figure 2) will not typically result in a failed event. BPEL
provides fault handlers and other ways to model for failure. For this
reason, if there is a ServiceRuntimeException (SRE)
failure calling JDBCOutboundInterface, the SRE is returned
to the BPEL for processing.  The error handling strategy for the project
should define how runtime exceptions are consistently handled in BPEL.

However,
failed events are created for asynchronous response message for the
BPEL client if these messages cannot be delivered to the process instance
due to an infrastructure failure.

When mediation Service Invoke
or Callout primitives are making an asynchronous invocation, retry
behavior is defined by the primitive and overrides any asynchronous
behavior from the destination. Failed events go to the failed event
manager if the fail terminal on the primitive is not wired.

The
following diagram illustrates how the failed event manager component
works. Descriptions of the processing associated with each numbered
step are provided in Figure 3.

Figure 3. Failed event manager processing

<!-- image -->

## Failed event manager processing

1. The source component makes a call using an asynchronous invocation
pattern
2. The SCA MDB picks the message up off the SCA destination
3. The SCA MDB makes the call to the correct target component
4. The target component throws a ServiceRuntimeException
5. The SCA MDB transaction rolls back to the SCA destination
6. The exception information is stored to the failed event manager
database with a status of not confirmed
7. The invocation is retried by the SIBus n number of times The
initial retry count value for new modules is 0 - one original and
0 retries. Existing modules from previous releases keep the existing
retry count value of 4. You can change the retry count value by setting
the asynchronous retry count for the modules at design time. Also,
administrators can change it at run time using the configSCAAsyncRetryCount command.
See Controlling system retries.
8. After the number of retries reaches the specified limit, the message
is moved to the failed event manager destination.
9. The failed event manager database picks up the message
10. The failed event manager database updates the failed event in
the database and the status is set to failed.

## When are failed events created?

As stated,
failed events are neither created for synchronous invocations nor
typically for two-way business process interactions.

Failed
events are generally created when clients use an asynchronous invocation
pattern and a ServiceRuntimeException is thrown by the service provider.

If
everything is done synchronously and in the same transaction, data
is not collected anywhere. Instead it is all rolled back to the client
that made the call.  Where ever a commit is occurs, data collects.
If the calls are all synchronous, but there are multiple commits,
then these commits become an issue.

In general, you should use
asynchronous processing calls or long running BPEL processes if multiple
transactions are needed. So each ASYNC call is a chance for data to
collect. Long running BPEL processes are a collection point.

| Invocation Pattern               | Failed Event Created Y/N?   | Notes                                                                                                                    |
|----------------------------------|-----------------------------|--------------------------------------------------------------------------------------------------------------------------|
| Synchronous                      | No                          | Failed events are not created for service business exceptions or when using a synchronous pattern                        |
| Asynchronous - One Way           | No                          | By definition, one-way invocations cannot declare faults, meaning, it is impossible to throw a ServiceBusinessException. |
| Asynchronous - Deferred Response | No                          | Failed events are not created for service business exceptions                                                            |
| Asynchronous - Callback          | No                          | Failed events are not created for service business exceptions                                                            |

| Invocation Pattern               | Failed Event Created Y/N?   | Notes                                                                                                                                                                                     |
|----------------------------------|-----------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Synchronous                      | No                          | Failed events are not created for service runtime exceptions or when using a synchronous pattern.                                                                                         |
| Asynchronous - One Way           | Yes                         |                                                                                                                                                                                           |
| Asynchronous - Deferred Response | Yes                         |                                                                                                                                                                                           |
| Asynchronous - Callback          | Yes                         |                                                                                                                                                                                           |
| BPEL - Two Way                   | No                          | Failed events are not created when the source component is a business process.Note: For an asynchronous call, if the response cannot be returned to BPEL, then a failed event is created. |
| BPEL - One Way                   | Yes                         |                                                                                                                                                                                           |

Additional
information about viewing and resubmitting failed events can be found
in section Resubmitting failed events.

## Service integration bus destinations

- Asynchronous requests for processing
- Asynchronous replies to requests
- Asynchronous messages that failed deserialization or function
selector resolutionNote: Asynchronous replies can be valid Business
Objects or faults returned as a result of a request.

## SCA module destination

Again, refer back
to our business case.

- sca/AccountRouting
- sca/AccountCreation

These destinations are created when the module is deployed
to an application server or a cluster.

There are rare opportunities
for messages to accumulate in these destinations.  The accumulation
of messages in these locations is a strong indication that there maybe
a performance problem or an application defect.  Investigate immediately.
  It is important to monitor the depth of the module destinations
(with your chosen IT monitoring solution), because a back up of messages
could lead to a system outage or a prolonged recycle time.

We
call these SCA module destinations because the generated name is the
same as the module name with the additional sca/.
These destinations are pivotal in the functioning of SCA asynchronous
invocations (brokering requests and responses). There are a varying
number of additional destinations that are generated during application
installation on the SCA.SYSTEM bus, but for the purpose of the discussion
we'll be addressing the importance of the SCA module destination.

## Service integration bus retry

As we learned earlier, the failed event manager has a built-in retry mechanism with the SCA
message driven bean (MDB).

Referring to our business
case, there are a number of service integration bus destinations created
by SCA to support asynchronous communication.

As we have learned,
one of these destinations is called sca/AccountRouting.
You can adjust the number of retries that happen when a ServiceRuntimeException
occurs on an asynchronous service invocation. The number of retries
can be controlled by setting the asynchronous retry count for the
module at design time or by using the configSCAAsyncRetryCount command
at run time. However, you cannot set the value less than 2 in modules
with a BPEL process.  The second delivery is required to return ServiceRuntimeExceptions
back to the BPEL for processing.

For more information about
retry behavior, see Controlling system retries.

## System exception destinations

The failed
event manager is one place where we can look to administer failures.
When dealing with imports and exports that are JMS or EIS based, we
must consider another important location.

Destinations on the SCA.Application bus are configured to route failed messages to the service
integration bus system exception destination for that bus. Thus, if a JMS export picks up a message
from the SCA.Application bus and runs into a rollback situation, the failed message is routed to the
service integration bus system exception destination instead of to the process server recovery
exception destination. This scenario differs from the previous failed event discussion in that a
failure to deserialize a message on the SCA.Application bus will not result in a failed event. There
is a system exception destination on every bus within the solution. These destinations must be
monitored and administered much like the dead letter queue common to MQ infrastructures.

Consider
the following scenario.

<!-- image -->

1. The JMS export successfully parses the message and determines
which operation on the interface to invoke at which point the message
is sent to the SCA runtime for processing.
2. The JMS export fails to recognize the message body as a valid
business object or the JMS export binding deserializes the message
body but is unable to determine the appropriate operation on the interface
to invoke.  At this point the message is placed on the system exception
destination for the bus.

We can have this type of failure when trying to receive
requests from the AccountRoutingJMSExport (1).  This
export is a JMS export and there is a possibility that events can
accumulate on the system exception destination on the SCA.Application.Bus.
 Use the chosen IT monitoring solution to observe the depth of this
destination.

## Failed event manager and service integration bus destinations

```
Node name: MyNode
Server name: server1
Recovery exception destination: WBI.FailedEvent.MyNode.server1
```

When
a system failure occurs, in addition to capturing the failed message
in this exception destination, the IBM Business Automation Workflow recovery
feature also generates a failed event that represents the system error
and stores it into the Recovery database as described in the failed
event manager section of this document.

## Summary

In summary, IBM Business Automation Workflow provides
administrative capabilities and beyond the underlying WebSphere Application Server platform. Proper measures should be made to understand and use
these capabilities along with following the guidance provided in the Planning error prevention
section of Planning error prevention and recovery.

| Administrative Capability               | Bundled With IBM Business Automation Workflow?   | Summary                                                                                                                                                                    |
|-----------------------------------------|--------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Business Process Choreographer Explorer | Yes                                              | Read/Write/Edit/Delete Access. This is the central place to administer business processes and human tasks.                                                                 |
| failed event manager                    | Yes                                              | Read/Edit/Delete Access. This is the central place to administer Service Runtime Exceptions and other forms of infrastructure failures.                                    |
| Service Integration Bus Browser         | Yes                                              | Read/Delete.  Use the Service Integration Bus Browser on the administrative console for browsing and performing day-to-day operational tasks on service integration buses. |