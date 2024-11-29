<!-- image -->

# Setting human task preferences

## About this task

- Show the Task Description Properties Change window-Shows a warning window when changing the check box Usedisplay name, description, and documentation from the correspondingbusiness process activity on the description propertiespage of an inline invocation to-do task.
    - When you clear this check box, no warning window is displayed.
You must be using V7.0.0.3 or later for both IBM® Integration
Designer and IBM Workflow
Server.
If you are using an earlier version, you must ensure the check box
is selected.
    - Enabling the setting of the display name, description, and documentation
properties of an inline invocation task or inline to-do task causes
errors with versions before V7.0.0.3 of IBM Integration
Designer and IBM Workflow
Server.
- Show People Directory Change warning window- Shows a warning window when changing the people directory on thedetails properties page of a human task.

- When you clear this check box, no warning window is displayed
when the people directory value on the human task details properties
page is changed.
- Changing the people directory on the details property page of
a human task may invalidate the current people assignment criteria.
- Show Expected Task State Change warning window- Shows a warning window when changing the expected task state onthe details properties page of an escalation in an escalation chain.

- When you clear this check box, no warning window is displayed
when the expected task state value on the escalation details properties
page in an escalation chain is changed.
- If an escalation is part of an escalation chain, changing the
expected task state affects all of the escalations in the chain.

To change the people directory and modify assignment criteria
settings, complete the following steps:

## Procedure

1. From the main menu, select Window > Preferences. The Preferences
window opens.
2 Expand Business Integration andexpand Human Task Editor . If youdo not see the Human Task editor in the Business Integration preferences,complete the following steps:
    1. Expand Workbench and select Capabilities.
    2. Select Integration Designer and
then click Apply. The business integration
tools are enabled.
    3. Click OK. The Preferences window closes.
If you open the Preferences window again, you see that Business
Integration is displayed.
3. To see the people directory settings that you can modify,
click People Directory. You can
select a people directory to be the default for new human tasks. You
can also add a new entry, and edit or delete an existing entry.
4 Optional: Add a new people directory.

1. Click Add. The Add
People Directory window opens.
2. Enter a unique name for the new people directory.
3. Enter the Java Naming and Directory Interface (JNDI)
name for the people directory. This entry associates
the JNDI name with the name that you provided in thePeople
Directory field. At
run time, the JNDI name identifies which staff resolution code to
use.
4. Select the people assignment criteria that are associated
with this people directory. For
each choice, there are predefined criteria.When
you specify people to work on a task, the assignment criteria that
you are presented with are determined by this selection. For example,
if you select LDAP as the people directory for your human task, when
you assign people to that task you are presented with the LDAP-specific
assignment criteria. 
You can choose your own people assignment
criteria (XML file) by selecting the last radio button in the people
assignment criteria list, and clicking Browse.
5 Optional: Edit a people directory.

1. Click Edit. The Edit
People Directory window opens.
2. Optional: Modify the name of the people
directory. You must provide a meaningful name because this
entry is used elsewhere to refer to this people directory.
3. Optional: Modify the JNDI name for the people
directory. This entry creates an association between
the JNDI name and the name that you provided in the People
directory field. At
run time, the JNDI name identifies which staff resolution code to
use.
4. Select the people assignment criteria that are associated
with this people directory.
For each choice, there are predefined criteria. When
you are specifying people to work on a task, the assignment criteria
that you are presented with are determined by this selection. For
example, if you select LDAP as the people directory for your human
task, when you assign people to that task you are presented with the
LDAP-specific assignment criteria. 
You can
choose your own people assignment criteria (XML file) by selecting
the last radio button in the people assignment criteria list, ,
and clicking Browse.
6. Click Apply and then click OK.

## Related concepts

- Types of human task
- Inline and stand-alone human tasks
- Task templates
- Task instances
- Human task clients
- Human task user interfaces
- Versioning of human tasks
- To-do tasks and collaboration tasks with parallel ownership
- Lifecycle of a human task

## Related tasks

- Improving performance when using human task list widgets