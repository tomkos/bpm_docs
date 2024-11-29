# System roles for the Security Roles widget

- BPMAdminBPMAdmin has the authority to add members to or remove
members from the BPMRoleManager role. For example, if the person performing
the BPMRoleManager role leaves the organization, only BPMAdmin can
assign another member to that role.
BPMAdmin is initially assigned
to one member-the primary administrative user. Change this assignment
to another member as soon as you restart the server after installation
or upgrade.
- BPMRoleManagerBPMRoleManager has the authority to add members
to or remove members from the three timetable-related roles-Owner,
Writer, and Reader. For example, if a Holiday timetable is created,
the BPMRoleManager assigns members to the HolidayOwner, HolidayWriter,
and HolidayReader roles.
BPMRoleManager
is initially assigned to one member-the primary administrative user.
Change this assignment to another member as soon as you restart the
server after installation or upgrade.