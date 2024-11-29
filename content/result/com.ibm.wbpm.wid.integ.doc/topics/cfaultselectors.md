<!-- image -->

# Faults overview

The following sections provide an overview of how faults can be
handled by your application, beginning with the types of faults.

- Business faults
- Runtime exceptions
- Fault handling on imports and exports
- Data format considerations
- Wizard for configuring faults
- Fault selectors
- Fault data handlers

## Business faults

Business
faults are business errors or exceptions that occur during processing.
 Consider the following interface which has a createCustomer operation
on it. This operation has two business faults defined on it: CustomerAlreadyExists
and MissingCustomerId.

<!-- image -->

In this example, if the client sends
a request to create a customer to this SCA application and that customer
already exists, the component throws a CustomerAlreadyExists fault
to the export. The export now needs to propagate this business fault
back to the calling client.

This is achieved by the
fault data handler that is setup on the export binding.  When a business
exception is received by the export binding, the binding calls the
fault data handler with the data object from the service business
exception.

1. The binding calls the appropriate data handler with the data object.
2. The fault data handler transforms the fault data object to a response
message and returns it to the export binding.
3. The export returns the response message to the client.

If the service business exception contains the name of
the fault, then the data handler setup on the fault will be called.
 If the service business exception does not contain the name of the
fault, then the fault name will be derived by matching the fault types.

## Runtime exceptions

Runtime
exceptions are classified as all the exceptions that occur in the
SCA application due to processing of the request and do not correspond
to a business fault. Runtime exceptions are not defined on the interface
as business faults are. In certain scenarios, you may want to propagate
these runtime exceptions to the client application so that the client
application can take the appropriate action.

For example, if
a client sends a request to create a customer to the SCA application
and an authorization error occurs during processing of this request,
the component throws a runtime exception. This runtime exception has
to be propagated back to the calling client so it can take the appropriate
action regarding the authorization. This is achieved by the runtime
exception data handler configured on the export binding.  The processing
of a runtime exception is similar to the processing of a business
fault.

If a runtime exception data handler was set up, the following
processing occurs:

1. The export binding calls the appropriate data handler with the
service runtime exception.
2. The data handler transforms the fault data object to a response
message and returns it to the export binding.
3. The export returns the response message to the client.

## Fault handling on imports and
exports

To handle both business faults and runtime exceptions,
you can set up fault handling on imports and exports. Handling faults
on either imports or exports is optional. You would likely create
fault handlers for the most common errors that could occur at run
time in your application.

You can create fault handlers on imports
and exports for the following bindings: JMS, MQ JMS, generic JMS,
MQ and HTTP. You can also add them to your imports and exports created
with EIS bindings for services using adapters, except for those services
that use CICS and IMS adapters.

In the following diagram of
an import, a fault occurs on the external service that the import
is calling. The numbers refer to the numbers in the diagram.

1. The fault is transformed into the data format expected by the
component either as a business fault or a runtime exception.
2. The fault originally is passed as a native response message. This
fault could be passed in to any JMS-type binding (JMS, MQ JMS and
generic JMS), MQ or HTTP binding, or as an exception from an EIS system.

Returning a fault in the expected format is discussed
in Data format considerations.

<!-- image -->

In the following
diagram of an export, a business fault or a runtime exception occurs
in the SCA environment. The numbers refer to the numbers in the diagram.

1. The fault is passed back to the client by the export in a response
message. The transport can be any JMS-type binding, an MQ binding
or an HTTP binding. It is transformed into the native data format
expected by the client.
2. The fault originally occurs in the SCA environment resulting in
either a business fault or a runtime exception.

Returning a fault in the expected format is discussed
in Data format considerations.

<!-- image -->

You
can create a fault handler for your import or export on three levels.
You can associate a fault handler with a binding, with an operation
or with a specific fault.

## Data format considerations

As
with transforming data formats on bindings, so to there must be a
way of transforming data formats for a fault handler since a fault
in one environment must be expressed in the data format of another
as the result of a request-response operation. For example, suppose
a fault is issued in a non-SCA environment as the result of a call
made to an application in this environment by an import. The fault
in that non-SCA environment might be returned as text in a response
message to the import. The import, on receiving the text in a message,
must transform this text to the expected XML format in the SCA environment.

When
you create a fault handler you are required to also specify how the
data will be transformed between the two environments. Specifying
the data format transformation for fault handlers is similar to specifying
the data format transformation for bindings.

## Wizard for configuring faults

Faults
are initially defined in the interface editor where you add faults
to the operations on the interface. For example, in the screen capture
that follows the getInventory operation has two faults, one to handle
a timeout condition and one to handle a system failure.

<!-- image -->

When you add
a binding to and import or export, these faults are detected by the
generate binding wizard.

Once you have generated a binding,
you can find and modify the fault information in the properties view
of the import or export. For example, in the following screen capture
of a JMS binding on an import, the fault selector, fault data format
and runtime exception data format are shown. Since implementing fault
handling is optional, none of these elements have been implemented.
If you wanted to add fault handling, you would begin by implementing
the fault selector, the fault data format and, if you wanted to handle
runtime exceptions, the runtime exception data format.

<!-- image -->

## Fault selectors

For bindings
on imports, you can configure a fault selector to determine
whether a response is a fault and, if so, the name of the fault. The
fault selector determines whether the import response is an actual
response, a business exception, or a runtime fault. It also determines,
from the response body or header, the native fault name.

The
fault selector is called by a binding whenever the binding interacts
with the native consumer (for example, a queue or an adapter) and
receives a normal response or an exception (business or runtime) in
the process.

The fault selector is optional. If you do not
specify a fault selector, the binding calls the response data binding
or data handler.

## Fault data handlers

A fault
data handler is nothing but a data handler. It has the same interface
as a data handler.

The use of fault data handlers with respect
to faults is similar to the use of data handlers with respect to bindings.
Though IBM® Integration
Designer provides
pre-packaged fault handlers, you may have a need to create your own
type of fault handler for your particular application. A fault
data handler transforms fault data into a data object that can
be returned in a service business exception object. A fault data handler
can be used by both import and export bindings.

- If the fault data handler is set at all three levels, the data
handler associated with a particular fault is called. No further fault
processing occurs.
- If fault data handlers are set at the operation and binding levels,
the data handler associated with the operation is called. No further
fault processing occurs.

You can configure a data handler to handle runtime exceptions
that are received from external applications or send runtime exceptions
that have occurred in your module to the external applications. If
your module does not want to send or receive runtime exceptions to
external applications or modules, then you should not define the data
handler for runtime exceptions and leave it blank.