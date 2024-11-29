<!-- image -->

# Workspaces

An Eclipse workspace is a collection of projects and other
physical resources that you are currently developing in the workbench.
Additional information about these resources resides in a directory
on the file system. The resources might reside in the same directory.

For an introduction to the structure of the Eclipse workbench,
see Workbench under the covers in the Eclipse
documentation.

## Considerations

The first time that you start IBM® Integration
Designer,
a window opens with the default workspace directory already specified.
If you are using Windows, by default, your work
is stored in a directory called workspace, located in C:\Documents
and Settings\youruserid\IBM\widversion. If you want
to save your work somewhere else, you can change the name and location
of the workspace by editing the field in the window. The file path
is case-sensitive, so ensure that your entry exactly matches the names
used on the file system.

When you create a new workspace in
a Windows environment, ensure that your file
path length does not exceed the Windows limitation
of 256 characters. Failure to use short workspace file paths can lead
to problems when building, deploying, or deleting your applications.
It is much easier to start with a short path than to try to correct
the problem after it occurs.

When you create a new workspace,
preference settings that you applied to earlier workspaces are not
transferred. You must set preferences on the new workspace if you
do not want to use the defaults.

## Switching workspaces

You can switch to another
workspace by clicking File > Switch Workspace.

- Switch back to the old workspace and uninstall the applications.
- Manually uninstall the applications using the administrative console
for IBM Workflow
Server.

- Keeping the workspace clean

In IBM Integration Designer, there are numerous ways to maintain a clean workspace. For example, whenever you delete certain kinds of primary workspace resources, you can choose to have their supporting artifacts automatically deleted rather than having them retained and unused in the workspace.
- Business Integration perspective and views

The Business Integration perspective provides simple, uncluttered views of essential resources so that you can model and build business solutions. Unnecessary details and unused tools are hidden.
- Business integration capabilities

IBM Integration Designer provides a filtering function known as capabilities. With capabilities, you can choose to hide tools not used during business integration application development. At any time, you can choose to show those tools again.
- Opening the Business Integration perspective

By default, the Business Integration perspective opens when you launch the product. You can switch between opened perspectives by selecting them at the upper-right corner of the Workbench. In the title of the Workbench window, you can see the name of the active perspective.
- Filtering in the Business Integration perspective

You can use filtering to reduce files you do not need in the Business Integration view or the Physical Resources view.
- Selecting favorite objects in the Business Integration perspective

If you work frequently with certain artifacts in the Business Integration perspective, and want to make them easy to find, you can mark them as favorites. If you have marked an artifact as a favorite, you can remove it from your favorites, if necessary.
- Enabling tool capabilities

Enable capabilities to limit the functions that are available to the user. You can enable and disable tool capabilities in several ways.

## Related concepts

- Creating modules and libraries

## Related tasks

- Organizing projects using integration solutions
- Creating and wiring components
- Working with implementations
- Adding notes
- Setting assembly editor preferences
- Finding errors in the assembly diagram

## Related information

- Assembling services: Customer enquiry example