# Restricting Inspector actions for online workflow servers

## About this task

## Procedure

1. Add an <inspector> element in the
<authoring-environment> section of the appropriate
100Custom.xml file in your topology. For more information about the
location of the 100Custom.xml file that must be updated, see Location of 100Custom configuration files.<properties>
...
   <authoring-environment>
   ...
      <inspector>
      </inspector>
   </authoring-environment>
</properties>
2. Add  one or more <target-server> elements.
 The <target-server> element describes
the server where the restrictions are applied.
3. Optional: To apply the restrictions to a particular type of server, add a
type attribute to the <target-server> element.
The type attribute can be development, test, staging, or
production. To find out the type of the server, open the 99Local.xml of
the server you are interested in (see Location of 100Custom configuration files for its
location) and look for <environment-type> in the server section.
4. Optional: To apply the restrictions to a specific
server, add a name attribute to the <target-server> element.
 To find out the name of a particular server, open the 99Local.xml of the
server you are interested in (see Location of 100Custom configuration files for its location)
and look for <server-name> (current environment name) in the server
section.
5. Optional: Add one <default-action-policy> element
to a <target-server> element.
6. Add one or more <action> elements
to the <default-action-policy> element.
 The <action> element describes a particular
Inspector action and the roles that are allowed to perform that action.
7 Add a type attribute to the <action> element. You can use the following values for the type attribute:
    - ACTION\_VIEW\_INSTANCE - Only the specified roles can view process
instances.
    - ACTION\_RUN\_PROCESS - Only the specified roles can run processes.
    - ACTION\_MANAGE\_INSTANCE - Only the specified roles can manage process
instances by suspending, resuming, stopping, or deleting instances.
    - ACTION\_RUN\_TASK - Only the specified roles can run or debug tasks.
    - ACTION\_CHANGE\_VARIABLE - Only the specified roles can change variables.
8. Add one or more <role> elements to the
<action> element. The <role> element
specifies the group that the user must be a part of to perform the parent action. The
<role> element can contain only one role, and that role must correspond to a
group that is defined in Workflow Center.

## Example

Here is an example that restricts all of the Inspector
actions on servers of type production:

```
<inspector>
   <target-server type="production">
      <default-action-policy>
         <action type="ACTION\_VIEW\_INSTANCE">
            <role>tw\_admins</role>
         </action>
         <action type="ACTION\_RUN\_PROCESS">
            <role>tw\_admins</role>
         </action>
         <action type="ACTION\_MANAGE\_INSTANCE">
            <role>tw\_admins</role>
         </action>
         <action type="ACTION\_RUN\_TASK">
            <role>tw\_admins</role>
         </action>
         <action type="ACTION\_CHANGE\_VARIABLE">
            <role>tw\_admins</role>
         </action>
      </default-action-policy>
   </target-server>
</inspector>
```

If an <action> type
is not specified or is empty, there are no restrictions for the user
on that action. The organization might determine that a process author
can use the Inspector to view instances on a staging server but not
allow the user to modify the running processes in any way. Assuming
that a user has administrative rights to the process application,
you can add the following lines to the appropriate 100Custom.xml file.
You can add more roles for particular servers or types of server,
as shown in this example:

```
<inspector>
   <target-server name="my staging server">
      <default-action-policy>
         <action type="ACTION\_VIEW\_INSTANCE">
            <!-- No Restrictions -->
         </action>
         <action type="ACTION\_RUN\_PROCESS">
            <role>tw\_admins</role>
            <role>staging\_admins</role>
         </action>
         . . .
      </default-action-policy>
   </target-server>
</inspector>
```