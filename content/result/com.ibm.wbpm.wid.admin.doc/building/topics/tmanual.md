<!-- image -->

# Invoking manual builds

## Before you begin

## About this task

## Procedure

1. In the Business Integration perspective, click the Build
Activities tab. (If the Build Activities tab
is not visible, open either the Business Integration view or the Physical
Resources view and click the Show Build Activities View icon .) The Build Activities
view opens.
2 In the Manual triggering of workspace buildactivities section, complete one of the following tasks:
    - If you want to invoke an immediate manual build that validates
your business integration projects and generates deploy code for your
integration modules and component test projects, click the Update
Deploy Code button. (Alternatively, you can select the Projects
> Business Integration Projects > Update Deploy Code menu
item.)
    - If you want to invoke an immediate manual build that validates
your projects and generates deploy code, plus updates the integration
modules and component test projects that currently reside on running
servers, click the Update Running Servers button.
Alternatively, you can select the Projects > Business Integration
Projects > Update Running Servers menu item.
3 If you want a greater degree of synchronization betweenthe projects that exist in your workspace and the projects deployedon the server, you can remove your projects from the server and completelyregenerate your deploy code and backing projects by completing thefollowing steps:

1. From the Project menu, select Business
Integration Projects > Regenerate Deploy Code and Reinstall on Servers.
The Regenerate window opens.
2. In the window, choose All projects to
have all of the projects updated or choose Selected projects to
select individual projects that you want to update.
3. Choose Perform all actions to
have all of the actions performed on the selected projects or choose Perform
the selected actions to select individual actions to perform
on the selected projects.
4. Select one or more of the following actions: 
Action
Description

Remove projects from server
Removes the selected projects from any server on which they
are deployed. If you do not currently have any projects deployed to
the server or if you have only selected the names of libraries, selecting
this check box will not result in any corresponding action.

Regenerate backing Java EE projects
Regenerates the supporting Java EE projects. This action
is not available unless you have selected the Remove projects
from server action.

Redeploy projects if server started
Redeploys the projects to the server after all other actions
have been completed. If the server is not started, then the projects
are not redeployed. This action is not available unless you have selected
the Remove projects from server action.

Clean projects
Cleans the projects in a manner similar to selecting the Project
> Clean menu item. 

Regenerate XSLT files for XML maps
Regenerates the XSLT files for any XML maps. This action
is not available unless you have selected the Clean projects action.
5. Click OK. Your selections will
be retained and available when you next launch the window.