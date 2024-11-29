# Customizing the Process Performance and Team Performance dashboards

## Before you begin

To customize the Process Performance and Team Performance dashboards, clone the most recent
snapshot of the Process Portal application. You can then modify the Process Performance and Team Performance dashboards in your
copy. If you apply a product update that contains changes to the Process Portal application, clone the
updated Process Portal
application, and then reapply your customization changes to the new copy. For information about
creating a snapshot, see Creating snapshots, comparing, setting status, and validating.

- dashboards\_artifacts\_debug.zip file Thisfile contains the resources, such as JavaScript files that are usedby the dashboards.
    1. Download the .zip file from the Dashboards
toolkit and extract the contents into a folder.
    2. In the new folder, create a lib folder, and
in the lib folder, create a dojo folder.
- dojo-release-1-8-5-src.zip file This filecontains the build scripts that you need to build the customized dashboards.

1. Download the .zip file from the Dojo Foundation website.
2. Extract the contents of the .zip file to
the lib/dojo folder.

## Procedure

1. Change the name of the dashboard by creating a key in a
resource bundle and then assigning the label of the human service
to that name. For information, see Globalizing dashboard names.
2. Edit the .css files.  To modify the styles that are used
for the Team Performance and Process Performance pages, edit the
PerformanceDashboard.css file in the copy of the Process Portal application. To modify
the styles that are used by individual coach views, edit the
dashboards\_controls.css file. This file is in the directory that contains the
contents of the extracted dashboards\_artifacts.zip file.
3. In your copy of the Process Portal application, change
the contents of the coaches themselves or the coach views that they
contain.
4. Test the customized pages.
5. Package and deploy the updated dashboard
artifacts.

- Creating a custom dashboard

To show the business information that you are interested in, you can create custom dashboards.