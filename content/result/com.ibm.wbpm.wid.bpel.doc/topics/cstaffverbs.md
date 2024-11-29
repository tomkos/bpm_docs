<!-- image -->

# People assignment criteria

You can use people assignment criteria definitions in Integration
Designer to model people assignments for task roles. A definition
comprises a query name and a set of query parameters. When the task
is deployed, the assignment criteria are transformed into queries
that are specific to the people directory, for example, virtual member
manager. When the task runs, these queries retrieve the set of people
who are assigned to a role, such as potential owner.

1. In Integration Designer, a modeler associates a new task with
the people directory configuration, for example, for virtual member
manager, bpe/staff/samplevmmconfiguration. This
step determines which people assignment criteria are available for
people assignment.
2 In Integration Designer, the modeler associates a task role withpeople assignment criteria. For example, the potential owner roleis associated with the people assignment criteria GroupMembers , including the parameters:
    - GroupName set to the value cn=group1,
dc=mycomp, dc=com
    - IncludeSubgroups set to the value true
3. When the task is deployed, the people assignment service establishes
which people directory provider to use. It transforms the people assignment
criteria into a query for the people directory provider, which is
stored internally.

- The LDAP and virtual member manager people directory providers
support all of the predefined definitions
- The user registry people directory provider supports only those
definitions that are based on user and group names. Support is not
provided for definitions based on manager, or email attributes.
- The system people directory provider is for testing purposes only.
Support is limited to specifying a set of hard-coded user IDs so that
access to a people directory is not required.

- Default people assignments and inheritance rules

Default people assignments are performed if you do not define people assignment criteria for certain task roles, or if people resolution fails or does not return a result. The default assignments differ for inline tasks and stand-alone tasks.
- Predefined people assignment criteria

Predefined people assignment criteria are provided for retrieving sets of users from people directories.
- Customizing people assignment criteria

You can also extend the set of predefined people assignment criteria by customizing your own criteria.
- People assignment criteria and people query results

A people assignment criteria is associated with a task authorization role. The people query that is derived from the people assignment criteria is stored as part of the deployed task template, or task instance. During the execution of a task, the authorization roles require the resolution of the associated people queries so that people can be assigned to the task.
- Replacement variables in people assignment criteria definitions

You can use replacement variables as parameter values in some people assignment criteria definitions. The people resolution can resolve the assignment criteria at run time, based on information supplied by the contexts.