<!-- image -->

# Scenario: Developing a new process with an Advanced Integration
service

This scenario describes in general terms the tasks required to create the Advanced Hiring sample.
You can access the sample from the Getting Started panel in IBM Business Process Manager Advanced.
See Instructions for running the Standard Hiring Sample process application for information about administering and running
the sample.

<!-- image -->

The Workflow Center repository
contains all the BPM assets. The high-level assets are process applications,
toolkits, tracks, and snapshots. Both the business analyst and the
integration developer contribute to the same process applications
and toolkits. Process Designer contributes
business processes and data types. Integration Designer contributes
modules, libraries, and BPEL business logic.

Workflow Center
provides a central user interface where you can manage multiple process
development efforts across the entire process lifecycle. From Workflow Center,
you can create process applications and toolkits, and you can grant
other users access to those process applications and toolkits. In
the Process Designer,
you can create process models, services, and other assets within process
applications.

- Process applications are top-level containers of
artifacts.
- A toolkit provides a way to share a collection of
assets across applications.
- Tracks are optional subdivisions in a process application
based on team tasks or process application versions. Tracks allow
parallel development to occur. Administrators determine if tracks
are necessary for each process application.
- A snapshot captures the state of the items within
a process application at a specific point in time. Any author with
write access to a process application can create a snapshot. Administrators
can deploy a snapshot to a runtime server.

# Creating a process application

This task is likely to be done by a business analyst or
a developer with good knowledge of the business.

## Procedure

Follow these steps to create a process that will use
an external service.

1. Plan your project. For a better understanding of the relationship between the
authoring environments and Workflow Center, see Authoring tools and The Workflow Center repository.
2. Connect to the Workflow Center and
log in.
3. In Workflow Center, create a new process application that
will contain the process model and underlying implementations.
4. Open the process application to start Process Designer.
5. Add dependencies to
any toolkits that you or other developers need. A toolkit provides
a way to share a collection of assets across applications.
6. Create a process 
In this scenario, one step in the new process requires a service
that does not yet exist. For example, you might want a service that
would allow your process to extract customer information from an SAP
database. The integration development team will implement this service
in a subsequent task.
7. Start the desktop Process Designer.
8. Using the desktop Process Designer, create an Advanced Integration service and
give it a name. Assign the input and output business objects for the
service.
9. Save your work to the Workflow Center.
10. Test your process using playback with emulation.

## What to do next

# Implementing an Advanced Integration service

This task is likely to be done by an integration developer.

## About this task

## Procedure

Follow these steps to create the shell that will provide
the ultimate implementation.

1. In the Integration Designer, Open the Workflow Center and
connect to the server.
2. Open the process application in
the Integration Designer workspace.
Advanced Integration services that have not yet been implemented
are marked with the phrase "no implementation".
3. Use the service implementation wizard to create an implementation.
You still need to develop the particular implementation that
you are using; only a shell has been created so far. The information
center provides instructions for creating several types of implementations.
The implementation can be long running or a microflow, Java component,
or empty implementation. When you choose an implementation, an SCA
(service component architecture) export will be created for the service.
See Exports and Creating exports for
more information about these artifacts.
4. Save your work. Once you use Refresh and Publish on
the process application or toolkit, the Advanced Integration service
will be available in the Workflow Center and
can be used in the Process Designer business
process.
5. Test the Advanced
Integration service.

# Using an Advanced Integration service in a process application

## About this task

## Procedure

To add the service to the process that was created earlier,
perform one of the following steps.

- If you are using the Process Designer,
perform the actions described in Invoking an Advanced Integration Service.
- If you are using the desktop Process Designer ,perform the following actions.
    1. In the desktop Process Designer,
locate the service in your process application and drag it to the
business process definition (BPD).
    2. Map the service
inputs and outputs to the business process definition process variables.
    3. Click the Run icon () to test the process.