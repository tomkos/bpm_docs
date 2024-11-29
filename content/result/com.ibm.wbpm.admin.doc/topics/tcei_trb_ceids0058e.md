# Event service does not start (message CEIDS0058E)

## Cause

The event service uses SQL statements
qualified with the user name. This error indicates that the user name
used by the event service to connect to the event database is not
the same as the user ID that was used to create the database.

## Remedy

The user ID used to connect to the
event database must be the same one used to create the event database.
To correct this problem:

    - For a single server, select Servers > Application servers
> server\_name.
    - For a cluster, select Servers > Clusters > cluster\_name.
- From the Configuration tab, select Business
Integration > Common Event Infrastructure > Common Event Infrastructure
Server.
- Change the specified user ID and password to match those used
to create the database.
- Save the configuration changes.
- Restart the server.