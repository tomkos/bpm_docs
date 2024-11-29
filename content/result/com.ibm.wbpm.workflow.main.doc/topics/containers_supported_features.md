# Feature support in Business Automation Workflow on
containers

## Key supported capabilities in the container environment

- Process apps, case solutions, and toolkits that are built with the web-based designers by using
non-deprecated capabilities.
- Online and offline deployment from IBM® Workflow
Center
- REST Operations APIs and REST Runtime APIs
- Process Admin Console
- Workplace
- Process Portal
- Playback server in the Workflow Center
traditional runtime environment for process applications destined for containers.
- Workflow patterns available in IBM Cloud Pak for Business
Automation, see Workflow automation.

The fundamentals of deploying an application onto the Workflow platform, running on containers
are the same as those for deploying an application onto a traditional environment. Load balancing,
clustering, and high-availability disaster recovery (HADR) rely on Kubernetes. Infrastructure ops,
including admin APIs and tuning, are different compared to what you might be familiar with in a
traditional environment.

## What is not supported in the container environment

If you have existing applications in the traditional environment that you want to move to
containers, these are the features that you must convert or remove.

- Deprecated features are not supported in the container environment. This includes using the
LiveConnect API to start Java from JavaScript. For a complete list of deprecated features, see Deprecated and removed features of IBM Business Automation Workflow.
- Deprecated artifacts (except heritage human services) that are created in the desktop Process Designer are not supported in containers. Although
heritage human services are supported, heritage coaches that are included in heritage human services
are not supported. For a detailed list, see Artifact support in traditional and container runtime environments.

- Advanced applications that are created in IBM Integration
Designer such as BPEL
processes, Mediation flows, and SCA applications
- Performance Data Warehouse
- Dynamic Event Framework (DEF) XML event emission
- WebSphere® MQ and JMS
integrations
- XML validation and transformation