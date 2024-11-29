<!-- image -->

# Discovering artifacts in a Universal Description Discovery
and Integration registry

## About this task

## Procedure

1. Right-click the module name and from the menu select New >
External Service. The External Service wizard
opens. Select Registries as the type of service
and click Next.  In the following page, select
a registry if defined and click Next. Click Next.
2. The Discovery Configuration page opens.
Select the registry to connect to. If no entry exists, you can configure
one at this time. Click Next.
3 The Object Discovery and Selection pageopens. If you click Run Query at this timethen all the interfaces on the UDDI registry you selected will bequeried and listed in the Discovered objects pane. If you wantto limit the result or if you want to query other artifact types likebusiness objects or other XML files, then click the EditQuery button. We will use the Edit Query buttonto demonstrate how to edit a query. Click Edit Query .The Query Properties page opens. The Searchterm field specifies the term that is searched in services, businessesor interfaces (technical models). A service, business or interface(technical model) will only be found if the search term is containedin their 'name' field at any position. The search term is case sensitive.For partial search term matching use the '%' wildcard character. Thebusiness, service and interface selections determine where the searchterm will be searched. Click OK .

Click Edit Query.
The Query Properties page opens. The Search
term field specifies the term that is searched in services, businesses
or interfaces (technical models). A service, business or interface
(technical model) will only be found if the search term is contained
in their 'name' field at any position. The search term is case sensitive.
For partial search term matching use the '%' wildcard character.

    - Business: If business is selected, then
all business names containing the search term are found.
    - Service: If service is selected, then all
service names containing the search term are found.
    - Interface: If interface is selected, then
all interface names containing the search term are found.

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
the artifact was added into the UDDI registry. Icons before the list
of discovered objects let you discover details about objects, if applicable
and available. The icons become active in these cases. The details
include the name, description, Uniform Resource Identifier (URI),
version, owner and location of the artifact. 
An
icon below the Discovered objects pane, lets you work with
a vertical layout, if you want.
Click Next when
all the objects you want have been added to the selected objects list.
5 The Service Location Properties pageopens. You can change the module at this time or create a new module.You can also specify a folder for the artifacts, which is helpfulfrom an organizational view if you have many artifacts in the module. The following options are available: Click Finish to add the artifactsinto your module.

- You can overwrite existing files (default).
- You can create a folder structure (default).
- You can specify that a WSDL service and its binding be placed
into a separate file.
- You can specify that inline schemas in interfaces should be placed
into separate files, which is recommended if you intend to use these
schemas with the IBM® Integration
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