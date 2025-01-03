# Identifying solution assets for migration

## About this task

- Other IBM Business Automation
Workflow assets.
These assets are associated with the solution but managed by Workflow Center.
These assets must be migrated and installed separately by using the Workflow Center.
- Other FileNet® P8 assets.
These assets are associated with the solution but managed by other FileNet P8 tools. These assets must be
migrated and deployed through FileNet Deployment
Manager and Process Configuration
Console.
- Other IBM and external assets. These assets are developed
outside of IBM Business Automation
Workflow and
FileNet P8 tools. Manual changes
are required to migrate and deploy these types of assets.

- Solution assets

Solution assets are created in the IBM Business Automation Workflow development environment when you design the solution. When you export a solution package with Workflow Center or Case administration client, these assets are included in the package.
- Solution application assets

Solutions can include assets that are not included in a solution snapshot or solution package. These extra assets, called solution application assets, are created and managed by Workflow Center or non-IBM Business Automation Workflow tools.
- Obtaining a solution description document

You, or your business analyst, can generate a solution description document by
running the Solution Document Generator from a command line. The solution description document
includes a list of all the cases and their assets for a specific solution.
- Obtaining a list of object store properties and document types

To help you prepare for solution migration, you or your business analyst can
generate text files that provide information about all object store properties and document types in
a development environment target object store.
- Solution List page

The Solution List page displays the solutions that are deployed to all object stores. You can see each solution's status, description, FileNet P8 target environment, and Case Client URL.