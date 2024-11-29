# Running the Case configuration tool tasks for the
development environment

## About this task

- (Always required)
Register the Administration Console for Content Platform Engine (ACCE) Plug-in (deprecated)
- (Always required)
Configure the case management object stores
- (Always required)
Define the default project area
- (Always required)
Configure the case integration with Business Automation Workflow
- (Always required)
Deploy the Content Platform Engine Workflow Service
- (Always required)
Deploy the Content Platform Engine Gateway Service (not available for Content Platform Engine in a container)
- (Always required)
Register the Business Automation Workflow plug-in
- (Always required)
Register the Case Management Services plug-in
- (Always required)
Register the case widgets package
- (Always required)
Register the Case Administration Client plug-in
- (Conditionally required)
Configure the Box collaboration
- (Conditionally required)
Register the Case Box Event Listener plug-in
- (Required)
Register the project area
- (Conditionally required)
Configure the business rules
- (Always required)
Register the Case Monitor widgets package
- (Conditionally required)
Register the external data service
- (Conditionally required)
Deploy and register the custom widgets package
- (Conditionally required)
Deploy and register the extensions package

## Register the Administration Console for Content Platform Engine (ACCE) Plug-in
(deprecated)

Always required if you use the embedded Content Platform Engine.  This task registers the
plug-in for the Administrative Console for Content Engine (ACCE) so that you can run the ACCE from
IBM Content
Navigator.

### About this task

<!-- image -->

<!-- image -->

- If you use an external IBM Content
Navigator, enter the
correct configuration values for your environment.
- As of Business Automation Workflow
V21.0.3, the ACCE has been removed. Use the ACCE console that is embedded in the Content Platform Engine. See Using the IBM Administration Console for Content Platform Engine.

Back to top

## Configure the case management object stores

Required for each target object store in your environment. This task
installs the case management add-ons for the case management design and target object stores, and
creates the required events and subscriptions in the Content Platform Engine. The case management
add-ons are custom implementations of classes, objects, and properties that extend the core Content Platform Engine features.

### About this task

<!-- image -->

Back to top

## Define the default project area

This task defines the default project area for the development environment. A project
area groups solutions in the design object store so that the entire object store is not affected
when you reset the test environment. Only users who are assigned to a project area can log on to
Case Builder.

### About this task

<!-- image -->

Back to top

## Configure the case integration with Business Automation Workflow

This task configures the connection between the case components and the
Business Automation Workflow host
server.

### About this task

<!-- image -->

- If you have multiple project areas in the profile, you need to run this task multiple times
against each one.

- Business Automation Workflow user name -
The user specified for this field is the Business Automation Workflow integration user. The
integration user is used by Case components to interact with Workflow components and requires
administrative permissions on Workflow assets. Thus ensure that the user specified for this task is
a member of tw\_admins security group in Business Automation Workflow.

Back to top

## Deploy the Content Platform Engine Workflow Service

This task configures the Content Platform Engine Workflow Service, which
uses a Web Services Reliable Messaging Protocol to ensure that requests are sent to Business Automation Workflow. The integration service
is required by the case components to provide communication between the Content Platform Engine server and the Business Automation Workflow server.

### About this task

<!-- image -->

Back to top

## Deploy the Content Platform Engine Gateway Service

(Not available for Content Platform Engine in a container) This task
configures the Content Platform Engine
Gateway Service (baw-interface), which implements installation of the CPE-BAW integration on CE
application server. This integration service is required by the case components to provide
communication between the Content Platform Engine server and the Business Automation Workflow server. This integration
service facilitates Business Automation Workflow activity process
creation, update, and completion. FileNet activities are not dependent on this integration service.
Case functions are impacted if this integration service is not running.

### About this task

<!-- image -->

Back to top

## Register the Business Automation Workflow plug-in

This task registers the plug-in for Business Automation Workflow that provides a unified
content workflow by bringing Workplace into an IBM Content
Navigator desktop. You
can then view your Workplace tasks in a desktop, claim them, and work on them just as you do in Workplace.

### About this task

<!-- image -->

Back to top

## Register the Case Management Services plug-in

This task registers the plug-in for IBM Content
Navigator that
contains the case management services that are used by other components.

### About this task

<!-- image -->

Back to top

## Register the case widgets package

Required to enable Case Client and the default widgets
package.  This task imports and registers the Case Client widgets package with the
case components, and registers the plug-in for the widgets package with the IBM Content
Navigator server.

### About this task

<!-- image -->

- Do not modify the file path that is predefined for the case widgets package.
- If you are using an external IBM Content
Navigator, enter the
correct configuration values for your environment.

Back to top

## Register the Case Administration Client plug-in

This task registers the plug-in for IBM Content
Navigator that
contains the administration client for the case components.

### About this task

<!-- image -->

Back to top

## Configure the Box
collaboration

Required if you want to enable case workers to use Box. This task configures the
connection to the Box
server.

### About this task

Back to top

## Register the Case Box Event Listener plug-in

Required if you want Box events to trigger the creation
of cases or work items. This task registers the plug-in for IBM Content
Navigator that listens
for case-related Box
events when Box
collaboration is enabled.

### About this task

<!-- image -->

Back to top

## Register the project area

This task registers a project area with an IBM Content
Navigator desktop,
creates default Case Client
and Case administration client desktops,
configures repositories for the case management design and target object stores, and adds the
Case Client feature to the
desktop. Also, this task configures the Case Operations component queue and configures the project
area's isolated region to work with solution workflows.

### About this task

<!-- image -->

Back to top

## Configure the business rules

Required only for target environments that are configured for business
rules. This task configures business rules for your environment and configures the Rules Operations
component queue.

### About this task

<!-- image -->

- Before you run this task, you must run the Register the project area
task.
- If you have multiple target environments in the profile, you need to run this task multiple
times, once against each target environment.

<!-- image -->

- During run time, rules are stored in the rules repository that you specify, which is located onthe Content Platform Engine server. Ifyou run this task again to change the location of the rules repository directory after you deployany solution, complete the following steps after you run the task:
    1. Stop the Content Platform Engine
server.
    2. From the previous rules repository directory, move the res\_data directory
to the new location of the rules repository directory. In a cluster environment, the rules directory
must be a shared directory that can be accessed by all Content Platform Engine cluster servers.
    3. Restart the Content Platform Engine
server.
- You can select only one locale in which to write the business rules for your solutions. If you
must create solutions with business rules in other locales, rerun this task to change the rule
persistence locale before you create the solution. After the first rule for a solution is saved, the
rule persistence locale cannot be changed.

Back to top

## Register the Case Monitor widgets package

Required to enable Case Monitor. This task imports and
registers the Case Monitor
widgets package with the case components, registers the plug-in for the widgets package with the
IBM Content
Navigator
server, and creates the Case Monitor desktop.

### About this task

<!-- image -->

- Do not modify the file path that is predefined for the Case Monitor widgets package.
- If you are using an external IBM Content
Navigator, enter the
correct configuration values for your environment.

Back to top

## Register the external data service

Required only for access to data from a source other than Content Platform Engine.  This task registers an
external data service for use with a solution.

### About this task

Back to top

## Deploy and register the custom widgets package

Required if you want to use a custom widgets package. This task imports and
registers the custom widgets package with the case components, registers the plug-in for the widgets
package with the IBM Content
Navigator, and deploys
the EAR file in the widgets package to the web application server, if present.

### About this task

<!-- image -->

- If you run this task in a cluster environment, you must ensure that the plug-in is loaded on
each node of the cluster. Either restart the cluster to force the plug-in to be loaded on all nodes
or manually load the plug-in on each node by using the IBM Content
Navigator
administration client.
- If you are using an external IBM Content
Navigator, enter the
correct configuration values for your environment.

Back to top

## Deploy and register the extensions package

Required only when you add an extensions package for a custom property
editor or controller. This task imports and registers the extensions package with the case
components, registers the plug-in for the extensions package with the IBM Content
Navigator server, and
deploys the EAR file in the extensions package to the web application server, if
present.

### About this task

<!-- image -->

- If you run this task in a cluster environment, you must ensure that the plug-in is loaded on
each node of the cluster. Either restart the cluster to force the plug-in to be loaded on all nodes
or manually load the plug-in on each node by using the IBM Content
Navigator
administration client.
- If you are using an external IBM Content
Navigator, enter the
correct configuration values for your environment.

Back to top