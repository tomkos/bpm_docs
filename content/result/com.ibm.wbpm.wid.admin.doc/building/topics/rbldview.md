<!-- image -->

# Build Activities view

In the Business Integration perspective, you can open
the Build Activities view by clicking the Build Activities tab.
(If the Build Activities tab is not visible,
you can open it by first opening either the Business Integration view
or the Physical Resources view and then clicking the Show
Build Activities View icon .) The Build Activities
view is shown in the following figure:

- 1 Select workspace activities to run during a build
- 2 Manual triggering of workspace build activities
- 3 Project status

These three sections are described in the following sections.

## The "Select workspace activities to run during a build"
section

In this section of the Build Activities view, you
can specify the build activities that you want to have invoked whenever
an automatic build or a manual build occurs as a result of selecting
one of the following menu items from the Project menu:

- Build All
- Build Project
- Build Working Set
- Clean
- Build Automatically

- Validate
- Validate and update deploy code
- Validate, update deploy code, and update running servers

If the Validate button is selected,
all workspace resources are validated whenever a build occurs.

If
the Validate and update deploy code button
is selected, all workspace resources are validated and deploy code
is generated whenever a build occurs. (This is the default selection.)
If deploy code has not yet been generated for one or more of your
integration modules or component test projects, selecting this button
will invoke an immediate build and the generation of deploy code.

If
the Validate, update deploy code, and update running servers button
is selected, all workspace resources are validated and deploy code
is generated whenever a build occurs, plus any integration modules
or component test projects that currently reside on running servers
will be automatically updated on completion of the build. If deploy
code has not yet been generated for one or more of your integration
modules or component test projects, selecting this button will invoke
an immediate build and the generation of deploy code, plus any integration
modules or component test projects that currently reside on running servers
will be automatically updated when the build completes.

Whenever
a build occurs, all of the buttons are disabled until the build has
completed.

If you close the Business Activities view after selecting
one of the buttons, your selection will be retained even though the
view has been closed.

## The "Manual triggering of workspace build activities"
section

- Update Deploy Code
- Update Running Servers

If you click the Update Deploy Code button
and your deploy code is not currently up-to-date, an immediate manual
build is invoked that validates your resources and generates deploy
code. If your deploy code is already up-to-date, a build will not
occur and a message will explain the reason. Note that the Update
Deploy Code button has a corresponding menu item (Projects
> Business Integration Projects > Update Deploy Code)
that has the same behavior as the button.

If you click the Update
Running Servers button and your deploy code is not currently
up-to-date, an immediate manual build is invoked that validates your
resources, generates deploy code, and updates any integration modules
or component test projects that currently reside on running servers.
If your deploy code is already up-to-date and the integration module
is already synchronized with the server, a build will not occur and
no attempt will be made to republish the integration module on the
server. A message will be displayed to explain the reason. Note that
the Update Running Servers button has a corresponding
menu item (Projects > Business Integration Projects > Update
Running Servers) that has the same behavior as the button.

Whenever
a build is invoked, both of the buttons (and their corresponding menu
items) are disabled until the build has completed.

- Select the specific projects that you want to update
- Remove the projects from the server
- Regenerate the backing Java EE projects
- Clean the projects
- Regenerate the XSLT files for XML maps
- Redeploy the projects to the server

## The "Project status" section

- Name
- Validated
- Deploy code updated
- Status on server

The Name column displays the name
of each business integration project in the workspace and it also
displays a symbol that identifies the specific project type, such
as integration module, library, or component test project.

The Validated column
indicates whether a business integration project has been validated.
If errors are detected in a project during a build, the column will
also display an error symbol and the number of errors detected.

The Deploy
code updated column indicates whether deploy code was
generated for an integration module or a component test project. If
errors are detected in the associated Java 2 Platform Enterprise Edition projects, the column will
also display an error symbol and the number of errors detected. (Note
that Not applicable is displayed for all libraries because
deploy code is never generated for libraries.)

The Status on server column shows the status of an integration module or
component test project on the server. The column heading takes the form "Status on
server\_state
server
server\_name", where server\_state is the current state of the server (starting,
started, stopping, stopped, or publishing) and server\_name is the
name of the supported server. There is one Status on server column for each
supported server listed in the Servers view. For example, if there are two supported servers listed
in the Servers view, then there are two Status on server columns listed in
the status table. However, if there are no supported servers listed in the Servers view, then no
Status on server column is displayed in the table.

## Project statuses

In the Status
on server column of the project status table, a project
can have one of several statuses, such as:

- Not applicable
- Ready to run
- Not ready to run
- Not deployed to this server

The Not applicable status is displayed
for all libraries because libraries do not get deployed to servers
and therefore do not have any status on servers.

The Ready
to run status is displayed for a module when it meets
the following conditions:

- Validation has occurred.
- Deploy code has been generated.
- There are no errors in the module.
- The contents of the module in the workspace are synchronized with
the contents of the same module deployed on the server.

The Not ready to run status is displayed
for a module that exhibits one of many possible conditions.