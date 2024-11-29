# Calendar widget incoming events

## Clear content event

| Description   | Clear the content in the Calendar widget.   |
|---------------|---------------------------------------------|
| Event ID      | icm.ClearContent                            |
| Payload       | null                                        |

## Receive calendar information event

| Description   | Display the calendar using the data from the payload.                                                             |
|---------------|-------------------------------------------------------------------------------------------------------------------|
| Event ID      | icm.SendCaseInfo                                                                                                  |
| Payload       | caseEditable An icm.model.CaseEditable object that represents the case for which the calendar is being displayed. |

## Refresh Calendar event

| Description   | Refresh the calendar to update the events that are displayed.   |
|---------------|-----------------------------------------------------------------|
| Event ID      | icm.RefreshCalendar                                             |
| Payload       | Any value                                                       |