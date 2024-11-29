# Creating custom desktops

## About this task

Use IBM Content
Navigator to define as many desktops as your
planned environment requires.

When you register a target environment, the target object store
repository is added both to the specified desktop and to the master IBM Content
Navigator desktop for IBM Business Automation
Workflow, baw.

## Procedure

To create a custom desktop to use with IBM Business Automation
Workflow:

1. Define a new desktop in the IBM Content
Navigator web client administration
feature.
For the authentication repository, specify a repository
for the Content Platform Engine domain
that you are using for your IBM Business Automation
Workflow environment.
2. Use the tasks for defining and registering your target
environments to add the desktop to your target environment.

## What to do next

Define and register your target environments. If you want to use the Case administration client on your custom desktop,
use IBM Content
Navigator to
add that feature to your desktop. You can also create a desktop that includes the administration
client feature without associating target environments with that desktop, if the authentication
repository is a FileNet P8 object store from the correct domain. You can also further customize your
desktop by using IBM Content
Navigator functions, such
as restricting access to the desktop to a specific list of users or applying a theme to control the
colors and images that display in the interface.

If you have a solution page that uses the Case Information widget or
Content List widget and the widget includes the Documents view, you can
choose to display a check box beside each document in the list of documents. The check box feature
is disabled by default, but you can enable it in the IBM Content
Navigator administration desktop by changing the
Content list checkboxes control to the Show state. For
more information about enabling the check box feature, see the topic Tips for working in IBM Content Navigator.