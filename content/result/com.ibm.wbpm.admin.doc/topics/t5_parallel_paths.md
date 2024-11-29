<!-- image -->

# Parallel paths are sequentialized

## Resolution

- To achieve real parallelism, each path must be in a separate transaction.
Set the 'transactional behavior' attribute of all the parallel invoke
activities to 'commit before' or 'requires own'.
- The process engine serializes the execution of parallel paths
for Oracle database
systems. You cannot change this behavior. This is because the locks
on database entities for these database systems are not as granular
as, for example, those for DB2® databases. However, services
that are triggered asynchronously by parallel branches still run in
parallel; it is only the process navigation that is serialized for
these database systems.