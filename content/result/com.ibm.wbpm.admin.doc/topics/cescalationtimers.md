<!-- image -->

# Changes to the timing of an escalation at run time

- Using a specific time
- Using a duration, for example, 2 days, based on a calendar, such
as a business calendar. You can also use the following constants in
duration expressions:
DURATION\_INFINITE
The initial escalation or the repeated escalations are canceled.

## Initial escalation

You can use the escalationTime
and the durationUntilEscalated properties to change the timing of
an escalation. The escalation state determines which of these properties
you can use.

You can
also trigger the escalation manually using the Human Task Manager
API triggerEscalation method.

## Repeated escalations