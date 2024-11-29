# Properties widget

For each case type, IBM® Business Automation
Workflow provides a
system-generated layout that you can use for the Properties widget. This layout is automatically
generated based on the schema of the properties or data field collection. In the system-generated
layout, the property controls are organized vertically in the Properties widget. The properties are
listed in alphabetical order. On Task Details pages, work groups are sorted at
the top of the list. Attachments are not included.

Alternatively, you can design custom layouts for the Properties widget. You can design these
layouts for a case type to meet the requirements of different roles, activities, or steps. By
creating a custom layout, you can determine what properties are included and the order in which the
properties are displayed. For example, you might want present a comprehensive set of case properties
to analysts, but only a limited set to clerks. You can create one properties layout that includes
all the case properties and another to include only a limited number of properties. You then create
a Case Details page for analysts and another page for clerks. On each page, you
edit the settings for the Properties widget to specify which layout is to be used.

You do not have to configure the properties layout for the Properties
widget. Instead, you specify the properties layout that is to be used
by default for a case type. This default is used on any page where
you have not configured a specific properties layout for a case type.

You can add multiple instances of the Properties widget
to a page. You can also add instances of the Properties widget and
Form widget to a page.

In the Case Builder Step Designer, you can create workgroups for
      the steps (work items) in the Manage Workgroups section. You can use
      workgroups to assign work to one or more specific users instead of to any user in a role. In
      the Case Client, the workgroups are displayed at the top of
      the Properties widget where you can also add users to the workgroup. The system-generated
      layout always includes the workgroups. In a custom layout, you can include workgroups to the
      Properties widget by adding a workflow field to the view.

```
max = 9 * Math.pow(10, 15-places);
     min = -9 * Math.pow(10, 15-places);
```

The Number Text Box and Number Spinner digits automatically
enforce these computed    ranges.

## IBM Business Automation
Workflow pages that include this
widget by default

## Content Platform Engine data
models

- Case properties, which are content data
- Activity properties, which are workflow data

- Number text box
- Number spinner

- Radio button set
- Select
- Filtering select

For workflow data, a timestamp property uses the time of the browser, which is the local
time and includes daylight saving time. A time property uses the local time zone that is based on an
offset from Coordinated Universal Time (UTC). A time property does not include any adjustments for
daylight saving time. If you want users to see the local time including daylight saving time,
include the timestamp property on a page. If you include both of these properties on a page, the
times they show might not match.

- Numeric fields and Boolean fields
- Reused numeric properties that are marked as write only for a step.
- Fields that represent a single value that might be part of a choice list in Content Platform Engine. A case property that is defined as a string
property with a single value might have a choice list, and the property might be mapped to a
workflow step parameter. Because content data accepts a null value, but workflow data does not, the
property is marked as required.

The Properties widget marks string fields and datetime
fields as required only if you define the fields as required in Case Builder. Because the check box
control that is used for Boolean fields automatically enforces a value,
the Properties widget does not mark Boolean fields as required.

- Properties widget events

The Properties widget publishes and handles events to display case and work item properties for users to view and edit.