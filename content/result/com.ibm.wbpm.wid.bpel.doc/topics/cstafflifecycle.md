<!-- image -->

# People assignment criteria and people query results

If you need to change the people assignment criteria, you must
change the task definition in Integration Designer, and deploy the
task template again.

- Explicitly by an administratorAn administrator can use eitherthe administrative console or the administrative commands to refreshpeople query results. Commands exist for the following actions:
    - Refreshing all of the people query results at once
    - Refreshing all of the people query results that are associated
with a task template
    - Refreshing people query results that contain a specific user ID
in the current result.
- Triggered by a scheduled refresh of expired people queries Thisapproach is based on the following parameters: The following parameters determine how people queriesare automatically refreshed: You can set the timeout value to be longer than the schedulerefresh interval. For example, you can set the timeout value to be24h, and the refresh interval to 1h. In this way, you can spread theupdates to the people queries throughout the day and avoid the extraload caused by refreshing all of the people query results at once.

- A timeout value for people query results (Tout).
- A refresh schedule for the people query. Use the WebSphere® Application
Server CRON-syntax
for defining the schedule: <Seconds> <Minutes> <Hours> <Day\_of\_the\_Month> <Month\_of\_the\_Year> <Day\_of\_the\_Week> For
example, every Monday at 1 pm (0 0 13 ? * MON), or
every work-day at midnight (0 0 24 ? * MON-FRI).

- When a query is run for the first time or it is refreshed, the
query result gets an expiration timestamp (texp =
tcurrent + Tout)
- When the query refresh daemon is invoked, all of the people queries
with results that have expired are run again