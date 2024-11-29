<!-- image -->

# Connectivity groups

Create connectivity groups to represent the possible request sources
for the system.

- Put all the logic to get the inbound data into one moduleThis
is also true for outbound data when it is going to an external system
or legacy system
- Put all the logic to connect and transform the data into one moduleAll
the other modules can now use a standard set of interfaces and not
have to worry about extra transformations.

The connectivity group will not contain stateful component types
like long-running business processes and Business State Machines.
 These connectivity groups provide encapsulation and isolation of
the specific endpoint's integration requirements. Commonly, mediation
modules are used for this purpose as they represent convenient ways
to implement "infrastructure" related tasks.

When the system is recovered and able to process new work, these
modules can be restarted.

The module that is outlined in the following screen capture is
considered part of a connectivity group.

<!-- image -->

Connectivity groups can be used for input from an external source
or an existing system such as SAP or CICS®.
Or for new work from a web browser-based clients.