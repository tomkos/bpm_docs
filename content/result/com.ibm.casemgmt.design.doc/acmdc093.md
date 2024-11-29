# Exporting solution assets from a version control system (VCS)

## About this task

Export only those solution assets and solution manifest that were created for the solution in
Case Builder.

## Procedure

To export solution assets from a VCS:

- Use the graphical user interface of your VCS, if one is provided, to export all the solution
assets and the solution manifest that are associated with a specific delivery label.
- Create a script that uses the delivery label to export all the solution assets and the solution
manifest from the VCS.

## What to do next

- If your solution contains assets that were created in FileNet® P8, use FileNet Deployment
Manager to create a deploy package that contains the
assets.
- If your solution is associated with a process application, you must export a snapshot of the process
application. Before you import the solution
package to the target environment, you must import the process
application.
- If your solution includes pages that contain custom widgets, which might not exist in the target
environment, you must migrate the widgets before you import the solution package. The pages are
included in the Pages folder of the exported solution.
- If your solution uses properties that are associated with marking sets and you move the solution
to a different environment, you must re-create the marking sets and any property templates that use
the marking sets in the target environment. To re-create the marking sets, use the appropriate
FileNet P8 tools. When you
re-create the properties, you must use the same symbolic name that is used in the source
environment.To migrate the marking sets, use FileNet Deployment
Manager to export and import the
marking sets but not any property templates, which are created when the solution is deployed by
Business Automation Workflow.