# Installing fix packs and interim fixes

## Before you begin

Visit the IBM
Support website to check for available fix packs and interim
fixes.

## Procedure

Before you install a fix pack or interim fix, perform
the following tasks:

1. Read the fix pack and interim fix documentation thoroughly.
The documentation lists dependencies, such as WebSphere® Application Server fix pack levels
or other IBM product fixes that
you must install before you apply the fix pack or interim fix.
2. To ensure that your implementation is performing the same
way that it did before you applied the fix pack or interim fix, prepare
a regression test plan.
3. Back up your databases and profiles.
4. Before you deploy the fix pack or interim fix to a production
environment, install the fix pack or interim fix in a development
or quality-assurance environment.

- Rolling upgrade

You can roll out maintenance incrementally in an IBM Business Automation Workflow installation that consists of Workflow Center and multiple workflow servers, allowing for the continued running of production applications during the upgrade and regression test period.
- Installing fix packs and interim fixes interactively

You can install updates to software packages using IBM Installation Manager interactively.
- Installing fix packs silently

You can install fix packs to IBM Business Automation Workflow silently.
- Installing interim fixes silently

You can install an interim fix for IBM Business Automation Workflow using the command-line mode of the Installation Manager.
- Rolling back fix packs interactively

Using the Roll back packages wizard, you can remove a fix pack from the IBM Business Automation Workflow installation and revert to a previous version.
- Rolling back fix packs silently

You can use imcl commands to roll back a fix pack from the IBM Business Automation Workflow installation and revert to a previous version.
- Uninstalling interim fixes interactively

You can uninstall one or more interim fixes for IBM Business Automation Workflow using Installation Manager.
- Uninstalling interim fixes silently

You can uninstall an interim fix for IBM Business Automation Workflow using the command-line mode of the Installation Manager.