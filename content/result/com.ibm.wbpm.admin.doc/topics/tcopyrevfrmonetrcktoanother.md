# Copying changed assets from one branch to another

After you work in isolation on separate features that are related to a
project, creating or updating assets, you need to copy those changes from a snapshot to the tip of a
branch, usually the main branch.

For Business Automation Workflow
Advanced
deployment environment content (later on called
advanced content), assets that are created in IBM® Process
Designer are defined as
top-down assets, while assets created in IBM Integration
Designer are defined as
bottom-up assets.

Because the copied modules and libraries and their contents are replaced in
the target branch, remember the following considerations regarding advanced content:

- If the asset is defined in IBM Process
Designer, do not update
the default module and library in IBM Integration
Designer.
This is a top-down asset.
- If the asset is defined in IBM Integration
Designer, do not place the
assets in the default library or module. This is a bottom-up asset. Instead, define these assets as
part of their own modules and libraries.
- Do not use IBM Process
Designer to update assets
that are defined in IBM Integration
Designer.

## Procedure

To copy assets from a source snapshot to the tip of a destination branch in the classic
Workflow Center, complete the following steps:

1. Select a process application or a toolkit.
2. Select the branch that you want to copy from.
You see the snapshots for the branch you selected.
3. Select the snapshot that you want to copy changes from.
The snapshot opens in the Process Documentation view. You can
see the categories of the assets.
4. Click Copy.  Note: If
an asset with the same name as the source snapshot is present in the
target snapshot, the asset name is changed to a different name after
the snapshot copy is complete. 
The Snapshot
Copy window opens.
5. Select the branch where you want to copy the revisions to. Assets that are not supported in
Process Documentation are listed under the Other and Advanced
Content categories. 

Tip: If you expand the twistie, you can see comparisons of the assets that are marked
Updated or Conflict and the updated and original assets side by side. For assets that are not
supported in Process Documentation, you cannot see a side-by-side comparison, but you can copy the
updated asset to the tip of the selected branch. When you expand the twistie for a New asset, you
can view only the new asset. To see a detailed view of either the original or updated supported
asset, click View. To go back to the side-by-side view, click the breadcrumb
at the top or beginning of the view.
6. Select the assets that you want to copy, and then click Copy from <source> to
<destination>, where the source is the snapshot of the revised branch and the
destination is another branch, usually the main branch. 
A confirmation window opens.
7. By default, all the dependencies that exist in the source
snapshot are included in the copy. Optionally, you can clear dependencies
that you do not want to include in the copy.

- States of assets when copying from one branch to another

Before they are copied from one branch to another, assets are in the New, Updated, Conflict, or No Change state as compared to the assets that are available in the destination branch.
- Importing a project into a branch

You can import a project into a new branch or an existing branch, which is the main branch.