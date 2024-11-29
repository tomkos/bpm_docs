<!-- image -->

# Guidance when working with the Workflow Center

This topic provides some tips and guidance for working
with the Workflow Center.

- Bindings interact with process applications and toolkits differently
than with components in modules. See Considerations when using bindings.
- When deployment occurs from the Workflow Center,
a shared library is shared with all the modules in the process application.
If you deploy a module independent of the Workflow Center,
the libraries are not shared. Each associated library is copied into
each module.
- Snapshots in the Workflow Center repository
are the equivalent of versioned files in previous releases. Therefore,
modules and libraries that are associated with process applications
and toolkits cannot be versioned.
- Snapshots are set to read-only when brought into IBM® Integration
Designer.
- Certain file types should not be stored in the Workflow Center repository.In some instances, certain file types may interrupt your build. Inother instances there is no need to share them. By disabling sharingyou can contain the size of your project. The following file typesshould not be stored or shared on the Workflow Center repository: You can set preferences to ignore specific file types in Windows > Preferences > Team > Ignored Resources .
    - Metadata such as "team private" files. Files of this type can
cause build issues as team private files contain tracking information
specific to the workspace they were generated in.
    - Any derived files.
    - File types such as wbiexetrace, smap, or jsrc files.
- Although the Workflow Center cannot
incorporate changes from Business Modeler, you can export your projects
from Business Modeler and import them into Process Designer, which
will allow you to interact with these business processes.
- A process application or toolkit must contain a default moduleor default library in order for you to open it in IBM IntegrationDesigner. When you first open a process application or toolkit inIntegration Designer, it is automatically initialized by associatinga default module or library. In the Process Center, when you opena process application that depends on a toolkit, and that snapshotof the toolkit does not contain a default module or library, you cando one of the following:

In the Process Center, when you open
a process application that depends on a toolkit, and that snapshot
of the toolkit does not contain a default module or library, you can
do one of the following:

- Continue to open the process application with the toolkit. However,
the tip of the toolkit is brought into your workspace and not the
snapshot.  You cannot bring the snapshot into your workspace because
a snapshot is read-only and cannot be initialized. If the tip was
not initialized, once the tip is brought into your workspace, it is
automatically initialized. You can then create a new snapshot from
the tip and update the dependency from the process application.
- Clear the toolkit in the Open in Workspace window. You can proceed
to open the process application if you are certain that you will not
be using any artifacts from the toolkit that you cleared.