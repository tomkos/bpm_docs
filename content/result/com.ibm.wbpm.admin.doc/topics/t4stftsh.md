<!-- image -->

# Troubleshooting people assignment

## About this task

- User cannot administer
process, scope, or activity instances
- Errors during the
deployment of the people directory provider
- Entries in the people
directory are not reflected in work item assignments
- Changes to the
people directory are not immediately reflected in work-item assignments
- Unexpected people
assignments for tasks or process instances
- Stopped human tasks
- Error and warning messages
relating to people assignment
- Enabling additional
messages about people assignment decisions
- Issues with group work
items and the "Group" people assignment criteria
- Cleanup of stored
people assignment results
- Adapted XSL transformation
file has no effect

You can also search for additional information in the Technical support search page.

- Make sure that all users and programs that perform administrative
actions are using user IDs that are in the appropriate role. For example,
BPESystemAdministrator or BPESystemmonitor.
- Restore instance-based administration, by turning the alternate
process administration authorization mode off. How
to turn it off is described in Optimizing BPEL process administration.

- Make sure that all mandatory parameters are set.
- To set the baseDN parameter to the root of
the LDAP directory tree, specify an empty string; set the baseDN parameter
to two apostrophe (') characters (''). Do not use double quotation
marks ("). Failure to set the baseDN parameter
results in a NullPointerException exception at
deployment time.

- On Linux® and UNIX platforms, this file is located in
install-root/ProcessChoreographer/Staff.
- On Windows platforms, this file is located in
install-root\ProcessChoreographer\Staff.

1. Create a new people directory provider configuration, providing your own version of the XSL
file.
2. Adapt the following entry in the XSL file according to your
needs: <xsl:variable name="Threshold">1000000</xsl:variable>

Business Process Choreographer caches the results of people
assignments evaluated against a people directory, such as an LDAP
server, in the runtime database. When changes occur in the people
directory, these are not immediately reflected in the database cache.

You
can refresh the cached results in the following ways:

- Refresh people query results, using the administrative
console. Use this method if you have major changes and need
to refresh the results for almost all people queries.
- Refresh people query results, using
administrative scripts.  Use this method if you write administration
scripts using the wsadmin tool, or if you want
to immediately refresh all or a subset of the people query results.
- Refresh people query results, using the refresh daemon.
Use this method to set up a regular and automatic refresh of all expired
people query results.

The following
tables illustrate which defaults apply for which situation:

| Roles for BPEL processes   | If the role is not defined in the process model ...   | If the role is defined in the process model, but people assignment fails or does not return proper results ...   |
|----------------------------|-------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|
| Process administrator      | Process starter becomes process administrator         | An exception occurs and the process is not started:  EngineAdministratorCannotBeResolvedException                |
| Process reader             | No reader                                             | No reader                                                                                                        |

| Roles for inline human tasks and their escalations       | If the role is not defined in the task model ...   | If the role is defined in the task model, but people assignment fails or does not return proper results ...   |
|----------------------------------------------------------|----------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Task administrator                                       | Only inheritance applies                           | Only inheritance applies                                                                                      |
| Task potential starter; applies to invocation tasks only | Everybody becomes potential starter                | An exception occurs and the process is not started                                                            |
| Task potential owner                                     | Everybody becomes potential owner                  | Administrators become potential owners                                                                        |
| Task editor                                              | No editor                                          | No editor                                                                                                     |
| Task reader                                              | Only inheritance applies                           | Only inheritance applies                                                                                      |
| Escalation receiver                                      | Administrators become escalation receivers         | Administrators become escalation receivers                                                                    |

- Process administrators become administrators for all inline tasks,
their subtasks, follow-on tasks, and escalations.
- Process readers become readers for all inline tasks, their subtasks,
follow-on tasks, and escalations.
- Task administrators become administrators for all subtasks, follow-on
tasks, and escalations of all these tasks.
- Task readers become readers for all subtasks, follow-on tasks,
and escalations of all these tasks.
- Members of any task role become readers for this task's escalations,
subtasks, and follow-on tasks.
- Escalation receivers become readers for the escalated task.

| Roles for stand-alone human tasks and their escalations   | If the role is not defined in the task model ...   | If the role is defined in task model, but people assignment fails or does not return correct results ...   |
|-----------------------------------------------------------|----------------------------------------------------|------------------------------------------------------------------------------------------------------------|
| Task administrator                                        | Originator becomes administrator                   | The task is not started                                                                                    |
| Task potential instance creator                           | Everybody becomes potential instance creator       | An exception is thrown and the task is not created                                                         |
| Task potential starter                                    | Originator becomes potential starter               | An exception is thrown and the task is not started                                                         |
| Potential owner                                           | Everybody becomes potential owner                  | Administrators become potential owners                                                                     |
| Editor                                                    | No editor                                          | No editor                                                                                                  |
| Reader                                                    | Only inheritance applies                           | Only inheritance applies                                                                                   |
| Escalation receiver                                       | Administrators become escalation receivers         | Administrators become escalation receivers                                                                 |

- Task administrators become administrators for all subtasks, follow-on
tasks, and escalations of all these tasks.
- Task readers become readers for all subtasks, follow-on tasks,
and escalations of all these tasks.
- Members of any task role become readers for this task's escalations,
subtasks, and follow-on tasks.
- Escalation receivers become readers for the escalated task.

- Human tasks cannot be claimed, even though the BPEL process started
navigating successfully.
- The SystemOut.log file contains the following
message: CWWB0057I: Activity 'MyStaffActivity' of processes
'MyProcess' has been stopped because of an unhandled failure...

These problems indicate that administrative security might
not be enabled. Human tasks and processes that use people authorization
require that security is enabled and the user registry is configured.
Take the following steps:

1. Check that administrative security is enabled. In the administrative
console, go to Security > Global security and
make sure the Enable administrative security check
box is selected.
2. Check that the user registry is configured. In the administrative
console, go to Security > User Registries and
check the Active user registry attribute.
3. Restart the activity, if stopped.

The
following common error situations are indicated by warning or error
messages:

- Could not connect to LDAP server in the trace.log file
indicates failure to connect to the LDAP server. Check your network
settings, the configuration (especially the provider URL) for the
people directory provider you use, and verify whether your LDAP server
requires an SSL connection.
- javax.xml.transform.TransformerException: org.xml.sax.SAXParseException:
Element type "xsl:template" must be followed by either attribute specifications,
">" or "/>" in the System.out or System.err files
indicates that the LDAPTransformation.xsl file
cannot be read. Check your people assignment configuration and the
configured XSLT file for errors.
- LDAP object not found. dn: uid=unknown,cn=users,dc=ibm,dc=com
[LDAP: error code 32 - No Such Object] in the trace.log file
indicates that an LDAP entry cannot be found. Check the task model's
people assignment criteria (verb) parameters and the LDAP directory
content for mismatches in the task model.
- Requested attribute "uid" not found in: uid=test222,cn=users,dc=ibm,dc=com in
the trace.log file indicates that an attribute
cannot be found in the queried LDAP object. Check the task model's
people assignment criteria (verb) parameters and the LDAP directory
content for mismatches in the task model. Also check the XSLT file
of your people assignment configuration for errors.

- If people resolution did not find any users for a task role, and
default users were selected.
- If you are using VMM, warnings when specified entities or specific
attributes could not be found in the VMM people directory.
- If you are using substitution, logs decisions whether or not users
have been substituted.

1. Using the administrative console, click Servers > Clusters > WebSphere application server clusters > cluster\_name,
then on the Configuration tab, in the Business Process Manager section, expand Business Process Choreographer, and click Human Task Manager.
2. On the Configuration tab, set the value
for the custom property Staff.Diagnosis to one of
the following values:
off
Never writes additional people assignment information.
on
Always writes additional people assignment information.
development\_mode
Only writes additional people assignment information when the
server is running in development mode. this is the default value.
3. Restart the server.

The following messages are generated:

- Core.StaffDiagMsgIsEnabled=CWTKE0057I: The output of people
(staff) resolution diagnosis messages is enabled. Indicates
that the diagnosis feature is enabled. This message is generated when
the Human Task Manager is started.
- Core.EverybodyIsPotInstanceCreator=CWTKE0047I: Everybody
is potential instance creator for task {0}. Indicates that Everybody became
the potential instance creator because no potential instance creator
is defined.
- Core.OriginatorBecomesPotStarter=CWTKE0046I: Originator
becomes potential starter of task {0}. For stand-alone tasks
only: Indicates that the originator became the potential starter because
no potential starter is defined.
- Core.EverybodyIsPotentialStarter=CWTKE0045I: Everybody
is potential starter of task {0}. For inline tasks only:
Indicates that Everybody became the potential starter
because no potential starter is defined.
- Core.OriginatorBecomesAdministrator=CWTKE0044I: Originator
becomes administrator of task {0}. Indicates that the originator
became the administrator because no administrator is defined.
- Core.EscalationReceiverDoesNotExist=CWTKE0043W: Administrator(s)
will be the escalation receiver(s) of the escalation {0}. Indicates
that the administrators became the escalation receivers because staff
resolution for the escalation receivers either failed or returned
an empty list.  If no escalation receiver is defined, the default
is Everybody, and a trace message is written.
- Core.EverybodyIsPotentialOwner=CWTKE0014I: Everybody is
potential owner of task {0}. Indicates that Everybody became
the potential owner because no potential owner is defined.
- Core.PotentialOwnerDoesNotExist=CWTKE0015W: Administrator(s)
will be the potential owner(s) of the task {0}. Indicates
that the administrators became the potential owners because staff
resolution for the potential owners either failed or returned an empty
list. If no potential owner is defined, the default is Everybody,
and a trace message is written.
- StaffPlugin.VMMEntityNotFound=CWWBS0457W: The VMM entity
could not be found, received VMM message is ''{0}''. Indicates
that a specified VMM entity (a group or person) was not found in the
people directory and the reason. People or groups that cannot be found
in the people directory are not included in the people resolution
result.
- StaffPlugin.VMMEntityAttributeNotFound=CWWBS0454W: VMM
entity ''{0}'' has no attribute with name ''{1}'' of type ''{2}''. Indicates
that a specified attribute was not found when searching for a VMM
entity (person) in the people directory. If no user email address
is found, the user cannot receive email notifications for escalations.
If no user preferredLanguage is found, the default
language setting is used. If no substitution attributes (isAbsent or substitutes)
are found when reading, an attempt is made to initialize the attributes.
If no substitution attributes are found when writing or updating,
an exception is generated.
- StaffPlugin.VMMResultIsEmpty=CWWBS0456W: The VMM invocation
returned no requested result entities. Indicates that a (get
or search) invocation of VMM did not return any entities. No users
are included in the people resolution result.

- Group members are not authorized, although the group name is specified: One possible reason for this situation is that you have configuredthe LDAP user registry for WebSphere security and selectedthe Ignore case for authorization option. Ifso, either clear the option, or specify LDAP group dn inall uppercase.
    - Specify the group short name when using the Local OS registry
for WebSphere security, and the group dn when
using the LDAP registry.
    - Make sure that you respect the case sensitivity of the group name.

One possible reason for this situation is that you have configured
the LDAP user registry for WebSphere security and selected
the Ignore case for authorization option. If
so, either clear the option, or specify LDAP group dn in
all uppercase.

- Changes in group membership are not immediately reflected in authorization.
This might happen, when the affected user is still logged on. The
group membership of a user is cached in her login session, and (by
default) expires after two hours. You can either wait for the login
session to expire (default is two hours), or restart the application
server. The refresh methods offered by Human Task Manager do not apply
for this people assignment criteria. Note that the group membership
list of the process starter is never refreshed.

1. Assess whether your people assignment criteria definitions lead
to shared or unshared people assignment results.
2. If unshared assignment results occur, consider putting a cleanup
procedure in place for people assignment results. Base the cleanup
interval on the expected number of task instances, and the unshared
people assignment results per cleanup interval. For more information
on how to apply a script-based cleanup procedure, refer to Removing unused people query results, using administrative scripts.