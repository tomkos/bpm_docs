# Adding an IBM ODM Decision Service
component to a service (deprecated)

## Before you begin

To perform
this task, you must be in the IBM Process
Designer desktop
editor, which is deprecated.

## About this task

IBM Business Automation Workflow integrates with IBM Operational Decision
Manager (formerly ILOG JRules) by providing an
IBM ODM Decision Service component. This rule
component enables you to use RuleApps available on an instance of Rule Execution Server for your
Business Automation Workflow implementations.

Why should you choose using an IBM ODM Decision Service component over creating a
standard web service when connecting to an instance of IBM ODM Rule Execution Server? The IBM ODM Decision Service component is specifically
designed for calling a IBM ODM decision
service. It has a closer conceptual mapping to the IBM ODM decision service called and, therefore, is a
more efficient representation of it in your business process model. A IBM ODM Decision Service component can handle decision
services hosted on either a WebSphere ILOG JRules BRMS 7.1, WebSphere Operational Decision
Management 7.5, or IBM Operational Decision
Manager Rule Execution
Server instance.

Conversely, the web service will treat the service called as it would any other generic service;
that is, the web service has no corresponding model representing the IBM ODM decision service called. Each time a new version
of IBM ODM is released, you will need to modify
the web service.

The following procedure describes how to use the IBM ODM Decision Service component to connect to an
instance of IBM ODM Rule Execution Server and
invoke the RuleApps and rulesets available on that server as decision services.

Before using the IBM ODM Decision Service
component in your Rules service, review the following requirements:

- For a secure connection to a Rule Execution Server instance running on WebSphere® Application
Server, you must provide the SOAP port and, if
necessary, the user name and password for the Rule Execution Server instance. This secure connection
enables you to choose the applications and rulesets that you want to use from  Rule Execution
Server.
- If you connect to a Rule Execution Server instance that is running on WebSphere Application
Server, but Rule Execution Server is not properly
configured for security or you are not able to provide the SOAP port, user name, and password, then
you cannot list the RuleApps and rulesets that are available on that Rule Execution Server instance.
In this case, you can manually enter the names of the RuleApps and rulesets that you want to use. If
the names that you provide are accurate, you can successfully generate types as described in the
following procedure.
- If you connect to a Rule Execution Server instance that is running on an application server
other than WebSphere, you cannot list the  RuleApps and rulesets available on that Rule Execution
Server. In this case, you can manually enter the names of the  RuleApps and rulesets that you want
to use. If the names that you provide are accurate, you can successfully generate types as described
in the following procedure.

## Procedure

To build a Decision service that includes an IBM ODM Decision Service component, complete these
steps:

1. Open the desktop Process Designer (deprecated).
2. Open a process application in the Designer view.
3. Create a Decision service.
4. Drag a IBM ODM Decision Service component
from the palette to the service diagram.
5. With the IBM ODM Decision Service
component selected, click the Implementation option in the Properties
tab.
6. In the Discovery section, enter the following information to connect to
a Rule Execution Server instance that contains deployed RuleApps that you want to use.

Table 1. Input required to connect to Rule Execution Server

Field
Action

Server
Select the server that you want from the list.

SOAP Port
Specify a port for the SOAP connection if Rule Execution Server is running on
WebSphere Application
Server.

User name
Enter the user name to use, if necessary, for a secure connection.

Password
Enter the password to use, if necessary, for a secure connection.

The SOAP port, user name, and password fields accept embedded JavaScript expressions, so
variables can be used to provide those values.
7. Click Connect.
8. In the Rule section, select the RuleApp that you want from the menu,
then select the version that you want to use.
If a secure connection to Rule Execution Server has not been established, the menu is not
populated. In this case, manually enter the name and version of the RuleApp and ruleset that you
want to use. The names must be accurate for the next step to work.
9. Click Generate Types.
10. In the Generating Types window, make sure the Generate
request/response wrapper types option is not selected.
Click Next.
11. Click Finish when type generation
is complete.
12. In the Properties section, click Data
Mapping.
13. Click the auto-map icon in the upper right corner of the Input Mapping section.
The Create variables for auto-mapping window opens, listing the
private variables needed for input parameters from the selected RuleApp.
14. Click to select each variable that you want to create in
your Decision service and then click OK.
15. Click the auto-map icon in upper right corner of the Output Mapping section.
The Create variables for auto-mapping window opens, listing the private variables needed
for output parameters from the selected RuleApp.
16. Click to select each variable that you want to create in
your Decision service and then click OK.
17. Use sequence lines to connect the IBM ODM
Decision Service component to the Start and End Events.
18. Save the new Decision service.

## What to do next

You can nest this Decision service in any other service
within your process application that requires the same logic. Be sure
to adjust the input and output variables as required for each implementation.
Refer to the related topic "Declaring and passing variables" for more
information.