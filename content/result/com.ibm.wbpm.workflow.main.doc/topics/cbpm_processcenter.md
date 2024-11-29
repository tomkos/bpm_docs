# The Workflow Center repository

Process Designer is the standard authoring tool
for business processes. A Business Automation Workflow
Advanced
deployment environment also offers Integration Designer with its associated editors and adapters.

Workflow Center is a
software component that runs as a server where Process Designer and Integration Designer share assets, in effect letting them develop
business processes cooperatively in a highly interactive manner.

In the diagram that follows, you see several related components
that together let you build complex business processes.

<!-- image -->

The Workflow Center includes two servers, the
Workflow Center server and the Performance Data
Warehouse server. The Workflow Center server allows
developers that are working in Process Designer to
run their process applications and store performance data for testing and playback during
development efforts. Performance Data Warehouse retrieves tracked data from Workflow Server or Workflow Center server at regular intervals.

In the authoring environments, you can create process models,
services, and other assets within process applications.

Workflow Center
provides the tools that you need to maintain the repository.

- You can create process applications and toolkits and grant other users access to those process
applications and toolkits.
- Administrators can install process applications that are ready for testing or production on the
servers in those environments.
- Administrators can manage running instances of process applications in configured
environments.

Workflow Center provides a
convenient location in which to create and maintain high-level containers such as process
applications and toolkits. Administrators can use Workflow Center to provide a framework
in which BPM analysts and developers can build their processes and underlying implementations.
Another primary task for administrators is managing access to the Workflow Center repository by setting
up the appropriate authorization for users and groups.

Users with appropriate authorization can perform some administrative tasks directly in Process Designer and Integration Designer. For example, a developer with write access to
the process application who wants to capture the state of all project assets at a significant stage
of development can create a snapshot while working in the designer.