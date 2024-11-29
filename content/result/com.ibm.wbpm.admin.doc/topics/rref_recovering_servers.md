# Restarting deployment environments

## About restarting deployment environments

The
procedure to restart a deployment environment varies depending on
the topology. Topologies are based on system configuration patterns,
each pattern designed to meet particular business requirements.

IBM® Business Automation Workflow supports
a set of predetermined deployment environment configuration patterns.
If none of the patterns meet your requirements, you can plan and create
your own customized deployment environment.

- Messaging servers Messaging servers are responsible for providing
the Service Integration Bus (SIB) messaging infrastructure.
- Workflow servers Servers with profiles capable of hosting and
running all module types. This profile hosts the Business Process
Choreographer component.
- Support serversThis server is responsible for providing support
and monitoring services such as the Common Event Infrastructure CEI.

The deployment patterns differ in how you group and organize
all the functional components, so that the pattern can address your
business requirements in the most cost effective fashion. For more
advanced and highly available environments, the servers would reside
in clusters that are distributed across physical resources.

## General practice for restarting servers as part of
a recovery operation

A general model for starting servers
is to start the messaging servers first, then the support servers,
and lastly the workflow servers.  Each application architecture may
have specific dependencies between application components that need
to be taken into consideration.

Shutdown
basically happens inverse to the startup procedure, starting with
the application server clusters and ending with shutting down the
messaging infrastructure after it has had time to quiesce and process
any inflight transactions.