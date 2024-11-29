# Interpreting Process Monitor data

## Completed Steps column

<!-- image -->

## Process App column

<!-- image -->

## Total Steps count

<!-- image -->

## Halt process and halt service buttons

## Inconsistent monitoring data

Figure 1. Processes
page

<!-- image -->

<!-- image -->

Figure 2. Services
page

<!-- image -->

<!-- image -->

Figure 3. Summary page

<!-- image -->

<!-- image -->

For example, the Processes page
shows no active processes (Figure 1), but there are active processes
in Heritage Process Portal,
and the Services and Summary pages (Figures 2 and 3) show active process
apps in the table.

1. The system is not monitoring when the process instance is created.
2. The system starts monitoring.
3. The task in the process instance starts running.

## Exit time calculation

If a process or service
is still executing when it is exported, there is no exit time, and
the system uses the current time as the exit time to calculate the
duration. As you refresh the information on screen or through the
JMX api, the duration time is updated. This explains why when a process
or service that is executing is exported more than once, the duration
time that shown in the exported file can vary.