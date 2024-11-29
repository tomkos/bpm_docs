<!-- image -->

# Using CVS with Integration Designer and Workflow Center

## Before you begin

- Store only the default projects and minimum artifacts required for collaboration in Workflow Center.
- Store non-default projects separately in the SCM system, not in Workflow Center.
- Store implementation content in the unshared and unmirrored library modules in the SCM
system.

- Best practices when using IBM Integration Designer and IBM Process Designer
together.
- Develop Advanced Integration services for IBM Business Process Manager
V8.5.6.

## About this task

- The SCM contains a history that is important for maintaining code
integrity.
- There are usually automated build scripts that run from the SCM.
- Corporate standards may require that you continue to use a specific
SCM.

Although this topic addresses working with Concurrent Versions
System (CVS), the principles also apply to other SCM systems. For
more information about working with CVS or other SCM systems, see
the related links at the end of this topic. You can access actions
for source control management system clients that you have currently
installed from the Integration Designer Business
Integration view by right clicking a project and opening the Team
menu.

Eclipse only allows one SCM to be associated with a project.
If you use Workflow Center with another SCM system, treat Workflow Center as
a secondary repository. The SCM system is the primary storage area
used by the developers as they work with their artifacts. Load projects
to the Workflow Center intermittently, perhaps at project milestones. Do not
check projects out from Workflow Center to
make changes.

Because you work from CVS, artifacts such as
business process definitions, which are solely associated with Workflow Center will
not exist in the CVS repository.

## Procedure

- Add projects to both repositories. A project
that is under CVS control can be added to Workflow Center by
associating it with a process application or toolkit (see the related
links for instructions). That association creates a bpm.repo.prefs
file in the Integration Designer .settings folder. That file contains the details about
the association. Integration Designer checks
for this file when a when a project is brought into a workspace. If Integration Designer finds
that file, it will connect to the Workflow Center repository
and show the project as contained in the specified process application
or toolkit. You can add a project to the repositories in either order,
but if you associate the project with Workflow Center last,
synchronize the project with CVS immediately after association so
that the bpm.repo.prefs file is visible if someone checks the file
out of CVS.
- Remove projects from the Workflow Center by disassociating them. You need access authorityon the Workflow Center to perform this task.
    1. In the Business Integration view of Integration Designer, right
click the project and select Disassociate from Process
Center. Disassociation removes the project
from the Process Center repository and deletes the bpm.repo.prefs
file. The file will still exist in previous snapshots, so a disassociation
can be reversed.
    2. Synchronize with CVS immediately so the disassociation
is registered there before someone else checks out the file.
- Check out files only from CVS, using the CVS Import wizard
or the CVS navigator. Although Integration Designer makes
it easy to bring in projects from Workflow Center using
the pop-up menu, you should not do that for projects that reside
in CVS. CVS metadata is stripped out when a project is shared with
the Workflow Center repository. If you pull projects from Workflow Center, the
files will not be connected to CVS. If you unintentionally make changes
to files that you have accessed in this way, you need to publish them
to Workflow Center and have someone pull them into another workspace that still contains
the CVS connection for the project. The revised project can then be
committed to CVS from there.
- Before publishing projects to Workflow Center, update
from CVS to capture any changes that have been made by the team. Immediately
after publishing, synchronize with CVS. Doing these
two actions keeps CVS as the system of reference and avoids conflicts
between the two repositories.
- Create tracks in Workflow Center beforecreating branches in CVS. Make the branch and track names similarso the relationship between them is easy to identify.

1. In the Process Center perspective, select a process
application.
2. In the process application title bar, select Manage. Select Allow users to create tracks
in this process app.
3. Select Snapshots and then select
an existing snapshot or create one. Click New Track:  You need to create the track from
a snapshot.
4. In the Create New Track window, provide a name and description
for the track. Click Create. Now that a track exists in Workflow Center, you
can create a corresponding branch in CVS.
5. Right-click a project in CVS and select Team > Branch.
6. In the Create a new CVS branch window,
give the branch a name and version.
7. At this point, the new CVS branch still points to the
main track, not the new track. To complete the process, you need to
replace the workspace content with the new track content. In the Business
Integration view, right-click the project and select Replace With > Latest from Tip of Track.
8. Select the new track and click OK. At this point, Integration Designer edits
the bpm.repo.prefs file to point to the new track. However, the projects
must still be reassociated with the new CVS branch.
9. In the Business Integration view, select Team > Share Project.
10. In the Share Project window, select Use an
existing module and select the module that you have associated
with the process application.  The program recognizes
that there is now a branch for that module and provides a page where
you can choose to synchronize with the branch instead of the HEAD
stream.
11. Select the branch and click Next. If you do not see your branch, click Refresh Tags.
12. Expand the module settings, right-click bpm.repo.prefs, and select Mark as Merged. Select Launch the Commit wizard and click Next.
13. Right-click bpm.repo.prefs, and
select Commit. Click Finish.
- If a Workflow Center machine
URL changes, edit the bpm.repo.prefs file to reflect the change.
- If a project in CVS is associated with a Workflow Center that
is no longer running, disassociate the project from the Workflow Center server.
Right-click the project in the Business Integration view. Select Disassociate and confirm the action.