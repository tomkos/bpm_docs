# Deployment environment function status

## Explanation of entities state

The function
status is typically used for clusters that perform a given function.
A cluster is an example of a redundant entity state where its cluster
members make up the redundant parts. A deployment environment status
is an example of a minimum entity state where all functions need to
be available for the deployment environment to be available.

| Icon   | Status            | Minimum entities state                                                                                            | Redundant entities state                                                                                              |
|--------|-------------------|-------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
|        | Unknown           | At least one of the minimum entities state is unknown, making the entire state unknown.                           | The configuration did not complete for the deployment environment.                                                    |
|        | Unavailable       | At least one of the minimum entities is unavailable.                                                              | All of the entities in the deployment environment are unavailable.                                                    |
|        | Stopped           | All entities are stopped.                                                                                         | All minimum entities are stopped. If some entities are not stopped, this indicates those entities have problems.      |
|        | Partially stopped | There is at least one partially stopped entity and any number of stopped entities.                                | At least one partially stopped or stopped entity and any number of unavailable entities.                              |
|        | Running           | All entities are running.                                                                                         | All minimum entities are running. If some entities are not running, this indicates that those entities have problems. |
|        | Partially started | There is at least one running entity and any number of stopped, partially stopped, or partially running entities. | At least one partially running or running and any number of stopped, partially stopped or unavailable entities.       |