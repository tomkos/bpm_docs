### Methods

### Parent

### Helpers

<!-- image -->

| Date Picker type:    | Set whether the datepicker has a textbox which when clicked shows a calendar, or simply has an inline calendar. {Text Input | Inline}                                                                                                                         | DatePickerType             |
|----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------|
| Width:               | Width of the Date Picker                                                                                                                                                                                                                                      | String                     |
| Size:                | The size of the view. {Default | Large | Small}                                                                                                                                                                                                               | TextSizeStyle              |
| Label placement:     | The label placement for the view {Top | Left}                                                                                                                                                                                                                 | LabelPlacement             |
| Label width:         | The width of the label in px, % or em.\r\nFor example\: 50px, 20%, 0.4em. If no unit is specified, px is assumed.                                                                                                                                             | String                     |
| Format:              | The format used to display and parse text that is entered into the text field, such as MM/dd/yyyy or dd/MM/yyyy. This option supports the same formats as the Java SimpleDateFormat, and applies only when a browser does not have a native date time picker. | String                     |
| Week start:          | The day used to start each week.  {Sunday | Monday | Tuesday | Wednesday | Thursday | Friday | Saturday}                                                                                                                                                      | DatePickerWeekStart        |
| Disabled week days:  | The days of the week that should be disabled.                                                                                                                                                                                                                 | DatePickerDisabledWeekDays |
| Show Today button:   | Display button to set date to today                                                                                                                                                                                                                           | Boolean                    |
| Show Clear button:   | Display button that clears date value                                                                                                                                                                                                                         | Boolean                    |
| Orientation:         | The position of the calendar when clicked. {Auto | Top Auto | Bottom Auto | Auto Left | Top Left | Bottom Left | Auto Right | Top Right | Bottom Right}                                                                                                       | DatePickerOrientation      |
| Color style:         | The color style for this view.  {Default | Info | Success | Warning | Danger}                                                                                                                                                                                 | DatePickerColorStyle       |
| Show week number:    | Shows the number of week it is in the year                                                                                                                                                                                                                    | Boolean                    |
| Highlight Today:     | Set to true to highlight today's date in the calendar                                                                                                                                                                                                         | Boolean                    |
| Hide header:         |                                                                                                                                                                                                                                                               | Boolean                    |
| Show calendar icon:  | Show the calendar icon in the text input box.                                                                                                                                                                                                                 | Boolean                    |
| Year selector style: | The style of the year selector. {Default | Modern}                                                                                                                                                                                                            | TableHFStyle               |

| Custom picker only:    | Check this option to always display the custom date time picker. On mobile devices attempt will be made to display native date time picker, if non-supported configuration options are specifed then custom date time picker will be displayed. Non-supported configuration options include "Disabled Week Days", "Blackout Dates", "Blackout date start", "Blackout date end", "Week Start", "Calendar type" as hebrew/islamic and "DatePicker Type" as "Inline"   | Boolean               |
|------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------|
| Include time picker:   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Boolean               |
| Calendar type:         | Select the type of calendar {Gregorian | Hebrew | Islamic}                                                                                                                                                                                                                                                                                                                                                                                                          | CalendarType          |
| Tab index:             | The tabbing sequence index of the form view. Indices start at 1, and can be set sparsely. For example, you can use 1, 5, 10.                                                                                                                                                                                                                                                                                                                                        | String                |
| Placeholder text:      | The text that is displayed when no date is entered.                                                                                                                                                                                                                                                                                                                                                                                                                 | String                |
| Available start date:  | Dates before the start date will be blocked out. The format for this date is specified by the Appearance, Format configuration option.                                                                                                                                                                                                                                                                                                                              | Date                  |
| Available end date:    | Dates after the end date will be blocked out. The format for this date is specified by the Appearance, Format configuration option.                                                                                                                                                                                                                                                                                                                                 | Date                  |
| Blackout dates:        | Set a date that the user cannot select. To set a range of blackout dates, create a variable containing the list of dates and use that variable for this configuration option                                                                                                                                                                                                                                                                                        | Date[]                |
| Blackout date start:   | Dates after the start date, including the selected date, will be blocked out                                                                                                                                                                                                                                                                                                                                                                                        | Date                  |
| Blackout date end:     | Dates before the end date, including the selected date, will be blocked out                                                                                                                                                                                                                                                                                                                                                                                         | Date                  |
| Start view:            | Level of granularity calendar should start at {Month | Year | Decade}                                                                                                                                                                                                                                                                                                                                                                                               | DatePickerStartView   |
| Minimum view mode:     | Minimum date granularity level to use in the calendar {Days | Months | Years}                                                                                                                                                                                                                                                                                                                                                                                       | DatePickerMinViewMode |
| No Auto close:         | When set to true, calendar will not close when a date is selected (calendar will close when view loses focus)                                                                                                                                                                                                                                                                                                                                                       | Boolean               |
| Century range:         | The interval that precedes the current year and marks the start of the 100-year range when a two-digit year is entered. By default, the value is set to 50 years, which means the date picker maps it to the 100-year range that starts 50 years ago. For example, for a century range of 50 in 2023, the start of the century range is 2023 - 50                                                                                                                   | Integer               |
| Disable smart parsing: | Select this option to disable the smart parsing of the text entered by the user. When the smart parsing is disabled, only values in the specified date/time format are accepted.                                                                                                                                                                                                                                                                                    | Boolean               |

| Name     | Type     | Default   | Description                                                                                                     |
|----------|----------|-----------|-----------------------------------------------------------------------------------------------------------------|
| name     | {string} |           | CSS class name(s) to add to the control. Separate class names by a space if more than one class.                |
| replaced | {string} |           | CSS class name(s) to be replaced by the first argument. Separate class names by a space if more than one class. |

| Name         | Type      | Default   | Description                                                               |
|--------------|-----------|-----------|---------------------------------------------------------------------------|
| collapseFlag | {boolean} |           | Set to true to collapse the view (equivalent to a view setting of "NONE") |

| Name   | Type      | Default   | Description                                           |
|--------|-----------|-----------|-------------------------------------------------------|
| flag   | {boolean} |           | Sets the visibility of the time picker {true | false} |

| Name   | Type    | Default   | Description                                    |
|--------|---------|-----------|------------------------------------------------|
| event  | {Event} |           | Value change event (usually an onchange event) |

| Name   | Type   | Default   | Description                                                               |
|--------|--------|-----------|---------------------------------------------------------------------------|
| date   | {date} |           | - Dates before the end date, including the end date, will be blocked out. |

| me.setBlackoutDateEnd(date);                   |
|------------------------------------------------|
| me.setBlackoutDateEnd(new Date("01/01/2018")); |
| me.setBlackoutDateEnd();                       |

| Name   | Type   | Default   | Description                                                                  |
|--------|--------|-----------|------------------------------------------------------------------------------|
| date   | {date} |           | - Dates after the start date, including the start date, will be blocked out. |

| me.setBlackoutDateStart(date);                   |
|--------------------------------------------------|
| me.setBlackoutDateStart(new Date("01/01/2018")); |
| me.setBlackoutDateStart();                       |

| Name   | Type     | Default   | Description                    |
|--------|----------|-----------|--------------------------------|
| list   | {date[]} |           | of dates that will be blocked. |

| me.setBlackoutDates([date, date, date]);                               |
|------------------------------------------------------------------------|
| me.setBlackoutDates([new Date("01/01/2018"), new Date("04/01/2018")]); |
| me.setBlackoutDates([]);                                               |

| Name   | Type     | Default   | Description                                                                                                                                   |
|--------|----------|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| style  | {string} |           | "DEFAULT"|"DEF"|"D"=Default | "INFO"|INF"|"I"=Info | "SUCCESS"|"S"=Success | "WARNING"|"WARN"|"W"=Warning | "DANGER"|"ERROR"|"ERR"|"G"=Danger |

| Name   | Type   | Default   | Description   |
|--------|--------|-----------|---------------|
| date   | {date} |           | Sets the date |

| Name     | Type      | Default   | Description                                                                   |
|----------|-----------|-----------|-------------------------------------------------------------------------------|
| enabled  | {boolean} |           | Enabled/read-only flag (true to enable view, false to disable/make read-only) |
| required | {boolean} |           | Enable/disable required field flag for control                                |

| Name   | Type   | Default   | Description                                                          |
|--------|--------|-----------|----------------------------------------------------------------------|
| end    | {date} |           | This sets the cut-off date, dates subsequent to this are disallowed. |

| me.setEnd(date);                   |
|------------------------------------|
| me.setEnd(new Date("06/07/2015")); |

| Name     | Type     | Default   | Description               |
|----------|----------|-----------|---------------------------|
| helptext | {string} |           | Help text for the control |

| Name   | Type     | Default   | Description       |
|--------|----------|-----------|-------------------|
| label  | {string} |           | Date picker label |

| Name      | Type     | Default   | Description                     |
|-----------|----------|-----------|---------------------------------|
| placement | {string} |           | "T"|"TOP"=Top | "L"|"LEFT"=Left |

| Name   | Type      | Default   | Description                                     |
|--------|-----------|-----------|-------------------------------------------------|
| flag   | {boolean} |           | Sets the visibility of the label {true | false} |

| Name       | Type     | Default   | Description           |
|------------|----------|-----------|-----------------------|
| labelWidth | {string} |           | Control's label width |

| Name   | Type     | Default   | Description      |
|--------|----------|-----------|------------------|
| text   | {string} |           | Placeholder text |

| Name   | Type     | Default   | Description                                                                  |
|--------|----------|-----------|------------------------------------------------------------------------------|
| style  | {string} |           | "DEFAULT"|"DEF"|"NORMAL"|"D"=Default | "SMALL"|"S"=Small | "LARGE"|"L"=Large |

| Name   | Type   | Default   | Description                                                        |
|--------|--------|-----------|--------------------------------------------------------------------|
| start  | {date} |           | This sets the start date, dates prior to this date are disallowed. |

| me.setStart(date);                   |
|--------------------------------------|
| me.setStart(new Date("06/01/2015")); |

| Name     | Type      | Default   | Description                                    |
|----------|-----------|-----------|------------------------------------------------|
| tabIndex | {integer} |           | Tab indices start at 1 and may be set sparsely |

| Name      | Type      | Default   | Description                                                                                                                                 |
|-----------|-----------|-----------|---------------------------------------------------------------------------------------------------------------------------------------------|
| valid     | {boolean} |           | Valid/invalid flag (true to set view valid, false to make it invalid - which typically shows the view with "invalid" styling and indicator) |
| errorText | {string}  |           | Validation error text to show on the invalid-styled view                                                                                    |

| Name                | Type      | Default   | Description                                                                            |
|---------------------|-----------|-----------|----------------------------------------------------------------------------------------|
| data                | {Object}  |           | Value of bound data. The type of this parameter must match the type of the bound data. |
| createPseudoBinding | {boolean} |           | If set to true, creates a pseudo binding if there is no current binding.               |

| Name     | Type      | Default   | Description                                                             |
|----------|-----------|-----------|-------------------------------------------------------------------------|
| visible  | {boolean} |           | Visibility flag (true to show view, false to hide)                      |
| collapse | {boolean} |           | Set to true to collapse the control space when visible is set to false. |

| MyView.setVisible(false, false); //Equivalent to MyView.hide()   |
|------------------------------------------------------------------|
| MyView.setVisible(false, true); // Sets visibility to "None"     |

| Name   | Type     | Default   | Description                   |
|--------|----------|-----------|-------------------------------|
| width  | {string} |           | sets the width of the control |

| Name   | Type     | Default   | Description                                        |
|--------|----------|-----------|----------------------------------------------------|
| style  | {string} |           | Sets style of the year selector (Default | Modern) |

| Name   | Type   | Default                | Description                   |
|--------|--------|------------------------|-------------------------------|
| phase  | {int}  | bpmext.ui.PHASE\_NORMAL | The phase we are currently in |