# Properties

## Width for property editors

The default label width is 30%. The label width cannot be specified if the horizontal alignment
is set for the container.

If you use the Long format or Full format setting
for a DateTime property, you might need to adjust the width of the setting to accommodate the
longest long or full format value of the supported locales.

- Adjusts the specified width to avoid unnecessary scroll bars
- Provides a default field width for each property editor if no width is specified
- Provides a minimum field width for each property editor if the specified width is less than the
minimum field width

## Patterns for Integer and DateTime fields

The canvas in the Properties View Designer shows you how the selected editor setting looks in
Case Client.

- For Integer fields, IBM Business Automation
Workflow supports the patterns that are
listed in Part 3: Number Format Patterns.
- For DateTime fields, IBM Business Automation
Workflow supports the patterns that are
listed in Part 8: Date Format Patterns.

## Displaying DateTime fields in coordinated universal time (UTC)

By default, DateTime values are displayed according to the user's local time. You can select the
Display in UTC check box to display a DateTime value in coordinated universal
time. If you select this check box, you must use either the short format or medium format for the
time.

Other widgets do not display DateTime values in coordinated universal time. For example, assume
that the same DateTime property appears in both the Properties widget and the Case Information
widget on a page. If the Properties widget is configured to display the property in coordinated
universal time, the property can appear to have different values.

## Reconciliation of conflicting property settings

The attributes of a property are determined by the view settings and by the settings in the
controller layer. The view settings are specified in Properties View Designer. The controller
settings are set either when you define the property in the solution or programmatically by an agent
such as an external data system, a script, or web service.

- Any property attribute in the controller layer that is set by using an external data service or
some other form of automation is automatically applied to the view. The corresponding property
editor setting in the view definition is ignored.
- For property attributes that are not set by automation, IBM Business AutomationWorkflow applies one of the following rules to reconcileany differences in a setting:
    1. Precedence is given to the view setting for settings such as label, which affect only the
display of the property.
    2. Precedence is given to the controller setting for settings such as pattern, which affect the
property data.
    3. View settings can never be less restrictive than the editor settings. For example, if the
controller maximum value is 100 and the view maximum value is 50, then the view setting is applied.
But if the controller maximum value is 100 and the view maximum value is 150, the controller setting
is applied.

The following tables identify the precedence rules that IBM Business Automation
Workflow applies to each setting:

| Setting   |   Precedence rule |
|-----------|-------------------|
| Label     |                 1 |
| Required  |                 3 |
| Hidden    |                 3 |
| Read-only |                 3 |

| Setting       |   Precedence rule |
|---------------|-------------------|
| Format        |                 1 |
| Date pattern  |                 1 |
| Time pattern  |                 1 |
| Minimum value |                 3 |
| Maximum value |                 3 |

| Setting             |   Precedence rule |
|---------------------|-------------------|
| Zero if empty       |                 3 |
| Round automatically |                 3 |
| Pattern             |                 2 |
| Decimal places      |                 3 |
| Minimum value       |                 3 |
| Maximum value       |                 3 |

| Setting                |   Precedence rule |
|------------------------|-------------------|
| Maximum length         |                 3 |
| Minimum length         |                 3 |
| Truncate automatically |                 3 |
| Capitalization         |                 2 |
| Adjust capitalization  |                 3 |
| Pattern                |                 2 |

| Setting        |   Precedence rule |
|----------------|-------------------|
| False if empty |                 3 |

## Best practices for property editor settings

If you set a property attribute dynamically by using an external data service or some other form
of automation, do not configure the property editor setting in the view definition. The setting must
be configured in the view definition to use the default value.

If you do not set a property attribute dynamically, use the view definition to customize the
property editor settings.

Whether you set a property attribute dynamically or through customized settings in the view
definition, do not specify a setting that exceeds the constraints of the object store. For example,
if the object store imposes a maximum length of 10 for a string property, do not set the length to
20 in the view definition.

## Multivalue editors and property tables

Use the Radio button set as the editor setting for a multivalue property
only if the property has a limited number of choices. When a multivalue property uses the
Radio button set editor setting, the field appears as a drop-down list in
Case Client. When the user clicks the list, a dialog box opens. The
user then clicks the Add icon to open the editor that displays the choices as
radio buttons. If the number of choices exceeds the size of the dialog box, a scroll bar is
displayed. However, the scroll bar does not work correctly.

If a multivalue property contains more than a few choices, consider using an editable entry list
as the editor setting.

- You must enter at least one value for the property, even if that value is an empty string.
However, if you are using an Oracle database, you can not enter empty strings in a multivalue
property.
- The required tooltip is always displayed. The user must click the Exit button (x) or press the
ESC key to close it.
- Entry of invalid data is supported, but you cannot save the data until all of the invalid data
is corrected.
- Double-click to change to edit mode. In Mozilla Firefox, the property field is automatically
editable when you add a row. In Microsoft Internet
Explorer, you must double-click to change to edit mode.
- When the property field is in edit mode, you must use the arrow keys to edit at a specific
location.
- When you use the hint inside the editor, the hint flashes. It is recommended to use a hint
position outside the editor.
- For multivalue editors only: Clicking any other area in the view does not close the multivalue
editor window.

## Boolean property

If you want check box editor settings to behave like other editor settings, you can use the
Uniform labels setting in the Layout and Titled Layout container objects.

- Set the Layout direction setting to Horizontal and
the Label position to Beside for a Layout
container.
- When you drag a Boolean property, the label appears on the right side whereas the label for the
other types of properties appears on the left.
- Setting the label position to Above has no effect on the Boolean
property.
- When no default value is configured for a Boolean property, the value for the
uninitiated property is left blank (not set to false).

## Filtering properties

You can use the filter in the property palette to filter the properties list.

## Cross-validating constraints

Properties View Designer validates the value type that you enter for a setting. However,
Properties View Designer does not cross validate that value with the constraints that are set by
other settings for the same property. For example, you can select the Zero when
empty check box for a property, and then also set Minimum value
to 1. You can save this combination in Properties View Designer. However, at run time, Case Client automatically displays an error state for the field because it
defaults to zero and the minimum value is 1.

## Editor behavior

Check boxes always force the null value to false.

- Radio buttons cannot be cleared to set to null after a selection is made.
- DateTime: Delete the date and time value to set it to null. You can enter date and time value by
using the keyboard without using the picker.
- DateTime: If the date is entered first, the time defaults to 12:00 PM. If the time is entered
first, the date defaults to the current date.
- If a property is marked both required and read-only, the asterisk character (*) is shown.
- The asterisk character is not shown if the Zero when empty check box or
False when empty check box is selected. You can use these settings to
suppress the required asterisk if zero or false is a suitable default value for the property.
Because the property always has a value, the required asterisk is not required.
- Empty rows are not supported in any data type except strings. If you are using an Oracle
database, empty rows are not supported for strings.

## The Required attribute for a Boolean property

## Rendering of editor settings that are shared by multiple tasks

1. Required: false
2. Hidden: false
3. Default value: null