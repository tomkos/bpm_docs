<!-- image -->

# Using software configuration management systems

You can add projects to a remote software configuration management
system through the Business Integration view. See the related links
to topics that provide additional details about using this view.

The Business Integration view provides a logical view of the resources
in each module, mediation module, and library. Within each project,
the resources are categorized by type. Logical resources shown in
the navigation tree in the Business Integration view do not necessarily
have a one-to-one mapping to physical files. When you use the Team menu
options you will notice that the physical files do not directly map
to the resources that you see in the Business Integration view. Always
work from the Business Integration view when sharing a project or
committing changes, so that you share or commit all the necessary
resources.

Make sure your preferences always use the .project file for the
project name, rather than using the folder name. Although this setting
can be changed, Integration Designer modules
rely on the name defined in the .project file, which is also used
by sca.module, sca.modulex, and other artifacts in the module. By
reading the module name from the .project metadata file, rather than
from a user-defined folder, you can avoid module name discrepancies.

When setting up source control processes, you must decide whether
to have everyone work off one stream or branch, or have developers
working off different streams or branches. Having developers working
off the same stream or branch helps to avoid concurrent development
and difficult merge scenarios if the team uses reserved checkouts.
This cautionary practice is particularly important if you are using
Rational ClearCase with pessimistic locks (checkout reserved). However,
silent checkouts of common resources can unknowingly lock files, and
that can cause build failures in other workspaces.

When
working in a team environment, one way of working is to allow all
users to edit resources concurrently, then merge the various files
later. This approach is not a good approach when working with IBM Integration Designer unless
all the users are very familiar with managing the physical files for
artifacts and working with their code. To help avoid overlapping changes
to files, set up the repository systems to avoid concurrent modification.
For example, set up ClearCase in
exclusive checkout mode or use the Watch/Edit feature when using the
CVS repository system.

After moving to a new workspace, be cautious of adding new files
to source control. The flag indicating a file is derived can be lost
after importing the files into a new workspace. See "Integration Designer artifacts
managed in source control" for a guide about which files should be
under source control.

- Managing SCA modules, libraries, and staging modules in Integration Designer

Team development with IBM Integration Designer is most effective if everyone on the team follows some basic practices.
- Synchronizing with the software configuration management system

As you work with modules managed in source control, differences arise between the local and remote copies of the modules. To keep the artifacts in the local working copy and remote source control system in accordance with one another, the local workspace should be synchronized with the remote software configuration management system (SCM).
- Integration Designer artifacts managed in source control

In general, only the module and dependent libraries need to be managed in source control. Most generated backing files should not be kept in source control. A detailed list of the files in each category appears below.
- Managing integration solutions in source control

Although integration solutions have no deployable logic, you can still manage them in source control like any other project.
- Sharing your integration project through CVS

IBM Integration Designer provides the capability to develop applications in a team environment using Concurrent Versions System (CVS).
- Using CVS with Integration Designer and Workflow Center

This topic shows you how to perform common tasks using IBM Integration Designer with IBM Workflow Center and a traditional software configuration management (SCM) system.
- Installing Rational Team Concert into the workbench

You can use the p2 installation method to install Rational Team Concert Client v2.x into the same workbench as IBM Integration Designer. You can use IBM Installation Manager to install Rational Team Concert Client v3.x.