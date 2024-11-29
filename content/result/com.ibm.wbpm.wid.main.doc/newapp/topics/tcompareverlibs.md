<!-- image -->

# Comparing business objects in modules and libraries

You can compare modules and libraries to see the differences
in the business objects. You can view, but not edit, the comparison
file.

## About this task

You can also compare business objects that are within
WSDL files, commonly referred to as inline schemas. In this case,
the business objects have decorators ( ) indicating that they are
inline schemas and not in separate files.

The comparison is
viewable though not editable.

## Procedure

To compare business objects, complete the following steps:

1. Select the modules or libraries in the Business Integration
view that you want to compare. Right-click the selected module or
libraries and from the menu, click Compare Business Objects. The compare editor opens with the original and revised modules
or libraries.
2 When you select a business object, you can see its descriptionin the Structural Changes pane and its references in the ReferencingComponents pane. Selecting any business object shows a descriptionin the Structural Changes pane and its referencesin the Referencing Components pane. Copy Report to Clipboard places the comparison on theclipboard. Differences are distinguished by color.

Differences are distinguished by color.

    - Yellow indicates changes in business objects with the same name.
    - Red indicates business objects that were in one module or library
and deleted in the other.
    - Green indicates business objects that were added to one module
or library.
3 To view information about a business object, right-clickthe object:

1. To view identical business objects that have been changed
in some way, right-click the object and click Open in Compare
Editor. Icons in the top-right corner let you move to
the previous or next difference.
2. To see changes in the Business Object editor, right-click
the object and click Show in Business Object Editor.
3. To see references to and from other artifacts, right-click
the object and click Show in References.
4 In the top-right corner are some icons that qualify thebusiness object comparison. From left-to-right, the left-most iconadds a qualification by namespace; that is, the business objects withthe same namespace are compared. The next icon qualifies by file nameand location, and then business object and name. To view informationabout business objects, click the following icons:

1. To show only identical business objects that have been
changed in some way, click Show Only Modified Business
Objects.
2. To show all business objects that have changes, such
as new or deleted business objects that are included in the view,
click Show Only Added, Deleted, and Modified Business Objects.
3. To show business objects that have been added to one
of the modules or libraries, click Show Only Added Business
Objects.
4. To show business objects that have been deleted from
one of the modules or libraries, click Show Only Deleted
Business Objects.
5 You can swap the comparison view of the source and targetlibraries or modules. To swap the comparison view, click the followingicon:

- To place the comparison on the clipboard, click Copy
Report to Clipboard.