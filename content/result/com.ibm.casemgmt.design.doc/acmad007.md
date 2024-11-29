# Creating a target object store

## Before you begin

## Procedure

To create a target object store for a project area:

1 Create an object store in IBM®FileNet® P8 . For more information, see Defining object stores .
    1 In the object store creation wizard, on the page where you specify the add-ons toinstall, click Default Application Configuration to select the add-ons thatare required by IBM Business AutomationWorkflow .
        - Content Engine base extensions are required for all Content Platform Engine configurations.
        - Base application extensions are a prerequisite for search extensions and the Workplace base
extensions.
        - Search extensions are required to browse and search for content in IBM Content
Navigator.
        - Workplace
base extensions are required to browse and search for content in IBM Content
Navigator
        - Workplace
template extensions are required to open folders in IBM Content
Navigator.
2. If you have not already created a workflow system to contain
isolated regions, create one now.
For more information, see Creating a workflow system.
3 Convert the object store to a case management target objectstore.

1. Start the IBM Business Automation
Workflow
Case administration client .
 Enter the following URL in a
browser:
http://server:port/navigator/?desktop=bawadmin
server
is the IBM Content
Navigator
server name or IP address.
port is the
IBM Content
Navigator port
number.
2. In the navigation tree in the left pane, right-click
the object store, select Convert to Target Object Store,
and complete the wizard steps.

## What to do next