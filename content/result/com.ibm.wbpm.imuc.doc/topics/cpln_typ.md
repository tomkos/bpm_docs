# Choosing typical or custom installation

The typical installation uses the product launchpad and interactively installs the software,
configures the deployment manager and managed-node profiles, and configures a single cluster
deployment environment that consists of a single node and single server. You do not need to create
the profiles or deployment environment later. A single cluster environment is the only option for
IBM Business Automation Workflow
Express, whereas, if you choose the custom
installation, you can choose a single or three cluster environment for IBM Business Automation Workflow
Enterprise.

The custom installation can also be performed interactively, or by choosing a silent
installation. Choose an interactive installation if you want to see the prompts as you make your
decisions. Choose a silent installation if you want to be able to script the installation in the
future, or if you want to use the same response file on multiple systems.

After using
the custom installation, you can use the BPMConfig command
to generate database scripts, configure a deployment manager and one
or more managed-node profiles, and create a pattern-based network
deployment environment.

Instead of using the BPMConfig command,
you can use the Profile Management Tool or manageprofiles command-line
utility to configure one or more deployment manager and managed node
profiles. After profile creation, you can use the deployment environment
wizard to generate a pattern-based network deployment configuration.

## Typical installation

The typical installation option is the simplest and quickest method for installing and
configuring the software. With a typical installation, you can maintain a personal copy of Business Automation Workflow on your system. You can use it to develop
integration services or business processes locally, or you can contribute artifacts using the export
and import functions in the product. A typical installation is recommended for proof of concept work
and for learning about the features and functions of the product.

- A typical installation creates a single-cluster deployment environment that consists of a single
node and single server.
- A typical installation can install Db2® Standard
Edition if an existing database is not
specified. Db2 is available only
for Windows and Linux systems, and the user must have administrative privileges (Administrator or
root) and must not have another DB2 product installed.
- A typical installation automatically populates the database.
- For IBM BPM Express on the
Windows operating system, a typical IBM Workflow
Center installation automatically installs
IBM Process
Designer.
- A typical installation creates shortcuts for the Workflow Center Administrative Console, Playback Server
Administrative Console, Process Designer (on
Windows), and WebSphere administrative console. It also creates a shortcut for the Quick Start
console, and will start the Quick Start console at the end of a successful typical
installation.
- If you ran the typical installation as an administrator, the installed
software and configured deployment environment must also be managed by an Administrator ID, or a
non-Administrator ID with its permissions elevated using Run As
Administrator.

## Custom installation

Choose custom installation to set up a production environment.

- You want to install on an existing installation of WebSphere Application
Server.
- Your deployment environment requires multiple cluster nodes.
- Your business requires complex deployment environment and database topologies.
- You prefer a silent installation.
- You are installing in Installation Manager group mode as a user in the installation
group.
- You are installing an online Workflow Server
that connects to a Workflow Center where a
customized context root has been set.
- You want a nonadministrative user ID to be able to perform server operations such as stopping
and starting the deployment environment or modifying profiles.