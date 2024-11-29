<!-- image -->

# Exporting integration solutions as serviceDeploy files

## About this task

## Procedure

1 If the Export an Integration Solution wizard is not currentlyopen, complete the following steps:
    1. From the File menu, select Export.
The Select page of the Export wizard opens.
    2. In the Select page, expand Business Integration and
select Integration solution.
    3. Click Next. The Export an Integration
Solution wizard opens to the Select a File Format page.
2. In the Select a File Format page, ensure that Command-line
service deployment is selected and click Next.
The Select an Integration Solution and Projects page opens.
3. In the Integration solution field,
select the integration solution that you want to export.
4. In the Integration solution projects list,
select the modules and mediation modules that you want to export.
5. Click Next. The Select the Files
and Specify the Target Directory page opens.
6. In the Target directory field, specify
the fully qualified path to the target folder where you want to export
the compressed files.
7. In the File Names column, accept
the default file names for the compressed files or type in new file
names.
8. If you want generated Java 2 Platform Enterprise Edition
staging projects from the workspace to be included in the compressed
files that will be exported, select the Include generated
Java 2 Platform Enterprise Edition projects from workspace check
box and then select the generated Java 2 Platform Enterprise Edition
projects from the Additional projects list.
9. In the Globally shared libraries that will need
to be deployed separately list, note the globally shared
libraries that are listed. You will need to manually package, export,
and deploy the globally shared libraries separately from the automatically
prepared compressed files that contain the modules and mediation modules.
10. Click Finish. The selected integration
solution, modules, and mediation modules are exported to compressed
files for command-line service deployment.