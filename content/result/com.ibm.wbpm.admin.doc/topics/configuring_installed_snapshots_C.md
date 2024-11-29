# Configuring runtime environment variables

You can use the Process Admin Console or REST API calls to
manage environment variables.

## Using the Process Admin Console

1. Log in to the Process Admin Console, and then click
Installed Apps to show the list of current snapshots on the server.
2. Click the snapshot that you want to work with.
3. From the menu bar, click Environment Vars.
4. For the variables listed, provide a value or ensure that the value shown is accurate for the
current server. If no variables are listed, no variables were established during process
development.

## Using a REST API call

Call the operations REST API ACTION
https://host:port/ops/std/bpm/containers/container\_acronym/versions/version\_acronym/env\_vars
or ACTION
https://host:port/ops/std/bpm/containers/container\_acronym/branches/branch\_acronym/env\_vars
where container\_acronym is the acronym of the process application or toolkit that
contains the targeted snapshot, version\_acronym is the acronym of the targeted
snapshot, and branch\_acronym is the acronym of the targeted track.

- Retrieve a list of environment variables for snapshot S1 of process application
APP1:GET http://host:port/ops/std/bpm/containers/APP1/versions/S1/env\_vars
- For process application APP1, snapshot S1, set the environment variable DEBUG to the value of
true:POST http://host:port/ops/std/bpm/containers/APP1/versions/S1/env\_vars{
  "pairs": [
    {
      "name": "DEBUG",
      "value": "true"
    }
  ]
}
- Copy the environment variable from snapshot S1 to snapshot S2 of process application
APP1:POST http://host:port/ops/std/bpm/containers/APP1/versions/S1/env\_vars/sync?target\_version=S2
- For the tip snapshot of track T1 of process application APP1, set the environment variable TRACE
to the value of
true:POST http://host:port/ops/std/bpm/containers/APP1/branches/T1/env\_vars{
  "pairs": [
    {
      "name": "TRACE",
      "value": "true"
    }
  ]
}