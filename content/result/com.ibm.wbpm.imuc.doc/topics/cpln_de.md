# Choosing the deployment environment type

Workflow Center provides a repository for process
assets, a runtime environment for testing and studying the performance of processes, and a console
for administering access to assets and deploying processes to development, test, staging, or
production environments. You need at least one Workflow Center deployment environment somewhere in your
system. The environment type of a Workflow Center
will always be Development.

Workflow Server is a runtime environment for process
applications and a data warehouse for collecting performance data from the applications. It includes
administrative consoles for managing and maintaining the runtime environments and data
warehouses.

When you install (deploy) a process application snapshot to a Workflow Server, the assets of that
snapshot are moved from the Workflow Center
repository to the selected Workflow Server. The Workflow Server can be connected to a Workflow Center or offline. Depending on your needs and
whether the Workflow Server is connected or offline, you can use Workflow Center or wsadmin commands to install the
snapshot. See Installing process application snapshots.

If you choose the offline server option during typical installation, Workflow Center is not installed. You might choose to install
an offline Workflow Server if you already have a
Workflow Center installed, or if the Workflow Server is behind a firewall. Once Workflow Server is installed, you can add the offline server
to a Workflow Center in order to deploy your process
applications.

Choose an Advanced deployment environment if you are not sure which to choose. The Advanced
deployment environment gives you access to all features and functions. Choose Standard if you are
sure you do not need the BPEL, SCA, or mediation flow (ESB) features. A Standard deployment
environment has a slightly smaller footprint. If you discover later that you need Advanced
components after all, you can update your deployment environment from Standard to Advanced.  For IBM Business Automation
Workflow Enterprise Service Bus,
choose AdvancedOnly. The AdvancedOnly deployment environment was added mainly for customers
migrating from WebSphere® Process
Server.