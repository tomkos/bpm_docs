# Resolving errors when running a BPD (deprecated)

## About this task

To perform
this task, you must be in the IBM® Process
Designer desktop
editor, which is deprecated.

When you run a process or a service and an exception
occurs in the instance, the Inspector clearly identifies the error
in the diagram and navigation tree. The Inspector also:

- Tells you exactly where the error happened
- Links directly to the source of the problem

The following steps describe how the Inspector identifies
an error in a running instance and how it helps you resolve the error:

## Procedure

1. When the execution of a BPD does not complete successfully,
the Inspector displays the error in the BPD diagram and also in the
navigation tree.
2. Click the error shown in the navigation tree to open the Runtime
Error Information window. The Runtime
Error Information window indicates where the error happened
and it also provides a link to the service in which the error occurred
so you can go directly to the source.
3. Click More in the Runtime
Error Information window to show additional details about
the error, such as stack trace details. You can also use
the Copy to Clipboard button if you want to
paste the contents of the window to a text file or support ticket.
The Inspector copies all information to the clipboard, including stack
traces.