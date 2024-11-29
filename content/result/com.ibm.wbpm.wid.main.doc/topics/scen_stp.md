<!-- image -->

# Scenario: Developing a straight through process

This set of tasks corresponds in a general way to the getting started procurement sample for Advanced
deployment environment.

In this scenario, an automated process, which was created using IBM Integration
Designer,
already exists. Using IBM Process
Designer,
a developer or a business analyst creates a task for human intervention
to handle exceptions.

The work described here is set up to be done using two different
authoring environments, each optimized to contribute its part of the
total process. The developers both contribute their work to a common
repository.

The Workflow Center repository
contains all the BPM assets. The high level assets are process applications,
toolkits, tracks, and snapshots. Both designers contribute to the
same process applications and toolkits. Process Designer contributes
business processes and data types. Integration Designer contributes
modules, libraries, and BPEL business logic.

Workflow Center
provides a central user interface where you can manage multiple process
development efforts across the entire process lifecycle. From Workflow Center,
you can create process applications and toolkits and grant other users
access to those process applications and toolkits. In the Process Designer, you
can create process models, services, and other assets within process
applications.

- Process applications are top-level containers of
artifacts.
- A toolkit provides a way to share a collection of
assets across applications.
- Tracks are optional subdivisions in a process application
based on team tasks or process application versions. When enabled,
tracks allow parallel development to occur. Administrators determine
if tracks are necessary for each process application.
- A snapshot captures the state of the items within
a process application at a specific point in time. Any author with
write access to a process application can create a snapshot. Administrators
can deploy a snapshot to a runtime server.
- A module is a software artifact that is used for
developing, organizing resources, implementing services, and deploying
to the runtime environment.

# Creating a process application for a BPEL process in IBM Integration
Designer

To make the BPEL process available for adaptation in Process Designer, the
process needs to be associated with a process application and published
in the Workflow Center.

## Procedure

1. Plan your project. For a better understanding of the relationship between the
authoring environments and Workflow Center, see Authoring tools and The Workflow Center repository.
2. In the Integration Designer, open the Workflow Center perspective and
connect to the server.
3. In the Workflow Center perspective,
create a new process application. Name the process application and
open it in your workspace.
4. Associate the BPEL process
(module and dependent libraries) with the process application.
5. Refactor and move business objects to a library that is
associated with the process application. Do not refactor the interfaces;
interfaces are not used in the Workflow Center.
6 Using the Business Process Choreographer Explorer, testthe BPEL process in isolation.
    1. Update the process application
in the Process Center repository.
    2. Launch Business Process Choreographer
Explorer.
    3. Start the process instance.
    4. Monitor the progress of
the process instance.

## Creating a business process definition in IBM Process
Designer

### About this task

### Procedure

1. Start Process Designer and
log in to Workflow Center.
2. Select the process application that you want to work with,
and open it in Process Designer.
3. Create a new business process
definition.
4. Declare variables..
In IBM Business Process Manager, variables capture the
business data that is passed from step to step in a process.
5. Add lanes for user groups
and systems.
6. Implement activities.
Activities represent the steps in your process. The procurement
sample uses activities to specify human tasks.
7. Add coaches.
Human tasks usually involve coaches. Coaches are the web-based
interfaces where process participants do the work that is required
to complete each task.
8. Test
the business process definition using the Inspector.

## Update the BPEL process to use the business process definition

### About this task

### Procedure

1. Open the Integration Designer Business
Integration perspective.
2. Retrieve the Process Designer service by
refreshing the process application from the Workflow Center.
The business process definition and interfaces created in Process Designer are now available in the module and library.
3. Create an SCA import for the
business process definition.
4. In the assembly editor, wire the
import to the BPEL process.

## Test and deploy the process application

### Procedure

1. In the Workflow Center perspective
in Integration Designer, create a new snapshot
of the process. Snapshots record the state of artifacts
within a process application or track at a specific point in time.
2. Activate the process application snapshot to
deploy it to the process server.