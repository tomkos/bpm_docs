# Integrating with Operational Decision Manager

## About this task

As an alternative to creating business rules in Case Builder, you can create and deploy
rules in Operational Decision Manager to allow
more sophisticated decisions and a full range of management capabilities.
You can also export rules that you created in Case Builder and deploy them in Operational Decision Manager.

You can deploy Operational Decision Manager to a dedicated
server cluster.
Alternatively,
you can collocate Operational Decision Manager on an existing
server. Operational Decision Manager is compatible with
various application servers, including WebSphere® Application
Server.

Operational Decision Manager allows
rules to be independently managed and exposed as web services. These
decision services can be imported into IBM Business Automation
Workflow and called by Content Platform Engine to allow workflow steps
to be controlled by the rules without modifying the workflow definition.

## Procedure

To install Operational Decision Manager:

- Exporting business rules to IBM Operational Decision Manager

You can export business rules to IBM Operational Decision Manager by using the IBM Business Automation Workflow Case administration client. For example, you might want to export to IBM Operational Decision Manager to manage your IBM Business Automation Workflow rules along with rules from other parts of your business in a single application.
- Adding business rules from IBM Operational Decision Manager to a solution

You can add business rules from IBM Operational Decision Manager to the steps of the workflow definition for a task, and then modify the business rules without modifying the workflow definition.