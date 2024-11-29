<!-- image -->

# Exporting WSDL files

## About this task

To export WSDL files from a module, right-click the module
name in the Business Integration navigation view, and select Export from
the menu. In the Export window, select WSDL/Interface and
click Next. The WSDL/Interface Export
to File System page opens. You can also select an interface,
business object or web service port in the module; and the wizard
will open with all the artifacts. Alternately, from the menu, you
can select File > Export.

- If you intend to export the selected WSDL files with their dependencies,
including other WSDL or XSD files, as they are, beside the To directory field,
click Browse and locate the folder to export
your files to. The wizard displays the files and any referenced files
in the lower pane. The default selection is to include all referenced
files when you complete the export, though you can clear the check
box and only export the specified file. You can also overwrite existing
files in the folder you selected. Selecting this overwrite option
means that files will be overwritten and you will not be warned. Clearing
this option means you will be warned if an identical file exists.
Check that Export dependent resources is selected
if you want to also export the dependencies.Click Finish and
the files are exported.
- If you intend to merge your separate files into one file containing
inline elements, beside the To directory field, click Browse and
locate the folder to export your files to. The wizard displays the
files and any referenced files in the lower pane. The default selection
is to include all referenced files when you complete the export, though
you can clear the check box and only export the specified file. You
can also overwrite existing files in the folder you selected. Selecting
this overwrite option means that files will be overwritten and you
will not be warned. Clearing this option means you will be warned
if an identical file exists. Check that Export dependent
resources is selected if you want to also export the dependencies.
Select Merge dependent resources into the parent WSDL file.Click Finish and
a single file is exported.
- If the referenced files in your module are currently inline and
you intend to export the file, beside the To directory field,
click Browse and locate the folder to export
your file to. The wizard displays a single file in the lower pane
as you do not have separate files for the references. Click Finish and
the file is exported.

Default file naming rule: The existing WSDL file name remains
the same in an export. If you merge all contents into a single WSDL
file then the interface (PortType) is used as the container. In refactoring
(that is, if you are extracting WSDL and XSD elements), a new name
is not generated. The default name is <old name>\_Endpoint.wsdl for
the file that contains the WSDL though you may override the name.

Note
that if you use a web services binding that uses the Java API for
XML Web Services (JAX-WS), the export name must comply with Java class
name rules.

## Related tasks

- Interoperability with services from other vendors
- Importing WSDL or XSD files

## Related reference

- WSDL binding styles