# Importing assets by using the Process Configuration console

## About this task

## Procedure

Use the Process Configuration console from within IBM Administration Console for
Content Platform Engine to import Process Services
assets from the development environment target object store to the
test or production environment target object store:

1. Start the Process Configuration console. For an object
store on the Administrative node, click Workflow
System > Actions > Configure
Workflow Settings.
2. From the Workflow Systems list,
select the connection point for the project area where the solution
application is to be deployed. In the Action menu,
click Connect to log on to the workflow system.
3. In the Action menu, click Import
to XML file to start the import wizard.
4 Complete the steps in the wizard. Keepin mind the following import guidelines:
    - Use the overwrite option to add new objects
or properties or to replace existing objects or properties in the
destination isolated region. If any transferred workflows use a queue,
the queue is overwritten even if the workflows are not running at
the time of the import. If the overwrite attempts to remove items
that are referenced, such as exposed fields or operation parameters,
then the import will fail (referenced items cannot be removed).
    - Use the merge option to add objects or
properties to the destination isolated region if these objects or
properties do not exist in the destination isolated region. If the
destination isolated region contains objects or properties with the
same name as those in the source isolated region, the items are merged.
Thus, for a solution redeployment, the merge option
preserves any existing properties in the destination target environment
and adds new properties from the development environment project area.
Use of the merge option is typical.
    - If the exported source contains system properties, the import
operation skips the import of user information if the user is not
defined on the destination system. This operation applies to both
overwrite and merge. You can use FileNet® Deployment
Manager to prepare the data for
deployment by mapping user information to values appropriate for the
destination target environment.