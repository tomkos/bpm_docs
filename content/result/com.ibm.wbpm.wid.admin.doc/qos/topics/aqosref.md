<!-- image -->

# Quality of service qualifier reference

- Interfaces
- References
- Implementations

The system generates qualifiers that promote the propagation of
transactions and reliable asynchronous message delivery where possible.
You can change these preset qualifiers in the assembly editor. In
some cases, the implementation requires that some qualifiers are set
a certain way. In such cases, the system either blocks you from making
the change or generates an error message. For additional information
on qualifiers, see Using Quality of Service qualifiers.

Some implementations determine how qualifiers must be set. In these
situations, the system generates the qualifiers for you. If you change
the values of those generated qualifiers, you risk creating validation
errors. If you are working with Java™ components,
you need to set the qualifiers yourself.

Here are the qualifiers that you can set in IBM® Integration
Designer.
Click the qualifier name to see details.

| Qualifier                                                | Set on ...     | Description                                                                                                                                                 |
|----------------------------------------------------------|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Activity session qualifier                               | Implementation | Determines if the component's processing will be run under an activity session, an alternative unit-of-work scope to a transaction.                         |
| Asynchronous invocation qualifier                        | Reference      | Determines if asynchronous invocations should occur as part of a client transaction.                                                                        |
| Asynchronous reliability qualifiers                      | Reference      | Three qualifiers (reliability, request expiration, and response expiration) that you can use to determine the reliability of asynchronous message delivery. |
| Qualifier: Business object (BO) instance data validation | Interface      | Confirms that the data passed in to an operation (usually a business object instance) matches the XSD types of the operation's inputs.                      |
| Event sequencing qualifier                               | Interface      | Places a control on the order in which the runtime environment processes events.                                                                            |
| Join activity session qualifier                          | Interface      | Specifies if the target service is capable of joining a client propagated activity session.                                                                 |
| Join transaction qualifier                               | Interface      | Specifies if the target service is capable of joining a client propagated transaction.                                                                      |
| Reliability                                              | Reference      | See "asynchronous reliability"                                                                                                                              |
| Security identity qualifier                              | Implementation | Provides a logical name for the identity under which the implementation runs at run time.                                                                   |
| Security permission qualifier                            | Interface      | Allows access only to users who have been granted a particular security role.                                                                               |
| Store and forward qualifier                              |                | Allows you to store asynchronous messages when exceptions occur at run time.                                                                                |
| Suspend activity session qualifier                       | Reference      | Determines whether the client will propagate the activity session to the referenced component.                                                              |
| Suspend transaction qualifier                            | Reference      | When the invocation is synchronous, the qualifier determines whether the client will propagate the transaction to the referenced component.                 |
| Transaction qualifier                                    | Implementation | Determines the logical unit of work that the component's processing runs.                                                                                   |

- Activity session qualifier

The activity session qualifier determines if the component's processing will be run under an activity session, which provides an alternative unit-of-work scope to the one provided by a transaction context.
- Asynchronous invocation qualifier

The asynchronous invocation qualifier allows you to specify that an asynchronous invocation should occur as part of a client transaction. The qualifier determines when the message is sent to the target.
- Asynchronous reliability qualifiers

The three asynchronous reliability  qualifiers (reliability, request expiration, and response expiration) determine the quality of the delivery of an asynchronous message.
- Business object (BO) instance data validation qualifier

A data validation qualifier confirms that the data passed in to an operation matches the XSD types of the operation's inputs. It can be used to validate instance data from a business object.
- Event sequencing qualifier

The event sequencing qualifier ensures that events are processed in order and that one event is completely processed before the next one is processed.
- Join activity session qualifier

The join activity session qualifier determines whether the target service is capable of joining a client propagated activity session.
- Join transaction qualifier

This qualifier determines whether the target service is capable of joining a client-propagated transaction.
- Security identity qualifier

The security identity qualifier is a privilege specification that you can use to provide a logical name for the identity under which the implementation runs at run time.
- Security permission qualifier

The security permission qualifier specifies a role, which is a semantic group of permissions that a given type of users must have to use an operation in an interface.
- Store and forward qualifier

The store and forward qualifier can be used to store asynchronous messages when exceptions occur at run time. By default, it is not enabled.
- Suspend activity session qualifier

When the invocation is synchronous, the suspend activity session qualifier determines whether the client will propagate the activity session to the referenced component.
- Suspend transaction qualifier

When the invocation is synchronous, this qualifier determines whether client will propagate the transaction to the target component.
- Transaction qualifier

This qualifier determines the logical unit of work that the component's processing runs. For a logical unit of work, all of the data modifications to resources (not to be confused with changes to the values in a business object) made during a transaction are either committed together as a unit or rolled back as a unit.