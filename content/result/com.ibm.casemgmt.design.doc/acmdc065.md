# Deploying prerequisite assets

## About this task

- Content Platform Engine Content
Services assets that the solution depends on, such as reused property
templates, document classes, or choice value lists. If the target
environment already contains the reused metadata, this step is not
required.
- Content Platform Engine Process
Services assets that are incorporated into the solution, such as a
workflow system configuration or component queues.
- Artifacts that were created with other IBM or external tools outside of IBM Business Automation
Workflow and FileNet P8 tools.
- Widgets that must be registered before the solution package is
deployed.

- Importing assets by using FileNet Deployment Manager

Other IBM FileNet P8 assets in the solution application that are managed by the Content Platform Engine are converted, analyzed, and imported by using the FileNet Deployment Manager.
- Importing assets by using the Process Configuration console

Import the required Content Platform Engine Process Services assets into the target environment where the solution application is to be deployed. Required Process Services assets are assets that are created with the Process Configuration console or Process Designer, not assets that are created in Case Builder.