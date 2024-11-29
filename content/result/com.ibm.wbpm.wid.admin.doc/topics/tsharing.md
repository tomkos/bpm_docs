<!-- image -->

# Sharing your integration project through CVS

## About this task

- Add (share) a project to CVS
- Synchronize changes between the local application and remote repository
- Commit local changes to the remote repository
- Update (replace) local workspace artifacts with latest version on remote repository

The Business Integration view provides a logical view of the resources in each module,
mediation module, and library. Within each project, the resources are categorized by type. Logical
resources shown in the navigation tree in the Business Integration view do not necessarily have a
one-to-one mapping to physical files. When you use the Team menu options you will notice that
the physical files presented in the Synchronize and CVS Repositories views do not directly map to
the resources that you see in the Business Integration view. Always work from the Business
Integration view when sharing a project or committing changes, so that you share or commit all the
necessary resources.

The topics that follow illustrate the basic steps to share a project
when working in a CVS environment.

## Procedure

1 Before you can share a project with a CVS repository, youneed to add the repository to the CVS repositories view.
    1. Switch to the CVS Repository Exploring perspective,
right-click and select New > Repository Location.
    2. In the Add CVS Repository wizard, enter the location,
authentication, and connection information.
    3. Click Finish.
2. In the Business Integration view, select the module or
library that you want to share, right-click, and select Team > Share project.
3. In the Share Project wizard, Select CVS as the repository
type, and click Next.
4. Choose to use the existing repository connection that you
created previously and click Next.
5. Choose to use the project name as the module name and click Next.
Never rename the module when placing it in CVS. The SCA.module file
depends on the module name.
6. The next page shows you the project that is to be shared.
Expand the project to view the physical files within it. The decorator
showing an arrow with a plus sign indicates that the file is new,
and does not exist on the server. Select the project and click Finish.
A version of the module including all its resources will
be created in the shared repository.

## Results

## Example

Before committing your resources, you should always
synchronize the project with the repository to see the resources that
have changed in the local workspace and in the repository. Select
the project, right-click and select Team> Synchronize with Repository.
 The Synchronize view shows the physical files in the module. Change
decorators indicate the changed files.

Switch to the Physical
Resources view. This view also shows the changed physical files, indicated
by a > decorator.

Always add or check out complete
modules to or from CVS, rather than individual folders or artifacts.
To commit your changes, work from the Business Integration view. Select
the module, right-click, and select Team > Commit. Commit updates
CVS with a new version of the file. If there are conflicts, you have
the opportunity to see and resolve them.

When you delete an
authored file from your local workspace and synchronize with CVS,
you will see a minus sign (-) beside the artifact, indicating that
you are deleting the artifact from the server.

The commit process
uploads an empty file structure to CVS, even though all the files
in the folders are derived. Empty folders are pruned by default when
you extract a module. You might see an error message for a missing
gen/scr directory. You can ignore the message. CVS flags the omission
if the directory is missing, but the gen/scr directory is optional.

When you check out a module from CVS, you are extracting the
entire service module, so you do not need to create a shell module
beforehand. The entire project structure that is in CVS is mirrored
in your Business Integration view, except that each entry from the
SCM has the label CVS in brackets after it.

Before you check
out a project, synchronize it to view changes that another team member
may have made to the server version of the project. Select the project
from the Business Integration view, right-click, and select Team
> Synchronize.  The left facing arrow beside a file shows that
it has changed in the shared repository. Always synchronize with the
repository before you commit changes.

To check out a project,
switch to the CVS Repositories view, select the project, right-click
and select Check Out. Check out dependent libraries if you
need to use artifacts from them.

You
might see an error message for a missing gen/scr directory.
You can ignore this message or get rid of it by disabling the directory
pruning option. From the menu, select Window > Preferences > Team > CVS. Clear the Prune empty directories option.
Click OK.

Conflicts
can be difficult to resolve if a user is unfamiliar with the artifacts
because conflict resolution takes place at the level of the XML structure
of the underlying files. It is usually better to update with a new
version of the artifacts and integrate your changes in the new copy
than it is to try to merge conflicts in the XML.

Some files
can be flagged as out of sync when they appear to be identical. This
condition can occur if the files have different timestamps. Use the
Clean Timestamps option in to automatically get rid of these problems.