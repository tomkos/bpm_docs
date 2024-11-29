<!-- image -->

# Store and forward qualifier

This qualifier lets you detect problems with a service,
such as if it is unavailable, and store the messages going to it.
When the problems are fixed, the messages can be resubmitted using
the business space store and forward widget. The goal of the qualifier
is to stop processing messages when the target service is unavailable
and prevent failed events from occurring.

This qualifier can
be specified on any import, an SCA export or a component. It can be
applied to all interfaces of the component, a specific interface,
or a specific operation. Once the qualifier is triggered by an exception,
messages remain in the queue.

These sections show how to set
up the qualifier, provide guidance on how to use it with common exceptions
and discuss the preferred interaction style (synchronous or asynchronous)
of the bindings:

- How to set up this qualifier
- Guidelines
- Preferred interaction style

## How to set up this qualifier

To add the store and forward qualifier and associate it with exceptions,
follow these steps:

1. Select the Properties view of an import
or component and click the Details tab.
2. Select the Qualifiers subtab and click Add.
3. In the Add Qualifier window, select Store and Forward and click OK. The properties fields for the qualifier open.
4. In the Configuration name field, enter
a name for your qualifier. The name should be suited to the service
it is associated with. For example, if it were associated with a service
that gets employee information from an EIS system it might be called EmployeeDataFromEISSystem. If you are using a Business Space
widget to monitor message storage and stop storage, if needed, this
name will appear in the widget to identify the qualifier.
5. To add an exception, click Add. The Add Exception window lists all the classes that are in
the classpath and extend the java.lang.RuntimeException class. You
can edit the text that is used for the search. Select a class and
click OK. The class name is added to a pane
and the fully qualified name is added to the Exception
Name field. If you use Browse beside
the Exception Name field, you can also select
by qualified name first, which retrieves the specific class name.
6. In the Message to match field, you can
optionally specify the message you want to match in the messages associated
with the exception. An asterisk (*) character can be used as a wild
card.
7 The Exception chain drop-down list providesoptions since an original exception often gets wrapped over time withother exceptions. This situation creates an exception chain from theoriginal exception to the top or outer level. The qualifier receivesthe top level and examines it based on the option you select.
    - Match wrapped exceptions starting with the original
exception (default): Message storage begins if the specified
exception is encountered either directly or wrapped by another exception.
It has the same result as Match wrapped exceptions but may
affect performance as this option examines the most-nested wrapped
exception first.
    - Match only the top-level exception: Message
storage begins if the specified exception is encountered. Wrapped
exceptions are not examined.
    - Match wrapped exceptions: Message storage
begins if the specified exception is encountered or if a wrapped exception
is encountered and it directly or indirectly wraps the specified exception.
The matching occurs starting from the top level exception in the chain.
    - Match only the original exception: If an
exception is encountered, it is recursively unwrapped. If the unwrapping
process results in finding the specified exception then message storage
begins.
8. Selecting Match types that inherit from this type includes the exceptions that inherit from the one you selected.
By default it is not selected.

The first message after a failure
is not stored. It is a security mechanism to avoid a poison message.
A poison message is a message that has exceeded the maximum number
of delivery attempts to the receiving application.

Your component
can have multiple operations and possibly multiple interfaces.  If
the message storage is triggered by one of those operations then messages
are stored for all operations on all interfaces. In other words, once
problems are detected for one operation of the service, the entire
service is considered affected; not just the specific operation which
encountered that problem.

## Guidelines

Setting up this
qualifier for several common exceptions is discussed. In addition,
information is provided on how the levels that the qualifier is applied
to (component, interface or operation) change the scope of the qualifier.
 A link has been added to help you find more information on this qualifier
from the runtime documentation.

If you want to assign an exception
to a web service that is not available at run time then you should
set up the qualifier in the following way:

1. Set the exception to the following: ServiceUnavailableException (default).
2. Leave the remaining fields as they are.
3. If you want to match a particular message for this exception,
add the text of the message to the Message to match field.

If you want to assign an exception to an SCA import that
was not installed and therefore not available at run time then you
should set up the qualifier in the following way:

1. Set the exception to the following: ServiceUnavailableException (default).
2. Leave the remaining fields as they are.
3. If you want to match a particular message for this exception,
add the text of the message to the Message to match field.

If an HTTP import is communicating with an external service
and that service is known to fail leading to many failed events, then
set up this qualifier on the import. Failures will be detected once
the import cannot communicate with the external service (HTTP status
code 503). The messages will be stored just before the import component.
Set up the qualifier in the following way:

1. Set the exception to the following: ServiceUnavailableException (default).
2. Set the exception chain option to Match wrapped exceptions
starting with the original exception.
3. Leave the remaining fields as they are.
4. For an HTTP import, the preferred interaction style is synchronous.
Change it to asynchronous. See Preferred interaction style for more information
on the preferred interaction style of the bindings.

If an SCA import is communicating with an external service
and that service is known to fail leading to many failed events, then
set up this qualifier on the import. Failures will be detected once
the import cannot communicate with the external service. The messages
will be stored just before the import component. Set up the qualifier
in the following way:

1. Set the exception to the following: ServiceRuntimeException.
2. Set the exception chain option to Match wrapped exceptions
starting with the original exception.
3. Leave the remaining fields as they are.
4. An SCA import defaults to the preferred interaction style of the
SCA export it refers to, which in turn has the preferred interaction
style of its target component. See Preferred interaction style for more information
on the preferred interaction style of the bindings.

The scope to the qualifier changes depending on the level
that it is applied to:

- Component level: The exception or exceptions apply to all interfaces
and operations on the component.
- Interface level: The exception or exceptions apply to the interface
and all its operations. Note that the exceptions you specify are in addition to those specified on the component of the interface.
- Operation level: The exception or exceptions apply only to the
operation. Note that the exceptions you specify are in addition to those specified on the component or the interface of the operation.

You can find more information on this qualifier in the Storing events topic in related links.

## Preferred interaction style

The preferred interaction style specifies the preferred communication
mode, synchronous or asynchronous, for a component. It is set at the
interface level and is not guaranteed. The default setting for each
binding is shown. Note that some settings can be changed.

| Binding           | Import default         | Export default         |
|-------------------|------------------------|------------------------|
| HTTP              | Synchronous (editable) | Synchronous            |
| JCA (EIS systems) | Synchronous (editable) | Synchronous (editable) |
| JMS               | Asynchronous           | Asynchronous           |
| MQ                | Asynchronous           | Asynchronous           |
| SCA               | Synchronous (editable) | Synchronous (editable) |
| Web services      | Synchronous (editable) | Synchronous            |