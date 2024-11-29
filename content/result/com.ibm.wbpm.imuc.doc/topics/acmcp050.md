# Integrating with a version control system (VCS)

## About this task

Whenever you click Commit on the Manage Solutions
page in Case Builder, the server saves new and updated solution
assets to the design object store. If you integrate with a VCS, the server also copies the changed
solution files to the directory that you designated to act as the sandbox. This sandbox provides a
staging area for the solution files that are to be stored in the VCS. Solution files are copied to
the appropriate sandbox subdirectory according to the solution and the user. The server then runs
your commit script to check in the changes from the sandbox to the VCS. The commit script creates a
change set that contains all new or modified solution assets, associates comments with each asset,
and checks the change set into the VCS.

Figure 1. Committing new and changed solution assets

<!-- image -->

After a solution is committed, you can click Deliver to check in the
solution as a whole to the VCS. After the server copies all solution files and a solution manifest
file to the sandbox, the server runs your deliver script to check in the files from the sandbox to
the VCS. The script then creates and labels a baseline or snapshot of the solution and delivers it
to the VCS.

Figure 2. Delivering the entire solution

<!-- image -->

After you deliver the files, you can deploy an IBM Business Automation
Workflow
solution from the VCS into another environment, such as a production environment or a different
development environment. You first extract the solution assets and solution manifest from the VCS
according to a specific delivery label. You then use the solution manifest file to import the
solution into the design object store in the new environment before you deploy the solution.

Figure 3. Deploying the solution into another environment

<!-- image -->

You can use the graphical user interface of your VCS to export the solution assets and solution
manifest from the VCS according to a delivery label and then use the IBM Business Automation
Workflow
Case administration client to import and deploy the solution to
the new environment. Alternatively, you can create a custom script to automatically extract, import,
and deploy the solution.

- Setting up and configuring VCS integration

To integrate IBM Business Automation Workflow with a version control system (VCS), you must first designate a directory to act as a sandbox. You then create scripts to check in and deliver solution files to the VCS, and use the IBM Business Automation Workflow configuration tool to enable and configure the VCS integration.
- Commit and deliver scripts

To integrate with a version control system (VCS), you must create two scripts to deliver change sets that contain new and modified solution assets the VCS. These scripts work with the Commit and Deliver actions in Case Builder.
- Disabling VCS integration

You can disable integration with a version control system (VCS).
- Adding an existing or a copied solution to a VCS

For a solution that existed before you integrated with a version control system (VCS), you should establish an initial baseline version in the VCS before you make additional changes to that solution. You should also establish an initial baseline version for a copied solution.
- Deleting a solution from a VCS

If you delete a solution in IBM Business Automation Workflow, the solution is not deleted from the version control system (VCS). If your company's established procedure requires a solution to be deleted, you must delete the solution separately from the VCS.