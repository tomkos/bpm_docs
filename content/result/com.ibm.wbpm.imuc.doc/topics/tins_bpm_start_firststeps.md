# Starting your environment by using Quick Start

A version of the Quick Start console is available for each deployment
environment in your installation, and can be used to manage that deployment
environment. Options on each console are displayed dynamically, depending
on features you install and the availability of elements on each operating
system. Options might include starting or stopping the server or deployment
manager, accessing the administrative console, and accessing the product
documentation.

You will usually want to start the Quick Start console
for a deployment environment. The following section provides detailed
information about starting a Quick Start console
based on the installed platform.

- Install Firefox in a location without a space in the path name.
- Alter the registry key to remove the space.
- Temporarily set Internet Explorer as the default browser, and then set Firefox as the default
browser. This approach automatically removes the space from the registry key.

- The Quick Start console might not start if the system
has the maximum number of open files set to an insufficient value. To change the default setting,
see Warnings about GTK or ulimit on Linux or UNIX when installing or migrating, and then try starting the Quick Start console again.
- Business Automation Workflow does not support runtime
provisioning in WebSphere® Application
Server. Disable the feature
before you start the environment. In the WebSphere Application
Server
administrative console, click Servers > Server Types > WebSphere application servers, select the application server, and clear the Start components as
needed option.

## Starting the Quick Start console for
a deployment environment on Linux®, UNIX, and Windows platforms

To start the Quick Start console for
a deployment environment, complete the following steps:

1. Open a command window.
2. Change to the following directory, where
installation\_root represents the installation location of
the IBM Business Automation Workflow:
installation\_root/bin/
3 Enter the following command to start the console:
    - BPMQuickStart.sh <deployment\_environment\_name>
<profile\_name>
<admin\_user\_name>
<admin\_user\_password>
    - BPMQuickStart.bat <deployment\_environment\_name>
<profile\_name>
<admin\_user\_name>
<admin\_user\_password>

- profile\_name is the deployment manager profile.

- Click Start > Programs > IBM > WorkflowCenter  OR WorkflowServer > Quick Start.
- Click Applications > IBM > Business Automation Workflow Edition
Version > Deployment Environments > profile\_name > deployment\_environment\_name > Quick Start.
- Click Applications > IBM > WorkflowCenter  OR WorkflowServer > Quick Start.

## Related information

- Starting and stopping your environment
- Troubleshooting server tools after a typical installation on Windows