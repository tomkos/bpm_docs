<!-- image -->

# Considerations when refactoring

- Using refactoring on an EIS import or export
- Using refactoring on a JMS or generic JMS import or export
- Using refactoring on an MQ JMS import or export
- Using refactoring on an HTTP import or export
- Using refactoring to move operations and merge interfaces
- Refactoring artifacts manually without using the refactoring wizard

## Using refactoring on an EIS import
or export

1. In the interface editor, right-click the operation that you want
to change.
2. From the menu, select Refactor > Rename Operation.

Correction:
The necessary updates will be performed by the refactoring operation
and the results can be viewed in the refactoring wizard's Details
view on the Preview page.

1. In the Business Integration view, right-click the module that
you want to rename.
2. From the menu, select Refactor > Rename.

Correction:
The necessary updates will be performed by the refactoring operation
and the results can be viewed in the refactoring wizard's Details
view on the Preview page. Undeploy the current instance of the resource
adapter and redeploy.

## Using refactoring on a JMS or generic
JMS import or export

1. In the interface editor, right-click the operation that you want
to change.
2. From the menu, select Refactor > Rename Operation.

Correction: The
necessary updates will be performed by the refactoring operation and
the results can be viewed in the refactoring wizard's Details view
on the Preview page.

1. In the Business Integration view, right-click the export that
you want to move.
2. From the menu, select Refactor > Move.
3. In the Move Artifact wizard, choose a new
location for the export. Click the plus sign to expand the menu to
see levels below modules and libraries.

```
<destination implType="com.ibm.ws.sib.api.jms.impl.JmsQueueImpl"
	target="ModuleWithExport/NewExportLocation/ExportName\_RECEIVE\_D"
	type="javax.jms.Queue" usage="send" />
<destination implType="com.ibm.ws.sib.api.jms.impl.JmsQueueImpl"
	target="ModuleWithExport/NewExportLocation/ExportName\_SEND\_D"
	type="javax.jms.Queue" usage="receive" />
```

1. In the Business Integration view, right-click the export that
you want to rename.
2. From the menu, select Refactor > Rename.

```
<destination implType="com.ibm.ws.sib.api.jms.impl.JmsQueueImpl"
	target="ModuleWithExport/NewExportName\_RECEIVE\_D"
	type="javax.jms.Queue" usage="send" />
<destination implType="com.ibm.ws.sib.api.jms.impl.JmsQueueImpl"
	target="ModuleWithExport/NewExportName\_SEND\_D" type="javax.jms.Queue"
	usage="receive" />
```

1. In the Business Integration view, right-click the module that
you want to rename.
2. From the menu, select Refactor > Rename.

```
<destination implType="com.ibm.ws.sib.api.jms.impl.JmsQueueImpl"
	target="NewModuleWithExport/ExportName\_RECEIVE\_D"
	type="javax.jms.Queue" usage="send" />
<destination implType="com.ibm.ws.sib.api.jms.impl.JmsQueueImpl"
	target="NewModuleWithExport/ExportName\_SEND\_D" type="javax.jms.Queue"
	usage="receive" />
```

Description: You
have an import with a JMS binding and you deployed it to the server.
You want to have an export that will communicate with the import.
Note that export has to have the same interface as import. You update
the export's destination JNDI names with the JNDI names that the import
is using. You retrieve the destination JNDI names from the import's
Summary page of the properties view. Then you deploy the export and
it will communicate with the import.

Problem:  When the
import is moved to another folder within the module, the destinations'
JNDI lookup name value that might be referenced by the JMS export
becomes invalid.

```
<destination implType="com.ibm.ws.sib.api.jms.impl.JmsQueueImpl"
	target="ModuleWithImport/NewImportLocation/ImportName\_SEND\_D"
	type="javax.jms.Queue" usage="receive" />
<destination implType="com.ibm.ws.sib.api.jms.impl.JmsQueueImpl"
	target="ModuleWithImport/NewImportLocation/ImportName\_RECEIVE\_D"
	type="javax.jms.Queue" usage="send" />
```

Description: You have an import with
a JMS binding and you deployed it to the server. You want to have
an export that will communicate with the import. Note that the export
has to have the same interface as the import. You update the export's
destination JNDI names with the JNDI names that the import is using.
You retrieve the destination JNDI names from the import's Summary
page of the properties view. Then you deploy the export and it will
communicate with the import.

Problem:  When the import
name is changed, the destinations' JNDI lookup name value that might
be referenced by the JMS export becomes invalid.

```
<destination implType="com.ibm.ws.sib.api.jms.impl.JmsQueueImpl"
	target="ModuleWithImport/NewImportName\_SEND\_D" type="javax.jms.Queue"
	usage="receive" />
<destination implType="com.ibm.ws.sib.api.jms.impl.JmsQueueImpl"
	target="ModuleWithImport/NewImportName\_RECEIVE\_D"
	type="javax.jms.Queue" usage="send" />
```

Description: You have an import with
a JMS binding and you deployed it to the server. You want to have
an export that will communicate with the import. Note that export
has to have the same interface as import. You update the export's
destination JNDI names with the JNDI names that the import is using.
You retrieve the destination JNDI names from the import's Summary
page of the properties view. Then you deploy the export and it will
communicate with the import.

Problem:  When the import's
module name is changed, the destinations' JNDI lookup name value that
might be referenced by the JMS export becomes invalid.

```
<destination implType="com.ibm.ws.sib.api.jms.impl.JmsQueueImpl"
	target="NewModuleWithImport/ImportName\_SEND\_D" type="javax.jms.Queue"
	usage="receive" />
<destination implType="com.ibm.ws.sib.api.jms.impl.JmsQueueImpl"
	target="NewModuleWithImport/ImportName\_RECEIVE\_D"
	type="javax.jms.Queue" usage="send" />
```

## Using refactoring on an MQ JMS
import or export

1. In the interface editor, right-click the operation that you want
to change.
2. From the menu, select Refactor > Rename Operation.

Correction: The
necessary updates will be performed by the refactoring operation and
the results can be viewed in the refactoring wizard's Details view
on the Preview page.

1. In the Business Integration view, right-click the export that
you want to move.
2. From the menu, select Refactor > Move.
3. In the Move Artifact wizard, choose a new
location for the export. Click the plus sign to expand the menu to
see levels below modules and libraries.

```
<send
	target="ModuleWithExport/NewExportLocation/ExportName\_MQ\_RECEIVE\_D"
	type="javax.jms.Queue" />
<receive
	target="ModuleWithExport/NewExportLocation/ExportName\_MQ\_SEND\_D"
	type="javax.jms.Queue" />
```

1. In the Business Integration view, right-click the export that
you want to rename.
2. From the menu, select Refactor > Rename.

```
<send target="ModuleWithExport/NewExportName\_MQ\_RECEIVE\_D"
	type="javax.jms.Queue" />
<receive target="ModuleWithExport/NewExportName\_MQ\_SEND\_D"
	type="javax.jms.Queue" />
```

1. In the Business Integration view, right-click the module that
you want to rename.
2. From the menu, select Refactor > Rename.

```
<send target="NewModuleWithExport/ExportName\_MQ\_RECEIVE\_D"
	type="javax.jms.Queue" />
<receive target="NewModuleWithExport/ExportName\_MQ\_SEND\_D"
	type="javax.jms.Queue" />
```

Description: You have an import with an
MQ JMS binding and you deployed it to the server. You want to have
an export that will communicate with the import. Note that the export
has to have the same interface as import. You update the export's
destination JNDI names with the JNDI names that the import is using.
You retrieve the destination JNDI names from the import's Summary
page of the properties view. Then you deploy the export and it will
communicate with the import.

Problem:  When the import
is moved to another folder within the module, the destinations' JNDI
lookup name value that might be referenced by the MQ JMS export becomes
invalid.

```
<receive
	target="ModuleWithImport/NewImportLocation/ImportName\_MQ\_SEND\_D"
	type="javax.jms.Queue" />
<send
	target="ModuleWithImport/NewImportLocation/ImportName\_MQ\_RECEIVE\_D"
	type="javax.jms.Queue" />
```

Description: You have an import with a MQ
JMS binding and you deployed it to the server. You want to have an
export that will communicate with the import. Note that the export
has to have the same interface as the import. You update the export's
destination JNDI names with the JNDI names that the import is using.
You retrieve the destination JNDI names from the import's Summary
page of the properties view. Then you deploy the export and it will
communicate with the import.

Problem:  When the import
name is changed, the destinations' JNDI lookup name value that might
be referenced by the MQ JMS export becomes invalid.

```
<receive target="ModuleWithImport/NewImportName\_MQ\_SEND\_D"
	type="javax.jms.Queue" />
<send target="ModuleWithImport/NewImportName\_MQ\_RECEIVE\_D"
	type="javax.jms.Queue" />
```

Description: You have an import with an MQ
JMS binding and you deployed it to the server. You want to have an
export that will communicate with the import. Note that the export
has to have the same interface as import. You update the export's
destination JNDI names with the JNDI names that the import is using.
You retrieve the destination JNDI names from the import's Summary
page of the properties view. Then you deploy the export and it will
communicate with the import.

Problem:  When the import's
module name is changed, the destinations' JNDI lookup name value that
might be referenced by the MQ JMS export becomes invalid.

```
<receive target="NewModuleWithImport/NewImportName\_MQ\_SEND\_D"
	type="javax.jms.Queue" />
<send target="NewModuleWithImport/NewImportName\_MQ\_RECEIVE\_D"
	type="javax.jms.Queue" />
```

## Using refactoring on an HTTP import
or export

1. In the interface editor, right-click the operation that you want
to change.
2. From the menu, select Refactor > Rename Operation.

Correction: The
necessary updates will be performed as you continue with the refactoring
operation and the results can be viewed in the refactoring wizard's
Details view on the Preview page.

## Using refactoring to move operations
and merge interfaces

Moving operations or merging interfaces
results in the following behavior.

When you move an operation,
you will receive a message that states that the method binding does
not have a matching operation on the interface. This method binding
is from the previous operation before you moved it. This old method
binding is intentionally left in case there is some configuration
information you may still need. If you do not need this old method
binding, you can delete it.

When you merge an interface, you
will receive a message that the interface does not have a method binding.
This message is intentional. You are being asked to consciously create
and configure method bindings and their properties that are consistent
with your existing method bindings.

## Refactoring artifacts manually without
using the refactoring wizard

- Business objects and XSD files
- Interfaces and WSDL files
- Imports and exports
- Exports
- Modules
- Libraries

## Business objects and XSD files

- Deleting a business object : manually, that is, not usingthe refactoring function, deleting a business object (including anelement, ComplexType or XSD file that points to another business objectthat is referenced by this business object) created by the externalservice wizard results in a WSDL message part error. Also, the databinding generator will not be able to find the business object XSD.To correct the problem, you can do one of the following actions:
    - Rerun the external data wizard, selecting the same properties
as selected originally when running the external service wizard. You
may also need to rebuild the module project.
    - Rerun the external service wizard if a business object with a
different name is wanted. You may want to clean up the deleted business
object data binding code by cleaning up the module project.
    - Remove the business object references from the interface and WSDL
files.
- Deleting a business object: manually, that is, not using
the refactoring function, deleting a business object (including an
element, ComplexType or XSD file) created by the external data wizard
can result in a referencing error, if the business object was referenced
from a library module. To correct the problem, rerun the external
data wizard selecting the same properties as the previous execution.
- Changing a business object structure: manually, that is,
not using the refactoring function, changing a business object structure
created by the external service wizard or the external data discovery
wizard results in a runtime exception as the business object does
not match the one on the Enterprise Information System (EIS). To correct
the problem, create the original business object with a valid structure.
- Renaming a business object : manually, that is, not usingthe refactoring function, renaming a business object created by theexternal service wizard results in a Web Services Description Language(WSDL) type definition error and data bindings will need to be regenerated.To correct the problem, follow these steps:

1. Rename the business object in the interface editor and WSDL editor.
2. Renaming will force you to save the changes, which will regenerate
the data bindings.
- Renaming a business object namespace : manually, that is,not using the refactoring function, renaming a business object namespaceof a business object created by the external service wizard resultsin a Web Services Description Language (WSDL) type definition errorand data bindings will need to be regenerated. To correct the problem,follow these steps:

1. Rename the business object's namespace in the interface editor
and WSDL editor.
2. Renaming will force you to save the changes, which will regenerate
the data bindings.
- Moving a business object : manually, that is, not usingthe refactoring function, moving a business object created by theexternal service wizard or external data wizard to the library moduleresults in a WSDL message part error. To correct the problem, followthese steps:

1. Correct the WSDL import schemaLocation attribute value to point
to the current location of the XSD file.
2. Add the library as a module dependency and rebuild the module.

## Interfaces and WSDL files

- Deleting an operation : if you have an interface generatedby the external service wizard or by using the assembly editor onan import or export and you delete an operation manually, that is,not using the refactoring function, then the method in the importor export will not have a matching operation on the interface. Tocorrect the problem, choose one of the following actions:
    - Rerun the external service wizard selecting the same properties
as the previous execution of the wizard.
    - Rerun the external service wizard or assembly editor if you want
an operation with a different name.
    - Delete the method binding in the import or export.
- Deleting a port type : if you have an interface generatedby the external service wizard or by using the assembly editor onan import or export and you delete a port type manually, that is,not using the refactoring function, then the WSDL port type definedin the interface is invalid. To correct the problem, choose one ofthe following actions:

- Rerun the external service wizard selecting the same properties
as the previous execution of the wizard.
- Rerun the external service wizard or assembly editor if you want
a port type with a different name and delete the original import or
export and WSDL files.
- Delete the interface and the binding in the import or export.
- Deleting a WSDL file : if you have an interface generatedby the external service wizard or by using the assembly editor onan import or export and you delete a WSDL file manually, that is,not using the refactoring function, then the WSDL port type definedin the interface is invalid. To correct the problem, choose one ofthe following actions:

- Rerun the external service wizard selecting the same properties
as the previous execution of the wizard.
- Rerun the external service wizard or assembly editor if you want
a port type with a different name and delete the original import or
export and WSDL files.
- Delete the interface and the binding in the import or export.
- Renaming a port type:  if you have an interface generated
by the external service wizard or by using the assembly editor on
an import or export and you rename a port type manually, that is,
not using the refactoring function, then the WSDL port type defined
in the interface is invalid. To correct the problem, rename the port
type in the import or export to match port type name on the interface.

## Imports and exports

- Deleting an import or export:  if you have an import or
export generated by the external service wizard or by using the assembly
editor and you delete it manually, that is, not using the refactoring
function, then there will not be a problem if it has not been wired
to other components. If the import or export was wired to other components,
then re-run the external service wizard or sequence in the assembly
editor, selecting the same properties as the previous execution of
the wizard  In the case of a Java™ Message
Service (JMS) binding where you created an import by dragging and
dropping an export, there is a matching export for that import. Re-create
the import and export pair if one of them is deleted.

## Exports

A shortcut often used
to create an import with a JMS binding is to drag an export with a
JMS binding from one module into the module where you want to create
the import. However, if you refactor the interface of the original
export, it will not modify the interface of the import accordingly.
This section describes the manual steps you would need to perform
to correct the interface of the import.

Moving an export
with a JMS binding to another module to create an import (drag scenario)

- Both the import and export have the same interface: if
you have added a JMS binding to an export in the assembly editor and
dragged that export into another module creating a matching import,
then the WSDL port type defined in the import interface will be invalid
if the module with import does not contain the right interface. To
correct the problem, copy the interface, WSDL files and business object
files from the module with the export to the module with the import.
- Both the modules containing the import and export have dependencies
on a library containing their interface: if you have added a JMS
binding to an export in the assembly editor and dragged that export
into a module creating a matching import, then the WSDL port type
defined in the import interface will be invalid. In this case, however,
the interface, WSDL files and business objects were created in a library,
the export was created without an interface, and the library was added
as a dependency to the module with the export. Then the interface
from the library was added to the export, the JMS binding generated
and the export dragged into another module to create the import. To
correct the problem of an invalid port type defined in the import
interface in this case, add the library as a dependency to the module
with the import and rebuild the project.

## Modules

- Deleting a module: if you added a JMS binding to an export
in the assembly editor and dragged that export into a module creating
a matching import and then deleted the module containing the export,
then there will be an invalid target attribute value on the destination
element in the import binding. To correct the problem, if you intended
to delete the module then delete the import. If you did not intend
to delete the module, create the module and the export. There is no
refactoring function that supports dragging and dropping an export
to create in import.

## Libraries

- Deleting a library : if you deleted a library manually andthe library had been added as a module dependency, then there willbe a module classpath error. The error will indicate the removal oflibrary artifacts that the dependent module artifacts depend upon.To correct the problem, choose one of the following actions:
    - Create the library with the removed artifacts and add it to the
module dependencies.
    - Remove the original library from the module dependencies and also
cleanup the module's artifacts (for example, you may need to delete
the interface and binding in an import or export if the library contained
an interface or WSDL files and the library's port type was referenced
by the import or export).

## Related concepts

- Pattern of accessing external services with adapters
- Developing services with adapters
- Simple adapter wizard
- Migrating applications using previous adapter levels

## Related tasks

- Configuring and using adapters
- Creating a business object from a source file

## Related reference

- J2C data bindings
- A closer look at business objects from data structures
- J2C imports and exports at run time
- Trade-offs when developing adapter imports and exports
- Considerations when using adapters
- Contributing your own external service or data wizard plug-in
- Limitations for adapter imports and exports