# Date/time picker

On mobile devices only that are running Android or iOS operating systems, the Date/time picker
view shows the native date and time picker that is included with the operating system (OS). This
behavior means that users see different date and time pickers. For example, on an Android OS, a user
might work on a task with Google Chrome and therefore see the native Android date and time picker.
If the user then switches to an Apple iPhone, the user will see the native iOS date and time picker
instead.

Although the date is stored in UTC time, the date and time that is shown is adjusted for the time
zone of the user's system.

## Restrictions and limitations

If the user types in content that is not a
complete date or not in a valid format, the bound data item is null when the user triggers a
boundary event such as clicking a button. If the flow returns to the page, the view is empty. Any
other views that are bound to the same data item are also empty.

Using native date and time
pickers means that some configuration properties are not applicable, such as the following
properties:

- Disabled week days
- Blackout dates
- Blackout date start
- Blackout date end
- Week start
- Calendar type (when Hebrew or
Islamic is selected)
- Date Picker type (when Inline is selected)

## Data binding

Set or modify the data binding for the view in the General properties tab.
The data binding contains the initial date and time to display and stores updates to the value. The
data type is Date.

## Configuration properties

Under Configuration,
set or modify the appearance and behavior properties for the view.

<!-- image -->

| Appearance configuration property   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Data type                  |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------|
| Date Picker type                    | The type of calendar display for the date time picker: Text Input: This calendar display features a text input box and initially hides the calendar. When the text box is clicked, the calendar is displayed. Inline: This calendar display features an inline calendar and hides the text input box.  The default value is Text Input.                                                                                                                                                                                                                                                                                                                                                                                                      | DatePickerType             |
| Width                               | The width of the date time picker when the Text Input type is selected for the Date Picker type property. You can specify the width in px (pixels), % (percent), or em units. For example, 200px. If no unit type is specified with the numeric value, then px is assumed. By default, no width is specified.                                                                                                                                                                                                                                                                                                                                                                                                                                | String                     |
| Size                                | The size of the text in the view, the size of the label text, and the amount of padding around the text. For example, to make the text and label more readable on smart phones, you can set this configuration option to Large to compensate for the small screen size.                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | TextSizeStyle              |
| Label placement                     | The label placement location for the date time picker.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | LabelPlacement             |
| Label width                         | The width of the label. You can specify the width in px (pixels), % (percent), or em units. For example, 50px, 20%, or 0.4em. If a unit type is not specified, px is assumed.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | String                     |
| Format                              | The format used to display and parse text that is entered into the text field. It accepts a variety of date inputs, including formats that are closer to natural language, with or without separators, day and month only, day only, and so on (MM/dd/yyyy,  dd/MM/yyyy, yyyy-MM-dd, yyyy MM dd, yyyyMMdd, DD MM, DD).  For example: If you type Jan 1, the date picker assumes the current year.  If you type 17, it assumes the 17th of the current month and year.  For the input 5/25, it assumes month/day of the current year. For the input Mar 86, it assumes 1/3/1986.   This configuration option supports the same formats as the Java SimpleDateFormat, and applies only when a browser does not have a native date time picker. | String                     |
| Week start                          | The day that starts each week. The default value is Sunday.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | DatePickerWeekStart        |
| Disabled week days                  | One or more days of the week that are blocked out on the calendar. By default, no days are disabled.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | DatePickerDisabledWeekDays |
| Show Today button                   | Show or hide the Today button, which sets the date to today's date. By default, the button is not displayed.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Boolean                    |
| Show Clear button                   | Show or hide the Clear button, which clears the date value. By default, the button is not displayed.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Boolean                    |
| Orientation                         | The orientation of the calendar when it is clicked.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | DatePickerOrientation      |
| Color style                         | The color style of the date time picker. The colors correspond to variables in the specified theme. The default value is Default (dark blue).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | DatePickerColorStyle       |
| Show week number                    | For Gregorian calendars, displays the number of the week in the year. For example, the last week in a Gregorian year is week number 52. By default, no week number is shown.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Boolean                    |
| Highlight today                     | Specifies whether today's date is highlighted in the calendar. By default, today's date is not highlighted.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Boolean                    |
| Hide header                         | Hides the header at the top of the custom date and time picker. By default, the header is not hidden.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Boolean                    |
| Show calendar icon                  | Displays the calendar icon in the text input box.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Boolean                    |
| Year selector style                 | The style of the year selector, Default or Modern.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | tableHFStyle               |

| Behavior configuration property   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Data type             |
|-----------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------|
| Custom picker only                | Always display the custom date and time picker on mobile devices rather than the native date and time picker.On mobile devices, an initial attempt is always made to display the native date and time picker. However, the custom date and time picker is displayed whenever any of the following unsupported configuration properties are specified:  Disabled week days Blackout dates Blackout date start Blackout date end Week start Calendar type (when Hebrew or Islamic is selected) Date Picker type (when Inline is selected)  By default, both the custom date and time picker and the native date and time picker are used where appropriate. | Boolean               |
| Include time picker               | Display the time picker with the Date/time picker view. By default, the time picker is not displayed.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Boolean               |
| Calendar type                     | The type of calendar: Gregorian Hebrew Islamic  The default value is Gregorian.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | CalendarType          |
| Tab index                         | The tabbing sequence index. The tab indices start at 1 and can be set sparsely. For example, you can use 1, 5, 10. The Tab index property controls the tabbing sequence when you move between UI areas by pressing the Tab key.                                                                                                                                                                                                                                                                                                                                                                                                                           | String                |
| Placeholder text                  | The placeholder text to use when no date is entered. Typically, the text is a brief description or example of the input required by the user. If the bound data item does not contain a value, users see the hint until they type in the field. By default, no placeholder text is specified.                                                                                                                                                                                                                                                                                                                                                             | String                |
| Available start date              | Specifies the available start date and time. All dates prior to the specified available start date will be blocked out. The format for the available start date is specified by the Format property in the Appearance properties. By default, no available start date is specified.                                                                                                                                                                                                                                                                                                                                                                       | Date                  |
| Available end date                | The available end date and time. All dates after the specified available end date will be blocked out. The format for the available end date is specified by the Format property in the Appearance properties. By default, no available end date is specified.                                                                                                                                                                                                                                                                                                                                                                                            | Date                  |
| Blackout dates                    | A single date or a list of multiple non-consecutive dates to black out. If a list of blackout dates is provided, the view uses the custom date and time picker instead of the native date and time picker. By default, no blackout dates are specified.                                                                                                                                                                                                                                                                                                                                                                                                   | Date (List)           |
| Blackout date start               | The starting date of a range of consecutive dates that you want to black out. By default, no blackout start date is specified.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Date                  |
| Blackout date end                 | The end date of a range of consecutive dates that you want to black out. By default, no blackout end date is specified.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Date                  |
| Start view                        | The level of granularity that the calendar should start at: Month Year Decade  The default value is Month.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | DatePickerStartView   |
| Minimum view mode                 | The minimum date granularity levels to use in the calendar: Days Months Years  The default value is Days.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | DatePickerMinViewMode |
| No auto close                     | Specifies that the calendar will not close when a date is selected. Instead, the calendar will close when the date time picker loses focus. By default, the calendar closes automatically when a date is selected.                                                                                                                                                                                                                                                                                                                                                                                                                                        | Boolean               |
| Century range                     | The interval that precedes the current year and marks the start of the 100-year range when a two-digit year is entered. By default, the value is set to 50 years, which means the date picker maps it to the 100-year range that starts 50 years ago. For example, for a century range of 50 in 2023, the start of the century range is 2023 - 50 = 1973, which makes 2072 the end of the century range.                                                                                                                                                                                                                                                  | Integer               |
| Disable smart parsing             | Disables the smart parsing of the text that the user enters. Smart parsing is enabled by default. When the smart parsing is disabled, only values that use the specified date/time format are accepted. Any format other than the specified format is declared invalid, and the user is prompted to use the accepted format instead.                                                                                                                                                                                                                                                                                                                      | Boolean               |

## Example

If you want to have a clickable calendar button, you can place a Date/time picker view inside of
an Input Group view. In the properties for the Input Group view, set the Button
type property to Icon and set the Button
info property to calendar. In the On button
click event for the Input Group view, type the following string:

```
${Control\_ID}.\_instance.pickerControl.show();
```

## Events

Set
or modify the event handlers for the view in the Events properties. You can set
events to be triggered programmatically or when a user interacts with the view. For information about how to define and code events, see User-defined events. Date/time picker has the following
types of event handlers:

- On load: Activated when the page loads. For example: var
workerStart = ${StartDate}.getDate(); me.setStart(workerStart);
- On change: Activated when a change is detected. For example:
return confirm("Are you sure you want to change date?")
- On day cell render: Activated when there is a day cell render. It is
triggered before the date shows on the date time picker. For example:
me.setDate("01/01/2015")

Depending on the specific event, you can use JavaScript logic to modify the effects of the view.
More information on using events with views is found in the topic User-defined events.

## Methods

For detailed information on the available methods for Date/time picker, see the Date/time picker JavaScript
API.

## Additional resources

For information about how to create a coach or page, see Building coaches. 
For information about standard properties
(General, Configuration,
Positioning, Visibility, and HTML
Attributes), see View properties.