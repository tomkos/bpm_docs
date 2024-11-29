# Enabling and disabling plug-ins for the IBM Business Automation
Workflow
desktop

## About this task

Previously, IBM Content
Navigator loaded all plug-ins, even if a plug-in
was not needed for the layout or features included in a desktop. IBM Content
Navigator displays the registered plug-ins so that you can enable all
plug-ins for the desktop or select only the plug-ins that are needed.

- IBM Business Automation
Workflow API plug-in
- IBM Business Automation
Workflow client plug-in
- IBM Business Automation
Workflow custom plug-in
- Content Platform Engine Applets Support plug-in

The Case configuration tool selects the IBM Business Automation
Workflow administration plug-in to be loaded for the
IBM Business Automation
Workflow Case administration desktop. If
Box collaboration is enabled, the Case configuration tool also selects the IBM Business Automation
Workflow API plug-in and Case Box Event Listener plug-in to be loaded.

- IBM Business Automation
Workflow API plug-in
- IBM Business Automation
Workflow client plug-in
- IBM Case Dashboard plug-in

You can configure the desktop to disable one or more of plug-ins or to enable other plug-ins for
use with the IBM Business Automation
Workflow desktop or IBM Business Automation
Workflow administration desktop.

The IBM Business Automation
Workflow Case configuration tool  does not affect the plug-ins
that are loaded for a custom desktop.

## Procedure

To enable or disable a plug-in for the IBM Business Automation
Workflow
desktop:

1. Log in to IBM Content
Navigator as an
administrator.
Enter the following URL in a browser:
http://server:port/navigator
server
is the IBM Content
Navigator
server name or IP address.
port is the IBM Content
Navigator port
number.
2. Navigate to Desktops > IBM Business Automation
Workflow > General.
3. In the Plug-ins area, select Select the deployed plug-ins to
enable for use with this desktop. Then, select the plug-ins that you want loaded for the
IBM Business Automation
Workflow desktop and clear the check box for any plug-in that
you do not want loaded.

## What to do next

After you enable or disable plug-ins for a desktop, ensure that the desktop works as expected.
For example, ensure that Case Client works correctly with the
Content Platform Engine Support Applets plug-in that is used to host Process
Designer and with any custom widgets packages.