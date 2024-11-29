# Configuring exposed processes and services

## About this task

Use the
Process Admin Console to configure exposed processes and services for a snapshot.

## Procedure

1. Log in to the Process Admin Console, and then click Installed
Apps to show the list of current snapshots on the server.
2. Click the snapshot you want to work with.
3. From the toolbar, click Exposing.
4 Click the check box next to the item that you want to disable. The item is no longer exposed to the selected group. When the exposure setting isdisabled, the users within the group can no longer start or otherwise manipulate the process orservice on the current server.Note: If you are disabling an undercover agent (UCA), you candetermine the specific type of the UCA by observing the symbol next to the UCA name: When you disable items that are not exposed to a particular team, such as web services andUCAs, those items cannot be run on the current server.
    - A Content UCA is identified by a folder symbol.
    - A Message UCA is identified by an envelope symbol.
    - A Timer UCA is identified by a clock symbol.