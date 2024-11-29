# Event Manager configuration settings

Do not directly edit the 80EventManager.xml file;
use the 100Custom.xml for any required configuration
changes. For information about changing configuration properties,
see Creating a 100Custom.xml configuration file.

## Task loader properties

## Queue capacity properties

When the server starts, the value of the async-queue-capacity setting is checked
and compared to the value of the maxConnections setting for the datasource. The
value of the async-queue-capacity setting is automatically adjusted if the
condition specified in the following formula is met:

```
maxConnections < 2 * (async-queue-capacity + bpd-queue-capacity + system-queue-capacity) + 5 synchronous queues
```

If the value of the async-queue-capacity setting is adjusted, warnings are
written to the server logs. For example:

```
CWLLG2156W: The database connection pool size (200) of the Process Server data source might be too small.
CWLLG2236W: The configured 'async-queue-capacity' parameter of '22900' has been changed to '5'.
CWLLG2236W: The configured 'bpd-queue-capacity' parameter of '22900' has been changed to '98'.
CWLLG2236W: The configured 'system-queue-capacity' parameter of '22900' has been changed to '5'
```

Use the following guidelines to help calculate or adjust the value of the
async-queue-capacity setting:

- If the connection pool is large enough, use the values that are currently configured.
- If the connection pool is too small, choose one of the following options:
    - If the queue capacity is less than or equal to the specified minimum value, only print a
warning.
    - If the queue capacity is greater than the specified minimum value, adjust the queue capacity
value but ensure that the value is not less than the minimum specified value.

## Thread pool properties

The web container threads also need database connections.

1. Event Manager tasks associated with a BPD instance, but Optimize Execution for
Latency is not selected in BPD.
2. All Event Manager tasks are not associated to any BPD instance.

## Heartbeat properties

## Reaper property

## Other Event Manager properties