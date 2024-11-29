<!-- image -->

# Refreshing people query results, using the refresh daemon

## About this task

People queries are resolved by the specified people directory provider. The result is stored in the Business
Process Choreographer database. To optimize the authorization performance,
the retrieved query results are cached. The cache content is checked
for currency when the people query refresh daemon is invoked.

In order to keep people query results up to date, a daemon
is provided that refreshes expired people query results on
a regular schedule. The daemon refreshes all cached people query results that have expired.

## Procedure

1 Open the custom properties page for the Human TaskManager :
    1. Click Servers > Clusters > WebSphere application server clusters > cluster\_name,
then on the Configuration tab, in the Business Process Manager section, expand Business Process Choreographer, and click Human Task Manager.
    2 Chooseone of the following options:
        - To change settings without having to restart the cluster, select
the Runtime tab.
        - To make changes that will only have an effect after the cluster
is restarted, select the Configuration tab.
2. In the field People query refresh schedule enter the schedule using the syntax as supported by the WebSphere® CRON calendar. This value determines
when the daemon will refresh any expired people query results.
The default value is "0 0 1 * * ?", which causes
a refresh every day at 1 am. If you want
to disable the daemon, delete the value. If you disable the daemon,
you should use administrative scripts to refresh the queries.
3. In the field Timeout for people query result enter a new value in seconds. This value determines how long a people
query result is considered to be valid. After this time period, the
people query result is considered to be no longer valid, and the people
query will be refreshed the next time that the daemon runs. The default
is one hour.
4. If you want any changes made on the Runtime tab
to remain in effect after the next server restart, select Save
runtime changes to configuration.
5. Click OK.
6. Save the changes. To make your changes that you made
on the Configuration tab effective, restart
the cluster. The new expiration time value applies
only to new people queries, it does not apply to existing people queries.

<!-- image -->