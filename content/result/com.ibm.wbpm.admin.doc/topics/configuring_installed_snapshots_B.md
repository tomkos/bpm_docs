# Configuring runtime teams

Teams can be defined statically or dynamically, and can have a team of managers that are
associated with them. During development, process authors create the teams for each process
application. After a process application is installed on a workflow server in the test or production
environment, you might need to add or remove users and groups in those teams so that the appropriate
staff can access and perform the tasks that are generated by the process application.

You can modify the membership of statically defined teams and designate the managers of teams.
For dynamic teams, which are defined by a team retrieval service, you can select whether the team is
resolved dynamically or statically.

You can use the Process Admin Console or REST API calls to
manage team bindings.

## Using the Process Admin Console

1. Log in to the Process Admin Console, and then click
Installed Apps to show the list of current snapshots on the server.
2. Click the snapshot that you want to work with.
3. From the menu bar, click Team Bindings. A list of each team and the
members of each team is displayed. The teams that are listed are the ones that were created during
process development.
4 All teams are listed. If there are multiple instances of teams that are resolved by the sameteam retrieval service, the instance name is displayed in brackets after the team name. For eachteam listed, you can perform the following actions:
    - The fields Members and Tasks show the number of
members and number of task instances that are currently assigned to the team. You can use these
values to help identify which teams might need more or less members.
    - Click Add Users. The Add Users window is displayed
where you can enter a partial or complete user name in the Retrieve text box
to display the users that are available on the current server. Select the check box for each user
that you want, and click Add.
    - Click Add Groups. The Add Groups window is displayed
where you can enter a partial or complete group name in the Retrieve text box
to display the groups that are available on the current server. Select the check box for each group
that you want, and click Add.
    - To remove a user or group from a team, click the Remove icon next to an
existing user or group.
    - To designate the managers of a team, click the corresponding Select
button, then select the appropriate team of managers.
    - Any teams that are dynamically defined by a team retrieval service, include a Dynamicresolution enabled option that you can use to switch between dynamic and static resolution. Tip: If the Dynamic resolution enabled option is cleared andthen selected again, the team resolution service is immediately called to refresh the list of teammembers.
        - When Dynamic resolution enabled is selected, which is the default, the
team is resolved dynamically by the associated service, and the statically defined list of users and
groups are ignored.
        - When Dynamic resolution enabled is cleared, which happens when you use
any of the controls to modify the static team list, the team is resolved statically.

## Using a REST API call

Call the operations REST API ACTION
https://host:port/ops/std/bpm/containers/container\_acronym/versions/version\_acronym/team\_bindings
where ACTION is GET, POST, or DELETE, container\_acronym is the acronym of the
application or toolkit that contains the targeted snapshot, and version\_acronym
is the acronym of the targeted snapshot.

- Retrieve a list of team bindings for snapshot S1 of application
APP1:GET http://host:port/ops/std/bpm/containers/APP1/versions/S1/team\_bindings
- Add the user jsmith to the A1 team in snapshot S1 of application
APP1:POST http://host:port/ops/std/bpm/containers/APP1/versions/S1/team\_bindings/A1{
  "add\_users": [
    "jsmith"
  ]
}
- Remove the user jsmith from the A1 team in snapshot S1 of application
APP1:DELETE http://host:port/ops/std/bpm/containers/APP1/versions/S1/team\_bindings/A1{
  "remove\_users": [
    "jsmith"
  ]
}
- Copy the team bindings from snapshot S1 to snapshot S2 of application
APP1:POST http://host:port/ops/std/bpm/containers/APP1/versions/S1/team\_bindings/sync?target\_version=S2