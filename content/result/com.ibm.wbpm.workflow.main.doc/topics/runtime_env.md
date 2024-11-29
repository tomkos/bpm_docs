# Runtime environments

The traditional runtime environment is based on WebSphere® Application
Server. The container runtime environment is
based on IBM
WebSphere Liberty.

The traditional runtime environment continues to offer the following features:

- Full compatibility with existing on-premise workflow installations.
- Support for familiar development and deployment tools, such as Process Designer, Case Builder, Workflow Center, and IBM Integration
Designer.
- Integrated process and case development and deployment in a single runtime environment.
- On-premise bare-metal deployment and VM-based deployment, which is the best option to leverage
private cloud if 100% compatibility is required.

The container runtime environment provides an enterprise workflow platform to run cloud-native
solutions. The environment offers the following features:

- Support for existing process applications and case solutions for running workflows in a
cloud-native way.
- Support for most non-deprecated artifacts in process application and case solution workloads
(but continued support for the deprecated Heritage Human Services). For a list of supported and
unsupported features and artifacts in container environments, see Feature support for Business Automation Workflow on containers and Artifact support in traditional and container runtime environments.
- Support for familiar on-premise development tools, such as Process Designer,Case Builder, and Workflow Center.
- A microservices architecture that utilizes Docker containers and the Kubernetes platform to
support autoscaling, continuous availability, and continuous upgrade.

In a traditional runtime environment, Business Automation Workflow configuration tasks
and WebSphere Application
Server
administration tasks are performed with wsadmin commands, REST API operations, and the WebSphere
administrative console. In a container runtime environment, these configuration and administration
tasks are performed with REST API operations.

## Target environment options

When you create a new project in Workflow Center,
you must select one of the following target environment options for your project:

- Traditional
- Traditional or Container

You can change the target environment option for an existing process app or toolkit at any time
in the Process App Settings view or the Toolkit Settings view of Process Designer. For an existing case solution, you must
first open the solution in Process Designer and then
change the target environment option in the Process App Settings view.

If you choose the Traditional option, your project is designated to be
installed and run on IBM Workflow
Server in the
traditional runtime environment. If you choose the Traditional or Container
option, your project is designated to be installed and run on either Workflow Server in the traditional runtime environment or
Workflow Server in the container runtime
environment.

Regardless of which target environment option you choose, your project artifacts are
automatically validated to ensure that they are supported in the corresponding runtime environment.
If your project contains any dependent toolkits or deprecated artifacts that are not compatible with
the runtime environment, critical validation errors will appear in the Validation pane of Process Designer. A Target
environment conversion tab will also open in the Process app
settings view or the Toolkit settings view to enable you to fix the
errors and compatibility problems. For more information, see Converting the target environment of projects.

## Architecture of Business Automation Workflow and its runtime
environments

The architecture of Business Automation Workflow and its runtime
environments is shown in the following topology diagram.

<!-- image -->

The diagram is composed of the following runtime-related components:

- Development
- Test
- Staging
- Production

    - Multiple IBM Business Automation
Workflow,
IBM Workflow Process Service, and
IBM Business Process Manager
 cells.
    - Multiple Business Automation Workflow, Workflow Process Service, and
Business Process Manager releases.
    - Business Automation Workflow and
Business Process Manager instances running on on-premises, and Business Automation Workflow and Workflow Process Service instances running
on containers.
    - Business process definition (BPD), case, workstream, and BPEL process instances and tasks.

For a system to be federated by Process Federation Server, the BPD, case
or BPEL data must be indexed into the federated data repository, which can be either Elasticsearch
or OpenSearch. For an on-premises system, it is your responsibility to set up and maintain your own
instance of Elasticsearch or OpenSearch. In container-based environments, an OpenSearch cluster is
provided out-of-the-box, but you can also bring your own instance of Elasticsearch or
OpenSearch.

- Business Automation Workflow
24.0.0.0 can be configured to index BPD data into the federated data repository.
- Business Automation Workflow on
premises 23.0.2 and later, as well as Business Automation Workflow on containers
20.0.0.2 and later can be configured to index case data into the federated data repository.
- For other federated run times or Business Automation Workflow versions, Process Federation Server must be
configured to index the corresponding data in the federated data repository.

Case Client is a web-based
application for case workers to complete their work for each case. Before Case Client is deployed into production
so that case workers can access it, business analysts can modify the application to customize
it.