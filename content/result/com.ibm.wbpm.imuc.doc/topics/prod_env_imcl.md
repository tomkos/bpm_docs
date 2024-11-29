# Changing Workflow Server use between
Production and Non-production by using the IMCL command

## Procedure

Make the appropriate version replacements and run the following commands:

1. From a command line, change directories to the /eclipse/tools directory
under Installation Manager.

Important: On Windows 7, Windows Vista, or Windows Server 2008, if the
product was installed as an administrator, start your command prompt by right-clicking and selecting
Run as administrator.
2. Download the installation image from Passport Advantage®, and verify the available packages and
features in the repository directory where they have been extracted, for example
extract\_BPM\_install\_image\_directory/repository/WBI.

imcl listAvailablePackages -features -repositories extract\_BPM\_install\_image\_directory/repository/WBI
com.ibm.bpm.ADV.v85\_8.6.0.20170915\_1258 : WorkflowEnterprise.Production,WorkflowEnterprise.NonProduction
3. List the packages that are installed in your IBM Business Automation
Workflow installation.

imcl listInstalledPackages -installationDirectory C:/IBM/BPM85
com.ibm.bpm.ADV.v85\_8.5.700201609.20160928\_1258
com.ibm.websphere.ND.v85\_8.5.5010.20160721\_0036Make
sure that the repository and the major version of the installed package (com.ibm.bpm.ADV.v85)
match.
4. List the installed features to verify the features that are available for the package ID.

imcl listInstalledFeatures com.ibm.bpm.ADV.v85\_8.6.0.20170915\_1258 
WorkflowEnterprise.Production
5. Modify the package to add the required software license by using the
-addFeature option. The following command adds the WorkflowEnterprise.NonProduction
license and automatically removes the existing software license.

imcl modify com.ibm.bpm.ADV.v85\_8.6.0.20170915\_1258 -addFeatures WorkflowEnterprise.NonProduction
-repositories extract\_BPM\_install\_image\_directory/repository/WBI/repository.config -installationDirectory C:/IBM/BPM85
6. Verify the change.

imcl listInstalledFeatures com.ibm.bpm.ADV.v85\_8.6.0.20170915\_1258 
WorkflowEnterprise.NonProduction