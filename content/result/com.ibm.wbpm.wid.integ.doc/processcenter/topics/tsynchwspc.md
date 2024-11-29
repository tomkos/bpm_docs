<!-- image -->

# Synchronizing artifacts in the workspace and the Workflow Center repository

## About this task

When you try to publish the artifact
to the Process Center, synchronization automatically starts to merge
changes into the workspace. If there is a conflict, the conflict shows
in the Synchronization window. You must resolve the conflict before
you can publish your changes to the Process Center.

To make
sure that you are using the latest version of an artifact, you must
synchronize the versions that exist in the workspace and the Process
Center repository. Select the file that contains the changes you want
to keep, and then click Commit to publish your
changes to the repository.

- For an XSD, WSDL, or assembly diagram, you need to go to the Changes
in Selected Artifacts  pane and accept the changes you
want to keep or import. You do not have to select and commit the file.
- For other artifact types, you have to manually copy the changes
from the repository to the workspace in the Change Details pane.

- Select the changes you want to bring into your workspace by clicking
the check box next to the change.
- Clear the changes you do not want to bring into your workspace.
- Click Commit.

## Procedure

To synchronize conflicting artifacts, complete the following
steps:

1 You can set preferences to always view the Synchronizationwindow, or to view it only when a conflict occurs. To specify howyou want the Synchronization window to function, select one of thefollowing options: Go to step 2 to synchronize assembly diagram, WSDL, and XSD artifacts.Go to step 3 to synchronize all other artifact types.
    - You can set the Synchronization window to show each time you publish
by selecting Always in the Preferences page.
To set this preference, click Windows > Preferences > Business Integration > Workflow Center.
    - You can set the Synchronization window to show only when there
is a conflict by selecting Open when a conflict is detected in the
Preferences page.  When you publish your artifacts to the repository,
all changes are merge silently into the workspace. To set this preference,
click Windows > Preferences > Business Integration > Workflow Center.
2 To synchronize assembly diagram, WSDL, and XSD artifacts,complete the following steps: Important: You can synchronize onlythose files that are marked with a mirroring flag. Module and librarynames must be unique within a deployed process application.

- The Synchronization window shows you the changes in your workspace
and the repository.
- Select which change you are going to keep by checking the box
next to those changes in the Changes in the Selected Artifact Pane,
and then click Commit.
3 To synchronize all other artifact types, complete the followingsteps:

- The Synchronization window shows you the workspace and repository
changes in a text-based compare/merge window in the Change Details pane.
- Copy the changes from the repository file to your workspace file,
and then click Commit.