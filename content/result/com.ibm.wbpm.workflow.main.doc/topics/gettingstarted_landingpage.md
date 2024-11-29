# Business process management overview

Every organization uses business processes to accomplish work.
A business process is a set of business activities that
represent the required steps to achieve a business objective. For
example, you might have a business process that handles credit card
disputes. In this case, the business objective is to resolve the dispute
in an efficient and accurate way in order to minimize cost to your
organization and to retain customer satisfaction. The process itself
includes all of the steps needed to meet the objective (in this case,
it might be activities like receiving the claim, examining the validity
of the claim, deciding whether to remove the charge, and informing
the customer of the decision).

Business processes often require a combination of internal activities
and activities that must be performed by humans. Therefore, we can
look at business process management as the intersection between people,
processes, and technology.

The business process management approach is iterative; you don't
implement it once, never to be touched again. Instead, you design,
model, create, simulate, monitor, and optimize your processes on a
regular basis. The feedback you receive from testing and monitoring
your processes drives continuous improvements to your organization's
workflows.

The following diagram illustrates the main tasks and activities that users complete to achieve
business objectives and the Business Automation Workflow components
that are used in the process lifecycle.

<!-- image -->

The process application is the fundamental container
for processes and their components in Business Automation Workflow. Process
designers create process applications in the authoring environments,
and might include services, tasks, and artifacts needed to support
execution.

From the Workflow Center, process
applications are deployed to the Workflow Server, which
is the process runtime environment for Business Automation Workflow.

For additional information about the various
factors that influence an Business Automation Workflow project,
see Chapter 1: Introduction to successful business process management and Chapter
2: Approaches and process discovery in Business Process Management Design Guide: Using IBM
Business Process Manager.

- Authoring tools

IBM Process Designer is the primary authoring tool for business processes; use it to efficiently model and test business processes in all editions of the product. A Business Automation Workflow Advanced deployment environment also includes IBM Integration Designer for building services that are self-contained, or that start other existing services (for example, web services, enterprise resource applications, or applications running in CICS and IMS).
- The Workflow Center repository

The Workflow Center includes a repository for all processes, services, and other assets created in the Process Designer and Integration Designer.
- Workflow Server and runtime environments

Workflow Server provides a single runtime environment that can support a range of business processes, service orchestration, and integration capabilities.
- Getting started with Process Federation Server

IBM Process Federation Server is an optional component for Business Automation Workflow environments. Install this component to create a federated process environment that provides business users with a single point of access to their task list and launch list, regardless of the type of process that they are working on and the Business Automation Workflow back-end system on which the process artifacts are stored.
- Business process administration tools

You can use a set of administration tools to accomplish tasks ranging from installing and managing snapshots to administering processes and working with the resources in your IT environment.
- Work management tools

Use the newer and more modern Workplace or the earlier Process Portal to work on your tasks, manage and complete work and, with the associated permission, use dashboards to manage and evaluate the workload and performance of your teams.
- IBM and accessibility

IBM strives to provide products that are accessible, regardless of age or ability.
- Tutorials

Business Automation Workflow features a Hiring tutorial and a Human Services Benchmark sample. The Hiring tutorial guides you through the creation of building process applications. Each lesson of the tutorial focuses on a specific implementation of a business process. The Human Services Benchmark sample features a business process application that you can use to evaluate the performance of Business Automation Workflow process handling. You can customize the sample to suit your applications.