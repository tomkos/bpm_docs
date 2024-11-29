<!-- image -->

# Exporting integration solutions as archive files

## About this task

## Procedure

1 If the Export an Integration Solution wizard is not currentlyopen, complete the following steps:
    1. From the File menu, select Export.
The Select page of the Export wizard opens.
    2. In the Select page, expand Business Integration and
select Integration solution.
    3. Click Next. The Export an Integration
Solution wizard opens to the Select a File Format page.
2. In the Select a File Format page, ensure that Server
deployment is selected and click Next.
The Select an Integration Solution and Projects page opens.
3. In the Integration solution field,
select the integration solution that you want to export.
4 In the Integration solution projects list,complete the following steps:

1. In the Core projects in integration solution section,
select the core projects that you want to export. These are projects
that can be deployed and run on a server, such as modules, mediation
modules, and user-authored enterprise application projects. Each project
is exported as an EAR file.
2. In the Global libraries referenced by core
projects or integration solution section, select the global
libraries that you want to export. Each global library is exported
as a JAR file.
5. Click Next. The Select the Files
and Specify the Target Directory page opens.
6. In the Target directory field, specify
the fully qualified path to the target folder where you want to export
the archive files.
7. In the File Names column, accept
the default EAR and JAR file names or type in new file names.
8. Click Finish. The selected integration
solution, projects, and libraries are exported to EAR and JAR files
for server deployment.