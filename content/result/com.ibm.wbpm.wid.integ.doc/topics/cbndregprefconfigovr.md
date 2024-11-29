<!-- image -->

# Binding registry preferences page

- Binding registry overview
- Binding registry preference page overview
- Importing and exporting user-specified entries
- Binding registry entry edit window
- Binding registry export window
- Binding registry import window

## Binding registry overview

When
working with a resource adapter, we need to capture the information
required by the adapter to marshal the EIS-neutral data objects to
the native objects used to interact with the Enterprise Information
System (EIS). There are several artifacts involved with the process
of data conversion, formatting, and generation. The data binding generator,
for example, generates a data binding implementation that is responsible
for marshalling a request business object to an EIS-internal data
format; it is also responsible for unmarshalling a response from an
EIS-internal data format into a business object. Generic, that is,
non-generated data bindings are common too. A function selector converts
an inbound message to the correct function on a target service.

A
data binding and function selector object can use data handlers that
provide data transformation functions from one form to another.

The
binding registry component provides a global point of access to the
repository for data binding, data binding generator, data handler
and function selector objects information. When a particular binding
is selected for a service component that is being created, the registry
information is accessed and the right level of the binding information
is provided to the user.

## Binding registry preference page
overview

You can register your own binding implementations
through the binding registry preference page available. To access
the binding registry preference page, from the menu select Window >
Preferences. In the Preferences window,
expand Business Integration and click Binding
Registry.

The preference page is divided into a Registry
Entries view where all registry entries are shown and
a Details view where properties of a selected
entry are shown. You can add a new entry to the User specified
entries section by using an Add button
or edit an existing user specified entry by using an Edit button.
These buttons launch windows that you complete. You can also remove
a user specified entry by using a Delete button.
 The plug-in specified entries and the adapter specified entries are
treated as system entries and cannot be changed.

## Importing and exporting user-specified
entries

You may decide to remove your entries from the binding
registry but do not want to lose the entries information itself. You
can store selected entries from the user-specified entries section
into a file by using the export function which is activated by clicking
the Advanced button. Subsequently, the entries
stored in the file can be added back into the binding registry by
using the import function, which is also activated by the Advanced button.
This feature lets you share binding registry content among workbenches.

## Binding registry entry edit window

- Display name: Contains a short name that
identifies the binding object and is intended to be displayed by tools.
- Description: Provides the detailed description
of the binding object.
- Class name: Specifies the fully-qualified
name of the binding object implementation class.
- Type: A constant that identifies the binding
object. A type from the list (DataBinding, DataHandler, FunctionSelector)
is prepopulated based on the top-level interface that the binding
object class implements.
- Supported type (optional): A list of fully-qualified
names for the Java™ interface or class that provides
the bindings contract. For example, with CICS® this
would be the javax.resource.cci.Streamable class
and with JMS it would be the com.ibm.websphere.sca.jms.data.JMSDataBinding class.
- Supported service type: A list of service
binding types that use the binding object. The following service types
are supported: JMS, MQ, HTTP, FTP, Email, Flat File.
- ASI namespace URI (optional): A list of
the namespaces of the Application Specific Information (ASI) Schemas
that are supported by the binding object. To indicate that the binding
object can handle a business object that does not have or does not
need ASI information specified, you can use special form of URI - urn:commonj.connector.asi:nil -
as a value for the ASI namespace URI property.
- Tag: A list of tags. A tag value specifies
an additional context for the binding object usage.

## Binding registry export window

The Export
Binding Registry User Specified Entries window lets you
copy user-defined entries to an external file so that the entries
can be shared among other workbenches. In the window you need to specify
the name of the file including a .bindings file extension,
and the location in the workspace where the file should be saved.
Typically you would save the file to a folder under your Business
Integration module and then export the module as an Integration module
or a Project Interchange file.

Important: Only files
with a .bindings file extension will be processed
by the import function at the time when you retrieve the entries stored
in the file back into binding registry. Therefore, DO NOT CHANGE this
file extension.

## Binding registry import window

The Import
Binding Registry User Specified Entries window lets you
load user-defined entries from an external file back into the binding
registry. In the window you need to specify the location in the workspace
where the file with the .bindings file extension
is stored. If you do not have the file in the workspace, you can import
it from the file system into workspace folder using the Import function
and specifying an import from the File System.