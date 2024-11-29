# Federation considerations for Workplace

Differences in behavior can be observed when Workplace runs in federated
environments instead of on a single system.

## Dashboards

| Single system                    | Federated environment                                     |
|----------------------------------|-----------------------------------------------------------|
| No Teams dashboard is available. | The Teams dashboard is available from the switcher menu . |

## Full-text search

| Single system                     | Federated environment          |
|-----------------------------------|--------------------------------|
| No full-text search is available. | Full-text search is available. |

## Refresh

There are no differences in the refresh behavior of the Tasks list between a
single system and a federated environment. In both situations, the task list is automatically
refreshed whenever task changes occur.

<!-- image -->

- For the single system, the auto refresh relies on the cometD on the Business Automation Workflow server.
- In a federated environment, the auto refresh relies on the notification server that is located
in Process Federation Server.
When the notification server is unavailable or the handshake fails, the refresh button  becomes
available for you to run a manual refresh.

## Entries in the Workflows and Cases lists

| Single system                                                                                      | Federated environment                                                                                                                         |
|----------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| The search filter  supports filtering by instance status only. No  saving or sharing is available. | The search filter  supports multiple filters. You can also select columns to show and sort by in the list. No saving or sharing is available. |

## Saved searches

| Single system                                                                                                                                   | Federated environment                                                                                                                           |
|-------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| Restricting the rights to create and update saved searches to a user or group of users is done through action policies.                         | Restricting the rights to create and update saved searches to a user or group of users is done through security roles.                          |
| For more information about the authorization for saved searches and security roles, see Federated systems and authorization for saved searches. | For more information about the authorization for saved searches and security roles, see Federated systems and authorization for saved searches. |