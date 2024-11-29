# Removing personal data from solutions and cases

## Properties

If the properties values in a case include personal data that must be removed for GDPR readiness,
you must manually delete the property values. For most properties, the easiest way to remove the
value is to open the case in Case Client and delete the value. If a
property requires a value, you must replace the personal data with a substitute value such as the
default value.

In certain situations, you might not be able to remove a property value in Case Client. For example, the property might be defined as read-only or
hidden in Case Client. In this situation, you must delete the value
directly from the target object store by using IBM Administration Console for
Content Platform Engine to
navigate to the Properties tab for the case.

If auditing is enabled for any property that stores personal data, IBM Business Automation
Workflow records the property value in event logs and case history. You
cannot remove the values from the case history. For information about pruning event log records from
the workflow system event logs, see pelog. For information about deleting audit entries, see Pruning audit entries. For information about remove processed
events from the Case Analyzer event table, see Pruning events on Case Analyzer.

If a property that stores personal data is populated by an external data service, you must remove
the data from the external server in addition to removing it from the case. Note that each external
data service has its own unique way of handling data.

## Case owners, case team members, and solution role members

Case owners, case team members, and solution role members are selected from Lightweight Directory
Access Protocol (LDAP) groups. However, removing a user from an LDAP group for GDPR readiness does
not automatically remove it from IBM Business Automation
Workflow. Instead, you must
manually remove the user. The user might also be retained in the IBM Content
Navigator cache. Ensure that you clear this cache to remove any user
information.

For a case owner or case team member, click the Manage Team action or
button on the Case Details page and delete the user from the team list.

For a solution role member, click the Manage Roles action or button on the
Work page and delete the user from the list of role members.

## Deleting a case

If necessary, you can delete an entire case. However, this process does require extra cleanup.
For more information, see Deleting a case.