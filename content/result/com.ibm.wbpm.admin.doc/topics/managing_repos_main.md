# Workflow Center

Workflow Center provides a convenient
location for you to create and maintain high-level library items such as process apps, case
solutions, and toolkits (collectively known as projects).

As a developer, you work on a project in either Process Designer or Case Builder. If you are primarily an administrator and don't
actively work in Process Designer or Case Builder, Workflow Center enables you to manage snapshot
creation and deployment as well as manage access to the Workflow Center repository by setting up the appropriate
authorization for users and groups.

## Overview

IBM® Business Automation Workflow
brings together the process and case management portfolios, enabling you to manage and deploy
unified process apps and case solutions through a common Workflow Center and grant other users access to those
projects.

The architecture of IBM Business Automation
Workflow and
its runtime environments is shown in the following topology diagram:

<!-- image -->

- From Workflow Center, administrators
install projects that are ready for testing or production on the Workflow Servers in those environments. For a quick review of the
types of projects that you can manage in the Workflow Center, see Workflow projects.
- Using IBM Process
Designer create process
models, services, and other assets within process applications, case solutions, and toolkits. Using
Case Builder, you focus on case solutions. For more
information, see Process Designer and Case Builder.
- Using the tools in IBM Integration
Designer, create
integration logic for invoking and exposing services, and to create BPEL processes that integrate
applications and data. For more information, see Getting started with IBM Integration Designer.
- In addition to a repository to store and maintain projects, Workflow Center includes a Workflow Center server for playbacks.
- The traditional runtime environment is based on WebSphere® Application Server. The container
runtime environment is based on IBM WebSphere Liberty. For more information, see Runtime environments.

## Starting Workflow Center

Depending on your requirements, you should start the appropriate Workflow Center. The classic Workflow Center includes a repository
for all processes, services, and other assets created in Process Designer and Integration Designer. However, an enhanced Workflow Center is now available that
includes the same repository but is optimized for working with both processes and associated case
solutions. If you don't want to use the enhanced Workflow Center interface, you can
continue to work with your process apps and toolkits in the classic Workflow Center. The Workflow Center repository is the same
as in previous releases, and regardless of which interface you use, the projects reside in the same
repository.

- Load the enhanced Workflow Center URL in a web browser,
for example https://servername:9443/WorkflowCenter.
- Load the classic Workflow Center URL in a web
browser, for example https://servername:9443/ProcessCenter.

<!-- image -->

Basic and Advanced modes in the Workflow Center

In the Workflow Center, you can create and manage
projects (case solutions, templates, process apps, and toolkits). By default, you log in to the
Workflow Center in Basic mode, which offers access
to simplified views. To gain access to advanced views in the Workflow Center and to perform administrative actions, such
as managing connections, users, user groups, and permissions, you must be in the Advanced mode.

To change the view mode, click your user name in the landing page toolbar, select
Preferences, and use the slider to select the mode that you need.

- Create, import, edit, sort, and manage case solutions, which you can then deploy and play back
for testing purposes.
- Create templates that you can use as starting points for other new case solutions.
- Create, import, edit, export, sort, and archive process apps.
- Create, import, export, edit, and sort toolkits.
- Change user preferences and localize user interfaces.
- (Advanced only) Perform administrative actions, such as adding and removing users and user
groups, and assigning read, write, and admin permissions to users and groups.