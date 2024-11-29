# Content Platform Engine process
services groups

| Group                                | Description                                                                                                                                                                                                                         |
|--------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Workflow system administration group | Required. Users in this group have full rights to all workflow rosters and queues, and can unlock work items locked by other users.                                                                                                 |
| Workflow system configuration group  | Recommended. If this group is assigned to an LDAP group, only users who belong to this group or the workflow system administration group can modify system configuration through the Process Configuration Console or through APIs. |

- workflow system configuration group members
- users and groups with write permissions to the application space

| Content Platform Engine entity   | Case management solution component   |
|----------------------------------|--------------------------------------|
| Queue                            | One queue per role in a solution     |
| Roster                           | One roster per solution              |
| Application space                | One application space per solution   |

If you do not assign anyone to an access right for a roster or
queue, then everyone has that right. For example, if you do not assign
anyone to the Query access right on the roster, then all users can
Query. As soon as you assign at least one user or group to have Query
rights, then only those users and the P8 Admin role can Query.

You must assign rights on the application space in order to modify
role membership. If you do not assign any rights, then only the workflow
system administration group and the workflow system configuration
group can modify role membership.

Members of the workflow system administration group have full rights
to everything, even if you do not explicitly assign rights to this
group.