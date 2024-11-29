# Modifying authentication aliases

## About this task

- Using the administrative console as described in the following
Procedure section.
- Using the WebSphere command-line administration tool (wsadmin) AdminConfig commands. See Commands for the AdminConfig object using wsadmin scripting.
- The procedures in this topic are used to modify authentication
aliases and change users associated with aliases. To change passwords,
see Changing IBM Business Automation Workflow passwords.

## Procedure

From the administrative console.

1. Access the Business Integration Authentication Alias page. From the administrative console, click Security > Global Security > Java Authentication and Authorization Service > J2C authentication data. Note: You can also access this page from various administrative
console pages that require authentication alias information.

The authentication alias configuration page is displayed.This page contains a list of authentication
aliases, the associated component, the user ID associated with this
alias, and optionally a description of the alias.
2. Select the authentication alias that you want to modify
by clicking its name in the Alias column.
Note: In some cases, the Alias column
might not provide a link, in which case you select the check box in
the Select column corresponding to the alias
that you want to edit.
3. Change the properties of the alias. On the
authentication alias configuration page for the selected
alias, you can modify either the alias name or the associated user
ID and password. You can also modify the description of the authentication
data entry.
4. Confirm your changes. Click either OK or Apply. Return to the Business
Integration Authentication Alias page, and click Apply to apply your changes to the master configuration. Note: For a Network Deployment installation, make sure that a file synchronize
operation is performed to propagate the changes to other nodes.