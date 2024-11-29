# Archiving and deleting projects and toolkits

## Before you begin

## About this task

- When you archive a project, the authoring data in all its branches and snapshots including the
tip is archived and can't be used. Instance data is not archived. For example, you can't run the
artifacts, such as processes and services, of an archived process application.
- Don't archive a toolkit that other projects depend on nor use archived toolkits when creating
toolkit dependencies in Process Designer. Archived
items are not part of the active library.

## Procedure

In the new Workflow Center, select
Archive from the three-dot menu on the project. Archiving is not required for
deletion in the new Workflow Center. In the
classic Workflow Center, archiving is required
before deletion. Complete the following steps:

1. Select the Process Apps, Case Solutions, or
Toolkits tab.
2. Click the project you want to archive.
3. Click Manage.
4. Click Archive Process App, Archive Case
Solutions, or Archive Toolkit.
5. When prompted, click Archive to confirm that you want to archive this
project.

## Results

To view or restore the archived project, click the
Archived filter in the tab.

## What to do next

Archiving a project doesn't delete it or reclaim its place in the database. Archiving merely
marks it so it does not show by default in Workflow Center. To delete an archived project in the classic
Workflow Center, click the
Archived filter in the tab. Then, select Delete next
to the project you want to delete.

Deleting a project deletes all snapshots and instances, as well as associated BPEL process
instances, business-level applications, and enterprise applications.