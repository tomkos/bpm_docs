# Roadmap to running projects on containers

You can develop your projects in Workflow Center
and run them in Workflow Server on containers. Start
by getting your existing process apps and toolkits ready to run in containers, playback and test and
then install and run them in a production container environment.

<!-- image -->

## Prepare to convert your projects

You can complete your move to containers in stages. First, move your process apps and toolkits
from desktop Process Designer to the web-based
Process Designer to make them container compatible.
When you're ready, you can install IBM® Business Automation
Workflow on
containers and move your projects to run in the container environment. For more information, see
Prepare your projects for containers.

## Convert your projects

Convert your toolkits first. Then, when you're converting your process app, you can simply select
the container compatible version of a toolkit that the process app has a dependency on.

IBM Process
Designer provides conversion tools
that validate the artifacts in a project and the toolkits it depends on, provide a list of the
artifacts that you need to convert and guide you through the conversion process. For more
information, see Converting the target environment of projects.

## Play back and test

You can run, test, and debug your processes and services in the Process Designer Inspector running in the Workflow Center server just as you do for projects that are
running in the traditional environment. For more information, see Running and debugging processes and services.

When you're happy with the playback, you can test your application more thoroughly by installing
and running it in a test workflow server in a container.

## Install snapshots

You can install snapshots to a container environment from IBM Workflow
Center for an offline or online Workflow Server, just as you do for traditional projects. To
automate snapshot installation, you must use REST APIs. See Operations REST APIs.

## Administer snapshots and applications

Use the Process Admin Console to view, manage and
administer snapshots.

- You can administer and configure runtime settings for snapshots that are installed on a workflow
server. See Managing installed snapshots.
- You can use Process Inspector to view, manage and troubleshoot process instances. See Administering processes with the Process Inspector.

To automate administrative tasks for snapshots that are installed in containers, you must use
REST APIs. See Operations REST APIs.

## Work on tasks

End users can orchestrate, prioritize, track, and complete their tasks in Workplace.Or, they can work on their tasks
as usual in Process Portal.
For limitations, see Limitations.

## Visualize business data

You can integrate IBM Business Process Manager
 in containers with
IBM Business Automation
Insights and get
insight into the performance of individuals and teams by viewing a dashboard of statistics such as
the status of user tasks and the workloads of teams or individuals. For information on how to
integrate Business Automation Insights,
see IBM Business Automation Workflow Runtime and Workstream Services
parameters. For information on how to use Business Automation Insights, see IBM Business Automation
Insights.