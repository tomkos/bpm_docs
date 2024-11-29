# Roles associated
with a timetable

How would these roles be used? Consider the case of a
holiday timetable
used in an organization. You want all employees to have access to
the timetable, but you want to limit the number of employees who can
update the timetable.

- HolidayOwnerMembers assigned to this role can
read the Holiday
timetable and can also write to it. For example, if the company decided
to add an extra holiday, a member with the HolidayOwner role would
be able to make the change.
Members of this role can also assign
members to the HolidayWriter and HolidayReader role. For example,
the HolidayOwner might decide to add a senior manager to the HolidayWriter
role.
- HolidayWriterMembers assigned to this role can
read the Holiday
timetable and can also write to it. As in the case of the HolidayOwner,
members of the HolidayWriter role could add the extra holiday.
- HolidayReaderMembers assigned to this role can read the Holiday
timetable but cannot write to it.

Figure 1. Example of roles assigned to a
timetable

<!-- image -->

- Members of the
Owner role can read and write to the timetable
and can assign other members to the Writer and Reader roles.
- Members
of the Writer role can read and write to the timetable.
- Members
of the Reader role can read the timetable.

In
the Security Roles widget, these timetable-related
roles are also known as module roles.