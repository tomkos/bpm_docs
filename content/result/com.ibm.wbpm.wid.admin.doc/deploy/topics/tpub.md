<!-- image -->

# Publishing changed resources to servers

## About this task

To publish changed resources to servers:

## Procedure

1. In the Business Integration perspective, click the Build
Activities tab. (If the Build Activities tab
is not visible, open either the Business Integration view or the Physical
Resources view and click the Show Build Activities View icon .) The Build Activities
view opens.
2. If the Project status section is
not yet expanded in the Build Activities view, expand it.
3. If the Status column for a server
indicates that an integration module or component test project requires
republishing (because it contains new, changed, or deleted resources),
click the Update Running Servers button. The
View and Publish Changes to Servers window opens. In
the Changes that will be published list, a
tree view displays the new or changed workspace resources that are
candidates for publishing to one or more of the supported servers
displayed in the Project Status section of
the Build Activities view. If the new, changed, or deleted resources
occur solely in business integration modules, component test projects,
or libraries, the tree view is displayed in logical mode. However,
if new, changed, or deleted resources are found in Java or Java 2
Platform Enterprise Edition projects, the tree view is displayed in
physical mode.
4. If you want to toggle the tree view between logical mode
and physical mode, click the Tree Mode button .
5. If you want to disable the View and Publish Changes to
Server window and prevent it from being displayed again, select the Do
not show this window again check box. (If you choose to
disable the window, you can later enable it again by following the
instructions in the topic "Disabling or enabling the Publish Changes
window".)
6. Click Publish to publish all of
the changed resources to the servers.  If you notice
timeout exceptions or out of memory exceptions, it might be caused
by the size of your resources. See "Preventing timeout and out-of-memory
exceptions during installation or deployment."