# Building a sample inbound integration

To implement an inbound integration in IBM® Business Automation Workflow,
you need to build several components that work together. The following
image represents the steps required to build a sample inbound integration.

Figure 1. Steps to build a sample inbound integration

<!-- image -->

For general and introductory information, see Integrating with web services, Java and databases.

The following sections describe how to create simple components
so that you can easily build the integration and also easily test
your initial implementation. References to more detailed descriptions
of the implementation options for each component are provided in the
relevant sections.

- Adding a message event to a BPD

Start building the sample integration by adding a message event to a business process definition (BPD).
- Creating an attached service for a BPD

Create a service to pass parameter values from the message event to the business process definition (BPD).
- Creating an undercover agent for a BPD

Create an event-based undercover agent.
- Attaching the undercover agent to the message event

Attach the undercover agent (UCA) to the message event. The event waits for the completion of the UCA. When the UCA completes, the event completes.
- Creating a caller service

Create a service with appropriate inputs to call the undercover agent (UCA) to send the event.
- Creating an inbound web service

Create an inbound web service to provide a way for an external system or application to call into IBM Business Automation Workflow.
- Testing the integration

Test the completed inbound integration using the Inspector.