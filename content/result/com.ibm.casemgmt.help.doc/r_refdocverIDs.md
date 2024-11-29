# Can't refer to document version IDs in the target object store

## Procedure

To get the IDs for reference documents in the target object store, complete the
following steps:

1. Export the  as a .twx file from
Workflow Center.
2. Extract artifacts.sdx from the case folder inside the exported
.twx file.
3. Rename artifacts.sdx file to artifacts.zip.
4. Log in to the workflow server environment and place the artifacts.zip in
the /home folder.
5. In the <bawserver-installation>/CaseManagement/configure folder, run the configuration tool
command to generate a data map:

.../configmgr\_cl generateObjectStoreDataMap -solutionPackage /home/artifacts.zip -file /home/DataMap\_ObjectStore.xml
6. Place the DataMap\_ObjectStore.xml inside the
artifacts.sdx file and repackage the .twx file by using
7-Zip.
7. Import the repackaged .twx file into Workflow Center.
8. Deploy the case solution from Workflow Center.