# Importing and exporting projects and toolkits

You can import projects and toolkits from other IBM® Workflow
Center repositories, and
you can also export projects toolkits.

Before installing the case project snapshot into another workflow environment, follow the steps
in Updating the data maps of a case project before importing to a workflow environment to ensure that the data maps, and the Design and the target object
stores mapping are correct.

## Before you begin

- The users and security groups, which the teams refer to, in a process app exist in the user
repository.
- To import or export a process application or toolkit, you have access to the repository or are a
repository administrator. For more information, see Managing access to the Workflow Center repository.
- To import or export a case solution, your role must be that of a business analyst or solution
administrator with permission to the target object store and the workflow system in the Content Platform Engine. Because case solutions
are assets in the object store. Security on the object stores depends on the role of the user. For
more information, see Planning for security in the development environment. To
import or export a case solution, use the new Workflow Center.
- Important:
    - Validate the case solution in Case Builder before you export it. Validation prevents any
solution errors during import or installation of the solution into a Workflow Server
environment.
    - Before importing the case project into another workflow environment, follow the steps in Updating the data maps of a case project before importing to a workflow environment to ensure that the data maps, and the Design and the target object stores
mapping are correct.

## Procedure

- To import a project or a toolkit from an IBM Business AutomationWorkflow export (.twx) file by using the classic Workflow Center , complete thefollowing steps: When the import is complete, the imported project is included under Processapps or Toolkits .Note:
    1. Select Process apps or Toolkits.
    2. Click Import.
    3. In the Import window, click Browse to locate the
Business Automation Workflow
export (.twx) file that you want to import.

Note: Projects that you import need to have unique acronyms or prefixes. If an acronym or prefix is
not unique, the import completes with a warning; however, attempts to install snapshots on test and
productions servers fail with an error.
    4. Click OK.
In the Import window, click to expand the sections that show both the
snapshots that get imported and that are already available (and will not be imported).
    5. Click Import to import the selected .twx
file.
    - If you import a process app from an IBM Business Automation
Workflow export
(.twx) file that was created before IBM Business Process Manager
 V7.5.1 and the
process app refers to an IBM Content Integrator Server, the connector name is lost and you must
manually specify it again in the Servers tab of the Process App
Settings editor.
    - Upgrading the case solution from a previous to the current version is supported for only a
single snapshot of the workflow project. However, once a case solution has been upgraded after
importing a previous snapshot, it cannot be upgraded again after importing a latest snapshot due to
a limitation in IBM
FileNet® Deployment Manager.
- To export process apps to Business Automation Workflow by using the classicWorkflow Center , complete thefollowing steps:

1. Select Process apps or Toolkits.
2. Click the projects that you want to export.
3. Find the snapshot that you want to export. If a snapshot doesn't exist, create one by clicking
Create New Snapshot.
4. Click Export.
5. To import the project into another Workflow Center or to use later in the
same Workflow Center (shared
or as a backup), select the .twx option. To install the project to a runtime
environment, select the .zip file option.
6. Locate the directory where you want to save the export file, name the file, and then save
it.
The exported file can be imported into any Workflow Center
repository.

## What to do next

Imported toolkits are immutable, which means that no one can change the items within an imported
toolkit. Administrators can change the immutable quality of a toolkit by enabling the
Allow users to update toolkit option in the Manage tab for the imported
toolkit.

The user who imports a toolkit has administrative access to that toolkit. Administrators can
grant access to other users and groups as described in Managing access to workflow projects.

- Importing and exporting BPMN models

You can import BPMN 2.0 models to use in your processes. You can also export your process applications to a BPMN 2.0 file archive (.zip).
- Subscribing to Blueworks Live processes

You can access IBM Blueworks Live processes from  Process Designer .

## Updating the data maps of a case project before importing to a workflow environment

You
can modify the data maps of a solution package before importing it into another
environment.

### Procedure

1. Copy the compressed file that contains the exported solution package to a location that
is accessible by IBM Business Automation
Workflow
Case administration client.
2. Start the Case administration client.
3. From the navigation tree in the left window, select the design object store to which you
want to import the solution.
4. Right-click Solutions and click Modify Data
Map and complete the wizard steps. 
Tip: Review the solution package, solution information, and object store mapping before
you modify its data maps.

After you complete the wizard steps, the solution package archive file is created, and would be
available to download with the updated data maps.Note: You can modify the data maps only of a
solution package that was exported from Workflow Center or Business Automation Studio.