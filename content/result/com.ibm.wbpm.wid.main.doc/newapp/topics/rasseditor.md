<!-- image -->

# Assembly editor

The IBM® Integration
Designer's
assembly editor lets you build applications by assembling the Service
Component Architecture (SCA) components.

The assembly editor works with the following views:

- Editor pane
- Properties view
- Outline view
- Problems view

## Editor pane

The Editor pane
is a part of the Business Integration perspective. When you open a
module assembly with the assembly editor, you can visually compose
the integrated application by adding components and connecting them
with wires in the Editor pane.

The modeled application is also
referred to as the assembly diagram. The Editor pane has a canvas where
you create the assembly diagram.

There is a palette where
you can pick an element and add it to the canvas.

The palette
groups its elements in folders.

- Components These components will have implementations
to provide the logic that operates on data.
The component
(with no implementation type) in the palette, , can be used when you want to create a new component but
do not know which type of implementation will be used for it. Later,
you can specify the implementation type and generate its implementation. 
The Java™ component in the palette, , will be implemented as a Java class.
It supports both WSDL type interfaces and Java type
interfaces. It is the only component type that supports Java type interfaces.
Other components
include process, mediation flow, human task, state machine, and so
forth. Hover help is available for each element. For more information
on each type of component, see related concepts.
- Import, export, and standalone references These elements
provide access to services and they do not have any implementations.
See "Components" under related concepts for more information.
- Interface map and selector These elements are special
components that do not have "business logic" implementations. Interface
map contains "mapping" logic for interface operations. Selector provides
"routing" logic to invoke required services. See related concepts
for more information on these components.
- Wire This is used to assemble components into an integrated
application by identifying target services.

See "Components" under related concepts for more information
on these elements.

## Properties view

When working
with the assembly editor, you use the Properties view to modify properties
of the selected element on the canvas.

The
component properties are grouped into Description, Details, and Implementation:

- Description properties include information such as the
name of the component and its location. The display name is not used
in the assembly diagram, but it is used in some runtime processes.
If you leave the Synchronize with the name field box
selected, the name and the display name will remain the same.
- Details properties are for component's interfaces and partner
references. A tree view lists all the interfaces and references; select
one of them to display its properties in a Details page or a Qualifiers
page.
- Implementation properties Depending of the type of implementation
that the component has, there may be different pages of implementation
properties. Use the F1 key to get additional help on the properties.
Binding
properties
For imports and exports, there are binding properties
(instead of implementation properties). Here is an example of the
Properties view showing the binding properties for an import:

## Outline view

The Outline
view works with the resource that is opened in the Editor pane. The
Outline view operates in two modes: Show Outline, which is a tree
view, and Show Overview, which is a graphical view.

The Outline
view in the Show Outline mode, displays all the elements in
the assembly diagram that is open in the Editor view. When you click
an element in the Outline view , the Editor view and Properties view
are synchronized to show the selected element.

You can invoke
actions from the elements in the Outline view; select an element and
right-click to see the actions that are available. For the module,
there is an Add action that lets you add artifacts
to the assembly diagram that is open in the Editor view.

Click
the Show Overview button, , on the upper-right corner of the Outline window to change
the view into a graphical view of the assembly diagram that is open
in the Editor view. The complete assembly diagram is displayed as
a miniature model in the Outline view. The gray box is the part of
the assembly diagram that is visible in the Editor view. Use your
mouse to drag the gray box to the part of the assembly diagram that
you want to see in the Editor view. This is an easy way for you to
shift the Editor view to the part of the diagram that you are interested
in.

## Problems view

Use the Problems
view to help you debug errors. For example, clicking on an error for
some component in a module assembly will open the assembly diagram
in the Editor view with the component that has the error selected.