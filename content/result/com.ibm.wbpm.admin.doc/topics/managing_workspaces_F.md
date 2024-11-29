# Cleaning up branches and snapshots

## Before you begin

If you want to delete branches without deleting the entire project, see Deleting branches.

To delete the project, you must have administrative access to the project.

## Procedure

If you are deleting a toolkit, you might need to repeat steps 1-3 multiple times before
you can re-import the snapshots you want to keep (step 4). To delete branches and all snapshots,
complete the following steps:

1. Remove all dependent snapshots and create a snapshot of the tip to preserve the most recent
changes.
See Creating snapshots, comparing, setting status, and validating.
2. Export all the snapshots you want to keep, including the tip snapshot you just created.
See Importing and exporting projects.Important: To restore a
deleted project, you must re-import it, which requires it or the latest snapshot of each branch, if
branches are enabled, to have been exported first.
3 Delete the entire project. See BPMRemoveProcessApplication command and BPMRemoveToolkit command .Attention:
    - Unnamed snapshots will also be deleted, which means the change history will be lost.
    - If you are trying to remove a toolkit, you might not be able to remove the target toolkit yet.
In this case, you must perform steps 1-3 again with any applications or toolkits that depend on the
toolkit you want to remove.
4. After you delete all applications and toolkit you want to clean, import the snapshots you want
to keep.
See Importing and exporting projects.