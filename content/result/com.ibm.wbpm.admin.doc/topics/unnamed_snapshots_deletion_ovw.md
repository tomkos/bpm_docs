# Deleting unnamed snapshots from a Workflow Center server,
automated method

## About this task

A named snapshot is a snapshot that has a version number or other identifier. Unnamed snapshots
exist between the named snapshots. Every time that a Process Designer user saves work, an unnamed snapshot is
created on the Workflow Center server. Hundreds of
unnamed snapshots quickly accumulate. If you have many projects under development in  Workflow Center, the Workflow Center database is likely to grow rapidly. Reduce
database bloat by removing the unnamed snapshots. You might also want to delete unnamed snapshots if
your Workflow Center server performance is slowly
degrading.

Depending on the requirements of the environment, you can choose to delete
unnamed snapshots in bulk at a scheduled time or piecemeal from active
projects on an ongoing basis.

- Deleting unnamed snapshots in bulk from a Workflow Center server

You can configure IBM Workflow Center to automatically delete unnamed snapshots in bulk at a scheduled time from all process applications and toolkits.
- Deleting unnamed snapshots dynamically from a Workflow Center server

You can configure IBM Workflow Center to automatically delete unnamed snapshots from active projects as and when named snapshots are created, on an ongoing basis.