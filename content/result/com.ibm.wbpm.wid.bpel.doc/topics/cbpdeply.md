<!-- image -->

# Planning to deploy a process

- If the update cycle of a component is tied tightly to the process,
deploy it with the process. Place the service component and the associated
process in the same module if updating one necessitates updating the
other.
- If the component can be updated independently of the process,
place it in a different module. This allows you to modify the component
independently of the process. An example would be a business rule
that sets the discount rate for preferred customers. You may want
to alter this discount rate in the future. Place the BPEL process
and the business rule in separate modules and have the process call
the business rule through an SCA Import and Export mechanism.
- If a process depends on an external service which it does notcontrol, you can ensure your ability to change the details of theimplementation in either of the following ways:
    - use a selector that allows a new implementation to be dynamically
introduced, based on certain criteria. This option is best suited
to a scenario where you have a set of predefined services from which
to select. The selection is most commonly time-based, with certain
services preferred at specific times of the year.
    - use invocations across the bus to allow administrative-level configuration
of the target.
- Consider using dynamic endpoint references. This is another mechanism
for dynamically assigning services. In this case the person who initiates
the process instance selects the service to use. Specifically, you
pass to the process instance, in the business data, the endpoint reference
of the service you want to use . In a selector the criteria are fixed,
whereas dynamic endpoint references are more flexible.
- Gain a careful understanding of late and early binding. (See Versioning business state machines.) Is the service component that you are
calling likely to be updated regularly? Do you want your process to
always use the most up to date version of the process? If so, choose
late binding. Does your process need to use the original version of
the component and ignore component updates? If so, choose early binding.
- When developing interfaces and business objects, consider whatwould happen if requirements change in the future. Note: If you change a business object or an interface this typicallymeans that you must rework your BPEL process. It is therefore recommendedthat you design your business objects and interfaces to be sufficientlygeneric that they will not require modification in the future.

- Will you need to modify your business object?
- Will you need to change your interface?
- Who would this impact?
- Can you make your interface more generic now?
- Should you include a version field (to add manual support
for versioning).
- When you update an application, running instances can continue
to use the old version, or, using a process migration specification,
transition to the new version. If you intend to use process instance
migrations, you must not use compensation logic in your process.
- When writing code inside the IBM® Workflow
Server or
client code, consider the use of dynamic invocation mechanisms. If
you use generated classes to invoke services (or to interact with
Business Objects), you are tying yourself to specific implementations.