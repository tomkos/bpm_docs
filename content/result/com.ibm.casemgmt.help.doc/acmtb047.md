# Deploy dataset not found when the test environment is reset

## Symptoms

When you try to reset the test
environment, you receive an error message similar to the following message:

## Resolving the problem

1 Verify that the deployDataSet1.xml file is in the content element list forthe DeployDataset document.
    1. In IBM® Administration Console for
Content Platform Engine, select the case management design object
store.
    2. Click Browse > Root Folder > IBM Business Automation
Workflow > Datasets > DevEnvReinitInfo > dev\_env\_connection\_definition.
    3. On the dev\_env\_connection\_definition page, click
DeployDataset in the Containment Name column.
    4. On the DeployDataset page, click the Content
Elements tab and verify that the deployDataSet1.xml file is
listed.
    5 If the deployDataSet1.xml file is not listed, you must add it to theDeployDataset document.
        1. Click Actions > Checkin, checkout, cancel > Exclusive checkout, and then click Actions > Checkin, checkout, cancel > Checkin.
        2. In the Checkin Document window, click Add to
navigate to the deploy dataset folder and attach the deployDataSet1.xml
file.
        3. Click Checkin.
2. Ensure that the application server administrative user has full control privileges for the
temporary directory in which the dataset content is saved. To determine the path to the temporary
directory, look in the Case Builder status pane for a message such
as FNRPA0439I The data set content is being saved to C:\Windows\TEMP\.