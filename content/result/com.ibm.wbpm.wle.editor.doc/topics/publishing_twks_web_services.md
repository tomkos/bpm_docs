# Publishing IBM Business Automation Workflow web
services

## Before you begin

To perform
this task, you must be in the IBM® Process
Designer desktop
editor, which is deprecated.

## About this task

You can create and publish a web service to enable
external applications to initiate a particular Business Automation Workflow service
or set of services. Using a SOAP integration, external applications
can call the web service.

Follow these steps to create a web service that external applications
can call:

## Procedure

1. Open the desktop Process Designer (deprecated).
2. Open a process application in the Designer view.
3. Select the plus sign next to the Implementation category
and then select Web Service from the list.
4. In the New Web Service window, type
a name for the service and then click the Finish button.
5. In the Common section, you can type a description of the
web service in the Documentation text box.
6. In the Operations section, click the Add button
to choose an existing service to add. Because the services
that Business Automation Workflow initiates
from a web service do not have an associated task, do not add services
that include the following components: Coach, Modify Task, and Browser
Script. See Service components in Process Designer for more information
about these components.
7. Under Operation Details, type a name for the selected service
in the Operation Name text box. (Change Untitled to
the name that you want.)
8. Optionally, you can type a description of the operation
in the Documentation text box.
9. Click the Add button in the Operation
section to continue adding services.
10. In the Behavior section, enable the Protected check box
if you want access to the WSDL URI to be password-protected. If password-protected,
a user must supply a user name and password to access the operations
described in the WSDL URI.
11. In the Behavior section, click the WSDL URI to view the
XML description of the resulting web service and its elements and
operations. You can supply this URI to the developers who
need to call the operations within the web service.
12. Include a message event in your BPD for the incoming request
as described in Modeling events.
13. Create an undercover agent that calls this web service
as described in Undercover agents and
then attach the undercover agent to the event from the preceding step.

## What to do next