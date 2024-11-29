# Using FileNet Deployment
Manager to
export other FileNet P8 assets

## About this task

If you extend your solution with non-case management assets, you must
migrate the assets to the target domain by using the appropriate migration tool for that asset. The
IT admin and the business analyst must track these extended assets and ensure that they are properly
managed. For example, form templates and some assets are stored in the target object store. If the
test environment is reset in Case Builder, these extended assets are
lost. To preserve extended assets that reside in the target object store you must export the assets
to a protected location, such as a removable disk, by using FileNet Deployment
Manager, and then import the assets after the next iteration of the
solution is deployed.

## Procedure

To move additional assets to a another development or
production target object store:

1. Create a list with the description and location of all
additional extended assets that are used in the solution design.
2 See the FileNet DeploymentManager documentation for details onthe steps in this procedure. Tip: Review these sections:
    - Deploying IBM FileNet P8 applications > Deployment overview
    - Deploying IBM FileNet P8 applications > FileNet P8 assets
    - Deploying IBM FileNet P8 applications > Prepare data for deployment > How to... > Prepare Content Engine data
    - Deploying IBM FileNet P8 applications > Deploy FileNet P8 Platform assets > How
to... > Deploy Content Engine > Import converted
objects
3. Create the deploy dataset.
FileNet Deployment
Manager uses the export manifest
file to generate a deploy dataset of exported objects.
4. Create the object store, security
principal, and optionally service half maps to capture information
from the IBM Business Automation
Workflow development,
or source, environment.
Follow all recommendations
in the FileNet Deployment
Manager documentation,
such as making a note of the security principals that are discovered
to ensure corresponding administrative groups can be identified in
the destination environment.
5. Use FileNet Deployment
Manager to
create a deploy package.
A deploy package is a compressed
file of deployable content that can be deployed from FileNet Deployment
Manager that is on a different
system. When you create a deploy package, you specify its deployable
content by selecting a deploy dataset folder that was created by the
export procedure in step 3.
You also have the option of including the half maps that were created
in step 4.