# Migrating source artifacts

## Before you begin

Before you migrate the source artifacts, review the information in Migrating generated Java EE staging projects and Migrating server runtime targets.

## Procedure

To migrate source artifacts, complete the following steps:

1. Export the artifacts as integration modules by selecting File > Export > Business
Integration > Integration modules and libraries.
2. From the Export Integration Modules and Libraries window,
select Project interchange for sharing between workspaces and
select the projects to export. Click Next.
3. From this window, specify the file names for each archive
and the target directory. Click Finish.
4. Import the archive file that is generated in the previous
steps as a project interchange file.  To import a project interchange
file, select File > Import > Other > Project Interchange and click Next.
5. Click Browse to select the archive
file and click Finish. By default, the projects
are set to build automatically.  Therefore, after the project interchange
is imported, the build, including the validation, begins automatically.
6. The Workspace Migration wizard opens after the project
interchange file is imported.
7. After the migration process ends, you see a window indicating
that the migration validation has completed successfully.

## What to do next

To see more details about the validation,
go to the Migration Results view.