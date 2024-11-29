# Defining the instance migration policy by using Workflow Center

## Procedure

1. In Workflow Center, click
Details for a process app and then select the
Snapshots tab.
2. Find the snapshot that you want to migrate, and then select Create migration
policy from its three-dot menu. This action sets the selected snapshot as the
target of the migration.
3. In Manage migration policies, click
Create.
4. In Create a migration policy file, select the snapshot that you
want to migrate from, and then click Create. You can use the toggle to see
all snapshots or only the installed ones. This action sets the source of the
migration.You now have a migration policy file associated with the target
snapshot for this source snapshot.
5. To set the policies for a specific migration policy file, go to Manage
migration policies and select Edit from the three-dot menu for
the policy with the same name as the source snapshot. Processes that have orphaned
tokens are listed.
6. Select each process or subprocess to edit its policy entries.
The first section displays the diagram for the process or subprocess that you select.
The steps in the diagram that might have an orphaned token are listed in the second section. As you
select a step, it is highlighted in both sections.
7. From the second section of the editor, select the process or subprocess.
8. For each step, set whether orphaned tokens that occur at that step should be moved or
deleted. You can also choose to suspend the process after a token is moved or deleted to prevent the
tasks from being worked on until the process resumes.
9. If you choose to move an orphaned token, the first section of the editor splits into two
sections. Use the diagram to select the step to move the orphaned token to.
For example, you have a subprocess that could generate an orphaned token. You select to
move these orphaned tokens. In the diagram, you browse until you see the step that you want the
token to move to and select it. 
When you select the target step for the move, the second section updates to add the name of
the target.
10. Click Save. The migration policy file is ready to
be exported.

## What to do next