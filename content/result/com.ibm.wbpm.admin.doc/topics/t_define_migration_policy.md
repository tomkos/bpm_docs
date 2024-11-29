# Defining the instance migration policy by using the Process Center console

## Procedure

1. In the Process Center console,
select the process app you want.
2. Select the snapshot that you want to migrate, click the
down arrow, and click Generate Migration Policy.
This action sets the target of the migration.
3. In the Generate Migration Policy File window,
click the snapshot that you want to migrate from. Click OK.
You can select to see all snapshots or only the installed ones.
This action sets the source of the migration.You
now have a migration policy file associated with the target snapshot
for this source snapshot.
4. To set the policies for a specific migration policy file,
expand the migration policy section and click Edit for
the policy with the same name as the source snapshot. Processes
that have orphaned tokens are listed.
5. Select each process or subprocess to edit its policy entries.
The first section displays the diagram for the process or subprocess that you select.
The steps in the diagram that might have an orphaned token are listed in the second section. As you
select a step, it is highlighted in both sections.
6. From the second section of the editor, select the process or subprocess.
7. For each step, set whether orphaned tokens that occur at
that step should be moved or deleted. You can also choose to suspend
the process after a token is moved or deleted to prevent the tasks
from being worked on until the process resumes.
8. If you choose to move an orphaned token, the first section of the editor splits into two
sections. Use the diagram to select the step to move the orphaned token to.
For example, you have a subprocess that could generate an orphaned token. You select to
move these orphaned tokens. In the diagram, you browse until you see the step that you want the
token to move to and select it. 
When you select the target step for the move, the second section updates to add the name of
the target.
9. Click Save. The
migration policy file is ready to be exported.

## What to do next