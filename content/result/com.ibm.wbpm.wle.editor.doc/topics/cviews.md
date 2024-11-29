# Views

Because views are reusable, each view instance can share parts of its user interface with other
view instances in a coach. For example, you create a coach that contains a view instance that
includes a set of address fields. If you create a second coach that needs the same address fields,
you can reuse the view. In both cases, the coach is using an instance of the view. You can edit the
properties of each instance independently. For example, changing the label of one view instance does
not change the label of the other. Both view instances use a reference to point to the view
definition. This approach means that if the view definition changes, you can see the change
reflected in the instances of the view.

You can modify the view instances by using configuration properties and by overriding default
styling. For each view, the data binding is optional. However, if you define a binding for an
instance, it must match the type in the view definition. A warning occurs if the business object
type does not match the type of the data binding that is defined for the view. In each view topic,
the business object binding table lists the business object type that is defined for the view. For
each view instance, the configuration properties are optional. If you want to override the default
value, you can provide a specific value or you assign a variable. As a convenience, you can also
expose the configuration property to any view or coach in a human service
that contains the view. Exposing the configuration property creates a configuration option in the
current view with matching binding. You do not have to create the configuration option and bind
it.

- Composite-style views are simple and do not require advanced technical skills to build. To
create a composite-style view, add content to the layout from the palette. If your view has multiple
areas of information, use the grid layout to arrange the views, then set their properties and
complete the data binding as required. Composite-style views can be reused in multiple coaches or in
other views that can be built hierarchically.
- Widget-style views are more complex and require a more technical skill set. Typically, the
widget-style views are custom views that can include, for example, a custom HTML segment that you
can populate with HTML code, or an iFrame that has a specific ID. You can set the configuration
properties of the widget-style view and add inline CSS and inline JavaScript logic in the
Behavior page. For behavior that occurs at run time, for example, when a page
is loaded or a button is clicked, you can place the JavaScript logic inside the view's event
handlers, under Events. For tips on how to develop
widget-style views for use with IBM® Robotic Process Automation
with Automation Anywhere, see the following
section.

## Considerations for IBM Robotic Process Automation
with Automation Anywhere (deprecated)

With IBM Robotic Process Automation
with Automation Anywhere
(IBM RPA),
repetitive tasks in Business Automation Workflow processes can be
automated and expedited by using bots. To enable an efficient interaction with the IBM RPA bots, the following
enhancements were made to the Business Automation Workflow coach framework.

- Use context.controlidpath as the base string for HTML IDs within the DOM
structure of your views. For example, when you build a Text view, you might want to give your label
DOM element the ID text-label-<controlidpath> and the input element the ID
text-input-<controlidpath>.
- Apply the unique identification to all the DOM elements with which the user might want tointeract in an RPA task, including the following elements:
    - Form-style fields
    - Read-only information that might be used by the task, for example, text that might be copied by
the task for some purpose
    - Page navigation fields, such as Tab
- To verify that a view works well with the IBM RPA bots, record the
interactions using the RPA Smart Recorder, and ensure that the captured HTML IDs are the expected
ones, as described earlier. Iterate through recording, playback, and HTML ID assignment until all
the interaction elements have stable IDs. Note: Users might still need to make minor adjustments to
the recorded objects to optimize the playback, but the adjustments should be limited to simple
changes such as changing keystroke delays, removing captured properties, and so on.

For more information about IBM RPA, see the IBM Robotic Process
Automation with Automation Anywhere documentation.

- Templates

Templates provide a way to create a standardized look across multiple views.
- View properties

Each view has a set of standard properties, including general, positioning, configuration, events, visibility, and HTML attributes.
- Formulas

Formulas allow you to set the value of a view based on the content of other views.
- Dynamic configuration of view properties

Typically, you would use data binding and variables to configure data in a coach. To configure a UI view, you can use references to the view instance data and public methods to dynamically change the view configuration.
- Drill-down trees

To organize chart data in categories and present the different categories in a hierarchical format, you can use drill-down trees. You specify the hierarchical structure of the chart data in XML format.
- Data binding for views

Binding a view to a business object creates an association between data and a user interface for it.
- Binding data and configuration options

A view may be associated with a data binding and configuration options. The view context provides access to this data. To access binding data and configuration options you must use the JavaScript get and set functions. You cannot use JavaScript dot notation.
- Boundary events

A boundary event acts as a trigger within a human service that sends information from a coach to the human service, where the information could then be committed and the human service moves to the next step of the flow.
- Event handlers for views

Views have predefined event handlers that perform callback functions when an event is detected. You can add your own code to these event handlers in the Behavior properties of the view.
- Addressing

Addressing is supported in all views in the UI toolkit, including views that are nested within other views that are defined in a UI page.
- Custom functions

For more flexibility, you can create custom JavaScript functions to manipulate data in pages and views.
- Framework managed versus view managed content for coaches

At run time, the content inside a content box of a coach can be managed by the runtime framework or by the view. By default, the framework manages the content, but if you want to code your own custom behavior, you can choose that the content be managed by the view.