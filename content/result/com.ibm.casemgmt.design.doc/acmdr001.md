# Saving user-defined assets before you reset the test environment

## About this task

## Procedure

To save user-defined assets before you reset the test
environment:

1 Create and save an export manifest of the assets that youwant to save from your target object store in the test environment:
    1. Start FileNet Deployment
Manager.
    2. Click Environments > environment definition for the environment definition that you want to export
assets from.
    3. Right-click Export Manifests and
click New > Export manifest.
    4. Open the manifest, click the Add Assets to
the export manifest editor icon, and select the assets
that you want to save from the target object store.
    5. Specify the export manifest file name, the output folder,
and the deploy dataset name.
    6. Click OK.
The
export starts.
2 Add the exported deploy dataset to the DeployDataset setdocument object in the reinitialization folder for the case managementdesign object store:

1. In IBM Administration Console for
Content Platform Engine, select the case management design object
store.
2. Click Browse > Root Folder > IBM Business Automation
Workflow > Datasets > DevEnvReinitInfo > dev\_env\_connection\_definition.
3. On the dev\_env\_connection\_definition page, click
DeployDataset in the Containment Name column.
4. On the DeployDataset page, click Actions > Checkin, checkout, cancel > Exclusive checkout, and then click Actions > Checkin, checkout, cancel > Checkin.
5 In the Checkin document window, add the exported deploy dataset XML files.Click Add to navigate to the deploy dataset folder that you selected when youexported the manifest in FileNet DeploymentManager , such as…\IBM\FileNet\ContentEngine\tools\deploy\P8DeploymentData\Environments\environment namefolder \Assets\export manifest name folder , and attach the followingXML files: Restriction: Do not change the names of the Catalog.xml anddeployDataset1.xml files. If you change the names, then Case Builder cannot read the files.
    - Catalog.xml
    - deployDataset1.xml
6. Click Checkin.

## What to do next