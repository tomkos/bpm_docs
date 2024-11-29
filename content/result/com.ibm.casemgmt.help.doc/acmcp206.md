# Troubleshooting case and process integration

- Snapshots are not visible for an upgraded workflow project

If you export a workflow project and an associated snapshot from IBM Business Automation Workflow 19.0.0.1 and then you import the workflow project and snapshot into IBM Business Automation Workflow 19.0.0.2 or later, you can upgrade the workflow project successfully but you cannot view the snapshot in Case Builder.
- Activities are associated with the wrong snapshot of a process application

If a process application has multiple active snapshots, Case Builder might select the wrong snapshot to apply to activities.
- Changes to process applications are not reflected in activities

When a process application is changed, Case Builder does not automatically apply the changes to activities. These changes can include the creation of a new snapshot or the rollback to previous snapshot.
- Results output by a business process are not shown in an activity

An activity that is associated with a business process is updated based on output results that are received by the Content Platform Engine server.