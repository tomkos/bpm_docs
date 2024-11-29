# Get Case Calendar Events service

The following parameters can be used in Get Case Calendar Events service.

| Name   | Description   | Data type             |
|--------|---------------|-----------------------|
| input  | data          | Any                   |
| output | result        | List of CalendarEvent |

| Name            | Description                                                                                                                                                                                                                                                           | Data type   |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| title           | Title of the Calendar event.                                                                                                                                                                                                                                          | String      |
| start           | (Date of ISO STANDAR format YYYY-MM-DD) - when an event begins.                                                                                                                                                                                                       | String      |
| end             | (Date of ISO STANDAR format YYYY-MM-DD) - when an event ends. It could be null if an end was not specified. This value is exclusive. For example, an event with the end of 2018-09-03 that appears to span through 2018-09-02 but end before the start of 2018-09-03. | String      |
| extendedProps   | A plain object holding miscellaneous other properties specified.                                                                                                                                                                                                      | Any         |
| allDay          | (true or false). Determines if the event is shown in the "all-day" section of relevant views. In addition, if true the time text is not displayed with the event.                                                                                                     | Boolean     |
| backgroundColor | The event background color override for this specific event.                                                                                                                                                                                                          | String      |
| textColor       | The event Text Color override for this specific event.                                                                                                                                                                                                                | String      |