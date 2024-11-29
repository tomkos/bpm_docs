# Rolling back fix packs silently

## About this task

Use the imcl rollback command if you
have applied a fix pack to a product package, and decide later that
you want to remove the update and revert to the earlier version of
the product. When you use the rollback function, the Installation
Manager uninstalls the updated resources, and reinstalls the resources
from the previous version.

When you roll back to an earlier
version of a package, it is restored with same features that were
associated with that version. Use the imcl modify command
to add and remove features.

For more information about Installation
Manager commands, see the Installation Manager documentation.

## Procedure

1. Stop
all software for the product that you are updating. Close
programs and stop servers that have profiles for this product.
2. Open a command prompt, and change directories to the /tools directory
under Installation Manager.  Important: If you are running Windows, start your command prompt by
right-clicking and selecting Run as administrator.
3 Make the appropriate replacements and run the followingcommand: imcl rollback offering\_ID \_version -installationDirectory installation\_directory -log log\_file where: For example:C:\Program Files\IBM\Installation Manager\eclipse\tools>imcl rollback com.ibm.bpm.EXP.v85\_8.5.0.20130504\_0134 -installationDirectory C:\IBM\BPM\v8.5 -log silent\_rollback.txt

```
imcl rollback offering\_ID\_version -installationDirectory installation\_directory -log log\_file
```

    - offering\_ID is the offering
ID of the product installed. For the list of offering IDs, see Table
1 in Installing fix packs silently.
    - version is the original version
of the product. Rolling back returns your installation to this version.
    - installation\_directory is
the location where you installed the product.
    - log\_file is the location and
name of the log file to write.

```
C:\Program Files\IBM\Installation Manager\eclipse\tools>imcl rollback com.ibm.bpm.EXP.v85\_8.5.0.20130504\_0134 -installationDirectory C:\IBM\BPM\v8.5 -log silent\_rollback.txt
```

4. When the rollback completes, check the log files to ensure
that the rollback completed successfully. A success
message displays on the command line.
5. Restore the profile and the database backup taken prior
to installing the refresh pack.