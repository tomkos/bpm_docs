# Process instance owners team

- Retrieve process details (GET)
- Start a process instance (POST)
- Modify the due date of a process instance (PUT)

- Retrieve task details (GET)
- Retrieve task data (GET)
- Retrieve task client settings (GET)
- Finish a task (PUT)
- Complete a task (PUT)
- Update a task (PUT) - due date, priority, not data
- Assign a task to a user (PUT)
- Assign a task to a group (PUT)
- Assign a task back (PUT)
- Cancel a task (PUT)
- Bulk task details (GET)
- Bulk cancel tasks (PUT)

- View user info (GET)
- View potential collaborators for a task (GET)
- View potential reassignees for a received or claimed
task (GET)

- For security of the data, do not add the All Users team
to the Instance owners team.
- Do not add All Users to the process owner
teams because this can result in unwanted user synchronization and
performance issues.
- Do not choose System teams as Instance
owners team. System teams are used in System lanes, for
System tasks or services that run automatically without a need for
user interaction.

To verify whether an instance owner is defined, you can review the process in the designer. You
can also determine the same by looking at the OWNER\_TEAM\_PARTICIPANT\_REF value in the LSW\_BPD table,
but make sure that you do not alter the entry.