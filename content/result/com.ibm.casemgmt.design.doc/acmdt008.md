# Copying an existing solution

## About this task

The copy solution operation is available in the IBM® Business Automation
Workflow Case administration client ,
which can be used in any domain. Project areas are only present in
the development domain.

You can either reuse the existing properties or document classes from the original solution, or
you can select the option to create properties or document classes when you deploy the new solution.
When you reuse existing properties or document classes in a solution, you cannot redefine them in
Case Builder. You can remove the property or document classes from
the solution in Case Builder, but you cannot change any of the
attributes, such as data type.

Copying an existing
solution applies only in the development environment.

- You cannot copy a solution that has currently running tasks or
that has files that are checked out.
- You cannot copy an solution that was not yet committed.
- If a property that was not defined in the solution,
such as a system property, is used as a parameter for a rule operation
in a workflow, the copy solution operation will fail validation. To
copy the solution, you must clear the validation checkbox.

## Procedure

To copy a solution:

1. Start the Case administration client.
 Enter the following URL in a
browser:
http://server:port/navigator/?desktop=bawadmin
where
server is the IBM Content
Navigator IP address or
fully qualified server name, and 
port is the
IBM Content
Navigator port
number.
2. In the navigation tree in the left pane, select an object
store and click Solutions.
3. On the Solutions page in the right
pane, select the solution that you want to copy.
4. Click Actions > Copy and complete the wizard steps.

- Copying a solution to another development environment

You might need to copy a solution to another development domain for additional development and testing. After you copy the solution to the additional environment, you can open it in Case Builder to edit, deploy, and test the solution in that environment.
- Copying case solutions that are associated with process applications

When you copy a case solution that is associated with a process application, you must also copy the associated process application.