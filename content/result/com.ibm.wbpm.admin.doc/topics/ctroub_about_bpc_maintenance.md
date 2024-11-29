<!-- image -->

# Business Process Choreographer maintenance and recovery scripts

You should run these scripts to remove from the database the templates
and their associated objects, as well as completed process instances,
that are not contained in any corresponding valid application in the
configuration repository.

There is also the possibility of having invalid process templates.
This situation can occur if an application installation was canceled
or not stored in the configuration repository by the user.

IBM® Business Automation Workflow also
provides a service that automates Business Process Choreographer cleanup.
You can run that service from the administrative console.

- Finished
- Terminated
- End
- Failed

## Deleting an allotment of completed process instances

You
can delete an allotment of process instances from the development
environment.

Using a script that wrappers the provided deleteCompletedProcessInstances.py

- By editing and placing correct user names, passwords, and paths
in this wrapper script, you can delete an allotment of process instances
from the development environment.
- Carefully selecting an adequate time slice prevents SOAP timeout
exceptions when communicating with the deployment manager.
- The adequate time slice of administrable instances depends onmany factors including, but not limited to, the following:
    - JVM tuning and memory allocations
    - Transaction log configuration for the database server
    - SOAP connection Time-Out configuration

## Example

```
wsadmin.<bat|sh> -user<USERNAME> -password<PASSWORD> -f loopDeleteProcessInstances.py
2008-04-02T21:00:00 3600
```

- An untuned database
- An overloaded system
- An attempt to delete "too many" process instances at once