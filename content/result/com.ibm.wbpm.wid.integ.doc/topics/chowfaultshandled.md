<!-- image -->

# Handling faults in bindings

You can configure your import and export bindings to handle faults
(for example, business exceptions) that occur during processing. You
can set up a fault handler at three levels: you can associate a fault
handler with a fault, with an operation, or with a binding. For import
bindings, you can also set up a fault selector to determine whether
a response is a fault and, if so, the name of the fault.

A fault data handler processes fault data and transforms it into
the correct format to be sent by the export or import binding.  For
an export binding, the fault data handler transforms the exception
business object sent from the component to a response message that
can be used by the client application.  For an import binding, the
fault data handler transforms the fault data or response message sent
from a service into an exception business object that can be used
by the SCA component.  For import bindings, the fault data handler
calls the fault selector, which determines the name of the fault.

You can specify a fault data handler for a particular fault, for
an operation, and for a binding.  If the fault data handler is set
at all three levels, the data handler associated with a particular
fault is called. No further fault processing occurs.  If fault data
handlers are set at the operation and binding levels, the data handler
associated with the operation is called. No further fault processing
occurs.

- Faults overview

Errors issued at run time in a Service Oriented Architecture (SOA) application can either be from a Service Component Architecture (SCA) application to another non-SCA application or from a non-SCA application to the SCA one.
- Prepackaged fault components

Some prepackaged fault components are provided for the bindings you work with.
- Developing a custom fault selector

To develop your own custom fault selector, you must implement the FaultSelector interface, implement a method in the BindingContext interface and understand Service Message Object (SMO) headers.