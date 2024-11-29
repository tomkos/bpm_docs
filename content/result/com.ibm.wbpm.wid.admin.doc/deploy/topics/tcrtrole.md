<!-- image -->

# Creating and assigning security roles to web service exports

## About this task

## Procedure

1. In the Business Integration view,
select the module that contains your web services export.
2. Right-click the selected module and select Open
Deployment Editor. The module deployment editor opens.
3. Click the Design tab.
4 Add a security role at the web project level by completingthe following steps:
    1. Select the Web Project node.
    2. Click Add and select Security Role. A Security Role node is added under Web
Project.
    3. In the Role name field, type
the name that you want to assign to the new security role. For example, Users.
    4. In the Description field, type
the description that you want to assign to the new security role.
For example, Security role for general users.
5 Add a security constraint by completing the following steps:

1. Select the Web Project node.
2. Click Add and select Security Constraint. A Security Constraint node is added
beneath Web Project.
3. In the Constraint name field,
type the name that you want to assign to the new export security constraint.
For example, constraint1.
4. Select the Web Resource Collection node.
5. In the Resource name field, type
the name that you want to assign to the web resource. For example, receiveWebServiceCallFromClient.
6. Under the Web Resource Collection node, add HTTP Method
nodes for all of the available HTTP methods that you want constrained.
7. Under the Web Resource Collection node, add URL Pattern
nodes for all the patterns that you want constrained.
6 Add the security role to the authorization constraint bycompleting the following steps:

1. Select the Authorized Roles node.
2. In the Description field, type
the description that you want to assign to the authorization constraint.
For example, UsersAuthConstraint.
3. Click Add and select Role. A role node is added under Authorized Roles.
4. For the Role field, select the
role that you want to associate with the authorization constraint.
For example, Users.
7. Press Ctrl-S to save your changes and then close
the module deployment editor.

## What to do next