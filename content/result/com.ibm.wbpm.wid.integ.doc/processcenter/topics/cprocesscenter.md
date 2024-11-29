<!-- image -->

# Workflow Center repository

To work with the Workflow Center repository, you must know how to access it, import process applications and toolkits from it, and associate modules and libraries with its process applications and toolkits. You must also know how to use the wizard that generates a service that a process application might require. Finally, you must know how to synchronize your artifacts with their associated process applications and toolkits, deploy a completed process application or toolkit, and understand the limitations when you are working with the Workflow Center repository.

- Accessing the Workflow Center repository

To work with process applications and toolkits, you must access the Workflow Center repository.
- Importing process applications and toolkits from the Workflow Center repository

You can import process applications and toolkits into your workspace from the Workflow Center repository, and then you can use them with your modules and libraries.
- Switching between simple and advanced mode

You can customize your mode of operation to show only what you need.
- Associating a module or library with a process application or toolkit

You can associate a module or library with a process application or toolkit to add additional functions to the application, or to take advantage of version control on Workflow Center.
- Disassociating a module or library from a process application or toolkit

When you disassociate a module or library from a process application or toolkit, you remove the association between the workspace and Workflow Center artifacts. You disassociate a module or library when it is no longer needed by the process application.
- Merging workspace and Process Center repository changes

As you update your process applications and toolkits, you will want to update the corresponding process applications and toolkits in the Workflow Center with your changes. You will also want to bring in changes made by other users from the process applications and toolkits in the Workflow Center, and resolve conflicts that might occur when multiple users change the same artifact.
- Synchronizing artifacts in the workspace and the Workflow Center repository

While you are updating an artifact, another user might be updating the same artifact at the same time. To make sure that you are using the latest version of an artifact, you must synchronize the versions that exist in the workspace and the Workflow Center repository.
- Implementing an Advanced Integration service

If a process application or toolkit in your workspace requires an Advanced Integration service, you can use a wizard to create the basic components that you need. You can then complete the logic in the generated components.
- Creating an export to implement an Advanced Integration Service

Creating an export is an alternative way to implement an Advanced Integration Service. If you drag-and-drop icons from the assembly editor palette to create exports, this approach could be a simpler way for you to implement the service.
- Creating an import to call a process

A service might need to start or interact with a process to enable a human-centric interaction. For example, the service might encounter an unexpected business situation and need human interaction to resolve it. You can create an SCA import to start or interact with a process. There are two ways to create the import, depending on whether your module is stand-alone, or associated with a process application.
- Making operations visible to process applications

If you have an SCA export and implementation, you can make it visible to Process Designer as an Advanced Integration Service.
- Examining the Process Designer configuration

You can launch the Advanced Integration service configuration in Process Designer corresponding to your Advanced Service implementation, which can be helpful when you are developing the service in Integration Designer.
- Emulating an Advanced Integration service

You can choose to run an implemented Advanced Integration service in the emulate mode, which means that you do not actually need to run the service during playback. You can emulate the interactions of the service by manually entering the outputs. This is useful if you want to test the business process when the service is not available.
- Changing toolkit dependencies

A process application can reference only one toolkit snapshot but that reference can be changed.
- Loading snapshots to the workspace

To view and manage a specific iteration of a process application and toolkit, you can download a snapshot to your workspace. A snapshot is a capture of a process application or toolkit, at a specific point in time.
- Changing connection properties for process applications and toolkits

If your process applications and toolkits are moved to another server, for example, because of a hardware failure, you must update your connection properties.
- Renaming a module or library associated with a process application or toolkit

If you have modules and libraries associated with a process application or toolkit, be aware that renaming the module or library requires you to remove any dependencies and to disassociate the library or module before changing its name.
- Library mirroring

In a collaborative development environment between IBM Integration Designer and IBM Process Designer artifacts like business objects are shared in libraries. Library mirroring means that when you put an artifact in your library in Integration Designer it is made available to others working with the same library in Process Designer who are using the same process application or toolkit.
- Guidance when working with the Workflow Center

Associating modules and libraries with process applications and toolkits in the Workflow Center changes the way that you work based on previous releases.
- Considerations when using bindings

Different bindings interact with process applications and toolkits in various ways. You should consider the following suggestions and be aware of some rules and conventions.
- Limitations when working with process applications and toolkits

Differences between the modules and libraries created in your workspace and the process applications and toolkits that originated in the Workflow Center repository mean that there are some limitations when you develop business processes in this collaborative environment.