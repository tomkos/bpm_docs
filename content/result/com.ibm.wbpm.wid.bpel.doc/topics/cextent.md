<!-- image -->

# Working with BPEL extensions

IBM Workflow
Server BPEL extensions are provided. These extensions are automatically
enabled if you model your process as a microflow. If you want to convert
a long-running process to a microflow you must enable these extensions.

The BPEL extensions provide the following capabilities:

- Microflow

- Java™

- Human Task
- Snippet
- Generalized Flow
- Collaboration scope

- Description
- Documentation
- Display Name
- Custom Properties (not applicable for Structures)
- Enable persistence and queries of business-relevant data

- Auto-delete
- Autonomy - whether a process runs as a peer or as a child of the
invoking process. Autonomy is controlled through the Bind
the lifecycle to the invoking BPEL process check box.
- Compensation Sphere
- Valid From
- Ignore missing data

- Scopes that can be flagged as noncompensable
- Transactional behavior and the continue processing upon unhandled
faults functionality of the invoke activity
- Compensation of the invoke activity
- Expiration setting on the Invoke activity
- Administrative Tasks for Processes, Invokes and Snippets
- Authorization Tasks for Receives, OnMessages and OnEvents
- Query Properties on Variables
- Usage of Data Type Variables on the Details tab of messaging activities
like Invoke, Receive, Reply, OnEvent, OnMessage

## When not to use the BPEL extensions

When
you first create a business process, you can disable the extensions.
You may want to do so in the following types of situations:

- When you are designing the process to be used or edited in another
set of tools
- When you are planning on executing the process in a runtime environment
other than IBM Workflow
Server
- When you want to exchange information with a business partner
who is not using the IBM Integration
Designer or IBM Workflow
Server set
of tools

## Related concepts

- Choosing the appropriate compensation for your process
- Best Practice: When to not use the BPEL extensions
- Key concepts for BPEL business processes
- Choosing between long-running processes and microflows

## Related tasks

- Creating a BPEL process
- Compensating activities in a long-running process
- Compensating a microflow

## Related reference

- Server tab: BPEL process editor