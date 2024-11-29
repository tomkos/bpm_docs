<!-- image -->

# Binding roles defined in assembly diagrams

## About this task

## Procedure

1. In the Business Integration view,
select the module that contains your web services export.
2. Right-click the selected module and select Open
Deployment Editor. The module deployment editor opens.
3. Click the Design tab.
4 Populate the application (module) level with the securityroles that you created in the web project section (and defined inqualifiers within the module's assembly diagram) by completing thefollowing steps:
    1. Select the Application Project node.
    2. In the Gather Security Roles subsection,
click Gather security roles to populate the
application (module) level with the security roles that you created
in the web project section and that are defined in qualifiers within
the module's assembly diagram. Under the Application Project node,
the available security roles are displayed.
5 Bind your security role by completing the following steps:

1. Select the Application Project node.
2. Click Add and select Authorization Table. An
authorization table and an authorization node are added.
3. Select the Authorization node and select the security role that you want
to bind.
4. Click Add and select the items you want to add to the role. You can add
users, groups, or special subjects.
5. Add additional authorization nodes if required.
6 Bind your RunAs users by completing the following steps:

1. Select the Application Project node.
2. Click Add and select RunAs Map. A RunAs map and a
RunAs node are added.
3. Select the RunAs node and ensure the security role matches the role you want to set. Add the
user name and the password to the authorization data.
4. Add additional RunAs nodes if required.
7. Save your changes and then close the Module Deployment editor.