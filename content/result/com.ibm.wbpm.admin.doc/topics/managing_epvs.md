# Managing exposed process values (EPVs)

Exposed process values (EPVs) are variables that certain users can change when processes
are running on the playback server or a workflow server in your test, production, or other runtime
environment.

The Process Admin Console restrictions must allow
managing the EPVs. See Restricting access to the Process Admin Console.

To view and manage a specific EPV, the EPV must be exposed to you as described in Creating exposed process values (EPVs).

The users who can manage EPVs is determined during process design. When a process author creates
an EPV, the exposure setting is used to select the users who can alter the EPV. If you are included
in the exposure setting, you can manage EPVs as described in the following procedure.

You can use the Process Admin Console or REST API calls to
manage EPVs.

## Using the Process Admin Console

1. In the Server Admin area of the Process Admin Console,
click the indicator next to Admin Tools to list the available options.
2. Click the Manage EPVs option.
3. Using the drop-down menu, select the process application snapshot that contains the EPV that you
want to modify. Each process application snapshot listed also includes the track name. Current
working versions of process applications are listed as Tip, enabling you to test
EPVs on the playback server without creating a snapshot.
4. Using the drop-down menu, select the EPV that you want to edit. The Process Admin Console displays the variable values in the EPV that you
can modify.
5 Complete the following steps for each variable that you want to modify: Note: You can enter multiple values for the same variable, each taking effect at a differenttime. The Process Admin Console displays all modifications foreach variable in a separate table.
    1. Click the row of the variable that you want to change, and then click
New.
    2. In the Exposed Process Value window, enter a new value, set the date and
time at which you want the new value to take effect, and click OK.Note: The
EPV can't be a blank value when it's set or changed in the Process Admin Console.
6. To edit or delete EPVs that have an effective date in the future, select the row in the table
and then use the Edit or Delete buttons to change or
remove the modifications. You cannot edit or delete the current EPV value. You can also delete
old EPVs that have an effective date in the past and are not the current EPV value.

## Using a REST API call

Call the operations REST API ACTION
https://host:port/ops/std/bpm/containers/container\_acronym/versions/version\_acronym/epvs
where ACTION is either GET or POST, container\_acronym is the acronym of the
application or toolkit that contains the targeted snapshot, and version\_acronym
is the acronym of the targeted snapshot.

- Retrieve a list of EPVs for snapshot S1 of application APP1:
GET http://host:port/ops/std/bpm/containers/APP1/versions/S1/epvs
- For application APP1, snapshot S1, exposed process value E1, set the variable PORT to the value
of
9090:POST http://host:port/ops/std/bpm/containers/APP1/versions/S1/epvs{
  "variable\_value\_details": [
    {
      "epv\_name": "E1",
      "epv\_variable\_name": "PORT",
      "epv\_variable\_value": "9090"
    }
  ]
}
- Copy the exposed process values from snapshot S1 to snapshot S2 of application
APP1:POST http://host:port/ops/std/bpm/containers/APP1/versions/S1/epvs/sync?target\_version=S2