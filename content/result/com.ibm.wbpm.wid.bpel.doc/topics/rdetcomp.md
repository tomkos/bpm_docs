<!-- image -->

# Compensation tab: BPEL process editor

## Invoke activity

Use the settings on this
page to configure the compensation for the associated invoke activity.

For a long-running process, this operation is performed
as part of the fault handling when the enclosing scope is compensated.
The compensation operation is thus a abbreviation for a simple compensation
handler associated with the invoke activity. For a microflow, this
compensation action will be run if the process cannot be committed
and must be rolled back and the effects of the invoked service are
not undone by the transaction rollback.

To configure the compensation
settings, browse to an appropriate Partner (in
which case the Interface is automatically chosen),
and then select an Operation and a variable that the service
that you will call can identify (for example, provide the reservation
number of your flight so it can be rolled back).

To clear an
existing compensation configuration, click Clear Compensation.

## Human task

Use the settings on this page
to configure the compensation for the selected human task.

For
a long-running process, this operation is performed as part of the
fault handling when the enclosing scope is compensated. The compensation
operation is thus a abbreviation for a simple compensation handler
associated with the human task.

To configure the compensation
settings, browse to an appropriate Partner (in
which case the Interface is automatically chosen),
and then select an Operation and a variable that the service
that you will call can identify (for example, provide the reservation
number of your flight so it can be rolled back).

To clear an existing
compensation configuration, click Clear Compensation.

## Related concepts

- Choosing the appropriate compensation for your process