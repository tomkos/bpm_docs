# Determining artifact usage

## About this task

## Procedure

To see where an artifact is used, complete the following steps:

1. In the designer, open your process application or toolkit
.
2. Open the library item.
3 In the footer, click References . You can open artifacts from the list to view their details or to edit them.

<!-- image -->

    - Referenced By : This list shows the artifacts in the current process application ortoolkit and their dependencies that use the library item, or the artifacts across all toolkits,depending on the scope that you choose. Use the Scope icon to togglebetween the two scopes.Local scope shows where artifacts are used only in the process application ortoolkit and its dependencies. This is the default view. Global scope shows where artifactsare used across all the toolkits in the repository and is available only for library items in namedsnapshots or versions of toolkits.

<!-- image -->

Local scope shows where artifacts are used only in the process application or
toolkit and its dependencies. This is the default view.

        - Expand a project to see the list of artifacts. Click an artifact to display all the snapshots
that refer to the library item. You can open any version of any artifact that can be edited in the
designer, which makes it easier for you to consistently apply related changes across multiple
items.
        - If you select an artifact that is defined in a process application or toolkit other than the
current process application or toolkit and its dependencies, the Process Designer opens the selected
artifact and its containing process application or toolkit in a new tab. The new tab shows the
artifacts only in the context of the newly opened process application or toolkit, independent of any
other open process application or toolkit.
- References: This list shows all the artifacts in the current application or
toolkit and their dependencies that the library item uses.

## Results

To refresh the list with the latest changes, save the changes and click
Refresh
.
The data refreshes when the changes are detected, which might take a few seconds. Therefore, if you
do not see the updates right away, click Refresh again.