# Rolling back fix packs interactively

## Before you begin

During the rollback process, Installation Manager must
access files from the earlier version of the package. By default,
these files are stored on your system when you install a package.
If the files are not available on your workstation, you must include
the location of the repository from which you installed the previous
version of the product in your Installation Manager preferences (File >
Preferences > Repository). If you installed the product
from DVDs or other media, they must be available when you use the
rollback function.

## About this task

Use the rollback function if you have applied a fix pack
to a product package, and decide later that you want to remove the
update and revert to the earlier version of the product. When you
use the rollback function, the Installation Manager uninstalls the
updated resources, and reinstalls the resources from the previous
version.

When you roll back to an earlier version of a package,
it is restored with same features that were associated with that version.
Use the Modify Packages wizard to add and remove features.

For
more information about Installation Manager, including how to perform
a rollback from the command line, refer to the Installation Manager
documentation.

## Procedure

1. Stop all software for the product that you are rolling
back. Close programs and stop servers that have profiles
for this product.
2. Start the Installation Manager.
3. From the Start page of the Installation Manager, click Roll
back to start the Roll back packages wizard.
4. On the Roll Back Packages page, from the Package Group
Name list, select the package group that contains the packages that
you want to roll back and click Next.
5. Select the version of the package that you want to roll
back to and click Next.
6. Read the summary information and click Roll
Back to roll back the package.
7. Optional: 
When the rollback process completes, a message that confirms the success of the process is
displayed. Click View log file to open the log file for the current session
in a new window.
8. Click Finish to close the wizard.
9. Close Installation Manager.

## Results

The fix pack you selected to roll back is removed.

## Related information

- IBM Installation Manager documentation