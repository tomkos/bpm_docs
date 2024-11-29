# Exporting other FileNet P8 assets
by using the Process Configuration console

## About this task

These
assets are not managed by IBM Business Automation
Workflow,
but the solution might incorporate them or the business processes
that are part of your solution application might use them. Examples
of these assets might be component queues or workflow system configuration
parameters.

## Procedure

To export other FileNet P8 assets
by using the Process Configuration console:

1. In IBM Administration Console for
Content Platform Engine,
select the target object store and click Administrative > Workflow System.
2. On the Workflow System tab, click Actions > Configure Workflow Settings.
3. From the Workflow Systems list,
select the connection point for the project area where the solution
application resides. In the Action menu, click Connect to
log on to the workflow system.
4. In the Action menu, click Export
to XML file to start the export wizard.
5 Complete the steps in the wizard. Keepin mind the following export guidelines:
    - Select only assets that were created with tools other than Case Builder. Migrating assets such
as work queues or event logs, which are created by the deploy solution
operation, can cause conflicts. Such assets can often be recognized
by the presence of the solution prefix in their name or when the asset
name is the same as the solution name.
    - Select the Include System Properties check
box to export workflow system configuration information. Some configuration
information is environment-specific. You might need to edit this information
by using Process Configuration console on the destination system after
the solution application is deployed.
    - If you want to export only system properties, select Export
selected components under Export Type.
On the Select Export Components page, clear the
check boxes for all components.

## What to do next