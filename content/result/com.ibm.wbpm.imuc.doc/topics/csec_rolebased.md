<!-- image -->

# Securing access to timetables in the Business Calendars widget

The Security Roles widget, which you use to administer
role-based access control for the Business Calendars widget,
is located in Business Space powered by WebSphere®.

This role-based access is based on XACML (eXtensible Access Control
Markup Language), an open standard.

- You can control access to a specific instance of a timetable. For
example, you can specify that a user has access only to the user's
own timetable and that the user does not have the ability to look
at or change anyone else's timetable.
- Controlling access is done at the role level, instead of the individual
user level. You map members to roles. It is the role that defines
the permission members have to the specific instance of the resource.

Using the Security Roles widget, you can assign a user
or group to the system roles. You can also assign a user or group
to the component roles associated with timetables.

- Roles associated with a timetable

When a timetable is installed, three roles are created for that timetable-Owner, Writer, and Reader. These roles are known as component-specific roles.
- System roles for the Security Roles widget

The BPMAdmin and BPMRoleManager roles are automatically created when you enable security after installing IBM Business Automation Workflow.
- Assigning component roles

Each timetable in the Business Calendars widget has three component roles-Owner, Writer, and Reader-associated with it. You use the Security Roles widget to assign users or groups to these roles.