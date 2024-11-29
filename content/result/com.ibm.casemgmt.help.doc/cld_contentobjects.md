# Content objects

There are three types of content objects:

- Business object
- Activity (which wraps activity properties)
- Case (which wraps case properties)

Content objects are created in one of the following ways:

- When a new business object is defined in Case Builder, a corresponding content object is automatically
created in Process Designer. These business
objects can define inheritance and the resulting content objects can convey the content.
- When case types and activities are defined in Case Builder, corresponding content objects are automatically
created in Case Builder to wrap the properties of each
case type and activity.

If you have an existing case solution and content
object support is enabled, content objects are automatically created for the solution artifacts when
you open the solution for editing in Case Builder. For
information about content object support, see the topic Content object support.

Content objects are primarily used in processes, coaches, and client-side human services, as
described in the following sections.

## Content objects in Process Designer

In the Process Designer library, business
object, activity, and case content objects are displayed in the Content
Objects section of the Data category. Activity and case content
objects are also used in the Variables tab of the process and client-side
human service.

A Content Object editor is available for viewing the read-only content objects and their
structure. The editor is composed of several panes, such as:

- The Common pane, which includes a Unique Identifier field that displays a
unique identifier used in the JavaScript API.
- The Behavior pane, which includes a Parent field that displays a link to
the content object parent.
- The Properties pane, which includes inherited properties and flags to indicate that they are
inherited.
- The Details pane, which is displayed when a property is selected in the Properties pane.The Details pane includes the
Required and Hidden check boxes. If the
Required check box is selected, the property is required. A required property
must have an assigned value. If the Hidden check box is selected, the
property is hidden in client user interfaces.

To launch the Content Object editor, select the name of a content object from the Content Objects
section of the Data category in the library.

## Content objects in coaches and client-side human services

In coaches, content objects are visualized in the same way as other business objects. The content
objects can be dragged onto a coach to enable the data to be viewed or edited by the task recipient.
The fields of the content object are Property objects that define display names.

Complex business objects, including content objects, can be specified as input to a client-side
human service. At run time, the process engine will only pass an instance of the business object
with the selected fields populated. This enables the capability to filter the data that is exposed
to the client without needing to create a new wrapper type that contains only the fields of
interest. The selected fields are flagged accordingly in the Variables pane. See Working with content object variables.