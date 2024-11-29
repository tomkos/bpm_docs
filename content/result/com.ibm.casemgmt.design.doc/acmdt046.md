# Defining and registering target environments

## Before you begin

## About this task

The first time that you run the Case configuration tool to configure the
production environment after you install IBM® Business Automation
Workflow, you must define at least one
target environment. Later, you can use the Case administration client to define more target
environments as needed to support your solutions.

A target environment definition specifies the target environment to which a solution
is deployed. It contains information about the connection point and a logical to physical page
mapping. By using the connection point, the target object store is discovered and the region number
isolated.

When you define a target environment, you select the connection point for the target object
store. Multiple connection points for the same target object store can exist. If required to support
solutions that you upgrade to Case Manager 5.2, multiple target environments can share the same
connection point.

When you register a target environment, you select the Case Client desktop that you want to use
to access solutions that are hosted in the target environment. You also specify credentials for the
user ID that you want to use to run workflows for case operations.

## Procedure

To define and register a new target environment by using the Case configuration tool:

1 Enter the appropriate command for your environment: Option Description AIX®Linux®Linux for System z® Windows Perform one of the following actions:

| Option                            | Description                                                                                                                                                                                                                                                                                    |
|-----------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| AIX®  Linux®  Linux for System z® | Change to the install\_root/configure/CaseManagement/ directory. install\_root is the location where IBM Business Automation Workflow is installed. Run the following command:./configmgr                                                                                                        |
| Windows                           | Perform one of the following actions: Click Start  > All Programs > IBM Business Automation Workflow > Case configuration tool. Run the following command:install\_root\configure\CaseManagement\configmgr.exeinstall\_root is the location where IBM Business Automation Workflow is installed. |

2. Click File > Open
profile and select a production environment
profile.
3 After the list of configuration tasks is displayed, edit,save, and run the following tasks:

- Define Target Environment
- Register Target Environment

To define and register a new target environment by using the Case administration client:

1. Start the Case administration client.
 Enter the following URL in a browser:
http://server:port/navigator/?desktop=bawadmin
where
server is the IBM Content
Navigator IP address or
fully qualified server name, and 
port is the
IBM Content
Navigator port
number.
2. From the list of object stores in the navigation tree in
the left pane, select a staging object store to open it. Click Target
Environments.
3. On the Target Environments page in
the right pane, click Define and complete the
wizard steps.
4 Register the target environment:
    1. On the Target Environments page
in the right pane, select the target environment that you want to
register.
    2. Click Actions > Register and complete the wizard
steps.

## What to do next

- Configure IBM Business Automation
Workflow
- Configure Business Rules
- Register the External Data Service