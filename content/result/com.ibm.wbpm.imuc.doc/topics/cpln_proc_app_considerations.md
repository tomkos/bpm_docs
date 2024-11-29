# Process and process application considerations

You need to know how your product or service is created and delivered.
 IBM® Business Automation Workflow comes
with deployment environment patterns designed to meet the requirements
of both production and test environments.

- Consider how process applications interact with existing services and back-end systems.
- Consider how process applications handle data and how data flows through your system to addressa specific business need.Understand how data persists across retrievals, sessions, processes, andother boundaries when you are developing a solution and configuring its environment. Consider the following items regarding the process applications to bedeployed to your environment:

Understand how data persists across retrievals, sessions, processes, and
other boundaries when you are developing a solution and configuring its environment.

    - Process application invocation patternsYou must understand how the runtime environment
handles asynchronous invocations and how the SCA runtime environment leverages the underlying
message system to implement asynchronous invocations.
Different applications have different
needs. Those needs are determined by factors such as export types, component types, interactions
between components, import types, resources needed such as databases or JMS resources, the need for
business events, and their transmission mechanism.
    - Types of business processes that you plan to implement (transactional business processes,
interruptible business processes, non-interruptible business processes) Non-interruptible
business processes, or microflows, are short-running business processes that run in one transaction
or without a transaction. Non-interruptible business processes are fast with little effect on
performance. All activities within one process are processed in a single thread.

Interruptible business processes, or macroflows, are long-running business processes that
contain a set of activities, each of which is performed in its own transaction. Interruptible
business processes can include activities that require human intervention or calls to remote systems
or both. Asynchronous activities cause a business process to be interruptible because these
activities might take minutes, hours, or even days to complete.

## Related concepts

- Resource considerations
- Development and deployment version levels
- Naming considerations for profiles, nodes, servers, hosts, and cells
- Invocation styles

## Related tasks

- Preparing necessary security authorizations

## Related reference

- Installation directories for the product and profiles

## Related information

- Business processes