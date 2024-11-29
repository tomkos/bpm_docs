# Importing existing assets into IBM Business Automation Workflow

## Procedure

1. Verify that the IBM Business Automation Workflow
Workflow Center is running. 
To access Workflow Center, open your web
browser to http://[host\_name]:[port]/WorkflowCenter.
2. Import previously exported process applications and toolkits as described in Importing and exporting projects. 

Important: Import first the toolkits and then the process applications. To preserve the
toolkit versioning order from your current Workflow Center, import them in the
correct order. The last imported toolkit will be the tip in the new Workflow Center.
3. If your imported assets include tracking groups or other data that is required by
Performance Data Warehouse, be sure that the warehouse is running and then select
File > Update tracking definitions from the main menu.
 Updating existing definitions enables authors to capture data that is needed to test
reports (and other assets that require performance data) while they develop those assets in IBM Process
Designer.
4 Update the existing dependencies by opening the Designer view in IBM ProcessDesigner and completingthe following steps for each process application and toolkit:
    1. Under Toolkits, right-click System Data toolkit.
    2. Select Change Version of dependency.
    3. Select the 24.x snapshot from the Change Dependency snapshot list.
5. To ensure an optimal display of elements in your user interface after any changes in CSS theme,
run the BPMRegenTheme command to regenerate the runtime CSS for your application
or toolkit snapshot.
For more information, see BPMRegenTheme command.