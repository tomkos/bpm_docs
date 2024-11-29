# Deleting snapshots on workflow servers

Traditional: 
Run the
BPMDeleteSnapshot command to delete the process application snapshot from the
server. If you are deleting the default snapshot, you must use the -force
parameter.

You can delete an inactive process application snapshot on any test or production workflow
server. The process that you use varies depending on whether you are using the IBM® Business Automation
Workflow Advanced deployment environment or the Standard
deployment environment. You might want to delete snapshots and their dependencies if you no longer
need them or if you have concerns about space on your system.

When the default snapshot of a process application is deleted, the process application is
removed. Toolkits that the process application depended on remain. There might be other toolkits and
process applications depending on those remaining toolkits. The toolkits cannot be deleted while
those dependencies exist.

## Procedure