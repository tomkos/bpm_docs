# Date Picker
(deprecated)

## Data binding

Set or modify the data binding for the view in the General properties. The
data binding contains the initial date to display and stores updates to the value. The data type is
Date.

## Configuration properties

Under Configuration,
set or modify the appearance and behavior properties for the view.

<!-- image -->

| Appearance configuration property   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Data type                  |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------|
| Date Picker type                    | The type of calendar display for the date picker: Text Input: This calendar display features a text input box and initially hides the calendar. When the text box is clicked, the calendar is displayed. Inline: This calendar display features an inline calendar and hides the text input box.  The default value is Text Input.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | DatePickerType             |
| Width                               | The width of the date picker when the Text Input type is selected for the Date Picker type property. You can specify the width in px (pixels), % (percent), or em units. For example, 200px. If no unit type is specified with the numeric value, then px is assumed. By default, no width is specified.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | String                     |
| Size                                | The size of the text in the view, the size of the label text, and the amount of padding around the text. For example, to make the text and label more readable on smart phones, you can set this configuration option to Large to compensate for the small screen size.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | TextSizeStyle              |
| Label placement                     | The label placement location for the date picker.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | LabelPlacement             |
| Label width                         | The width of the label. You can specify the width in px (pixels), % (percent), or em units. For example, 50px, 20%, or 0.4em. If a unit type is not specified, px is assumed.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | String                     |
| Format                              | The format used to display and parse text that is entered into the text field, such as mm/dd/yyyy or dd/mm/yyyy.The default format is mm/dd/yyyy. Acceptable combinations are d, dd, D, DD, m, mm, M, MM, yy, yyyy d Numeric date, no leading zero. For example, 5 dd Numeric date, leading zero. For example, 05 D Abbreviated weekday names. For example Mon DD Full weekday names. For example Monday m Numeric month, no leading zero. For example, 7 mm Numeric month, leading zero. For example, 07 M Abbreviated month names. For example, Jan MM Full month names. For example, January yy 2 digit years. For example, 12 yyyy 4 digit years. For example, 2012   Note: The abbreviated and full month (M, MM) and abbreviated and full weekday names above (D, DD) do not support all capitalized letters (e.g. MAR, MARCH, MON, MONDAY). The view only supports the mixed-case formats shown above. | String                     |
| Week start                          | The day that starts each week. The default value is Sunday.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | DatePickerWeekStart        |
| Disabled week days                  | One or more days of the week that are blocked out on the calendar. By default, no days are disabled.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | DatePickerDisabledWeekDays |
| Show Today button                   | Show or hide the Today button, which sets the date to today's date. By default, the button is not displayed.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Boolean                    |
| Show Clear button                   | Show or hide the Clear button, which clears the date value. By default, the button is not displayed.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Boolean                    |
| Orientation                         | The orientations of the calendar when it is clicked.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | DatePickerOrientation      |
| Color style                         | The color style of the date picker. The colors correspond to variables in the specified theme. The default value is Default (dark blue).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | DatePickerColorStyle       |
| Show week number                    | For Gregorian calendars, displays the number of the week in the year. For example, the last week in a Gregorian year is week number 52. By default, no week number is shown.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Boolean                    |
| Highlight Today                     | Specifies whether today's date is highlighted in the calendar. By default, today's date is not highlighted.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Boolean                    |

| Behavior configuration property   | Description                                                                                                                                                                                                                                                                                   | Data type             |
|-----------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------|
| Tab index                         | The tabbing sequence index. The tab indices start at 1 and can be set sparsely. For example, you can use 1, 5, 10. The Tab index property controls the tabbing sequence when you move between UI areas by pressing the Tab key.                                                               | String                |
| Placeholder text                  | The placeholder text to use when no date is entered. Typically, the text is a brief description or example of the input required by the user. If the bound data item does not contain a value, users see the hint until they type in the field. By default, no placeholder text is specified. | String                |
| Available start date              | Specifies the available start date and time. All dates prior to the specified available start date will be blocked out. The format for the available start date is specified by the Format property in the Appearance properties. By default, no available start date is specified.           | String                |
| Available end date                | The available end date and time. All dates after the specified available end date will be blocked out. The format for the available end date is specified by the Format property in the Appearance properties. By default, no available end date is specified.                                | String                |
| Start view                        | The level of granularity that the calendar should start at: Month Year Decade  The default value is Month.                                                                                                                                                                                    | DatePickerStartView   |
| Minimum view mode                 | The minimum date granularity levels to use in the calendar: Days Months Years  The default value is Days.                                                                                                                                                                                     | DatePickerMinViewMode |
| No auto close                     | Specifies that the calendar will not close when a date is selected. Instead, the calendar will close when the date picker loses focus. By default, the calendar closes automatically when a date is selected.                                                                                 | Boolean               |

## Example

If you want to have a clickable calendar button, you can place a Date Picker view inside of an
Input Group view. In the properties for the Input Group view, set the Button
type property to Icon and set the Button
info property to calendar. In the On button
click event for the Input Group view, type the following string:

```
${Control\_ID}.\_instance.pickerControl.show();
```

## Events

Set
or modify the event handlers for the view in the Events properties. You can set
events to be triggered programmatically or when a user interacts with the view. For information about how to define and code events, see User-defined events. Date Picker has the following types
of event handlers:

- On load: Activated when the date picker loads. For example: var
workerStart = ${StartDate}.getDate(); me.setStart(workerStart);
- On change: Activated when a change is detected. For example:
return confirm("Are you sure you want to change date?")
- On day cell render: Activated when there is a day cell render. It is
triggered before the date shows on the date picker. For example:
me.setDate("01/01/2015")

Depending on the specific event, you can use JavaScript logic to modify the effects of the view.
More information on using events with views is found in the topic User-defined events.

## Methods

For detailed information on the available methods for Date Picker, see the Date Picker JavaScript API.

## Additional resources

For information about how to create a coach or page, see Building coaches. 
For information about standard properties
(General, Configuration,
Positioning, Visibility, and HTML
Attributes), see View properties.