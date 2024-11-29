<!-- image -->

# Creating a web service to implement a IBM Business Automation
Workflow task

## About this task

To create a web service that can be used by a case management
task, follow these steps:

## Procedure

1. Right-click your module in the Business Integration view and select New > External Service. In
the New External Service window, expand Case Management and select Web Service Implementation
of a Task. Click Next.
2. In the Specify Name and Location page,
the Module and Namespace fields will be filled but can be changed. If you want the generated
web service artifacts to be in a folder, add the folder name you want
or browse to a folder for the Folder field.
In the Name field, add a name for your web
service or accept the default name. Click Next.
3. In the Specify the Connection Information for
the FileNet Repository page, specify the type of connection
in the Connection field or accept the default
(HTTP). This connection is to the FileNet repository. In the Server and Port number fields,
add the appropriate values or accept the defaults (localhost with
a 9080 port). Add the relative path on the server in the Path field. Note that the port number and the path are
in different fields, however, as you enter them the complete URL is
shown beside Repository URL. In the User ID and Password fields, enter
the user ID and password. Note that these values will be checked and
an error message will be shown if they are not valid. Click Next.
4. In the Select a Task page, select
the task you want to implement as a service. At the highest level
of the tree structure are object stores. They contain solutions which,
in turn, contain case types. Each case type contains the tasks that
you can implement as a service. Tasks that cannot be selected are
already implemented. Click Next.
5. The Select the Input and Output Parameters page opens. For the input and output parameters of the task, select
the case type properties to use. Click Next.
6 The Specify the Process Properties page gives you the following options to complete building your webservice. Select the appropriate option and click Next .
    - Create a microflow. Select this option
if your service will invoke a business process that provides an immediate
response.
    - Create a long-running business process. Select this option if your service will invoke a business process
that runs for an extended time; that is, does not provide an immediate
response.
    - Do not create a business process. Select
this option if you want to choose all the components your service
uses. For example, your service implementation could use a mediation
flow component as the service implementation.
7 The Specify the Deployment Target pagedesignates the server where the service will be deployed to and ifsecurity will be used. The information is necessary for the case managementtask to locate the service at run time and determine the level ofsecurity. You have the following choices.

- You can enter the information for the Target server, that is, the Host name and Port
number fields. Then you can select if your service will
include security by selecting the Use security to access
the web service from the case management task check box.
Optionally, you can select the Use a secure socket (SSL)
connection check box. SSL refers to a Secure Sockets Layer
security. Selecting security does not impact your next steps, however,
you will need to do some extra work after you generate the web service
as indicated in the note below. Click Finish.Note: Clicking the security check boxes indicates your service will
use security. You must set the security up independent of this wizard.
See Security for exports and imports used with IBM Case Manager tasks.
- Click New and follow these steps:
    1. In the Define a New Server page, enter the
appropriate values for the Server's host name, Select the server type, Server
name and Server runtime environment fields. Selecting a server from the pane where the servers are listed
will fill these fields for you. Click Next.
    2. The following pages may vary depending on the server you selected
but the pattern is similar. For example, if you had chosen Workflow Server  then
the WebSphere Application Server Runtime Environment page opens. The name of the server that was previously specified
previously appears in the Name field. Enter
or browse to the installation directory to complete the Installation directory field. Click Next.
    3. In the WebSphere Application Server Settings page, add or select the appropriate values for the profile name
and server connection types and administrative ports. Select if security
will be enabled and, if so, the user ID and password. Enter the application
server name. At this point you can click Finish and be returned to the Specify the Deployment Target page where you can complete generating your service with or without
security. Alternately, you can click Next and
follow the next step to deploy your service to the server, which we
will do for instruction purposes.
    4. The Add and Remove Projects page opens. Select
your project from the Available projects pane
and click Add. Click Finish.
    5. The Specify the Deployment Target opens.
All the fields are completed based on the information from the previous
pages. You can select if your service will include security by selecting
the Use security to access the web service from the case
management task check box. Optionally, you can select Use a secure socket (SSL) connection check box. SSL refers
to a Secure Sockets Layer security. Selecting security does not impact
your next steps, however, you will need to do some extra work after
you generate the web service as indicated in the note below. Click Finish.Note: Clicking the security check boxes indicates
your service will use security. You must set the security up independent
of this wizard. See Security for exports and imports used with IBM Case Manager tasks.
8. The service is generated. If had selected a microflow,
you will see an export and a business process. If you had selected
a long-running business process, you will see in the assembly editor
an export, a business process and an import. The business process
will be a skeleton business process for you to complete. If you chose
to not create a business process, only the web service export will
be shown in the assembly editor. In the Business Integration view beneath your module, you will find the artifacts expected such
as an interface, business object, web service port, process, export
and import (for a long-running business process).

## What to do next

The service you generated contains critical information
that lets your service interact with a specific task on a specific
server. Therefore you should not modify the generated code as explained
in Working with generated code.

## Related concepts

- Design considerations for web services used with IBM Business Automation Workflow tasks

## Related tasks

- Editing and validating exports used with IBM Business Automation Workflow activities

## Related reference

- Deleting a web service export used with a IBM Business Automation Workflow task