<!-- image -->

# Troubleshooting the failed event manager

You might encounter problems while using the failed event manager.

For information about finding, modifying, resubmitting, or deleting failed events, see Working with failed events in IBM Business Automation Workflow and Collect troubleshooting data for the failed-event resolution problems
in IBM Business Automation Workflow.

| Problem                                                                                     | Reference                                                                                        |
|---------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|
| I am having trouble entering values in the Search page's By Date tab                        | Values in the From Date and By Date field automatically change to default if entered incorrectly |
| I am having trouble deleting expired events                                                 | Using the Delete Expired Events function appears to suspend the failed event manager             |
| I am having trouble with failed events not being created                                    | Failed events are not being created                                                              |
| I am having trouble retrieving or deleting large numbers of failed events                   | The server fails when retrieving or deleting large numbers of failed events                      |
| I am having trouble clearing a large number of failed events                                | The server fails when clearing a large number of failed events                                   |
| I am having trouble deleting failed events after the associated application was uninstalled | Deletion of failed events after uninstalling the associated application                          |

## Searching for failed events takes too long

Searching for failed events takes over five minutes and, in some cases, the results don't load at
all.

The slow response time occurs when the database indexes of several critical tables are not up to
date. Even when only a few events are in the database, an outdated index might cause the system to
respond so slowly that timeouts occur.

- PROCESS\_INSTANCE\_B\_T
- ACTIVITY\_INSTANCE\_B\_T
- PROCESS\_TEMPLATE\_B\_T
- ACTIVITY\_TEMPLATE\_B\_T

```
db2 'RUNSTATS ON TABLE PROCESS\_INSTANCE\_B\_T FOR INDEXES ALL'
db2 'RUNSTATS ON TABLE ACTIVITY\_INSTANCE\_B\_T FOR INDEXES ALL'
db2 'RUNSTATS ON TABLE PROCESS\_TEMPLATE\_B\_T FOR INDEXES ALL'
db2 'RUNSTATS ON TABLE ACTIVITY\_TEMPLATE\_B\_T FOR INDEXES ALL'
```

## Values in the From Date and By Date field
automatically change to default if entered incorrectly

The Search page's From Date and To Date fields
require correctly formatted locale-dependent values. Any inconsistency in the value's format (for
example, including four digits in the year instead of 2, or omitting the time) will cause the failed
event manager to issue the following warning and substitute a default value in the field:

CWMAN0017E: The date entered could not be parsed correctly:
your\_incorrectly\_formatted\_date. Date: default\_date is being
used.

To avoid this problem, always enter your dates and times carefully, following the example
provided with each field.

## Using the Delete Expired Events function appears to suspend the failed event manager

If you use the Delete Expired Events button in situations where there are many failed events in
the current search results, or where those events contain a large amount of business data, the
failed event manager can appear to be suspended indefinitely.

In this situation, the failed event manager is not suspended: it is working through the large
data set, and will refresh the results set as soon as the command completes.

## Failed events are not being created

- Ensure that the wpsFEMgr application is running. If necessary, restart it.
- Ensure that the failed event manager's database has been created, and that the connection has
been tested.
- Ensure that the necessary failed event destination has been created on the SCA system bus. There
should be one failed event destination for each deployment target.
- Ensure that the Quality of Service (QoS) Reliability qualifier has been set
to Assured for any Service Component Architecture (SCA) implementation,
interface, or partner reference that participates in events you want the Recovery service to
handle.

## The server fails when retrieving or deleting large numbers of failed events

## The server fails when clearing a large number of failed events

The server can fail if you try to clear a large number of failed events using the Clear
All option. To prevent this from happening, set a limit for the number of failed events
that can be cleared using the JVM property failedEventLimit. If the failed event
count is higher than that limit, the Clear All option returns an error, and you
must delete the failed events (up to the limit specified) one at a time.

## Deletion of failed events after uninstalling the associated application

- FAILEDEVENTBOTYPES
- FAILEDEVENTDETAIL
- FAILEDEVENTMESSAGE
- FAILEDEVENTS

Identify the failed event messages to be deleted in the APPLICATIONNAME column of the
FAILEDEVENTDETAIL table. Use the MSGID value to correlate the identified messages
in all the tables, and then delete all the related records from all the specified tables.