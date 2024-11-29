# BPMRemoveToolkit command

Use the BPMRemoveToolkit command in
connected mode to remove a process application from Workflow Center. You
can run this command only on Workflow Center.

The BPMRemoveToolkit command
is run using the AdminTask object of the wsadmin scripting client.

## Prerequisites

- In a network deployment environment, you must run
this command on the node containing the application cluster member
that handles Workflow Center applications.
Do not run this command from the deployment manager profile. The 
input file is read from the machine on which the connected server
is running. If you want to access the file from another machine, establish
a remote wsadmin session from the current machine to the server on
the machine where the file is stored.
- The toolkit must be in an archived state before you run this command. Run the BPMArchiveToolkit command to archive the toolkit.
- Delete all snapshots that you can identify as having dependencies on this toolkit, perhaps
following the steps in Cleaning up branches and snapshots if there are projects with many such
snapshots.
- Try to remove the toolkit by running the BPMRemoveToolkit
command, addressing any overlooked dependencies.

## Location

Start the wsadmin scripting client from the profile\_root/bin directory.

## Syntax

```
BPMRemoveToolkit
-containerAcronym toolkit\_acronym
```

## Parameters

## Example

```
wsadmin -conntype SOAP -port 8880 -host ProcessServer01.mycompany.com -user admin -password admin -lang jython

wsadmin>AdminTask.BPMRemoveToolkit('[-containerAcronym MYCOTK]')
```