<!-- image -->

# Shared work items

## What are shared work items?

Work items are
created in the Business Process Choreographer database for each combination
of human task instance and all people who are permitted to perform
actions on that instance. If the number of human task instances and
the number of users increases significantly, the number of work items
in the database can grow so large that the database performance is
affected.

The idea behind shared work items is an optimized
implementation of work items, such that redundant information about
work items is not stored in the database. This can improve the performance
of many BPEL process and human task queries. Whether shared work items
are being used, or not, is transparent to the users of Business Process
Choreographer APIs.

## How to decide whether to add support for shared work
items

It is only if you migrate your Business Process Choreographer
configuration from Version 7.0.0.2 or earlier, that the support for
shared work items is not activated. Although activating is optional,
certain factors indicate that using shared work items will improve
performance.

- If you only have hundreds or a few thousands of human task instances
in your system, there is probably little or no performance advantage
in migrating to using shared work items.
- If you have hundreds of thousands of human task instances in your
system, and your task list and process list queries are taking too
long, migrating to using shared work items should improve the performance.
- Using shared work items can improve the performance of the followingqueries:
    - query()
    - queryAll()
    - queryEntities()
    - queryEntityCount()
    - queryRows()
    - queryRowCount()

## Restrictions

- Queries that run against the WORK\_ITEM view exclusively.
- Queries that reference one or more of the following columns inthe WORK\_ITEM view:
    - ASSOC\_OBJECT\_TYPE
    - ASSOC\_OID
    - OBJECT\_ID
    - CREATION\_TIME
    - OBJECT\_TYPE
- Queries referencing a custom table that is directly joined with
the WORK\_ITEM view.
- Queries that were created as materialized views.
- Queries that use authorization with inherited work items.

## Related information

- Adding support for shared work items