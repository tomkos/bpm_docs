# Hiding warnings about missing groups

## About this task

IBM® Business Automation Workflow looks up the WebSphere® Application
Server user registry for information about a user's
group memberships. By default, if it does not find the groups, it logs a warning message similar to
the message CWLLG1087W User <user name> is a member of <group name>, but this role does
not exist. Ignoring.

When IBM Business Automation Workflow queries
the WebSphere Application
Server user
registry for user information, the returned list of groups includes
groups that are visible for group membership queries but are hidden
for a group lookup. The hidden groups are filtered out by a group
search filter that you defined for an LDAP directory in the WebSphere Application
Server federated
repositories configuration. The returned list also excludes groups
outside the scope of the base distinguished name of the repository.
As a result, when IBM Business Automation Workflow looks
up groups and does not find the filtered or excluded groups, it logs
the warning message.

Warnings are printed to the SystemOut.log file
by default. Because thousands of such messages can be generated in
a production system, they might clutter the log file, and reduce performance
because of the extensive logging of trace statements. Therefore, you
might want to suppress this warning message.

To enable or disable
logging of these warnings, add the warn-of-membership-referring-to-missing-group configuration
property to the appropriate 100Custom.xml files
in your topology (see the topic Location of 100Custom configuration files for its location).

## Procedure

```
<common merge="mergeChildren">
  <security merge="mergeChildren">
    <warn-of-membership-referring-to-missing-group merge="replace">false</warn-of-membership-referring-to-missing-group>
  </security>
</common>
```