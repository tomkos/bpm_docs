# Copying existing metadata into the case management development
environment

## About this task

Reusable assets are limited to document subclasses, property
templates, non-hierarchical choice lists, or other classes, such as
custom object subclasses. Additionally, because you can reinitialize
the target object store, IBM® Business Automation
Workflow provides
a method for you to store the exported metadata in a location in the
design object store so that the target object store can be automatically
repopulated with this metadata when the environment is reset.

## Procedure

To reuse metadata from an object store when designing
your solution:

1. See the FileNet Deployment
Manager documentation
for details on exporting and importing metadata for the steps in this
procedure.
2. In FileNet Deployment
Manager,
create and save an export manifest of the wanted metadata from the
production object store that contains the items that you want to reuse.
FileNet Deployment
Manager saves
the new export manifest as an XML file with the name that you specified
in the following directory: deployment\_location\Environments\source\_environment\Assets\ExportManifests.
3. Create the deploy dataset.
FileNet Deployment
Manager uses the export manifest
file to generate a deploy dataset of exported objects. The dataset
directory includes a set of files where the exported metadata is stored.
4. Convert the objects in the export files for import.
FileNet Deployment
Manager creates
the converted data set in a new subfolder of the folder that you specified.
The subfolder is named after the deploy dataset name with .converted appended
to the name.
5. Make a note of the converted data set location and directory
name.
6. Import the exported metadata into the case management development
environment target object store.
Select the following options:
  

Table 1. Import options

Option
Specify

Deploy Dataset

The deploy dataset directory with the converted
export objects.

Storage Policy for Imported Objects

As the exported data is metadata only, no
content is present.

Import Security Permissions

Select this option to include security permission
lists for the objects imported into the target object store. A permission
list consists of an Access Control List (ACL) for an object. By default,
this option is selected.

Import Owner

Select this option to include the owner information
in the target object store. By default, this option is selected.

Import Object ID

Select this option to import the existing
ID of the imported objects, allowing object relationships by ID to
be maintained. If the option is not selected, the import process generates
new object IDs. By default, this option is selected.

Use Original Create/Update Timestamps and
Users

Select this option to preserve the source
system property settings for Creator, DateCreated, DateLastModified,
and LastModifier. These property values in the converted objects are
carried over into the target environment. By default, this option
is selected. 
This option requires privileged write access (AccessRight.PRIVILEGED\_WRITE).
See the IBM FileNet P8 documentation's security topics
for more information about this permission.

Update Options

These options affect objects that already
exist in the target object store.
Update if newer
The object in the destination is only updated if the object being
imported has been modified more recently.
Always Update
The object in the destination will always be updated, even if
it has been modified more recently than the object being imported.
Never Update
The object in the destination will never be updated, even if the
object being imported has been modified more recently.
7 To simplify resetting the development environment, addthe exported deploy dataset to the data set document object that islocated in the reinitialization folder for the case management designobject store.
    1. In IBM Administration Console for
Content Platform Engine,
select the case management design object store.
    2. Click Browse > Root Folder > IBM Business Automation
Workflow > Datasets > DevEnvReinitInfo > dev\_env\_connection\_definition.
    3. On the dev\_env\_connection\_definition page
in the right pane, click DeployDataset in the Containment
Name column.
    4. On the DeployDataset page, click Actions > Checkin, checkout, cancel > Exclusive checkout, and then
click Actions > Checkin,
checkout, cancel > Checkin.
    5 In the Checkin document window,add the following exported deploy dataset XML files by clicking Add tonavigate to the converted deploy dataset folder and attach each XMLfile that is contained in that folder. Restriction: Do not change the names of the Catalog.xml and deployDataset1.xml files.If you change the names, then Case Builder cannotread the files.
        - Catalog.xml
        - deployDataset1.xml
6. Click Checkin.
8. Notify the business analyst that the object store is ready
for use with the imported data.

- Creating a list of object store properties and document classes

 Traditional:  You can reuse existing Content Platform Engine properties and document classes in your case management solutions. You can create text files that provide the information from a target object store that you need for reusing existing properties and document classes.