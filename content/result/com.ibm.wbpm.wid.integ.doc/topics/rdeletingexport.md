<!-- image -->

# Deleting a web service export used with a IBM Business Automation
Workflow task

The following information shows how to
delete a web service export used by a IBM® Business Automation
Workflow task.
It also shows how to handle a web service export that has been deleted
in Integration Designer but the IBM Business Automation
Workflow task still has code that points to a BPEL process.

## Deleting a web service export used with a IBM Business Automation
Workflow task

To remove a web service export, follow these steps:

1. In the assembly editor, right-click the export and select Delete.
2 A message asks you to confirm the deletion with the followingoptions:
    - Also delete the implementation in the FileNet repository
(this operation cannot be undone). It is preselected and
the implementation cannot be restored afterward. Removing the implementation
in the FileNet repository at the time of deleting the export is recommended.
If you need the implementation on the FileNet repository for an error
situation or some temporary reason, see the following section on removing
out-of-sync references to remove the implementation later.
    - Also delete the generated web service port. It is not preselected. If you want to reuse the port later for
another export you will create later, you should leave the check box
cleared; otherwise, making this selection will delete the port defined
for the web service export.
3. Click Yes and the web service export is
deleted.

## Removing out-of-sync IBM Business Automation
Workflow task
references

Deleting a web service export does not guarantee
that the corresponding code in the IBM Business Automation
Workflow task
is removed and the code may still exist.

To remove the extraneous
code on the FileNet repository, follow these steps:

1. From the menu, click Window > Preferences. Expand Business Integration and click Case Management. Click Launch the Cleanup
wizard. The Specify the Connection Information page opens.
2. Specify the values for the connection information. Click Next.
3. In the Select a Task page, select the task
implementation that you want to delete from the FileNet repository.
At the highest level of the tree structure are object stores. They
contain solutions which, in turn, contain case types. Each case type
contains implemented tasks. Click Finish to
delete the task implementation. With this deletion you will now be
able to select the task again when you build a new web service in Integration Designer. When
finished deleting out-of-sync case management task references, click OK to close the Preferences window.

## Related concepts

- Design considerations for web services used with IBM Business Automation Workflow tasks

## Related tasks

- Creating a web service to implement a IBM Business Automation Workflow task
- Editing and validating exports used with IBM Business Automation Workflow activities