<!-- image -->

# Discovering artifacts in an IBM WebSphere Service Registry
and Repository

## About this task

## Procedure

1. Right-click the module name and from the menu select New >
External Service. The External Service wizard
opens. Select Registries as the type of service
and select IBM WebSphere Service Registry and Repository.
Click Next. In the following page, select a
registry if defined and click Next.
2. The Discovery Configuration page opens.
Select the registry and repository to connect to. If no entry exists,
you can configure one at this time. Click Next.
3 The Object Discovery and Selection pageopens. If you click Run Query at this timethen all the interfaces on the IBM WebSphere Service Registryand Repository you selected will be queried and listed in the Discoveredobjects pane. If you want to limit the result or if you want toquery other artifact types like business objects or other XML files,then click the Edit Query button. We will usethe Edit Query button to demonstrate how toedit a query. Click Edit Query . The QueryProperties page opens. The File type field specifiesif the search will be for web services (WSDL), business objects (XSD)or other XML code, such as business process execution language (BPEL)files. The Search term field specifies the term thatis searched in the name, description and owner properties. The searchterm is case sensitive. The search will find results that containthe search term in any position. The name, description and ownerselections determine where the search term will be searched. Objects in the IBM WebSphere Service Registryand Repository can be organized through classification metadata. Whenyou initially configure your registry within IBM IntegrationDesigner ,you include a classification host address where the classificationservice is located. Beneath Classification ,as shown below, all classifications available in the IBM WebSphere ServiceRegistry and Repository will be displayed. One or more classificationsin the classification tree can be selected which also will constrainyour search. The search can be further constrained by specifyingvalues in the Custom properties table. For example, if therewere several versions of the web services in the IBM WebSphere ServiceRegistry and Repository, then your query could specify a version. Click OK .

Click Edit Query. The Query
Properties page opens. The File type field specifies
if the search will be for web services (WSDL), business objects (XSD)
or other XML code, such as business process execution language (BPEL)
files.

The Search term field specifies the term that
is searched in the name, description and owner properties. The search
term is case sensitive. The search will find results that contain
the search term in any position.

    - Name: If file type Web services
(WSDL) is selected, then select name to find the search
term in the file name, port type name or operation name. If file type Business
object (XSD) is selected, then select name to find the
search term in the file name, complex type name or simple type name.
If file type other XML is selected, then select
name to find the search term in the file name.
    - Description: If description is selected,
then the search term is searched in the description property.
    - Owner: If owner is selected, then the search
term is searched in the owner property.

Objects in the IBM WebSphere Service Registry
and Repository can be organized through classification metadata. When
you initially configure your registry within IBM Integration
Designer,
you include a classification host address where the classification
service is located. Beneath Classification,
as shown below, all classifications available in the IBM WebSphere Service
Registry and Repository will be displayed. One or more classifications
in the classification tree can be selected which also will constrain
your search.

The search can be further constrained by specifying
values in the Custom properties table. For example, if there
were several versions of the web services in the IBM WebSphere Service
Registry and Repository, then your query could specify a version.

Click OK.

4. Click Run Query to retrieve the
artifacts you want. They will appear in the Discovered objects pane.
Select the artifacts you want, which will begin creating your query
by adding the artifacts to the Selected objects pane. The default
is to include referenced files with your selection. For example, if
you chose an interface then the default would be to include its business
objects. However, a message will let you clear referenced files. Return
to editing the query with the Edit Query button
to add more selections.  Hover help provides descriptions
of the artifacts you are viewing, if descriptions were added when
the artifact was added into the IBM WebSphere Service Registry
and Repository. Icons before the list of discovered objects let you
discover details about objects, if applicable and available. The icons
become active in these cases. The details include the name, description,
Uniform Resource Identifier (URI), version and owner of the artifact. 
An icon below the Discovered objects pane, lets
you work with a vertical layout, if you want.
Click Next when
all the objects you want have been added to the selected objects list.
5 The Service Location Properties pageopens. You can change the module at this time or create a new module.You can also specify a folder for the artifacts, which is helpfulfrom an organizational view if you have many artifacts in the module. The following options are available: Click Finish to add the artifactsinto your module.

- You can overwrite existing files (default).
- You can create a folder structure (default).
- You can specify that a WSDL service and its binding be placed
into a separate file.
- You can specify that inline schemas in interfaces should be placed
into separate files, which is recommended if you intend to use these
schemas with the IBM Integration
Designer tools.
If you choose this option, you can specify that the folder structure
be derived from the business object namespace.

Click Finish to add the artifacts
into your module.

6. The artifacts are added to the module. The file structure
of the original files placed in the registry may differ from the file
structure in the module. For example, you may have added a folder
in the final page of the wizard that places the files in an unknown
folder from the original reference point.

## What to do next