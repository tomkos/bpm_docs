# Selecting Business Automation Workflow or an external ECM
system to manage folders

## About this task

In the Process editor under the Folder tab, you specify whether Business Automation Workflow or an external ECM system handles your ECM
folders and documents in the Folder Management section. In addition, if you
select Business Automation Workflow, you can control the actions of
your users, such as whether they can only view folders and documents or create folders and
documents.

You do not require any permission to create a folder that uses the IBM Business Automation Workflow selection. For the
Enterprise Content Management system selection, your selection is from the
ECM systems listed in the Process App Settings page. Therefore, you must set up
access to an external ECM system first before you can add a folder to it.

Though the user interface in the Folder Management section contains hover
help for many of the fields, use this information to understand the complete view of the set of
interacting fields. Links to key concepts such as local documents, references to external documents
and folders, and the effect of linked processes are also important when you make your folder
management decisions.

## Procedure

1 Select whether Business Automation Workflow or an external ECMsystem will contain the folder for your subsequent ECM documents and subfolders.
    - IBM Business Automation Workflow : Use Business Automation Workflow as the system to contain the base folder foryour subsequent ECM documents and subfolders. This selection is the default. Next, select theoptions that you want for your users
        - Allow locally managed documents: A user can create Business Automation Workflow documents for the duration of a process. See
Local documents.
        - Allow locally managed folders: A user can create an Business Automation Workflow folder for the duration of a process. Locally
managed folders are helpful for grouping documents and folders into a meaningful structure without
relying on this structure in an external ECM system. For example, you might create a tree structure
of folders for financial information. You can add subfolders for United States and China, and then
add financial documents for those countries.
        - Allow external document references: A user can add a reference to a
document on an external ECM system. See Adding references.
        - Allow external folder references: A user can add a reference to a folder
on an external ECM system. See Adding references.
- Enterprise Content Management system : Use an external ECM system andfolder to contain the base folder for your subsequent ECM documents and subfolders. When you createa new folder, this selection becomes preselected. Next, add the server and path.
    - Server: Select the server that you want to use.
    - Path : Enter a path for the folder. Paths can bestatic or dynamic. A static path might be /templates/claim-documents . The folder inthis path would contain templates that are relevant for a claim. A dynamic path can be created byusing environment and local variables in a JavaScript expression. For example,tw.env.claimsRootFolderPath + "/" + new Date().getFullYear() + "-" +tw.local.claimId would link to a folder specific to the Claim instance.

Paths can be
static or dynamic. A static path might be /templates/claim-documents. The folder in
this path would contain templates that are relevant for a claim. A dynamic path can be created by
using environment and local variables in a JavaScript expression. For example,
tw.env.claimsRootFolderPath + "/" + new Date().getFullYear() + "-" +
tw.local.claimId would link to a folder specific to the Claim instance.

        - Create automatically: If you select this check box, the folder is
created. If you do not select this check box, you must use a folder that is in the
Type drop-down list.
        - Type: If other folders available, such as a Financial Records folder, you
can select one of those folders from the drop-down list. The default type is Folder.
2. Click Save or Finish Editing.

- Adding references

References to documents and folders on Enterprise Content Management (ECM) systems can be added by users of a process application. These references allow users to add information important to their work.
- Local documents

Local documents are created and used within a business process instance. Local documents are helpful as they can add new content that your users require when they are working with your business process.
- Linked process folders

Because linked processes contain root folders, linked processes are also shown in the Folders tab.