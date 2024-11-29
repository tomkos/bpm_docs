<!-- image -->

# Importing WSDL or XSD files

## About this task

To import WSDL or XSD files into a module, right-click
the module or library name in the Business Integration navigation
view, and select Import from the menu. In the Import window,
select WSDL and XSD and click Next.
The Import a WSDL, XSD or Both wizard opens.
Alternately, from the menu, you can select File > Import.
In both cases if a module is selected then it will be preselected
as the module for the imported files. If no module is selected, then
you must select the module from the list available or create a new
module.

- In the case of making the Local WSDL or XSD, or both selection, browse to
the WSDL or XSD file and select the file or files. The Import dependent
resources option, which is preselected, lets you see the references to the file you want
to import in the lower pane. You can complete your import at this point by selecting
Finish. The Target module or library field
indicates where the file or files will be sent. If you selected a module or library, you will see
the name in the field. You can also choose another module or library or create a new one.

Selecting Download remote resources lets you also import the
references your file may have. Clicking Next shows you the URL addresses of
the remote references. You can select them if you want and complete the import by clicking
Finish.

Note: The imported file structure is preserved with respect to referenced files. For example,
suppose you had a file folder /customer containing PreferredCust.xsd and a file folder structure
/customer/interface containing CustomerType.wsdl, which referenced PreferredCust.xsd. If you
imported CustomerType.wsdl then the imported structure would have a root directory based on
/customer (not /customer/interface).

Some vendors nest their interfaces and business objects within the WSDL file, in other words,
the interfaces, and business objects are not in separate files they are inline. Selecting
Extract inline elements (both interfaces and inline business objects) lets
you extract any inline elements into separate files when you import the WSDL file. The recommended
practice is to select this option as separate interfaces and business objects are easier to share
and reuse with other applications.
If you leave this option not selected, then your imported
interfaces and business objects are not put into separate files. A decorator appears in the upper
right corner of the icon to indicate that they are not separate files. You might want to import a
WSDL file with inline interfaces and business objects to quickly import a set of WSDL files. To
extract your imported inline interfaces and business objects later, right-click the interface or
business object and select Refactor or Analyze Impact. To extract a business
object, select Extract In-lined Business Objects. To extract an interface,
select Extract WSDL Components. The decorator is removed after
extraction.
If you select this option, then the behavior of how the business objects are
extracted is controlled by a preference setting. By default each business object, regardless of its
namespace, is placed in its own separate file. This is setting is best for maximum reuse of business
objects. However, if there is a very large number of business objects (for example, hundreds or
thousands) for the namespace, it is more efficient to place all of these business objects in one
physical file (both at authoring time and run time). Fewer physical files reduces the amount of
memory that is required to load the business objects.
To change the default behavior select Preferences > Business Integration. Select the check box beside Extract in-lined business objects into a
namespace file instead of separate files per business object.
The last page of the
wizard allows you to modify the generated file names for the resources.
Note: The option to
extract in-lined business objects into a namespace file is only available through the
Local WSDL or XSD, or both import option. It does not have affect on the
remote import, or refactoring operations.
- In the case of making the Remote XSD or WSDL file selection, the
interaction is similar to the Download remote resources selection. In the
URL field, enter the URL address of the remote computer. The
Target module or library field indicates where the file or files will be
sent. If you selected a module or library, you will see the name in the field. You can also choose
another module or library or create a new one. 
Separate inline business
objects separates inline XSD elements into business objects at the time that you import
the file. If you do not make this selection, your inline elements will have a decorator beside their
name after you perform the import. You can perform extraction later. 
Separate
interfaces (port types) from the other WSDL elements lets you extract the interface from
a file. This feature is useful if you plan to use mediation or some other processing using these
files and then want to have that work referred to from the same interface.

At
run time, business objects are rendered. See Supported XSD and WSDL artifacts. Avoid duplicate business objects and duplicate
WSDL interfaces. You might not notice the duplicates if they are in
another library or module that you are interacting with. See Duplicate business objects.

## Related tasks

- Interoperability with services from other vendors
- Exporting WSDL files

## Related reference

- WSDL binding styles