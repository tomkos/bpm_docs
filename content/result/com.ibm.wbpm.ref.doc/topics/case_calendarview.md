# Case Calendar

Use the following configuration options and services to customize the view as needed.

## Configuration properties

| Property                 | Description                                                                                                                   | Data type                                     |
|--------------------------|-------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------|
| Case Identifier          | Mandatory option that needs to be bound to the input variable caseId.                                                         | String                                        |
| Target Object Store Name | Mandatory option that needs to be bound to the input variable tosName.                                                        | String                                        |
| Calendar Size            | Displays the calendar in a large or small size.                                                                               | CalendarSize (Large/Small )                   |
| Calendar View            | Displays the calendar in a large size, in a month/week/day view.                                                              | CalendarViews (Month View/Week View/Day View) |
| Display Week Numbers     | Displays the week numbers in the calendar in size large. By clicking a week number, the calendar view changes to a week view. | Boolean                                       |
| Case Calendar Events     | Retrieves the case-related calendar events for case stages or quick task due dates.                                           | Service flow                                  |

## Events

You can assign the following types of event handlers to events:

```
var d = dayObject.date.toISOString().substring(0, dayObject.date.toISOString().indexOf('T'));
var dateStr = prompt('Enter a date in YYYY-MM-DD format', d);
var date = new Date(dateStr + 'T00:00:00');
if (!isNaN(date.valueOf())) {
    me.addCalendarEvent({
      title: 'Dynamic event',
      start: date,
      allDay: true
    });
} else {
    alert('Invalid date.');
}
```

```
alert("Event Title : " + eventObject.event.title);
```

If the Case Calendar view is not rendered when
it is placed in the Tab section layout, follow these steps to call the Case
Calendar render function:

1. Select the tab section and click Event.
2. Place the following code snippet in On Tab change event.

```
var calendar = page.ui.get(<Case Calendar viewID/controlID>);
 if (calendar)
   calendar.render();
```

```
var calendar = page.ui.get("Case\_Calendar");
if (calendar)
   calendar.render();
```

## Internet calendars subscription