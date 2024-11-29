# Recovery: First steps

- Do not delete the transaction log fileThe transaction (tranlog)
log file stores critical transactional data that is written to databases.
It is an internal file that WebSphere® Application
Server uses to manage in-flight transactions and attempt to recover
them should the server lock up.
- Do not have the transaction logs local on the cluster membersPut
the transaction logs on a shared drive. This is the only way to allow
peer recovery, which helps minimize the downtime during recovery.
- Do not attempt database operations where the result set is large
enough to create additional resource contention (OutOfMemory)
- Avoid performing Business Process Choreographer Explorer operations
that return large result sets.
- Avoid executing administrative scripts on process instances without
considering the result set size.
- Do not drop or re-create databases in production
- Do not uninstall applications as part of your standard recovery
procedures You should only uninstall applications with the direction
from the IBM support organization.
- Do not enable too much trace if the system is overloaded. Too
much trace will cause a slowdown in system throughput and might cause
transaction time-outs. Too much trace can often add to the problems
that need to be addressed, rather than providing insight as to how
to solve the original problems.  
Get immediate assistance from IBM support to define the correct
trace specification.
- Do not experiment or try out new scripts or new commands on production
systems.
- Do not run your production servers in development mode Enabling
the Run in development mode option may reduce
the startup time of an application server. This may include JVM settings
such as disabling bytecode verification and reducing JIT compilation
costs.

The following list describes the recommended recovery actions.

- Always take a snapshot of the configuration tree, the PI
file of the application in question and the logs which are available.
 Logs may be overwriting themselves depending on the configuration.
 Capturing a set early and often is an important step for postmortem
analysis. See the topic on IBM Support
Assistant (ISA) for details on the IBM Support
Assistant, which helps with this type of activity.
- Always understand your database settings, especially related to
database transaction log file size, connection pools, and lock timeouts.