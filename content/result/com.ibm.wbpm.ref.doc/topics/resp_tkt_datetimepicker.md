# Date Time Picker (deprecated)

For most browsers, the Date Time Picker view shows the native date and time picker that is
included with the browser. This behavior means that when users switch browsers, they see different
date time pickers. For example, on a notebook computer, a user might work on a task with Google
Chrome and therefore see the Chrome date and time picker. If the user then switches to an Apple
iPhone, the user will see the Apple Safari date and time picker instead. If a browser does not have
a native date and time picker, the view uses its own date and time picker. For example, Mozilla
Firefox is a browser that does not include a native date and time picker.

Because
the date time picker uses browser date and time pickers, users must
set their language preference in both their Business Automation Workflow profile
and in the browser. Setting the language in both places ensures correct
behavior.

Although the date is stored in UTC time, the date
and time that is shown is adjusted for the time zone of the user's
system.

## Restrictions and limitations

- Attention: If the user types in content that is not a complete date or not in a valid
format, the bound data item is null when the user triggers a boundary event such as clicking a
button. If the flow returns to the coach, the view is empty. Any other views that are bound to the
same data item are also empty.
- With Microsoft Internet Explorer 9 (deprecated),
users see a Date Time Picker view that is within a section that has a horizontal layout occupying
the entire width of the section. Other views in the section are wrapped so that they are placed
above or below the Date Time Picker like in the vertical layout. To prevent this behavior, set a
width such as 25em in the Layout properties of the
Date Time Picker view.

## Data binding

| Binding description                                                             | Data type   |
|---------------------------------------------------------------------------------|-------------|
| Contains the initial date and time to display and stores updates to this value. | Date        |

## Theme definitions

The design mode of the theme editor contains a simulation of this view. If you hover over the
simulation, it lists the theme definitions that determine the appearance of the view. For
information on the theme editor, see Creating themes.

## Configuration properties

<!-- image -->

Using native date and
time pickers means that some configuration options do not apply for certain browsers or have an
alternate behavior. For example, if you are using Google Chrome V30 or later, the Date
format and Show calendar configuration options do not apply. In
addition, the Show calendar option has limited functionality because there is
no inline calendar and no separate button to click (instead, the user sees an arrow at the edge of
the field).

| Configuration property   | Description                                                                                                                                                                                                                                                                                                                                                                                                | Data type             |
|--------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------|
| Date format              | Set the format used to display and parse text that is entered into the text field, such as MM/dd/yyyy or dd/MM/yyyy. This configuration option supports the same formats as the Java™ SimpleDateFormat. For information, see http://docs.oracle.com/javase/6/docs/api/index.html?java/text/SimpleDateFormat.html.This configuration option applies only when a browser does not have a native date picker. | String                |
| Placeholder hint         | A brief description or example of the input required by the user. If the bound data item does not contain a value, users see the hint until they type in the field.                                                                                                                                                                                                                                        | String                |
| Show calendar            | Select the calendar display. On click shows the calendar only when the user clicks the text field or clicks the icon next to the text field. On click is the default value. Inline shows the calendar inline and hides the input text field Never shows the input text field and hides the calendar.                                                                                                       | CalendarShowSelection |
| Calendar type            | Select the type of calendar: Gregorian (default) Hebrew Islamic                                                                                                                                                                                                                                                                                                                                            | CalendarType          |
| Include time picker      | Select whether to add a time picker to the date time picker.The default value is not selected (False).                                                                                                                                                                                                                                                                                                     | Boolean               |
| Blackout Dates           | Set one or more dates that the user cannot select. If the browser does not support blackout dates and a list of blackout dates is provided, the view uses its own date and time picker instead of the native browser date and time picker.                                                                                                                                                                 | Date (List)           |
| Style > Text size        | Set the size of the text in the view, the size of the label text, and the amount of padding around the text. For example, to make the text and label more readable on smart phones, you can set this configuration option to Large for the small screen size. The default value is Medium.                                                                                                                 | String                |