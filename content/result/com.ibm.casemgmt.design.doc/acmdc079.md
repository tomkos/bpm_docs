# Importing assets by using FileNet Deployment
Manager

## About this task

## Procedure

To deploy additional Content Platform Engine assets to another development
or production target object store, use FileNet Deployment
Manager:

1. Place the exported deploy dataset onto a system where the FileNet Deployment
Manager tool is installed and
has access to the target environment.
The exported data
is typically transferred as a compressed file, such as a ZIP file.
Expand the compressed file into a deploy dataset folder of a FileNet Deployment
Manager deployment tree.

If the data was transferred as a FileNet Deployment
Manager Deploy Package, use the FileNet Deployment
Manager Expand Deploy
Package operation to expand the compressed file. The extraction places
the data into the selected deploy dataset folder. You can also choose
to extract the halfmaps into a source environment that exists in FileNet Deployment
Manager.
If the data is
not a Deploy Package, the halfmaps for both the source and destination
environments must be available to the FileNet Deployment
Manager instance that performs
the import. These halfmaps can either be created, if the source environment
is available, or passed along with the deploy dataset. The preferred
method for this second option is to use a Deploy Package.
2. Populate the halfmaps for the destination environment.
3. Join the source and destination halfmaps to create data
maps by associating correct mappings for object stores, security principals,
and services between the environments.
Follow all
recommendations in the FileNet Deployment
Manager documentation.
For example, ensure that there are corresponding administrative groups
in the source and destination environments with privileges appropriate
for importing and deploying the solution application. The security
principal mapping must also consider the ownership of assets, as described
in the summary of key options in step 6.
4. Convert the objects in the deploy dataset for import.
FileNet Deployment
Manager creates
the converted data set into a new subfolder of the folder that you
specified. The subfolder is named after the deploy dataset name with .converted appended
to the name.
5. Generate and review the analysis of the impact report to
verify the effect that the import operation has on the target environment.
The change impact analysis operation also validates the converted deploy dataset
file with the destination environment. This operation provides information
only; it does not actually import data or modify the destination environment
in any way.
6 Import the converted deploy dataset. Keep in mind the following import guidelines:
    - Some assets in the target object store are required by the solution
deployment and must be imported as prerequisite assets. Some assets
depend on the solution being deployed before they can be successfully
imported and must be imported as postrequisite assets. However, some
assets can be imported either before or after the solution is deployed if
the validation logic in the solution deployment or the import operation
do not enforce the presence of the asset or its dependents for a successful deployment.
Those assets can be packaged with either the prerequisite or postrequisite
assets. To avoid potential issues, consider how the asset is used
in the solution and choose a package that makes the most sense for
the overall solution application deployment process.
    - Deploy metadata extensions that were created by using the Content Platform Engine addOns feature to the
non-development target object store. Deploy these extensions by using
the same methods that were used when the asset was originally added
to the development environment target object store. For example, install
the integrated product into the non-development environment and apply
the addOn to the target object store, as directed by the product documentation.
    - Summary of key import options:
Import Owner
Ownership of solution application assets in the target environment
must be included in the security planning for the solution. Choose
this option to retain the owner information from the source environment.
Use data mapping for the security principals if you plan to switch
ownership to another user in the destination environment.
Import Object ID
This option must be selected.
Use Original Create/Update Timestamps and Users
Select this option only if the Update if Newer option
is also selected. Selecting this option might cause modifications
to Content Platform Engine system
properties. To modify system properties, the FileNet P8 domain user that is logged
in to FileNet Deployment
Manager must have
the Modify certain system properties privilege
on the destination object store or the import operation returns errors.
Transfer workflows after import 
Select this option if the import includes a workflow definition
document that is to be used as the current version in the destination
environment, and you want FileNet Deployment
Manager to
automatically transfer the workflow definition into the destination
workflow system as a part of the import process. If the workflow definition
references a Content Platform Engine Process
Services asset like a component queue, the import or definition of
that component queue must be performed first.
Always Update vs. Update if newer
Because it is important for a solution application deployment
to fully replicate the design from the source development environment,
use of the Always Update option is typical. However,
if your business needs require that assets modified directly in the
target environment take precedence over older changes from the IBM Business Automation
Workflow development environment,
you can select the Update if newer option.
The DateLastModified property on the objects in the deploy dataset
are compared to the same objects in the target environment to determine
which objects are newer.