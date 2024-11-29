<!-- image -->

# Business Integration perspective and views

The Business Integration perspective provides simple, uncluttered
views of essential resources so that you can model and build business
solutions. Unnecessary details and unused tools are hidden.

By default, when you launch the product, the Business
Integration perspective opens. This perspective has the following
views:

- Business Integration view
- Physical Resources view
- Editor pane
- References view
- Outline view
- Quick Outline view
- Visual Snippets view
- Build Activities view
- Properties view
- Problems view
- Servers view

## Business Integration view

The
Business Integration perspective has a Business Integration view,
which provides a logical view of the key resources in each module,
mediation module, and library. Within each project, the resources
are categorized by type. You can also use the Business Integration
view to navigate through Java™ and
Java 2 Platform Enterprise Edition resources and to open the various Java and Java 2 Platform Enterprise Edition
editors.

Logical resources shown in the navigation tree do
not necessarily have a one-to-one mapping to files. Artifacts that
are not necessary for the development of integration applications
are not shown in this navigation tree.

In the Business Integration
view, a module's resources are organized by type:

- Double-click Assembly Diagram to open the
assembly editor.
- Double-click Dependencies to open the dependencies
editor to see and manage the dependencies on other modules or libraries.
- Integration Logic contains all the artifacts
that perform specific tasks. Processes, mediation flows, state machines,
and human tasks are some examples of integration logic implementations.
- Data contains all the data representations
in the system. It contains business objects, business graphs, and
user-defined simple types.
- Interfaces contains interfaces that define
the operations that can be called from services.
- Mapping contains business object maps,
interface maps, relationships, and roles. In mediation modules, the
mapping category contains business object maps, XML maps, and XSL
style sheets.
- Events contains event definitions that
were created in the event definition editor. (The Events category
is shown only if there are event definitions (.cbe) files created
in that module.)

Click the Show Namespaces button,, to show the namespaces of the resources.

By default
the resources are sorted by type of object. You can also sort all
the resources within each module or library by the folders that contain
the resources or by namespaces (which would turn on and display the
namespaces of all the resources).

You can apply filters to exclude
all but required objects from the view. By default, filters are enabled
for data and interfaces. You can apply filters to other types of artifacts
in Preferences.

## Physical Resources view

The
Physical Resources view shows all of the file-level resources from
the modules and libraries in their natural form. Related projects
that are generated when you create business integration applications
are still hidden in this view.

The logical contents of the physical
file are also displayed in this view. For example, if you have several
business objects in an XSD file, you will be able to expand the XSD
file in this view and see all the business objects in the file.

If
you have an artifact open in an editor, you can click the opened artifact
in the editor pane (to focus on it) and then click the Link
with Editor  button to quickly locate the file
in the Business Integration view.

You can apply filters to exclude
all but required objects from the Physical Resources view. By default,
filters are enabled for XSD files to make it easier to find data types.
You can also apply filters to WSDL files by enabling that function
in Preferences and you can apply a filter to hide secondary artifacts.

The
.settings folder in this view contains properties that are used by IBM® Integration
Designer and
should be shared with each project. For that reason, the .settings
folder should be added to team repositories.

## Editor pane

When you open
a resource from the Business Integration view with an editor, the
resource is displayed in the editor pane. Many business integration
tools are graphical editors so that the diagrams are composed on the
canvas of the editor.

Graphical editors usually work with the
Properties view to show the properties of selected elements on the
canvas. Also, see the Outline view to
see how an editor works with that view.

## References view

For a selected
object in the Business Integration view, the References view shows
all of the artifacts that reference it and all the artifacts that
it references.

Select an artifact in the References view to
focus on that artifact and to show its relationships to other artifacts.
Click the Lock View button  to
lock the References view so that selecting objects in the Business
Integration view will not affect the References view.

## Outline view

The Outline
view works with the resource that is opened in the editor pane. For
some editors, including the assembly editor, the Outline view operates
in two modes: Show Outline, which is a navigation tree view, and Show
Overview, which is a graphical view.

- Right-click in the editor and click Show
in > Outline view.
- At the top of some editors, press the Outline view icon .

The Outline view in the Show
Outline mode, displays all the elements in the assembly diagram
that are open in the editor pane. When you click an element in the
Outline view, the editor pane and Properties view are synchronized
to show the selected element.

You can invoke actions from the
elements in the Outline view; select an element and right-click to
see the actions that are available.

Click the Show Overview button, , on the upper-right corner of the Outline window to change
the view into a graphical view of assembly diagram that is open in
the editor pane. The complete assembly diagram is displayed as a miniature
model in the Outline view. The gray box is the part of the assembly
diagram that is visible in the assembly editor. Use your mouse to
drag the gray box to the part of the assembly diagram that you want
to see in the assembly editor. This is an easy way for you to shift
the editor to the part of the diagram that you are interested in.

## Quick Outline

The Quick Outline
works with the resource that is opened in the editor pane. You can
use the Quick Outline to quickly examine and navigate the elements
in the resource of interest.

- Right-click in the editor and click Show
in > Quick Outline.
- From the editor press Ctrl+O.
- At the top of the graphical editor, on the end of the breadcrumb
area, press the Quick Outline icon .

In the Quick Outline, you can see a navigation tree of
the elements in the selected resources. When you select an element
in the navigation tree view, you set the focus to that element in
the editor pane.

## Visual Snippets view

The
Visual Snippets view is used to compose customized behavior in the
form of Java code.

## Build Activities view

You
can use the Build Activities view to help you manage builds. You can
select build activities for both automatic and manual builds. You
can also open immediate manual builds that are independent of those
build activity selections. You can use the Build Activities view to
show the build and server status of business integration projects
as well as the operational state of supported servers.

## Properties view

When you use
the Properties view with the Business Integration view or Physical
Resources view, you can see information about a selected artifact.

When
you use the Properties view with editors, you can modify properties
of selected elements in the editor.

## Problems view

Use the Problems
view to debug errors. For example, when you click an error for a component
in a module assembly, the assembly diagram and the component that
contains the error is highlighted.

To see additional help for
the problem message in the form of an explanation and recommended
actions, select the message and press F1.

In some contexts,
quick fixes are available. You can right-click an error or warning
and then select Quick Fix from the menu. If
there are quick fixes available, the program lists them for you. Select
the one you want to apply and press Enter.
The fix is applied and the warning or error marker disappears.

## Servers view

Use the Servers
view to create servers. You will use the view for testing and deploying
business integration applications.