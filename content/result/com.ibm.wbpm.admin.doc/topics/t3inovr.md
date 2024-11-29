<!-- image -->

# Deploying BPEL process and human task applications

## Before you begin

Verify that Business Flow Manager and Human Task Manager
are installed and configured for each application server or cluster
on which you want to deploy your application.

## About this task

## Results

After a BPEL process or human task application is deployed,
all of the BPEL process templates and human task templates are put
into the start state. You can create process instances and task instances
from these templates.

## What to do next

Before you can create process instances or task instances,
you must start the application.

- How BPEL process and human task applications are deployed in a network deployment environment

When process templates or human task templates are deployed in a network deployment environment, the following actions are performed automatically when the application is deployed.
- Deployment of BPEL processes and human tasks

Use Integration Designer or the serviceDeploy command to package process components or task components in an enterprise application (EAR) file. Each new version of a model that is to be deployed must be packaged in a new enterprise application.
- Deploying BPEL process and human task applications interactively

You can deploy an application interactively at run time using the wsadmin tool and the installInteractive script. You can use this script to change settings that cannot be changed if you use the administrative console to deploy the application.
- Migrating BPEL processes

When you deploy a new version of a BPEL process, you might want the latest process version to apply to both new process instances and to process instances that have already started. To migrate running BPEL process instances to a new version of the process, you can use either an administrative script to migrate process instances in bulk or Business Process Choreographer Explorer to migrate specific instances.
- Undeploying BPEL process and human task applications, using the administrative console

You can use the administrative console to undeploy applications that contain BPEL processes or human tasks.
- Undeploying BPEL process and human task applications, using an administrative command

Use the manageTemplates.py administrative script to start or stop process and task templates that belong to a particular application. This script can also uninstall BPEL applications and human task applications, and you can have the opportunity to verify whether the application disappeared from the installed application list after a successful uninstallation.