# Considerations for migrating to a different operating system

To migrate to a computer with a different operating system, you must
perform more migration steps.

To migrate to a computer with a different operating system, you must install
IBM Business Automation Workflow
24.x on a third
computer with the same operating system as the migration source computer (for example, Windows if
you are migrating from Windows to Linux). Then, run the
BPMCreateRemoteMigrationUtilities command to create a compressed file that you
can use on the migration source computer. Copy the file to the source computer.

- You must install IBM Business Automation Workflow on an operating system
version that 24.x
supports. If your source system is on an operating system version that is not supported, use a
supported newer version of that operating system for the third computer mentioned in the preceding
paragraph.
- If 24.x does
not support your source operating system type, you cannot use the business data migration method.
However, you can still do artifact migration. For more details, see Migrating artifacts to IBM Business Automation Workflow.