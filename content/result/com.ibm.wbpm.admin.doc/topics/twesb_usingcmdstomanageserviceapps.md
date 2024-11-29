<!-- image -->

# Using wsadmin to administer service applications

## Before you begin

Use the wsadmin tool to run service application commands.

## About this task

You can use the wsadmin tool in different ways. You can use the tool interactively, as an
individual command, or with a script. Running multiple commands in a script is useful if you are
administering multiple machines.

IBM® Business Automation Workflow includes commands that display
SCA modules and their imports and exports and that change the details of import and export binding.
For example, you can use the listSCAModules,
showSCAModuleProperties, and modifySCAModuleProperty to
examine and modify SCA modules. To examine the import and export bindings for a module, use
thelistSCAImports, listSCAExports,
showSCAImport, and showSCAExport commands. To modify an import
or export binding, use the appropriate wsadmin command for your binding type (for example,
modifySCAImportJMSBinding or modifySCAExportHttpBinding).